# INF601 - Advanced Programming in Python
 Jesse Heckman
Final Project: Simple Flask app to connect to PLC.
 
## Install 
`pip install -r requirements.txt`
This will install all of the modules that you will need for the program. 

## Run the Application

`$ flask --app PLC_Data --debug run`

You’ll see output similar to this:

* Serving Flask app "PLC_Data"
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: nnn-nnn-nnn



## Initalize the db file

Run the init-db command:

`$ flask --app PLC_Data init-db`
Initialized the database.



## Running the program
To run this program clicking the green code button `clone` the code and run in you're preferred python editor. 


## Log in and Create a Username and Password
Once you log in, you need to create a username and password.  Click the log in and register.
After registration you will be able to enter your PLC info and connect to view tag data. 

## FLASK Documentation 
Flask Tutorial Documentation is available here: [Flask Tutorial Documentation](https://flask.palletsprojects.com/en/2.2.x/tutorial/).
Pylogix Documentation is available here: [Pylogix Documentation](https://pypi.org/project/pylogix/).

