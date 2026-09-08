#!/usr/bin/env bash
# Build glove80.uf2 locally with nix, mirroring .github/workflows/build.yml.
# Requires nix. First run clones MoErgo's ZMK fork into ./src (gitignored).
set -euo pipefail
cd "$(dirname "$0")"

ZMK_REF="${ZMK_REF:-main}"
if [ ! -d src ]; then
  git clone --depth 1 --branch "$ZMK_REF" https://github.com/moergo-sc/zmk.git src
fi

# The cachix substituter only kicks in if your user is a nix trusted-user;
# otherwise nix prints a warning and builds from source (slower, still works).
nix-build config -o combined \
  --option extra-substituters https://moergo-glove80-zmk-dev.cachix.org \
  --option extra-trusted-public-keys moergo-glove80-zmk-dev.cachix.org-1:D8fhPJ1c3gkuckuyBLRtGYarCVptIDn4g5k8u91NbyM=

cp -f combined/glove80.uf2 glove80.uf2
echo "wrote $(pwd)/glove80.uf2"
