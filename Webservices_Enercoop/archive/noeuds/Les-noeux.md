# Les noeuds (ou "nodes")

Les noeuds sont des fonctions permettant de charger des webservices selon des strucutures d'URL dépendants des fournisseurs de données. Pour plus d'informations [Ajouter un webservice au catalogue](https://github.com/enercoop/WebservicesQgisPlugin/wiki/Ajouter-un-webservice-au-catalogue).

## Définir un noeud dans le plugin Webservices Enercoop

Un noeud correspond à une structure d'URL, il faut donc adapter le code python aux URL de webservices.

### 1. Définir les paramètres du nouveau nœud dans `nodes.py`

- Ouvrez le fichier `nodes.py`.
- Créez une nouvelle classe de nœud pour le nouveau type d'URL, la fonction la plus importante est `get_qgis_layer_details`, celle-ci précise la strucuture de l'URL et les informations nécessaires aux chargements du webservice que l'on retrouvera dans la YAML que l'on peut identifier par les variables commençant par `.self`.

Exemple d'URL :

```text
`crs=EPSG:2154&featureCount=10&format=image/png&layers=Znieff1&maxHeight=256&maxWidth=256&styles=default&url=https://ws.carmencarto.fr/WMS/119/fxx_inpn?` 
```

Exemple de construction de node pouvant correspondre:

```python
    def get_qgis_layer_details(self):
        """
        Return the details of the layer used by QGIS to add the layer to the map.
        This dictionary is used by the run_add_to_map_action and layerMimeData methods.
        """
        qgis_layer_uri_details = {
            "type": "raster",
            "provider": "wms",
            # Titre donné dans le YAML
            "title": self.title,
            # Strucuture de l'URL correspondant à un ou plusieurs webservices, les {} permettent de passer les variables .self issues du YAML
            "uri": u"crs={}&featureCount=10&format={}&layers={}&maxHeight=256&maxWidth=256&styles={}&url={}".format(
                # Le CRS défini dans le YAML, dans l'exemple "EPSG:2154"
                self.layer_srs,
                # Le format défini dans le YAML, dans l'exemple "image/png"
                self.layer_format,
                # Le nom du webservice défini dans le YAML, dans l'exemple "Znieff1"
                self.layer_name,
                # Le style du webservice défini dans le YAML, dans l'exemple "default"
                self.layer_style_name,
                # L'url du service défini dans le YAML, dans l'exemple "https://ws.carmencarto.fr/WMS/119/fxx_inpn?"
                self.service_url,
            ),
        }

        return qgis_layer_uri_details
```

### 2. Ajouter le nouveau nœud à `tree_node_factory.py` :

   - Ouvrez le fichier `tree_node_factory.py`.
   - Importez la classe du nouveau nœud depuis `nodes.py`.
   - Dans la méthode `build_tree`, ajoutez une condition pour créer le nouveau nœud lorsque cela est nécessaire en fonction des paramètres fournis.

```python
from .nodes import (
    WmsLayerTreeNode)
```

Puis:

```python
    def build_tree(self, tree_config, parent_node=None):
        """
        Function that do the job
        """

        # Read the node attributes
        node_title = tree_config.get("title", None)
        node_description = tree_config.get("description", None)
        node_type = tree_config.get("type", None)
        node_status = tree_config.get("status", None)
        node_metadata_url = tree_config.get("metadata_url", None)
        node_raw_data_url = tree_config.get("raw_data_url", None)
        node_ident = tree_config.get("ident", None)
        node_params = tree_config.get("params", None)
        node_bounding_boxes = tree_config.get("bounding_boxes", None)

        if node_title:
            # Creation of the node
            if node_type == PluginGlobals.instance().NODE_TYPE_WMS_LAYER:
                node = WmsLayerTreeNode(
                    node_title,
                    node_type,
                    node_description,
                    node_status,
                    node_metadata_url,
                    node_raw_data_url,
                    node_ident,
                    node_params,
                    node_bounding_boxes,
                    parent_node,
                )
```

### 3. Mettre à jour `plugins_globals.py` :
   - Ouvrez le fichier `plugins_globals.py`.
   - Ajoutez une nouvelle variable pour représenter le type de nœud du nouveau service dans le fichier de config.

```python
    NODE_TYPE_WMS_LAYER = "wms_layer"
```

### 4. Utiliser le nouveau nœud dans `config.json` :

Lire la documentation sur [Ajouter un webservice au catalogue](https://github.com/enercoop/WebservicesQgisPlugin/wiki/Ajouter-un-webservice-au-catalogue)