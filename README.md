# Plugin Webservices Enercoop

Plugin pour QGIS 3 fournissant des accès aux flux géographiques intéressants pour les salarié(e)s d'Enercoop (WMS, WMTS, WFS, etc.)

Ce projet est un fork du plugin [GeoGrandEst](https://github.com/geograndest/qgis-plugin), lui-même étant un fork du plugin [Géo2France](https://github.com/geo2france/idg-qgis-plugin). Ce plugin a donné lieu à plusieurs forks : Géo2France a été forké par le [CRAIG](https://github.com/gipcraig/qgis-plugin), [GéoBretagne](https://github.com/geobretagne/qgis-plugin) a fait un fork de GéoGrandEst, et [Indigéo](https://gitlab.in2p3.fr/letg/indigeo-for-qgis/-/tree/master) a fait un fork de GéoBretagne (ouf!).

## Installation

## Méthode 1 : Pour les développeurs (Lucas & Milo)

Chacun d'entre nous dispose en local du dépôt GitHub `Enercoop/prodspection` entier dans `~/prodspection`. Le répertoire des extensions QGIS 3 est quant à lui situé dans `$HOME/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`. Afin de pouvoir à la fois développer et tester rapidement les modifications apportées avec QGIS, on crée dans le répertoire d'extensions un lien symbolique vers le répertoire de développement :

```bash
cd $HOME/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
ln -s ~/prodspection/qgis/plugins/Webservices_Enercoop Webservices_Enercoop
```

Pour les autres salariés du Pôle Num qui souhaiteraient tester la dernière version dev du plugin, télécharger le répertoire `Webservices_Enercoop` et le copier-coller dans `$HOME/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`.

Il faut ensuite activer l'extension avec QGIS : `Extensions > Installer/Gérer les extensions > Installées` puis cocher Webservices Enercoop. Puis pour afficher le panneau : `Extensions > Webservices Enercoop > Afficher le panneau latéral`.

## Méthode 2 : Pour les salariés

Voir documentation [SI interne](https://si.enercoop.org/eprod:qgis_plugin_webservices)

A l'avenir, pour rendre l'installation et la MAJ plus aisée, on pourra mettre le `.zip` du plugin sur un dépôt public, comme l'a fait Géo2France (cf. code [repo](https://github.com/geo2france/idg-qgis-plugin/tree/main/repo) et [lien](https://www.geo2france.fr/public/qgis3/plugins/plugins.xml) vers le dépôt), puis déclarer et activer celui-ci dans les dépôts d'extensions QGIS.

Pour zipper le plugin et le mettre à dispo sur le clood, on éxecute `./zip_and_export.sh`.

## Utilisation

Voir documentation [SI interne](https://si.enercoop.org/eprod:qgis_plugin_webservices)
