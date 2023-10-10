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

### Géoportail de l'urbanisme (GPU)

Les flux WMS du GPU ont pour problème de ne s'ouvrir que si le SCR du projet QGIS est en WGS84 (`EPSG:4326`). Comme expliqué [ici](https://www.geoportail-urbanisme.gouv.fr/image/UtilisationWMS_GPU_Qgis_1-0.pdf#page=3) dans leur documentation :

> Atention ! L’appel au flux WMS du GPU dans Qgis ne fonctionne pour le moment qu’en WGS84. Il faut donc, avant d’ajouter une couche WMS, passer le projet Qgis dans cette projection, réaliser l’ajout de la couche, puis repasser dans la projection souhaitée si différente.

Cette limite étant un frein important à l'utilisation de ce flux WMS par les salariés, nous avons décidé de corriger ce problème dans ce plugin.  Pour ce faire, il a été nécessaire de créer un nouveau type de noeud .Un noeud est une méthode python permettant de créer une requête à un webservice demandant un `capabilities` spécifique au fournisseur de données. Ce noeud reprend la même structure que le noeud WMS, mais possède un facteur d'items différents. Les facteurs d'items sont des éléments nécessaires dans une requête afin de spécifier le webservice que l'on veut charger. Les facteurs d'items d'une requête sont les suivants : l'url de connexion, le style attribué par le fournisseur, ainsi que le type de chargements de données (zoom ou nombre d'entités) choisi par le fournisseur.

### Modification des noeuds

La création de nouveau noeud a nécessité la modification de trois fichiers dans le répertoire du plugin :

- `nodes/nodes.py` est le fichier python permettant de créer des nouveaux noeuds à travers de classe python. Dans ce fichier ont défini les différents paramètres que notre nouveau noeud va prendre comme l'url, le style, le type de chargement ect. Dans le cadre du plugin, nous avons rajouté deux types de noeud :

  - `class WmsLayerUrbaTreeNode` permettant de se connecter au webservice de l'urbanisme.

  - `class WmsLayerOrthoTreeNode` permettant de se connecter au webservice wms de l'IGN et spécifiquement de la BD Ortho.
  
  - `class WmsLayerPlanTreeNode` permettant de se connecter au webservice de l'IGN possédant une clé.

  - `class WmsEnrTreeNode` permettant de se connecter au webservice du portail cartographique des Enr possédant une clé.
  
  - `class VectorTilesTreeNode` permettant de se connecter au webservice en VectorTiles, en l'occurance ceux de l'IGN. Ici la méthode PyQGIS de rajout de couche a été modifiée, en passant de `PluginGlobals.instance().iface.addRasterLayer()` vers `PluginGlobals.instance().iface.addVectorTileslayer`. Les paramètres d'entrées de la méthode ont été modifiés et adaptés à VectorTiles, ainsi que l'url de connexion.

- `nodes/tree_node_factory.py` est le fichier python permettant d'initialiser le type de connexion issu des noeuds de `nodes.py`, lors de l'appel des webservices. La modification apportée est le rajout dans une boucle d'appel des deux noeuds crées dans `nodes.py`

- `plugins_globals.py` est un fichier python permettant de définir le nom d'appel des noeuds dans le `config.json`. Les nouveaux noeuds sont alors définis par une variable qui est reconnue spécifier dans la définition des couches du `config.json`

### Ajout d'un curseur d'opacité

Afin de rendre les couches plus flexibles, nous avons décidé de rajouter un curseur d'opacité affectant les couches raster .Cela permet d'obtenir une meilleure visualisation et lecture des informations. Pour ce rajout nous avons modifié `plugin.py` en rajoutant au démarrage une fonction `def transparency_slider(layers)`.