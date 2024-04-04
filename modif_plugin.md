# Fonctionnement du plugin

## Séparation entre code source du plugin et configuration

Pour modifier la liste des webservices accessibles depuis le panneau latéral, il n'est pas nécessaire de modifier le code Python du plugin : tout se passe dans le fichier `config.json`, placé ici dans sur un dépôt public distant. Cette séparation entre code du plugin et fichier de configuration est une simplicité à l'origine du succès du plugin.

## Chargement du `config.json` externe

Le fichier de configuration `config.json` est téléchargé par le plugin `Webservices Enercoop` au démarrage de QGIS. L'URL par défaut vers ce fichier est défini par la variable `CONFIG_FILE_URLS` dans `utils/plugin_globals.py`, juste [ici](https://github.com/enercoop/prodspection/blob/main/qgis/plugins/Webservices_Enercoop/utils/plugin_globals.py). Il est possible dans QGIS de modifier l'URL de ce `config.json` pour en charger un nouveau : `Extensions > Webservices Enercoop > Paramétrer le plugin ... > Fichier de configuration de l'arbre des ressources > URL du fichier`

## Bricolage avec le GitHub perso de Lucas

Cet URL doit être accessible en ligne et donc placé sur un dépôt (GitHub par exemple) public. Celui d'Enercoop étant privé, on s'appuiera sur le GitHub personnel de Lucas, dans lequel on crée un [dépôt](https://github.com/LucasJumMou/config) dédié à ce fichier. Puis on règle la variable `CONFIG_FILE_URLS` sur le [fichier brut](https://raw.githubusercontent.com/LucasJumMou/config/main/config.json).

On souhaite néanmoins pouvoir modifier en commun de `config.json` depuis le dépôt Enercoop. On crée donc un lien (non symbolique) sur la machine de Lucas :

```bash
cd /home/lucas.jumeaumousset/Documents/config/
ln $HOME/prodspection/qgis/plugins/Webservices_Enercoop/config/config.json config.json
```

Pour que les modifications soient effectives, il faut faire un 2ème `git push` sur le GitHub perso de Lucas ... A l'avenir, le config.json sera stocké directement sur un serveur interne à Enercoop.

## Modifications apportées dans ce fork (Lucas)

### Utilisation de fichiers YAML pour générer le config.json

L'une des principales modification est l'utilisation de multiples fichiers .yaml dans le dossier `Webservices_Enercoop/config` afin de générer le `config.json` alimentant le plugin. Cette fragmentations du config.json en plusieurs YAML permet de faciliter les modification du `config.json` et éviter de se perdre et de générer des erreurs.

Les YAML sont convertis en JSON et insérés dans le template JSON du config.json. Pour automatiser cela on utilise le script python `merge_to_json.py` présent dans le `Webservices_Enercoop/config` qui prends l'ensemble des YAML du dossier afin de générer le JSON de config.

Pour plus d'informations ce référer au [README du config](Webservices_Enercoop/config/README.md)

Pour l'utiser on effectue les commandes suivantes :

```bash
cd WebservicesQgisPlugin/Webservices_Enercoop/config
python3 merge_to_json.py config.json *.yaml
```

### Géoportail de l'urbanisme (GPU)

Les flux WMS du GPU ont pour problème de ne s'ouvrir que si le SCR du projet QGIS est en WGS84 (`EPSG:4326`). Comme expliqué [ici](https://www.geoportail-urbanisme.gouv.fr/image/UtilisationWMS_GPU_Qgis_1-0.pdf#page=3) dans leur documentation :

> Atention ! L’appel au flux WMS du GPU dans Qgis ne fonctionne pour le moment qu’en WGS84. Il faut donc, avant d’ajouter une couche WMS, passer le projet Qgis dans cette projection, réaliser l’ajout de la couche, puis repasser dans la projection souhaitée si différente.

Cette limite étant un frein important à l'utilisation de ce flux WMS par les salariés, nous avons décidé de corriger ce problème dans ce plugin.  Pour ce faire, il a été nécessaire de créer un nouveau type de noeud .Un noeud est une méthode python permettant de créer une requête à un webservice demandant un `capabilities` spécifique au fournisseur de données. Ce noeud reprend la même structure que le noeud WMS, mais possède un facteur d'items différents. Les facteurs d'items sont des éléments nécessaires dans une requête afin de spécifier le webservice que l'on veut charger. Les facteurs d'items d'une requête sont les suivants : l'url de connexion, le style attribué par le fournisseur, ainsi que le type de chargements de données (zoom ou nombre d'entités) choisi par le fournisseur.

### Modification des noeuds

Afin de pouvoir accepter de nouvelle structure connexion (URL) au webservices il est nécessaire de créer de nouveaux noeuds dans le code du plugin. C'est modification ce passe dans plusieurs fichiers.

- `nodes/nodes.py` : défini les différents paramètres que notre nouveau noeud va prendre comme l'url, le style, le type de chargement ect. Dans le cadre du plugin, nous avons rajouté plusieurs types noeuds :

  - `class WmsLayerUrbaTreeNode`, `class WmsLayerOrthoTreeNode` , `class WmsLayerPlanTreeNode`, `class WmsEnrTreeNode`, etc

- `nodes/tree_node_factory.py` : permet d'initialiser le type de connexion issu des noeuds de `nodes.py`, lors de l'appel des webservices. La modification apportée est le rajout dans une boucle d'appel des noeuds crées dans `nodes.py`

- `plugins_globals.py` permet de définir le nom d'appel des noeuds dans le `config.json`. Les nouveaux noeuds sont alors définis par une variable qui est reconnue spécifier dans la définition des couches du `config.json`

La création des noeuds est un aller-retour avec les webservices existants. Il se peut que le webservice possède un noeud capable de le charger, ou non. Pour vérifier cela, il suffit de charger le webservice sur traditionnele sur QGIS (`WMS/WMTS > Nouvelle connexion > Rajouter le webservices > Propriétés de la couche > Informations (URL + source)`).
Puis de disséquer l'URL et la source du webservice.

Exemple : Cartes IGN de datara.
URL : `https://datacarto.datara.gouv.fr/map/carte_zonage_amenagement?VERSION=1.3.0`
Source : `crs=EPSG:2154&dpiMode=7&format=image/png&layers=layer23&styles&tilePixelRatio=0&url=https://datacarto.datara.gouv.fr/map/carte_zonage_amenagement?VERSION%3D1.3.0`

Dans cet exemple, la source possède un ordre avec le crs puis un dpi, puis un format, puis un layer, puis un style et enfin un url.

Si on compare à nos nodes, celui-ci correspond à `WmsLayerUrbaSandreTreeNode` avec une structure du node ressemblant à :

```python
            "uri": u"crs={}&dpiMode=7&format={}&layers={}&styles&url={}".format(
                self.layer_srs,
                self.layer_format,
                self.layer_name,
                self.service_url,
            )
```

Puisque le node existe déjà, on va pouvoir appeler `WmsLayerUrbaSandreTreeNode` comme `type` dans le config.json afin de charger le webservice.

Si le webservice ne possède pas de node pouvant le charger, il faudra en créer un nouveau en modifiant les trois fichiers spécifiés en haut: `nodes/nodes.py`, `nodes/tree_node_factory.py`, `plugins_globals.py`.

### Ajout d'un curseur d'opacité

Afin de rendre les couches plus flexibles, nous avons décidé de rajouter un curseur d'opacité affectant les couches raster .Cela permet d'obtenir une meilleure visualisation et lecture des informations. Pour ce rajout nous avons modifié `plugin.py` en rajoutant au démarrage une fonction `def transparency_slider(layers)`.