# -*- coding: utf-8 -*-

from Webservices_Enercoop.nodes.favorites_tree_node import FavoritesTreeNode
from Webservices_Enercoop.utils.plugin_globals import PluginGlobals
from Webservices_Enercoop.utils.plugin_icons import PluginIcons

class VoidTreeNode(FavoritesTreeNode):
    """
    Tree node for a void layer
    """

    def __init__(
        self,
        title,
        node_type=PluginGlobals.instance().NODE_TYPE_VOID_LAYER,
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

        self.can_be_added_to_map = False

        # Icon
        plugin_icons = PluginIcons.instance()
        self.icon = plugin_icons.wms_style_icon
        if self.status == PluginGlobals.instance().NODE_STATUS_WARN:
            self.icon = plugin_icons.warn_icon

    def get_qgis_layer_details(self):
        """
        Return the details of the layer used by QGIS to add the layer to the map.
        This dictionary is used by the run_add_to_map_action and layerMimeData methods.
        """
        qgis_layer_uri_details = {
            "type": "void",
            "provider": "void",
            "title": self.title
        }

        return qgis_layer_uri_details