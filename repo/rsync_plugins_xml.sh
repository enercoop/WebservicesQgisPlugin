#!/bin/bash
cd "$(dirname "$0")" || exit # Open script directory
rsync -av -e ssh plugins.xml  geo@geo.enercoop.infra:/var/www/public.geo.enercoop.org/plugins