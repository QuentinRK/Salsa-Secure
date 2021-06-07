# Salsa Secure


Salsa Secure is a GUI application that is used to encrypt directories with sensitive or private information.
Salsa Secure implements the salsa20 cipher which is used for the encryption along with multiple hashing alogrithims. 
To get started follow the simple steps below.


## Table Contents

* [SetUp](#setup)
* [Technologies](#technologies)
* [Encryption](#encryption)
* [Decryption](#decryption)
* [Notes](#notes)


## SetUp

* The requirements.txt is located in the repository
* Download the code and install the dependencies in a virutal environment 
* Run the main.py file 


## Technologies

* PYQT5
* Python 3.8.3
* CSS 


## Encryption 
* To encrypt a directory simply press the encrypt button. 
* This will prompt a window where you can select a directory of your choice.
* Once a directory has been selected, choose a secure password (do not forget the password as this is validated & used for decryption).


## Decryption 

* To decrypt an encrypted file simply press the decrypt button.
* The password used to encrypt the folder must be entered in order to decrypt the .tar file
* Once the password has been validated the decryption process will begin.


![Image alt text](code/imgs/Salsa-secure.png?raw=true)

## Notes 

* Large directories may take a while to compress, ensure that Salsa Secure runs to completion.
* dmg and exe files are coming soon 
