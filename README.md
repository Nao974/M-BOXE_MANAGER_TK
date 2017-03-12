# M-BOXE_MANAGER_TK

To manage your M-BOXE Servo-motor with GUI from a Rapsberry Pi by I2C  


*Gérer votre M-BOXE Servo-moteur par interface graphique à partir d'une Rapsberry Pi par I2C*

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK.png" title="Screenshoot Menu" alt="ScrenShoot Menu">

## First of all / Avant tout

This program is an implementation of the `mboxe.py` library, allowing to parameterize and order an M-Boxe whose construction is detailed in the repository [M-BOXE] (https://github.com/Nao974/M-BOXE/blob/master/README.md)  


*Ce programme est une mise en oeuvre de la librairie `mboxe.py`, permettant de paramétrer et commander une M-Boxe dont la construction est detaillée dans le dépot [M-BOXE] (https://github.com/Nao974/M-BOXE/blob/master/README.md)*  

## Contents / Contenu

`Ah_I2C.py` Libraries for I2C protocol from the ADAFRUIT_I2C library
`M-BOXE.py` Class defining the M-BOXE object with parameter and function based on the Ah-I2C.py library  


`M-BOXE_MANAGER_TK.py` Main program for setting up your M-BOXE  


`frame__.py` Description of application frameworks  
`interface.py` Creating the interface with calls from different frames and the menu    
`lang__.py` Language files  

--

*`Ah_I2C.py` Librairie pour protocole I2C issue de la librairie ADAFRUIT_I2C*  
*`M-BOXE.py` Classe définissant l'objet M-BOXE avec paramétre et fonction s'appuyant sur la librairie Ah-I2C.py*  


*`M-BOXE_MANAGER_TK.py` Programme principal permettant le paramétrage de votre M-BOXE*  


*`frame__.py` Description des cadres de l'application*    
*`interface.py` Création de l'interface avec appels des différents cadres et du menu*  
*`lang__.py` Fichiers des langues*  


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

Go to folder, then type `python3 M-BOXE_MANAGER_TK.py`, or lunch with Python IDE.  
  

###Scanning the I2C bus and connecting to an M-BOXE

Start a reseach:  
<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Scan.png" title="Mboxe/To Scan" alt="Mboxe/To Scan">  
The M-BOXE list appears in the `Mboxe` menu, just select one.


###Frame Main Config

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Main.png" title="Frame Main" alt="Frame Main">  
Enables you to view the status of the M-BOXE, the firmware version and specify configuration information.

* Get from Memeory
Allows to reload the configuration of the M-BOXE selected in the Manager

* Set in Memory
Allows the manager to go back to the M-BOXE RAM
 
* Reload from EEPROM
Allows you to reload the configuration saved in the EEPROM into the RAM memory of the M-BOXE and then upload it to the Manager
 
* Write in EEPROM
Allows the Manager's current configuration to be lowered to the M-BOXE's RAM and then saved in the EEPROM


###Frame Advanced  

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Advanced.png" title="Frame Advanced" alt="Frame Advanced">  
Allows the adjustment of the parameters described in the document[Parameter_M-BOXE.pdf](https://github.com/Nao974/M-BOXE/blob/master/doc/Parameter_M-BOXE.pdf).  


###Frame Position

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Position.png" title="Frame Position" alt="Frame Position">  
* Allows you to set the front and rear terminals
* To retrieve the current position with the `Get` button
* Send the position setpoint with the `Set` button


###Frame Speed

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Speed.png" title="Frame Speed" alt="Frame Speed">  
*Coming Soon*


###Frame Data

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Data.png" title="Frame Data" alt="Frame Data">  
To view the various data recorded by the M-BOXE, see document[Parameter_M-BOXE.pdf](https://github.com/Nao974/M-BOXE/blob/master/doc/Parameter_M-BOXE.pdf).  
* This data is updated every time the M-Boxes are reloaded by the `Get from Memeory` button on the Main frame
* The check mark `Real Time` allows a loop playback whose delay and set by the adjoining ruler.


###Frame Log

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Log.png" title="Frame Log" alt="Frame Log">  
Allows a detailed reading of the operations carried out.

--

Aller dans le dossier, puis tapez `python3 M-BOXE_MANAGER_TK.py`, ou lancez le à partir de l'IDE Python.  


###Scan du bus I2C et connexion à une M-BOXE  

Lancer la recherche:  
<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Scan.png" title="Mboxe/To Scan" alt="Mboxe/To Scan">  
La liste des M-BOXE apparait dans le menu `Mboxe`, il vous suffit d'en selectionner une.  


###Cadre Main Config  

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Main.png" title="Frame Main" alt="Frame Main">  
Permet de visualiser l'état de la M-BOXE, la version du firmware et indiquer des informations sur la configuration.  

* Get from Memeory  
Permet de recharger la configuration de la M-BOXE selectionnée dans le Manager  

* Set in Memory  
Permet de faire redescendre la configuration actuelle du Manager vers la mémoire vive de la M-BOXE  
 
* Reload from EEPROM  
Permet de recharger dans la mémoire vive de la M-BOXE, la configuration sauvegardée dans l'EEPROM, puis la faire remonter dans le Manager  
 
* Write in EEPROM  
Permet de faire redescendre la configuration actuelle du Manager vers la mémoire vive de la M-BOXE, puis la sauvegarder dans l'EEPROM   


###Cadre Advanced  

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Advanced.png" title="Frame Advanced" alt="Frame Advanced">  
Permet le réglage des paramètres décrits dans le document [Parameter_M-BOXE.pdf](https://github.com/Nao974/M-BOXE/blob/master/doc/Parameter_M-BOXE.pdf).  


###Cadre Position

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Position.png" title="Frame Position" alt="Frame Position">  
* Permet de paramétrer les bornes avant et arriere  
* De récuperer la position actuelle avec le bouton `Get`  
* D'envoyer la consigne de position avec le bouton `Set`


###Cadre Speed

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Speed.png" title="Frame Speed" alt="Frame Speed">  
*Prochainement*


###Cadre Data

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Data.png" title="Frame Data" alt="Frame Data">  
Permet de visualiser les différentes données remontées par la M-BOXE, voir le document [Parameter_M-BOXE.pdf](https://github.com/Nao974/M-BOXE/blob/master/doc/Parameter_M-BOXE.pdf).  
* Ces données sont mises à jour à chaque rechargement des paramétres de la M-Boxe par le bouton `Get from Memeory` du cadre Main  
* la coche `Real Time` permet une lecture en boucle dont le delai et paramétré par la reglette voisine.  


###Cadre Log

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Log.png" title="Frame Log" alt="Frame Log">  
Permet une lecture détaillée des opérations effectuées.   


## History / Historique

- [History] (https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/history.md)


