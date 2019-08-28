# Getting and Sending GPS Coordinates Over the LoRa Network

## Table of Contents

- [Overview](#Overview)
- [Files](#Files)
- [Libraries](#Libraries)
- [PostgreSQL Database](#PostgreSQL-Database)
- [DbVisualiser](#DbVisualiser)
- [Particle Electron Code](#Particle-Electron-Code)
- [The Python Code](#The-Python-Code)
- [Further References](#Further-References)

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

## Glossary

**WDT** - A watchdog timer is a piece of hardware that can be used to automatically detect software anomalies and reset the processor if any occur. Read this article - https://www.embedded.com/electronics-blogs/beginner-s-corner/4023849/Introduction-to-Watchdog-Timers

**Socket** - One of the 2 ends in an internet connection. Watch this video - https://www.youtube.com/watch?v=Y0g3M4VG6Ns

**GC** - Garbage collection (GC) is a form of automatic memory management. Read the following article - https://en.wikibooks.org/wiki/Introduction_to_Programming_Languages/Garbage_Collection
