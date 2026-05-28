#!/usr/bin/env bash
# Validate the Robomotion MCP-server contract.
#
# Contract:
#   * Every server lives at servers/<name>/ and has .robomotion/mcp.yaml.
#   * mcp.yaml declares: type: mcp, name, transport (stdio|http).
#   * transport: stdio  → requires `command:`.
#   * transport: http   → requires `url:`.
#   * env.required / env.optional contain valid env-var names.
#   * MCP.md exists (the human-readable docs surfaced in the Designer/hub).
#   * index.yaml is up-to-date with build-index.py.
set -uo pipefail
cd "$(dirname "$0")"

fail=0
servers=0

is_valid_env_name() { [[ "$1" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; }

check_env_file() {
  local file="$1"
  [ -f "$file" ] || return 0
  local n=0 line name
  while IFS= read -r line || [ -n "$line" ]; do
    n=$((n+1))
    line="${line#"${line%%[![:space:]]*}"}"
    [ -z "$line" ] && continue
    case "$line" in \#*) continue;; esac
    name="${line%%=*}"
    name="${name%"${name##*[![:space:]]}"}"
    if ! is_valid_env_name "$name"; then
      echo "    FAIL: $(basename "$file"):$n invalid env name: '$name'"; fail=1
    fi
  done < "$file"
}

yaml_scalar() {
  # crude top-level "key: value" reader (value unquoted, no block scalars)
  sed -n "s/^$2:[[:space:]]*//p" "$1" | head -1 | tr -d '"'"'"' '
}

while IFS= read -r my; do
  server_dir="$(dirname "$(dirname "$my")")"
  server_rel="${server_dir#./}"
  servers=$((servers+1))
  echo "▼ SERVER: $server_rel"

  type="$(yaml_scalar "$my" type)"
  [ "$type" = "mcp" ] || echo "    WARN: $server_rel/.robomotion/mcp.yaml type is '${type:-?}' (expected 'mcp')"

  name="$(yaml_scalar "$my" name)"
  base="$(basename "$server_dir")"
  if [ -n "$name" ] && [ "$name" != "$base" ]; then
    echo "    FAIL: name '$name' != directory '$base'"; fail=1
  fi

  transport="$(yaml_scalar "$my" transport)"
  case "$transport" in
    stdio)
      command="$(yaml_scalar "$my" command)"
      [ -n "$command" ] || { echo "    FAIL: stdio transport requires 'command:'"; fail=1; }
      ;;
    http)
      url="$(yaml_scalar "$my" url)"
      [ -n "$url" ] || { echo "    FAIL: http transport requires 'url:'"; fail=1; }
      ;;
    *)
      echo "    FAIL: unknown transport '${transport:-?}' (expected stdio|http)"; fail=1
      ;;
  esac

  [ -f "$server_dir/MCP.md" ] || echo "    WARN: $server_rel/MCP.md missing"

  check_env_file "$server_dir/env.required"
  check_env_file "$server_dir/env.optional"

  # egress_hosts (optional): each list item must be a bare host or a leading
  # "*." wildcard — no scheme, no path, no port. credproxy binds the
  # credential placeholder to these and refuses substitution elsewhere.
  egress=$(awk '
    /^egress_hosts:[[:space:]]*\[/ {
      line=$0; sub(/^egress_hosts:[[:space:]]*\[/,"",line); sub(/\].*$/,"",line);
      n=split(line, a, ","); for (i=1;i<=n;i++){gsub(/[[:space:]"'"'"']/,"",a[i]); if(a[i]!="") print a[i]} next
    }
    /^egress_hosts:[[:space:]]*$/ {inblk=1; next}
    inblk && /^[[:space:]]*-[[:space:]]*/ {sub(/^[[:space:]]*-[[:space:]]*/,""); gsub(/["'"'"']/,""); print; next}
    inblk && /^[^[:space:]]/ {inblk=0}
  ' "$my")
  while IFS= read -r host; do
    [ -z "$host" ] && continue
    [ "$host" = "[]" ] && continue
    case "$host" in
      *://*|*/*|*:*)
        echo "    FAIL: egress_hosts entry '$host' must be a bare host (no scheme/path/port)"; fail=1; continue;;
    esac
    case "$host" in
      *\**)  # contains a wildcard — only a leading "*." is allowed
        case "$host" in
          \*.?*) : ;;
          *) echo "    FAIL: egress_hosts wildcard '$host' must be a leading '*.' (e.g. *.example.com)"; fail=1;;
        esac;;
    esac
  done <<< "$egress"

  echo "    transport: ${transport:-?}"
done < <(find . \( -name .git -o -name node_modules \) -prune -o -path '*/.robomotion/mcp.yaml' -print | sort)

if command -v python3 >/dev/null 2>&1; then
  echo
  python3 build-index.py --check || fail=1
fi

echo
if [ "$fail" -ne 0 ]; then
  echo "FAILED — $servers server(s), errors above."
  exit 1
fi
echo "OK — $servers server(s) valid."
