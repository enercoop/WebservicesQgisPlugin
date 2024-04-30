# -*- coding: utf-8 -*-

from Webservices_Enercoop.nodes.favorites_tree_node import FavoritesTreeNode
from Webservices_Enercoop.utils.plugin_globals import PluginGlobals
from Webservices_Enercoop.utils.plugin_icons import PluginIcons

class VectorTilesTreeNode(FavoritesTreeNode):
    """
    VectorTilesTreeNode
    """

    def __init__(
        self,
        title,
        node_type=PluginGlobals.instance().NODE_TYPE_VECTOR_TILES_LAYER,
        description=None,
        status=None,
        metadata_url=None,
        raw_data_url=None,
        ident=None,
        params=None,
        bounding_boxes=None,
        parent_node=None,
    ):
        """ """
        FavoritesTreeNode.__init__(
            self,
            title,
            node_type,
            description,
            status,
            metadata_url,
            raw_data_url,
            ident,
            params,
            bounding_boxes,
            parent_node,
        )

        self.service_url = params.get("url")
        self.can_be_added_to_map = True

        # Icon
        plugin_icons = PluginIcons.instance()
        self.icon = plugin_icons.wms_layer_icon
        if self.status == PluginGlobals.instance().NODE_STATUS_WARN:
            self.icon = plugin_icons.warn_icon

    def get_qgis_layer_details(self):
        """
        Return the details of the layer used by QGIS to add the layer to the map.
        This dictionary is used by the run_add_to_map_action and layerMimeData methods.
        """
        qgis_layer_uri_details = {
            "type": "raster",
            "title": self.title,
            "uri": u"type=xyz&url={}&zmax=14&zmin=0http-header:referer=".format(
                self.service_url,
            ),
        }

        return qgis_layer_uri_details

    def run_add_to_map_action(self):
        """
        Add the WMS layer with the specified style to the map
        """
        qgis_layer_details = self.get_qgis_layer_details()
        PluginGlobals.instance().iface.addVectorTileLayer(
            qgis_layer_details["uri"],
            qgis_layer_details["title"],
            )