# Plugin Webservices Enercoop

Plugin QGIS 3 fournissant des accès aux webservices cartographiques (WMS, WMTS, WFS, etc.) intéressants pour les salarié(e)s d'Enercoop. Pour l'installer, **il nécessite le VPN**.

Ce projet est un fork du plugin [GeoGrandEst](https://github.com/geograndest/qgis-plugin), lui-même étant un fork du plugin [Géo2France](https://github.com/geo2france/idg-qgis-plugin). Ce plugin a donné lieu à plusieurs forks : Géo2France a été forké par le [CRAIG](https://github.com/gipcraig/qgis-plugin), [GéoBretagne](https://github.com/geobretagne/qgis-plugin) a fait un fork de GéoGrandEst, et [Indigéo](https://gitlab.in2p3.fr/letg/indigeo-for-qgis/-/tree/master) a fait un fork de GéoBretagne (ouf!).

## Installation

### Pour les salariés

L'installation et l'utilisation du plugin est documentée dans la [doc interne](https://si.enercoop.org/eprod:plugin_webservices). Il est nécessaire d'ajouter au préalable le dépôt de plugins interne à la liste des dépôts d'extensions QGIS, étape nécessitant le VPN et documentée [ici](https://si.enercoop.org/eprod:depot_plugins).

### Pour les développeurs

Pour effectuer des modifications et des tests de code sur le plugin, il faut suivre la même procédure que les salariés pour installer une version locale de celui-ci, puis ouvrir le répertoire des plugins QGIS en allant dans (`Préférences > Profils utilisateurs > ouvrir le dossier du profil actif > python > plugins > Webservices_ENnercoop`) et effectuer ses modifications de code via un éditeur de code tel que Visual Studio Code.

Afin de voir en temps réel les modifications on peut utiliser le plugin [Plugin Reloader](https://plugins.qgis.org/plugins/plugin_reloader/) qui permet de recharger un plugin sans quitter QGIS. Il suffit de sélectionner l'îcone de Plugin Reloader aller dans `Configurer Plugin Reloder > Sélectionner l'extension à recharger > Webservices_Enercoop` et de cliquer sur `Recharger l'extension Webservices_Enercoop`

Une fois les modifications actives et fonctionnels, il faut alors les transférer dans le dépot local de Webservices Enercoop, afin de les passer en production.

## Mise à jour du plugin

Les mises à jour sont facilement faisible depuis QGIS grâce à un dépôt distant nécessitant le VPN d'activé. Pour le configuré ce référer [ici](https://si.enercoop.org/eprod:depot_plugins).
Pour mettre à jour le plugin depuis QGIS, il suffira alors d'aller dans (`Extensions > Paramètres > Recharger tous les dépôts > Mises à jour disponibles > Webservices Enercoop > Mettre à jour l'extension`)

## Séparation entre code `.py` du plugin et la liste de webservices `config.json`

### Simplicité d'évolution et confidentialité

Le plugin fonctionne grâce à 2 éléments distincts :

- Le code Python du plugin, que l'utilisateur installe avec le dépôt distant Enercoop.
- La liste des adresses de webservices chargée par le plugin au démarrage de QGIS, contenue dans le `config.json`.

Ainsi, les utilisateurs voient cette liste s'enrichir automatiquement de nouveaux webservices lorsqu'ils redémarrent QGIS, sans avoir besoin de télécharger une nouvelle version du plugin. Nous faisons évoluer la liste des webservices accessibles via le plugin indépendament de son code Python en modifiant le fichier `config.json` chargé à chaque démarrage de QGIS. Ce `config.json` est placé sur [public.geo.enercoop.org](https://public.geo.enercoop.org/plugins/), accessible et est accesible en public.

### Mise à jour du dépôt distant

Le plugin `.zip` et le `config.json` sont placés sur le serveur `geo`, dans le dossier `/var/www/public.geo.enercoop.org/plugins`, diffusés sur [public.geo.enercoop.org](https://public.geo.enercoop.org/plugins/).

L'ensemble est ensuite diffusé à travers un dépôt distant aux salariés:

Le dépôt d'extensions QGIS d'Enercoop est un point d'accès unique vers les plugins développés en interne permettant de faciliter leur installation et leur mise à jour. Ajouter ce dépôt d'extensions à votre QGIS vous permettra d'installer nos extensions, et surtout de les mettre à jour avec plus de facilité par la suite quand nous y apportons des améliorations. A ce jour, un seul plugin a été développé, Webservices Enercoop, et d'autres pourront suivre à l'avenir.

Le dépôt est un fichier XML demandant une structure bien précise. Comme le montre ce [guide](https://portailsig.org/content/creer-un-depot-d-extensions-pour-qgis.html) présente sur [public.geo.enercoop.org/plugins/](https://public.geo.enercoop.org/plugins/) accessible par VPN.

Lors d'une montée de version du plugin, la `version` présente dans le `plugins.xml` doit être montée, comme le nom du `.zip` présente dans [public.geo.enercoop.org/plugins/Webservices_Enercoop](https://public.geo.enercoop.org/plugins/Webservices_Enercoop/).

Pour cela on utilise le script `update_plugin.sh` en adaptant la `version` du script.

A l'avenir, pour rendre l'installation et la MAJ plus aisée, on pourra mettre le `.zip` du plugin sur un dépôt public, comme l'a fait Géo2France (cf. code [repo](https://github.com/geo2france/idg-qgis-plugin/tree/main/repo) et [lien](https://www.geo2france.fr/public/qgis3/plugins/plugins.xml) vers le dépôt), puis déclarer et activer celui-ci dans les dépôts d'extensions QGIS.

## Utilisation

Voir la [documentation interne](https://si.enercoop.org/eprod:qgis_plugin_webservices).
