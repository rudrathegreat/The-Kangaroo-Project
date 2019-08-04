# Retrieving Events from the Particle Cloud and Saving it in a Database

## Table of Contents

- [Overview](#Overview)
- [Files](#Files)
- [Libraries](#Libraries)
- [PostgreSQL Database](#PostgreSQL%20Database)
- [DbVisualiser](#DbVisualiser)
- [Particle Electron Code](#Particle%20Electron%20Code)
- [The Python Code](#The%20Python%20Code)
- [Further References](#Further%20References)
## Overview

Currently, our project uses two Arduinos, a Particle Electron and a computer to get GPS coordinates from the Arduino to our database stored on a computer. To do that. The Arduino communicates with another Arduino via the LoRa Network adn transmits the data to it. The Arduino then uses serial connections (physical wires) to send the data to the ParticleElectron. The Particle Electron will publish an event, containing the time at which the event was published, the data (in this case, the GPS coordinates from the first Arduino) and which device it came from.

When the Particle Electron publishes an event, it is saved on the Particle Cloud and can be pulled from anywhere at any time. The final part of the system uses a computer to grab the data from the Particle Cloud and save it in a database. This database can then be used later, for e.g - 

> Presenting data in apps
>
> Or presenting data on a website

This repository focuses on publishing and retreving events from the Particle Cloud

## Files

The files which you will be using are - 

> `subscribePublishEvent.py`
>
> `Publish_Event.ino`

The `subscibePublishEvent.py` file is used on the computer to store the data in a database. The `Publish_Event.ino` file is flashed on the Particle Electron which allows to Particle Electron to publish events.

You can download the files by simply clicking the `Clone or Download` button and selecting the .zip version. Once it has downloaded, you can simply go into the folder where the file has been downloaded and you should the folder `Retreiving-Events-master` which contains all the files in it.

![Image description](https://github.com/rudrathegreat/Retreiving-Events/blob/master/Cloning%20Project.png)

## Libraries

If you having some trouble with the Python file, especially some module not found errors, then run the following command in the terminal - 

```Bash

pip install -r requirements.txt.

```

You can find the requirements.txt file here - https://github.com/rudrathegreat/Retreiving-Events/blob/master/requirements.txt

## PostgreSQL Database

You also need to install PostgreSQL. PostgreSQL allows you to make databases and search for data in databases. To install PostgreSQL, you simply go to the following link - https://www.postgresql.org

Download the .dmg (macOS) file and follow the installation instructions. After that, you should receive a username and password. **REMEMBER THAT!!!**

Next, open up PSQL (SQL Shell). You can do this by searching it in Spotlight Search (`Command+Space`) - 

![Image description](https://github.com/rudrathegreat/Retreiving-Events/blob/master/Screen%20Shot%202019-08-04%20at%2010.03.03%20am.png)

or you can go to the PostgreSQL folder and run it from there (The PostgreSQL folder is usually in the Applications Folder). - 

![Image description](https://github.com/rudrathegreat/Retreiving-Events/blob/master/Screen%20Shot%202019-08-04%20at%2010.04.59%20am.png)

Inside it, it will first confirm your username and password. Just press enter if the parameter in the square brackets matches what you were going to give to psql. My username is postgres, so I am just going to hit enter to tell PSQL that I want to use the parameter inside the square brackets - 

![Image description](https://github.com/rudrathegreat/Retreiving-Events/blob/master/Screen%20Shot%202019-08-04%20at%2010.06.02%20am.png)

Once all of that is configured, you can run the following command to create a database - 

```Bash

create database mydb;

```

Once we have made our database, we need to copy our username, password and database name to the Python file and insert it this line - 

```Python

connection = psycopg2.connect(host="localhost", database="{{database name}}", user="{{your username}}", password="{{your password}}")
                                      
```

The Python file is ready to go! Now we need a way to view the data in the database and for that, we will need an application called DbVisualiser.

## DbVisualiser

DbVisualier allows you to view data inside database and search for data using queries. We can go to this link and download/install DbVisualiser - https://www.dbvis.com

Once you are done installing (remember to follow the instructions), open it up and create a new database connection. This database connection simple allows you to connect to that database.

![Image description](https://github.com/rudrathegreat/Retreiving-Events/blob/master/Screen%20Shot%202019-08-01%20at%2010.03.04%20pm.png)

Enter in your username in the UserId parameter, the password in the password parameter, the name of your database in the database parameter and the name of your database connection in the database connection parameter (see image above for reference). Change the port if necessary.

Once you are connected, you are good to go!

## Particle Electron Code

So basically the Particle Electron code is not to hard to understand. Basically, it is creating a bunch of variables and then sending their values to the Particle Cloud. It is also publishing an event which will then be recorded in the database. The main line is this - 

```C

Particle.publish("motion-detected", "Kangroo is moved!", PRIVATE);

```

This is the line that publishes the event.


## The Python Code

The Python Code then obtains the event using get requests (basically asking the Cloud for the data) in the following line - 

```Python

messages = SSEClient('https://api.particle.io/v1/devices/events/motion-detected?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')

```

And then splitting it up into its constituent parts - 

```Python

for msg in messages:
    eventName = str(msg.event)#.encode('utf-8')
    data = str(msg.data)#.encode('utf-8')

```

Then it will check if there is anything in data. If there is, then it will save in the database - 

```Python

dataJson = json.loads(data)
print(dataJson)
eventData = dataJson["data"]
coreid = dataJson["coreid"]
published_at = dataJson["published_at"]
ttl = str(dataJson["ttl"])
save_data(eventName, eventData, coreid, published_at, ttl)

```

This is how the program works.


## Further References

> https://www.youtube.com/watch?v=fD7x8hd9yE4
>
> https://pip.pypa.io/en/stable/user_guide/
>
> https://build.particle.io

```Python

print('Thanks for reading!')

```
