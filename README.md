
# Aleksandra Kula - Boat Rental

[![Build Status](https://travis-ci.org/OlaQla/BoatRental.svg?branch=master)](https://travis-ci.org/OlaQla/BoatRental)

Code Institute, Full Stack Frameworks with Django 2019/2020

# Introduction

"Boat rental" service is a Django application created for educational purpose that will be hosted online. As an educational exercise the goal is to implement full stack application using Python and Django framework, with well styled interactive frontend featuring data storage, search capabilities, account management, autohization and authentication, checkout and transaction history. 

## Project purpose

The purpose of application is to let people search for luxurious boats for rent, check their availability, make a booking for selected dates and finalize the transaction with a payment. 
Customers are able to register an account in a service, browse the boat catalog or use search functionality to help them find exactly the boat they are looking for. 
Customers can view details and pictures of boats they are interested in and if they find one they would like and it is available they can place it in a basket and finalize transaction by processing the credit card payment of the contents of their basket. 
Each customer can view history of their transactions.

## Demo

# Programming language and libraries

For the purpose of creating boat rental service following programming languaes and libraries were used: 

**Python (3.7.4)**
Scripting language available on multiple platforms that is used for writing backend code (data management, application configuration, interaction with operating system, environment variables and files)

**Django**
Modular web application framework written in Python, provides application structure and common components like authentication and authorization. 

**Boto3**
Amazon Web Services (AWS Cloud) client used for interation with files stored in S3 bucket (Simple Storage Service)

**Javascript**
Scripting language running in web browsers. It was used in projects for implementing inteactive frontend components, mainly the search component, though in current project it's use is rather sparse. Javascript (.js) files are stored as static files in folder static/js.
Integration with Stripe payments is done through stripe javascript client.

**jQuery**
Javascript library simplifying interaction with html elements, executing ajax queries and providing utility functions. jQuery is also required by some interactive bootstrap components. In the project jQuery was used to implement part of the search component. 

**CSS**
Web styling language used to apply styles to html document. All css is stored in a single, shared file style.css stored in static files css folder. 

**Bootstrap**
Library providing responsive, styled web components. Used on most of the templates and tuned with custom stylesheet.  

**Powershell**
CLI scripting language available on Microsoft Windows operating system by default. In the project it was used for minor scripting tasks like automating running linter and autopep against multiple .py files

**Stripe**

Payments provider and library.

# Tools used
- Balsamiq mockups
- Visual Studio Code with Python plugin (by Microsoft)
- pylint (added path C:\Users\aleks\AppData\Roaming\Python\Python37\Scripts)
- pycodestyle
- autopep8 ($ autopep8 --in-place --aggressive --aggressive <filename>)
- Postgresql windows client

# Payments
- Stripe

# Authentication and authorization
- Default Django mechanism
- Overriden default templates

# Django application structure
- Accounts
- Boats
- Cart
- Checkout

# API
- Description of all API endpoints
  
# Testing 
- 3 test types
- test coverage 
- coverage manage.py test, coverage report, coverage html, ./htmlcov/index.html

# Linting

In visual studio code with Python extension (by Microsoft) installed press Ctrl + Shift + P to open task context menu ...

- ls . -filter *.py -recurse | % { autopep8 --in-place --aggressive --aggressive $_.fullname }

# Deployment and hosting
- Code repository (https://github.com/OlaQla/BoatRental)
- CI/CD with Travis (https://travis-ci.org/OlaQla/BoatRental)
- Static content on S3 (custom_storages.py)
- Hosting on Heroku

# Limitations, further development

# Credits

** Purpose of this project is educational **