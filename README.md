
[![Build Status](https://travis-ci.com/llwasampijja/Store-Manager-Challenge-Two.svg?branch=feature)](https://travis-ci.com/llwasampijja/Store-Manager-Challenge-Two)          [![Coverage Status](https://coveralls.io/repos/github/llwasampijja/Store-Manager-Challenge-Two/badge.svg?branch=feature)](https://coveralls.io/github/llwasampijja/Store-Manager-Challenge-Two?branch=feature)          [![Maintainability](https://api.codeclimate.com/v1/badges/57f01820e2adec3aaf6b/maintainability)](https://codeclimate.com/github/llwasampijja/Store-Manager-Challenge-Two/maintainability)


# Store Manager API Endpoints
This project is about a set of endpoints for the Store Manager App. The data used in testing the various endpoints is stored in memory using data structures and not a database.
The endpoints include:
* Endpoint for viewing all the products.
* Endpoint for retrieving a product by its product id.
* Endpoint for adding a product.
* Endpoint for updating a product
* Endpoint for creating a sale record.
* Endpoint for retrieving a sale record by its id/index.
* Endpoint for retrieving all sale records.

## Table of Contents
- [Language](##Language)
- [Installing](##Installing)
- [Running the application](##RunningtheApplication)
- [Unit Testing the app](##UnitTestingtheApplication)
- [Available Version](##URLVersioning)
- [Deployed Version](##DeployedVersion)

## Language
This API has been developed using [Python3](https://www.python.org).
## Installing
### Pre-Installations
##### Python3 Installation on Windows PC
Since this API was developed using Python, you need to first install python3 in order to be able to run it. You can download python from [here](https://www.python.org/downloads/ "Official Python Site").
After downloading it, double click the executable file and follow the prompts to install python on your machine.
##### Git Installation on Windows PC
You can also install git, although it is not mandatory to run this application. However, it should be noted that you won’t be able to view the different branches in this project without git. If you need git, head to [Git ](https://git-scm.com/downloads "Official Git Download Site")  and the executable file.
Double click the executable file to run the installer and follow the prompts to install it on your windows PC. The process of installing git installs two tools which you can use, that is the Git Bash and Git GUI. For this project, you are going to use Git Bash for all the command-line prompt /terminal commands.
##### Postman installation On Windows PC
You will need to install postman (or any of its alternatives) so as to test the different endpoints in this application. You won’t be able to test the endpoints in the browser since they use other HTTP methods other than the “GET” method.
To use postman, you need to install chrome as it (postman) is an extension of chrome. Install postman and postman interceptor extensions.

### Installing Requirements
All the requirements required to run this application are listed in the requirements.txt file in the root folder of the project.
While in the folder, run the command below to install these requirements.

`pip3 install -r requirements.txt`

### How to Clone This Repository to Your Local Machine (Windows PC)
- Step 1: Create folder on your local machine and give it any name you want.
- Step 2: Open the git bash tool and navigate to the folder that you just created in the step above.
- Step 3: Now run this command in git bash CLI.

`git clone https://github.com/llwasampijja/Store-Manager-Challenge-Two`

This will copy the entire project onto your local machine. Project name should be “Store-Manager-Challenge-Two”
- Step 4: Navigate to that folder in git bash and change from the master branch to feature branch using the command below

`Git checkout feature`

And now you have successfully cloned the project and also configured it to run it on your computer.


## Running the Application
To run this application, navigate to the root folder of the project via the Terminal or command prompt, and run the command below:

`py main.py`

On running that command, the application server will be launched and the URL to that server will be shown to you in the command-line/terminal.

#### Trying out the different Endpoints using postman
|Endpoint|Endpoint Purpose|Allowed HTTP Method|Requirements|
|---|---|---|---|
| /products  | Return all products  |GET  | None |
| /products/product_id | Return product with specified product_id  |GET  |None  |
| /products/add | Add a product  |POST  |•	product_id (int), product_name (string), unit_price (int), category (string), stock_date (string), quantity (int), acceptable_minimum (int) •	Must be an admin|
| /products/product_id  | Update product  |PATCH  |•	Any or some of all of below: product_id (int), product_name (string), unit_price (int), category (string), stock_date (string), quantity (int), acceptable_minimum (int) •	Must be an admin |
| /sales  | Get all sale records  |GET  |Must be an admin  |
| /sales/sale_index  | Get a sale record of specified sale_index  |GET  |Must be an admin or the store attendant who created the sale.  |
| /sales/add  | Create a sale record  |POST  |Must be a store attendant.  |


NB: You can switch the API privileges from the utilities.py file under the app folder.
## Unit Testing the Application
* In order to run unit tests for this application, you must install pytest, pytest-cov and coverage installed on your pc or virtual environment.
* While in the root of the project, run the command below to run the unit test.

`pytest`

* To generate a coverage report of the unite tests, run the command add “—cov” to the above command.
* That is the command will now be:

`pytest –cov`

## URL Versioning
The endpoints of this application have been versioned. The current version is one (1); i.e.: `api/v1`

## Deployed Version
This API is deployed on heroku. Find it [here](https://store-manager-two.herokuapp.com/api/v1 "Store Manager on Heroku")


 The postman collections can be found [here](https://web.postman.co/collections/5689256-a13e8abe-46dc-514f-638d-38d2be40c2a2?workspace=6f3eb107-ee9c-4777-8d0e-a855b8794983)