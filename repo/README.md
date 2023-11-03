# Dépôt d'extensions interne

Le fichier `plugins.xml` constitue la page d'accueil du dépôt d'extensions interne dont les salariés ajouteront l'URL à la liste des dépôts d'extensions de leurs QGIS Desktop. Cette étape est documentée [ici](https://si.enercoop.org/eprod:qgis_ajout_depot_interne).

On synchronise `plugins.xml` sur [public.geo.enercoop.org](https://public.geo.enercoop.org/plugins/) avec le script `./rsync_plugins_xml.sh`. A chaque nouvelle version, il faut penser à faire évoluer le numéro de version dans la balise `<pyqgis_plugin name="Webservices Enercoop" version="X.X.X">`
