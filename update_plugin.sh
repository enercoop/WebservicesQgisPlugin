#!/bin/bash
cd "$(dirname "$0")" || exit # Open script directory

version=0.1.0

# TODO: Check if the metadata is correctly filled
# metadata_version=$(grep version= < Webservices_Enercoop/metadata.txt | awk -F '=' '{print $2}')
# metadata_version="$(cat Webservices_Enercoop/metadata.txt | grep version= | cut -d '=' -f 2)"

# Compress the plugin and put it on the repository
echo "Compress the plugin ..."
zip -r Webservices_Enercoop-${version}.zip Webservices_Enercoop/
echo "Send plugin to public.geo.enercoop.org ..."
rsync -av -e ssh Webservices_Enercoop-${version}.zip geo@geo.enercoop.infra:/var/www/public.geo.enercoop.org/plugins/Webservices_Enercoop

# Update the config.json on geo.enercoop (for test)
echo "Update config.json ..."
rsync -av -e ssh Webservices_Enercoop/config/config.json geo@geo.enercoop.infra:/var/www/public.geo.enercoop.org/plugins/Webservices_Enercoop

# TODO: Update the config.json on Lucas GitHub (for prod)

# Update the repo XML
echo "Update plugins.xml ..."
rsync -av -e ssh repo/plugins.xml  geo@geo.enercoop.infra:/var/www/public.geo.enercoop.org/plugins