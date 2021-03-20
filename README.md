# furbies

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

this is my own copy of the database of **f**ast **r**adio **b**ursts (**FRB**s), which is now maintained as a part of the [**T**ransient **N**ame **S**erver (**TNS**)](https://www.wis-tns.org/), the official IAU mechanism for reporting new astronomical transients. the code that scraps the database is in the **scrap.py** file, and the data itself (in all of its JSONic glory) is in the **furbies.json** file. the data is updated on the 15th of every month, at midnight. if you want the latest version of this database, the easiest way would be to git clone this repository, and running the scraping code yourself.

> :warning: **warning!**
> i could have scraped the database two ways: by getting an api token from the **TNS**, downloading the entire database as a CSV, and parsing all the FRBs from it, or by scraping the webpages themselves. i have chosen the latter method. since the workflow runs only once a month, i hope to never drastically affect the operation of the **TNS**. if you use the code in the repository to scrap the database yourself, please keep this in mind. you do so at your own risk.

this repository powers the **neko** package, which aims to make accessing catalogues on pulsars and radio transients easier.
