[![Build Status](https://travis-ci.com/llwasampijja/Store-Manager-Challenge-Two.svg?branch=develop)](https://travis-ci.com/llwasampijja/Store-Manager-Challenge-Two)          [![Coverage Status](https://coveralls.io/repos/github/llwasampijja/Store-Manager-Challenge-Two/badge.svg?branch=develop)](https://coveralls.io/github/llwasampijja/Store-Manager-Challenge-Two?branch=develop)          [![Maintainability](https://api.codeclimate.com/v1/badges/57f01820e2adec3aaf6b/maintainability)](https://codeclimate.com/github/llwasampijja/Store-Manager-Challenge-Two/maintainability)

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
This API has been developed using Python3.
## Installing
### Pre-Installations
##### Python3 Installation
Since this API was developed using Python, you need to first install python3 in order to be able to run it. You can download python from [here](https://www.python.org/downloads/ "Official Python Site").
##### Flask Installation
You also need to install flask on your machine. Head to the [Flask Download Site](http://flask.pocoo.org/docs/1.0/installation/ "flask.pocoo")  for instructions on how to install Flask on your machine.
##### Git Installation
You can also install git, although it is not mandatory to run this application. However, it should be noted that you won’t be able to view the different branches in this project without git. If you need git, head to [Git ](https://git-scm.com/downloads "Official Git Download Site")  and follow the steps provided to install git on your machine.
##### Postman installation
You may also need to install postman (or any of its alternatives so as to test the different endpoints of this application. You won’t be able to test the endpoints in the browser since they (the endpoints) use other HTTP methods other than the “GET” method.

### Installing the Project on Your Machine
You can download the project by clicking on the “clone or download” button in the top right corner of this page. If you have git installed, you can choose to clone it using the URL; if not, just click the “download zip” option. Extract the contents of the zipped folder and you are done.
### Other Requirements
You may need to install other packages which are listed in the “requirements.txt” file. Depending on your preferences, these may be installed in a virtual environment or on your PC using pip.
## Running the Application
To run this application, navigate to the extracted folder via the Terminal or command prompt, and run the command below:
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
pytest
* To generate a coverage report of the unite tests, run the command add “—cov” to the above command.
* That is the command will now be:
`pytest –cov`
## URL Versioning
The endpoints of this application have been versioned. The current version is one (1); i.e.: `api/v1`

## Deployed Version
This API is deployed on heroku. Find it [here](https://store-manager-two.herokuapp.com/api/v1 "Store Manager on Heroku")
