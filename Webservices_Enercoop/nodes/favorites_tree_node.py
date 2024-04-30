# -*- coding: utf-8 -*-

from Webservices_Enercoop.utils.plugin_globals import PluginGlobals


class FavoritesTreeNode:
    """ """

    def __init__(
        self,
        title,
        node_type=PluginGlobals.instance().NODE_TYPE_FOLDER,
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

        self.parent_node = parent_node
        self.node_type = node_type
        self.title = title
        self.description = description
        self.status = status
        self.metadata_url = metadata_url
        self.raw_data_url = raw_data_url
        self.ident = ident
        self.bounding_boxes = bounding_boxes
        self.children = []
        self.can_be_added_to_map = False
        self.icon = None

    def layer_mime_data(self):
        """
        Return the mime data used by the drag and drop process
        and needed by QGIS to add the right layer to the map
        """

        qgis_layer_details = self.get_qgis_layer_details()
        mime_data = ":".join(
            [
                qgis_layer_details["type"],
                qgis_layer_details["provider"],
                qgis_layer_details["title"].replace(":", "\\:"),
                qgis_layer_details["uri"].replace(":", "\\:"),
            ]
        )

        return mime_data

    def run_add_to_map_action(self):
        """ """

        pass

    def run_show_metadata_action(self):
        """
        Opens in the default user web browser the web page displaying the resource metadata
        """

        import webbrowser

        if self.metadata_url:
            webbrowser.open_new_tab(self.metadata_url)

    def run_show_raw_data_action(self):
        """
        Opens in the default user web browser the web page displaying the brut resource
        """

        import webbrowser

        if self.raw_data_url:
            webbrowser.open_new_tab(self.raw_data_url)

    def run_report_issue_action(self):
        """
        Opens the default mail client to let the user send an issue report by email
        """

        # import webbrowser
        # webbrowser.open('mailto:')
        pass