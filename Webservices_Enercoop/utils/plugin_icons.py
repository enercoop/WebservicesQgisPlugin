# -*- coding: utf-8 -*-

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QStyle

from qgis.core import QgsApplication
import os

from Webservices_Enercoop.utils.plugin_globals import PluginGlobals
from Webservices_Enercoop.utils.singleton import Singleton


@Singleton
class PluginIcons:
    """ """

    def __init__(self):
        """ """

        # Initialize the QGIS application
        # QgsApplication.initQgis()
        style = QgsApplication.style()

        # Load standard folder icon
        self.folder_icon = style.standardIcon(QStyle.SP_DirClosedIcon)

        # Load warning icon from images
        warn_icon_path = os.path.join(
            PluginGlobals.instance().images_dir_path,
            PluginGlobals.instance().ICON_WARN_FILE_NAME,
        )
        self.warn_icon = QIcon(warn_icon_path)

        # Load WMS layer icon from images
        wms_layer_icon_path = os.path.join(
            PluginGlobals.instance().images_dir_path,
            PluginGlobals.instance().ICON_WMS_LAYER_FILE_NAME,
        )
        self.wms_layer_icon = QIcon(wms_layer_icon_path)

        # Load WMS style icon from images
        wms_style_icon_path = os.path.join(
            PluginGlobals.instance().images_dir_path,
            PluginGlobals.instance().ICON_WMS_STYLE_FILE_NAME,
        )
        self.wms_style_icon = QIcon(wms_style_icon_path)

        # Load WFS layer icon from images
        wfs_layer_icon_path = os.path.join(
            PluginGlobals.instance().images_dir_path,
            PluginGlobals.instance().ICON_WFS_LAYER_FILE_NAME,
        )
        self.wfs_layer_icon = QIcon(wfs_layer_icon_path)

        # Load raster layer icon from images
        raster_layer_icon_path = os.path.join(
            PluginGlobals.instance().images_dir_path,
            PluginGlobals.instance().ICON_RASTER_LAYER_FILE_NAME,
        )
        self.raster_layer_icon = QIcon(raster_layer_icon_path)
