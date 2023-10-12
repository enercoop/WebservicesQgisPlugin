#!/bin/bash
cd "$(dirname "$0")" || exit # Open script directory
zip -r Webservices_Enercoop.zip Webservices_Enercoop/
outdir="$HOME/Clood/Production - REZO - Public/Outils cartographiques/plugin"
cp Webservices_Enercoop.zip "$outdir"
