# M-BOXE_MANAGER_TK
[Version Française](https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/README_FR.md)  

To manage your M-BOXE Servo-motor with GUI from a Rapsberry Pi by I2C.  

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK.png" title="Screenshoot Menu" alt="ScrenShoot Menu">

## First of all

This program is an implementation of the `mboxe.py` library, allowing to parameterize and order an M-Boxe whose construction is detailed in the repository [M-BOXE](https://github.com/Nao974/M-BOXE/blob/master/README.md).  

## Contents

`Ah_I2C.py` Libraries for I2C protocol from the ADAFRUIT_I2C library  
`M-BOXE.py` Class defining the M-BOXE object with parameter and function based on the Ah-I2C.py library  


`M-BOXE_MANAGER_TK.py` Main program for setting up your M-BOXE  


`frame__.py` Description of application frameworks  
`interface.py` Creating the interface with calls from different frames and the menu    
`lang__.py` Language files  


## Installation

#### Step 1: Install Python3

Python 3.4 is already installed if you use 'python3' instead of 'python', if it's not the case `sudo apt-get install python3`.  
TKinter is part of standard Python libraries.There is no need to install it.  


#### Step 2: Active I2C

* Comment the line `blacklist i2c-bcm2708` in the file `/ etc / modprobe.d / raspi-blacklist.conf`
* Install the suite of I2C management tools `apt-get install i2c-tools`
* Restart your Raspberry.

Once your M-BOXE is set up and connected to the I2C bus, type `i2cdetect -y 1` (replace '1' with '0' with 256MB versions):  
<img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/i2cdetect.png" title="screenshoot_i2cdetect" alt="screenshoot_i2cdetect">  


## Usage

Go to folder, then type `python3 M-BOXE_MANAGER_TK.py`, or lunch with Python IDE.  
  

### Scanning the I2C bus and connecting to an M-BOXE

Start a reseach:  
<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Scan.png" title="Mboxe/To Scan" alt="Mboxe/To Scan">  
The M-BOXE list appears in the `Mboxe` menu, just select one.


### Frame Main Config

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


### Frame Advanced  

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Advanced.png" title="Frame Advanced" alt="Frame Advanced">  
Allows the adjustment of the parameters described in the document: [Parameter_M-BOXE.pdf](https://github.com/Nao974/M-BOXE/blob/master/doc/Parameter_M-BOXE.pdf) .  


### Frame Position

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Position.png" title="Frame Position" alt="Frame Position">  
* Allows you to set the front and rear terminals
* To retrieve the current position with the `Get` button
* Send the position setpoint with the `Set` button


### Frame Speed

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Speed.png" title="Frame Speed" alt="Frame Speed">  
*Coming Soon*


### Frame Data

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Frame_Data.png" title="Frame Data" alt="Frame Data">  
To view the various data recorded by the M-BOXE, see document: [Parameter_M-BOXE.pdf](https://github.com/Nao974/M-BOXE/blob/master/doc/Parameter_M-BOXE.pdf) .  
* This data is updated every time the M-Boxes are reloaded by the `Get from Memeory` button on the Main frame
* The check mark `Real Time` allows a loop playback whose delay and set by the adjoining ruler.


### Frame Log

<img src="https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/screenshoot/Manager_TK_Log.png" title="Frame Log" alt="Frame Log">  
Allows a detailed reading of the operations carried out.


## History

- [History](https://github.com/Nao974/M-BOXE_MANAGER_TK/blob/master/history.md)


