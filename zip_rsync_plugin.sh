#!/bin/bash
cd "$(dirname "$0")" || exit # Open script directory
zip -r Webservices_Enercoop.zip Webservices_Enercoop/
rsync -av -e ssh Webservices_Enercoop.zip geo@geo.enercoop.infra:/var/www/public.geo.enercoop.org/plugins