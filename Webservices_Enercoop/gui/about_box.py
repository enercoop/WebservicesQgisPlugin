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

        # Initialize the dialog
        QWidget.__init__(self, parent)

        # Create a vertical layout for the dialog
        mainLayout = QVBoxLayout()

        # Get the path to the logo file from plugin globals
        logo_file_path = PluginGlobals.instance().logo_file_path

        # Create a label for displaying the plugin logo
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap(logo_file_path))
        mainLayout.addWidget(self.logo)

        # Define the title and descriptions for the About box
        title = u"À propos de l'extension Webservices Enercoop ..."
        description1 = """Extension QGIS 3 simplifiant, via un panneau, l'accès aux services webs utilisés par les salarié⋅es d'Enercoop.
        \n Documentation interne : https://si.enercoop.org/eprod:qgis:extensions:webservices_enercoop
        \n Code source : https://github.com/enercoop/WebservicesQgisPlugin""".format(
            PluginGlobals.instance().PLUGIN_VERSION
        )
        description2 = """Plus d'informations à l'adresse suivante : <a href="https://github.com/enercoop/prodspection/tree/main/qgis/QgisEnercoopPlugin/Webservices_Enercoop">GitHub </a>""".format(
            PluginGlobals.instance().PLUGIN_SOURCE_REPOSITORY
        )
        description3 = """Merci aux créateurs des plugins <a href="https://github.com/geo2france/idg-qgis3-plugin">Géo2France </a>, <a href="https://github.com/geobretagne/qgis-plugin">GéoBretagne</a> , <a href="https://gitlab.in2p3.fr/letg/indigeo-for-qgis">Indigéo </a> et <a href="https://github.com/geograndest/qgis-plugin">geograndest </a> sur lesquels ce plugin est basé !"""

        # Create a QTextBrowser widget for displaying the descriptions
        self.textArea = QTextBrowser()
        # self.textArea.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.textArea.setOpenExternalLinks(True)  # Enable external links
        self.textArea.setReadOnly(True)  # Make the text area read-only
        self.textArea.setHtml(description1)
        self.textArea.append(description2)
        self.textArea.append(description3)
        self.textArea.setFrameShape(QFrame.NoFrame)  # Remove frame
        mainLayout.addWidget(self.textArea)

        # Set dialog properties
        self.setModal(True)  # Make it a modal dialog
        self.setSizeGripEnabled(False)  # Disable size grip

        # Set the layout for the dialog
        self.setLayout(mainLayout)

        # Set the fixed size of the dialog
        self.setFixedSize(500, 350)

        # Set the title of the dialog
        self.setWindowTitle(title)
