# Plugin Webservices Enercoop

Plugin QGIS 3 fournissant des accès aux webservices cartographiques (WMS, WMTS, WFS, etc.) intéressants pour les salarié(e)s d'Enercoop. Pour fonctionner, **il nécessite le VPN**.

Ce projet est un fork du plugin [GeoGrandEst](https://github.com/geograndest/qgis-plugin), lui-même étant un fork du plugin [Géo2France](https://github.com/geo2france/idg-qgis-plugin). Ce plugin a donné lieu à plusieurs forks : Géo2France a été forké par le [CRAIG](https://github.com/gipcraig/qgis-plugin), [GéoBretagne](https://github.com/geobretagne/qgis-plugin) a fait un fork de GéoGrandEst, et [Indigéo](https://gitlab.in2p3.fr/letg/indigeo-for-qgis/-/tree/master) a fait un fork de GéoBretagne (ouf!).

## Installation

### Pour les développeurs

Le répertoire des extensions externes de QGIS 3 est localisé dans :

- Linux : `$HOME/.local/share/QGIS/QGIS3/profiles/default/python/plugins`
- Windows : `C:\Users\USER\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`
- Mac OS : `Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins`

Afin de développer et tester rapidement les modifications, on clone ce dépôt, puis l'on crée dans le répertoire d'extensions un lien symbolique vers celui-ci :

```bash
cd $HOME/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
ln -s <chemin_vers_le_depot>/WebservicesQgisPlugin
```

Puis, dans QGIS, activez l'extension (`Extensions > Installer/Gérer les extensions > Installées` - cocher "Webservices Enercoop"), et affichez le panneau latéral (`Extensions > Webservices Enercoop > Afficher le panneau latéral`).

### Pour les salariés

L'installation et l'utilisation du plugin est documentée dans la [doc interne](https://si.enercoop.org/eprod:qgis_plugin_webservices). Il est nécessaire d'ajouter au préalable le dépôt de plugins interne à la liste des dépôts d'extensions QGIS, étape documentée [ici](https://si.enercoop.org/eprod:qgis_ajout_depot_interne).

## Séparation entre code `.py` du plugin et la liste de webservices `config.json`

### Simplicité d'évolution et confidentialité

Le plugin fonctionne grâce à 2 éléments distincts :

- Le code Python du plugin, que l'utilisateur installe avec `Webservices_Enercoop.zip`.
- La liste des adresses de webservices chargée par le plugin au démarrage de QGIS, contenue dans le `config.json`.

Ainsi, les utilisateurs voient cette liste s'enrichir automatiquement de nouveaux webservices lorsqu'ils redémarrent QGIS, sans avoir besoin de télécharger une nouvelle version du plugin. Nous faisons évoluer la liste des webservices accessibles via le plugin indépendament de son code Python en modifiant le fichier `config.json` chargé à chaque démarrage de QGIS. Ce `config.json` est placé sur [public.geo.enercoop.org](https://public.geo.enercoop.org/plugins/), accessible uniquement via le VPN, ce qui demane donc à l'utilisateur **d'activer le VPN au démarrage de QGIS** pour que le plugin puisse charger la liste des webservices - le VPN pouvant être ensuite coupé, tant que QGIS n'est pas redémarré.

### Mise à jour du plugin et de la configuration

Le plugin `.zip` et le `config.json` sont placés sur le serveur `geo`, dans le dossier `/var/www/public.geo.enercoop.org/plugins`, diffusés sur [public.geo.enercoop.org](https://public.geo.enercoop.org/plugins/) :

```bash
geo@geo:~$ ls -l /var/www/public.geo.enercoop.org/plugins/
total 208
-rw-r--r-- 1 geo geo 115890 Oct 12 11:06 config.json
-rw-r--r-- 1 geo geo  90870 Nov  2 12:15 Webservices_Enercoop.zip
```

Pour mettre à jour sur le serveur le `config.json` après l'avoir modifié, on exécute `./rsync_config.sh`. Pour mettre à jour le plugin, on exécute `./zip_rsync_plugin.sh`.

A l'avenir, pour rendre l'installation et la MAJ plus aisée, on pourra mettre le `.zip` du plugin sur un dépôt public, comme l'a fait Géo2France (cf. code [repo](https://github.com/geo2france/idg-qgis-plugin/tree/main/repo) et [lien](https://www.geo2france.fr/public/qgis3/plugins/plugins.xml) vers le dépôt), puis déclarer et activer celui-ci dans les dépôts d'extensions QGIS.

## Utilisation

Voir la [documentation interne](https://si.enercoop.org/eprod:qgis_plugin_webservices).
