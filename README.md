# **What's this?**
This is a django project meant to be run locally that gives you your OAuth 2.0 tokens needed to interact with Conta Azul's API

## **Prerequisites**
### **Creating Your Conta Azul consumer application**
First of all, if you haven't done this, before getting your tokens, you need to head over to https://portaldevs.contaazul.com/ and create an application. **PLEASE NOTE THAT THE APPLICATION'S REDIRECT_URI SHOULD BE SET TO http://localhost:8000/auth/get-token FOR THIS SERVER TO WORK**

### **Setting up environment variables**
After your application is created, you will need to set the following environment variables [How to set up environment variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html):
* **CONTA_AZUL_CLIENT_ID**: The value of this environment variable should match you application's client_id

* **HASHED_CONTA_AZUL_CLIENT_CREDENTIALS**: This one is a bit trickier to set up right, but shouldn't take more than 2 minutes. What you need to do is to head over to 
https://www.base64encode.org/ and encode to base 64 the string made of your client id and secret separated by a colon: {client_id}:{client_secret}.   
Example: QsaiBIwQWJBcHTHHcQza:MhRFOTswQlzwJUzfOATW is               UXNhaUJJd1FXSkJjSFRISGNRemE6TWhSRk9Uc3dRbHp3SlV6Zk9BVFc= once encoded.  
The encoded string should be the value of this environment variable

### **Installing python and Django (Ignore if already installed in your machine)**
As descbribed, the server is built with Django, so you will need to have Python and it's dependencies installed to run the server.  
The simplest way to do this is to install python, open a terminal in the project's root folder, and run:  
 ```pip install requirements.txt```  
This will install Django, the requests lib, and django's dependencies. So you will be able to run the server


## **How to get your tokens?**
Simply run the server through the terminal with  ```python manage.py runserver```, go to http://localhost:8000/auth/authorize, log into your conta azul account and click on "Autorizar". This will generate a file called *token.json* in the root of the project with your credentials.

If you have any doubts or need help regarding the API (after all, the official documentation on the authentication flow is subpar to say the least), please feel free to contact me through my email: fabio.david.contato@gmail.com