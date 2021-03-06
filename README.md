# THE PASSWORD LOCKER

## Brief Description
#### Python app that helps in Accounts and Passwords management, February 2022

## Author
#### *Kelvin Karanja*

## Screenshot
<img src='https://github.com/KaranjaK/Password-Locker/blob/master/Images/p1.png'>

## User Stories
The user would like to.... :
* To create an account for the application or log into the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the account name.
* Delete stored account login details that i do now want anymore.
* Copy my credentials to the clipboard

## Setup/Installation Requirements
### For the application to run, install
* Python3.8
* pyperclip
* pip

### Cloning
* Open Terminal {Ctrl+Alt+T}
* Git clone: https://github.com/KaranjaK/Password-Locker
* cd Password-Locker
* code . or atom . based on the text editor you have.

### Running the Application
* To run the applicaton, change directory to where you have cloned and run the following commands:
        $ chmod +x interface.py
        $ ./interface.py

# Behavior Driven Development 
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./interface.py```|Hello Welcome to your Accounts Password Store... <br>* CA ---  Create New Account * LI ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```D```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```D```| The application exits|

## Known Bugs
* The are no known bugs as per now. However, for any bugs detected, pull requests are allowed.

## Technologies Used
* python3.8

## Support and contact details
For any further clarifications or inquiry, kindly reach out @ karanjakelvin77@gmail.com

### License
MIT License
Copyright (c) 2022 Kelvin Karanja
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.