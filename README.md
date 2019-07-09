# Mac Address Application
This application utilizes the macaddress.io API to look up the company name based on MAC address.

# Requirements
Please follow the below steps to obtain an API key. Also chose one of the requirement options.

## Obtaining an API key
Please register for an account or log into https://macaddress.io/ to obtain an API key. Please store the API key somewhere to be used in running the application.

### Option 1: Using Application on the Command Line
The request library is required to use this script with a python interpreter.
> pip install --trusted-host pypi.python.org 
 requests

### Option 2: Using Application in a Container
A docker image is required to run the application in a dockerized container.
> docker build --tag=mac_app .

# Running the Application
## Command Line
please insert the required arguments below:

> ./mac_address.py    *<"INSERT API KEY"> <"INSERT MAC ADDRESS">*

## Docker Container
After building the image in Option2 in the Requirements, you can run the application by passing arguments to docker:

> docker run mac_app *<"INSERT API KEY"> <"INSERT MAC ADDRESS">*

# Security Considerations
Although the API key is not being store as a variable, it is being passed to the application via the command line and this risk should be considered.

Users of this application should also consider security regarding the implementation of https.

In addition, the use of Docker may also introduce additional security risks