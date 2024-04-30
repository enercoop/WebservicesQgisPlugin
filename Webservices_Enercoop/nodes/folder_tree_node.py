# -*- coding: utf-8 -*-

from Webservices_Enercoop.nodes.favorites_tree_node import FavoritesTreeNode
from Webservices_Enercoop.utils.plugin_globals import PluginGlobals
from Webservices_Enercoop.utils.plugin_icons import PluginIcons

class FolderTreeNode(FavoritesTreeNode):
    """
    Tree node for a folder containing other nodes
    """

    def __init__(
        self,
        title,
        node_type=PluginGlobals.instance().NODE_TYPE_FOLDER,
        description=None,
        status=None,
        metadata_url=None,
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
            ident,
            params,
            bounding_boxes,
            parent_node,
        )

        # Icon
        plugin_icons = PluginIcons.instance()
        self.icon = plugin_icons.folder_icon
        if self.status == PluginGlobals.instance().NODE_STATUS_WARN:
            self.icon = plugin_icons.warn_icon