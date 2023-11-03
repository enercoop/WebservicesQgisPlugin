#!/bin/bash
cd "$(dirname "$0")" || exit # Open script directory
rsync -av -e ssh Webservices_Enercoop/config/config.json geo@geo.enercoop.infra:/var/www/public.geo.enercoop.org/plugins