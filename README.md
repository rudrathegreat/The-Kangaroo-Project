# Sending Data via LoRa Network

## Table of Contents

## Overview

Currently, our project uses two Arduinos, a Particle Electron and a computer to get GPS coordinates from the Arduino to our database stored on a computer. To do that. The Arduino communicates with another Arduino via the LoRa Network adn transmits the data to it. The Arduino then uses serial connections (physical wires) to send the data to the ParticleElectron. The Particle Electron will publish an event, containing the time at which the event was published, the data (in this case, the GPS coordinates from the first Arduino) and which device it came from.

When the Particle Electron publishes an event, it is saved on the Particle Cloud and can be pulled from anywhere at any time. The final part of the system uses a computer to grab the data from the Particle Cloud and save it in a database. This database can then be used later, for e.g - 

> Presenting data in apps
>
> Or presenting data on a website

This repository focuses on publishing and retreving events from the Particle Cloud

## Files

The files which you will be using are - 

> `LoRa_Send.py`
>
> `LoRa_Receive.py`

The file `LoRa_Send.py` is used to allow a LoRa module to send data over the LoRa Network. The `LoRa_Receive.py` file however is used to receive data from the LoRa Network.

![Image description](https://github.com/rudrathegreat/Retreiving-Events/blob/master/Cloning%20Project.png)

## Libraries

There are several modules which we are using, most of which is coded in an implementation of Python called `MicroPython`. MicroPython is a language that is similar to Python that can be used for small microcontrollers.

We will also be using `ftp`, a deprecated command if you are using the latest MacOS system. To install it, you need `homebrew`, also known as `brew`. To install brew, you can follow the documentation from here - https://brew.sh. Once you have done that, yuo need to install a package of utilities called `inetutils`, which contains deprecated commands and programs, including `ftp`. To do that, you simply type the following command in the terminal - 

```Bash

brew install inetutils

```

With this, you can access the PyCom Module, a module which can be used to connect, transmit and receive data from the LoRa Network, and view all the files inside. We need this to place all the files we want to run in there.


## The Code

The first piece of the code is the `LoRa_Send.py` file. This program allows the PyCom Module to connect and send messages on the LoRa Network. The program first creates a stable connection on the LoRa Network. After that, it sends a message over and over and over and over again... forever. This can be summed up in these three lines - 

```Python

while True:
  s.send('Ping')
  time.sleep(1)

```

The receiving code is not too dissimilar. The program first creates a stable connection as with the previous program. It then waits until a message `Ping` has been received. If it has, then it shall send `Pong` back.

## Ftp

`Ftp` is a program that allows you to see, view and edit files inside somebody else's device. There are some basic commands.

To start a ftp connection, just type - 

```Bash

ftp xxx.xxx.x.x

```

Next, you need to type the username and password for that device. After that, you can list all the directories by doing -

```Bash

ftp> ls

```

You can check the current directory by doing - 

```Bash

ftp> pwd

```

You can place files by doing the following - 

```Bash

ftp> put filename.filetype

```

And then you can exit it by simply -

```Bash

ftp> quit

```

## Uploading the Code

To upload the code, we need to place our code from our computer/laptop to the PyCom module. To do that, we first need to rename our program to `main.py`. This is because the program which the PyCom module executes is `main.py`. The PyCom module cannot run any other program besides `main.py`, unless we tell is to from `boot.py`.

Next, we need to connect to the PyCom Router, which is built in the PyCom module, similar to how you connect to your WiFi Router. Next, go to the folder in which your `main.py` file is in via the terminal. Then connect to the device via ftp in the terminal - 

```

ftp xxx.xxx.x.x

```

After that, we need to go inside the `flash` folder. Inside this folder, there are the files `boot.py` and `main.py`. We need to replace the `main.py` file inside the `flash` folder with your `main.py` in your computer. To do that, simply use the put command - 

```Bash

put main.py

```

Now that the `main.py` file in the PyCom module has been updated, we need to reboot the the pyCom module. Once that is done, the LED on the PyCom module should be changing colour and signals should be being sent on the LoRa Network.

And that's how you do it.


## Further References

> https://www.youtube.com/watch?v=fD7x8hd9yE4
>
> https://pip.pypa.io/en/stable/user_guide/
>
> https://build.particle.io

```Python

print('Thanks for reading!')

```
