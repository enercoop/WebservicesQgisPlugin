# -*- coding: utf-8 -*-

from qgis.PyQt.QtWidgets import (
    QWidget,
    QDialog,
    QVBoxLayout,
    QLabel,
    QTextBrowser,
    QFrame,
)
from qgis.PyQt.QtGui import QPixmap

from Webservices_Enercoop.utils.plugin_globals import PluginGlobals


class AboutBox(QDialog):
    """
    About box of the plugin
    """

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        mainLayout = QVBoxLayout()

        logo_file_path = PluginGlobals.instance().logo_file_path
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap(logo_file_path))
        mainLayout.addWidget(self.logo)

        title = u"À propos de l'extension Webservices Enercoop…"
        description1 = """Extension pour QGIS donnant un accès simplifié aux ressources géographiques qu'Enercoop utilisent""".format(
            PluginGlobals.instance().PLUGIN_VERSION
        )
        description2 = """Plus d'informations à l'adresse suivante : <a href="https://github.com/enercoop/prodspection/tree/main/qgis/QgisEnercoopPlugin/Webservices_Enercoop">GitHub </a>""".format(
            PluginGlobals.instance().PLUGIN_SOURCE_REPOSITORY
        )
        description3 = """Merci aux créateurs des plugins <a href="https://github.com/geo2france/idg-qgis3-plugin">Géo2France </a>, <a href="https://github.com/geobretagne/qgis-plugin">GéoBretagne</a> , <a href="https://gitlab.in2p3.fr/letg/indigeo-for-qgis">Indigéo </a> et <a href="https://github.com/geograndest/qgis-plugin">geograndest </a> sur lesquels ce plugin est basé !"""

        self.textArea = QTextBrowser()
        #        self.textArea.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.textArea.setOpenExternalLinks(True)
        self.textArea.setReadOnly(True)
        self.textArea.setHtml(description1)
        self.textArea.append(description2)
        self.textArea.append(description3)
        self.textArea.setFrameShape(QFrame.NoFrame)
        mainLayout.addWidget(self.textArea)

        self.setModal(True)
        self.setSizeGripEnabled(False)

        self.setLayout(mainLayout)

        self.setFixedSize(500, 350)
        self.setWindowTitle(title)
