# WhatsMappening

This project is made in conjuction with the course [TBA4250 - Geographic Information Handling 2, Basic Course.](https://www.ntnu.edu/studies/courses/TBA4250#tab=omEmnet) taught at the Norwegian University of Science and Technology.

This is a web applications that allowed users to create, share and manage events on a online map.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine

### Prerequisites

What things you need to install the software and how to install them

* [Python](https://www.python.org/) - version 3.4 or higher
* [PostgreSQL](https://www.postgresql.org/) - PostgreSQL for database in order to use PostGIS

Linux/Max:
* [GDAL](http://www.gdal.org/) - Geospatial Data Abstraction Library

Windows:
* [OSGeo4W](https://trac.osgeo.org/osgeo4w/) - includes many geospatial libraries such as GDAL


### Installing

A step by step series of examples that tell you have to get a development enviroment running

First step is to clone the project and navigate to the project folder
```
virtualenv venv          # create virtualenv venv
source venv/bin/activate # activate 
```
make a virtual enviroment and activate it. For linux/mac:
```
git clone https://github.com/Strand94/WhatsMappening.git
cd whatsmappening
```
For windows make virtualenv manually (can be done in pycharm settings at project interprenter)
```
cd Venv/Scripts         # Go to the virtualenv folder
activate # activate 
cd ../.. # navigate back to project folder
```
To ensure this worked, there should now be a (venv) marker to the left of you navigation path in the terminal.

After that you need to install the development dependencies,
```
pip install -r requirements.txt
```
After you have installed all the requirements, its time to generate the database
```
Python manage.py migrate
```
Run the web application locally,
```
Python manage.py runserver
```

## Deployment

In order to deply the latest version of our application to the live server, one simply updates the deployment branch of the git repository. This sends a notification to the heroku server hosting our application that it should build and deply the newest version. 


## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Leaflet](http://leafletjs.com/) - a JavaScript library for interactive maps
* [PostGIS](http://postgis.net/) - Spatial and Geographic Objects for PostgreSQL
* [django-datetime-widget](https://github.com/asaglimbeni/django-datetime-widget) - Widget for selecting valid DateTime data
 
## Authors

* **Andreas G. Strand** - *Developer* - [Strand94](https://github.com/Strand94)
* **Bartosz J. Zarosa** - *Developer* - [Bartors](https://github.com/Bartors)
* **Inès Blomvågnes** - *Developer* - [Blomsi](https://github.com/blomsi)
* **Kari M. Johannessen** - *Developer* - [ThaiKari](https://github.com/ThaiKari)
* **Nicolaj Nielsen** - *Developer* - [Nicolajn](https://github.com/nicolajn)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used.
* Norkart for hosting the database.
* A big thanks to Adrian Tofting, the course student assistant for helping us in times of need.

