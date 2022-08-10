#!/bin/bash
set -e
for palette in black dark white light; do
  pname="selenized_${palette}.py"
  python3 evaluate_template.py "palettes/${pname}" "./templates/vscode-color-theme.json.template"
  mv "selenized-${palette}.json" "./vscode/Selenized ${palette}-color-theme.json"

  python3 evaluate_template.py "palettes/${pname}" "./templates/color-listing.template"
  mv "selenized-${palette}.color-listing" "./vscode/"
done
