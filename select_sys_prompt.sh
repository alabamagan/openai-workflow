#!/bin/bash
# ==========================================================================================
# Description:
# This script parses a YAML file to find and display the value associated with a given key.
#
# Usage:
# ./script_name.sh <key>
# Replace <key> with the desired key to search for in the YAML file.
#
# Variables:
# key_to_find: The key to search for in the YAML file.
# yaml_file: The path to the YAML file (default: "data.yaml").
# ==========================================================================================
 

# Read the YAML file
yaml_file="system_prompts.yaml"  

if [ -z "$1" ]; then
  # No key provided, list all top-level keys in JSON format
  keys=$(awk -F: '/^[^ ]/ {print $1}' "$yaml_file" | paste -sd ',' - | sed 's/,/\\n/g')
  echo -e "{\"response\":\"# Available system prompts: \n${keys}\n\",\"rerun\":1,\"footer\":\"Available Prompts\",\"behaviour\":{\"response\":\"replace\",\"scroll\":\"auto\",\"inputfield\":\"clear\"}}"
  exit 0
fi

# The key to look for
key_to_find="$1"


# Parse the YAML file and find the first matching key
value=$(awk -v key="$key_to_find" '
BEGIN {found = 0; value = ""}
$0 ~ "^"key":" {
    found = 1
    next
}
found && /^[^ ]/ {exit}
found {
    gsub(/"/, "\\\"");
    gsub(/\n/, "\\n");
    value = value $0 "\n"
}
END {gsub(/\n$/, "", value); print value}
' "$yaml_file")

result="{\"rerun\":1,\"response\":\"${value}\",\"footer\":\"Value for ${key_to_find}\",\"behaviour\":{\"response\":\"replace\",\"scroll\":\"end\",\"inputfield\":\"select\"}}"
echo "$result"
