# Recipe Ease

A recipe finder that connects to your google calendar to provide recipes from multiple websites that fit time constraints and diets

## Description

Recipe Ease uses the google calendar api and edamam api to connect to a user's calendar and search multiple websites
for recipes that users have the time to create and fit within certain filters provided by the user. These filters
include multiple dietary options, mealtime, an optional cook time (in the case the user does not want to use their calendar),
and a query box to zone in on recipe options. The program also provides links to each recipe as well as images, names, and
cook times.

## Getting Started

### Dependencies

* Windows 10 (only tested platform so far)
* Python 3
* Pillow (Python Library)
* Selenium (Python Library)
* Google Calender API
* Edamam API

### Installing

* Clone entire repository into a folder
* Setup the Google calendar API and copy the credentials.json file into the externalFiles folder (https://developers.google.com/workspace/guides/getstarted-overview)
* Setup the Edamam recipe search API and input the app_id and app_key in edamam.txt in the externalFiles folder (https://developer.edamam.com/edamam-recipe-api)
* Install Python libraries shown in dependancies

### Executing program

* To run program execute the mainWindow.py class in the gui folder

## TODO

* Rework parsing algoritham for Edamam API
* Add options for multiple users into GUI
* Add save option for filters
* Update GUI graphics

## Authors

Avi J Choksi
www.linkedin.com/in/avi-choksi

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
