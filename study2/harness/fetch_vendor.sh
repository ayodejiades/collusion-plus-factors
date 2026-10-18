#!/bin/sh
# Fetch the Agrawal et al. (2025) market code at the pinned commit into vendor/.
# The upstream repository has no license file, so this project does not redistribute it.
set -e
cd "$(dirname "$0")/.."
DEST=vendor/llm-agent-collusion
COMMIT=2bb2a7e22860160d1fddb5d2e5cb460cc6ec6aff
if [ -d "$DEST/src" ]; then echo "fetch_vendor: $DEST already present"; exit 0; fi
mkdir -p vendor
git clone -q https://github.com/andyjliu/llm-agent-collusion "$DEST"
git -C "$DEST" checkout -q "$COMMIT"
rm -rf "$DEST/.git" "$DEST/data" "$DEST/assets"
echo "fetch_vendor: $DEST at $COMMIT"
