
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

Payments provider and javascript library.

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

Application is using authentication and authorization mechanisms in order to identify users and provide relevant contents accoring to their identity and access levels. There are application pages that can be browsed without having an account and having to log in, like homepage or boat catalog. Then there are pages that require user to be logged in to see the content related to their account like for example profile page or checkout. There is also and admin page that requires user to have administrative priviledges. 
Most of the authentication and authorization is done by enabling and customizing existing Django mechanisms ("accounts.backends.EmailAuth", "django.contrib.auth.backends.ModelBackend"). 
Sending emails is using another Django mechanism ("django.core.mail.backends.smtp.EmailBackend") and is configured to utilize gmail smtp gateway. 
In addition to configuring existing mechanisms in templates/registration folder i have created customized templates that override default django templates and provide look and feel of password related emails consistent with the rest of the application. 

# Django application structure

Django application consists of multiple reusable components that are in Django nomenclature also called applications. Django is pluggable, extensible and provides multiple applications out of the box. To implement mu project I used following default Django applications: 

- django.contrib.admin
- django.contrib.auth
- django.contrib.contenttypes
- django.contrib.sessions
- django.contrib.messages
- django.contrib.staticfiles

I have added some applications not delivered with default Django installation. For the purpose of working with bootstrap and especially forms presented with bootstrap styles i used: 

- django_forms_bootstrap
- crispy_forms

And in order to configure and use S3 bucket i used application: 
- storages

I have also created some applications for handling different parts of the solution, which are described below: 

|Application name | Purpose |
|homepage|The main page of application|
|accounts|Handling user account registration, profile and log-in / log-out|
|boats|Boat catalog, boats data and availability for calendar view|
|reviews|Site reviews listing and loading|
|comments|User comments on provided boats|
|cart|Handling user cart management|
|checkout|Selected products checkout, stripe integration for card processing|

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

Application code is stored in a public github repository specially created for the project (https://github.com/OlaQla/BoatRental). Thanks to using git (distributed version control system) and github (git hosting platform owned by Microsoft) it is easy to share the code, track changes in application logic and assets and if needed to revert unwanted changes. 

For the purpose of validating code on all code check-ins before it gets deployed and potentially something gets broken, In Travis CI there is a dedicated project configured (https://travis-ci.org/OlaQla/BoatRental) to run the tests and either allow or block the deployment. 
In code repository i have created a file .travis.yml that contains configuration instructing Travis how to build the project and instructs it to run included tests.
Travis also provides a successful / failing build badge that helps visually indicate if code stored in repository is in healthy state. 

Production version of application (http://boat-rental.herokuapp.com/) is hosted on a free tier of Heroku platform. In Heroku i have created dedicated project and connected it to code stored in github repository in CD (continuous delivery) fashion, what makes the most recent version of code to be deployed automatically after it's pushed to code repository and passes validation in Travis. 
In Heroku application is utilizing a Heroku managed PostgreSQL database which was the easiest way of attaching production database to hosted application. 
For the purpose of correctly building application for hosting in Heroku container i have installed python package django-heroku (v.0.3.1).
In settings.py i had to import django_heroku package and at the end of the file i have added an invocation of a django_heroku.settings function to correctly set application options for hosting.

Media files are stored in AWS S3 bucket. It is due to Heroku dynos storage not being persistent what would make uploaded media files to go away if application was to be scheduled in a different dyno which is in Heroku nomenclature type of a virtual machine. Heroku applications could be scheduled in different dynos after each deployment, when old application instance is removed and a new one is created. Free tier dynos are also not guaranteed to be active all the time and can be recycled and application scheduled on a different node when someone tries to access it. 
AWS S3 has a free tier that provided me with enough capacity to host the files i needed. 
In order to host media files in a folder in S3 bucket in a transparent way for the application i have created and custom storage for media files in custom_storages.py and plugged it in settings.py as a media file storage class.

Static files are hosted in the same S3 bucket as media files. The reason for hosting static files in S3 bucket are that it provides potentially better bandwidth and quicker response times due to being architected in a way to serve files efficiently, rather than running applications. 
To avoid clashing in the same bucket with media files, i have created a custom storage for static files (inheriting from S3Boto3Storage class) and configured it in settings.py. 
I found few issues when trying to push static files to the bucket. First issue was that when running manage.py collectstatic command i expected files to be uploaded to S3 storage, instead files were collected locally only and nothing was uploaded. I googled for potential solutions until i found a suggestion on stackoverflow (https://stackoverflow.com/questions/49742714/collecstatic-does-not-push-to-files-s3) that it might be related to open issue in django_heroku package (https://github.com/heroku/django-heroku/issues/25). After passing parameter `staticfiles=False` to django_herku.settings call the collectstatic started working as expected. 
Once files were uploaded i found the second issue that static files were not served correctly from S3 bucket, images were missing, there was not styling on a page and layout was broken due to browser nto being able to validate https certificate correctly. The issue appeared to be the name of the bucket, which contained `.` and broser was unable to identify which part of url is the domain name. Solution to this problem was to create a new bucket with dash, instead of dot in the name. 
After thatchange i could see in developer tools network tab that all the assets are loaded from S3 bucket correctly and they are being updated before every deployment of the application. 
 
# Limitations, further development

# Credits
  
** Purpose of this project is educational **