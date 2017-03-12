# M-BOXE_MANAGER_TK

To manage your M-BOXE Servo-motor with graphic interface from a Rapsberry Pi by I2C  


*Gérer votre M-BOXE Servo-moteur par interface graphique à partir d'une Rapsberry Pi par I2C*

<img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/Manager_TK.png" title="Screenshoot Menu" alt="ScrenShoot Menu">

## First of all / Avant tout

This program allows to parameterize an M-Boxe whose construction is detailed in the deposit [M-BOXE] (https://github.com/Nao974/M-BOXE/blob/master/README.md)  


*Ce programme permet de paramétrer une M-Boxe dont la construction est detaillée dans le dépot [M-BOXE] (https://github.com/Nao974/M-BOXE/blob/master/README.md)*  

## Contents / Contenu

`Ah_I2C.py` Libraries for I2C protocol from the ADAFRUIT_I2C library
`M-BOXE.py` Class defining the M-BOXE object with parameter and function based on the Ah-I2C.py library  


`M-BOXE_MANAGER_TK.py` Main program for setting up your M-BOXE  


`frame_*.py` Description of application frameworks  
`interface.py` Creating the interface with calls from different frames and the menu    
`lang_*.py` Language files  

--

*`Ah_I2C.py` Librairie pour protocole I2C issue de la librairie ADAFRUIT_I2C*  
*`M-BOXE.py` Classe définissant l'objet M-BOXE avec paramétre et fonction s'appuyant sur la librairie Ah-I2C.py*  


*`M-BOXE_MANAGER_TK.py` Programme principal permettant le paramétrage de votre M-BOXE*  


*`frame_*.py` Description des cadres de l'application*    
*`interface.py` Création de l'interface avec appels des différents cadres et du menu*  
*`lang_*.py` Fichiers des langues  


## Installation

####Step 1: Install Python3

Python 3.4 is already installed if you use 'python3' instead of 'python', if it's not the case `sudo apt-get install python3`.  
TKinter is part of standard Python libraries.There is no need to install it.  

*Python 3.4 est normalement déja installé sur Raspbian si vous utilisé `python3`au lieu de `python`, si ce n'est pas le cas `sudo apt-get install python3`.*  
*TKinter fait partie des librairies standards de Python.Il n'est pas besoin de l'installer.*


####Step 2: Active I2C

* Comment the line `blacklist i2c-bcm2708` in the file `/ etc / modprobe.d / raspi-blacklist.conf`
* Install the suite of I2C management tools `apt-get install i2c-tools`
* Restart your Raspberry.

Once your M-BOXE is set up and connected to the I2C bus, type `i2cdetect -y 1` (replace '1' with '0' with 256MB versions):  
<img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/i2cdetect.png" title="screenshoot_i2cdetect" alt="screenshoot_i2cdetect">  


* *Mettre en commentaire la ligne `blacklist i2c-bcm2708` dans le fichier `/etc/modprobe.d/raspi-blacklist.conf`*
* *Installez la suite des outils de gestion I2C `apt-get install i2c-tools`*
* *Redémarrer votre Raspberry.*

*Une fois votre M-BOXE paramétrée et connectée au bus I2C, tapez la commande `i2cdetect -y 1` (remplacer '1' par '0' par les versions 256Mo).*  
*Dans l'exemple ci dessus, la M-BOXE est configurée à l'adresse 0x14.*  


## Usage

Go to folder, then type `python3 M-BOXE_MANAGER_TK.py`, or lunch with Python IDE
  <img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/Manager_TK_go.png" title="Go" alt="Go">  
  
  **Writing in progress**  

--

*Aller dans dossier, puis tapez `python3 M-BOXE_MANAGER_TK.py`, ou lancez le à partir de l'IDE Python.

**Rédaction en cours**  


## History / Historique

- [History] (https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/history.md)


