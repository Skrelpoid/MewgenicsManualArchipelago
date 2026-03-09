#!/bin/sh
set -eu

AP_NAME="manual_mewgenics_skrelpoid"
ZIP_NAME="${AP_NAME}.apworld"

# Ensure we end up back here even if script changes directory later
BASE_DIR=$(pwd)

[ -f "$ZIP_NAME" ] && rm -f "$ZIP_NAME"

# Puts non dot files into $1
set -- *
[ "$1" = "*" ] && echo "Nothing to put in the zip found (dotfiles ignored)" && exit 1

# Create a temporary staging dir (in system TMPDIR)
tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT INT TERM

# Create the root dir name we want inside the zip
root="$tmpdir/$AP_NAME"
mkdir -p "$root"

# Copy non-dot content of current directory into that root
# Skip the output file itself so it never gets embedded
for item in "$@"; do
    [ "$item" = "$ZIP_NAME" ] && continue
    cp -a -- "$item" "$root/"
done

# Now create the zip in the *original* directory, with AP_NAME as the root folder
cd "$tmpdir"
zip -r "$BASE_DIR/$ZIP_NAME" "$AP_NAME"
cd "$BASE_DIR"
