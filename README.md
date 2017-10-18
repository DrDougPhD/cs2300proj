# cs2300proj

Barebones project skeleton for the Fall 2017 CS2300 Databases class at Missouri S&amp;T.


## Downloading the Sample Project

You'll first need to download the sample project and set up your development environment.
Log into one of the S&T CLC Linux machines through `PuTTY` (or your favorite `ssh` client) and execute the following commands.

```
    djmvfb@rc04xcs213:~$ git clone https://github.com/DrDougPhD/cs2300proj.git
    djmvfb@rc04xcs213:~$ cd cs2300proj/
    djmvfb@rc04xcs213:~/cs2300proj$ virtualenv -p python3 venv
    djmvfb@rc04xcs213:~/cs2300proj$ source venv/bin/activate
    (venv) djmvfb@rc04xcs213:~/cs2300proj$ pip install -r requirements.txt
```

Everything should now be set up for you: 
 your Python 3 virtual environment (`venv`) 
 and the `Flask` microframework for Python.


## Initialize Your Database

Before running the `Flask` server, you need to initialize your SQLite database.
Do so by executing the following command from within your project's directory.

```
    (venv) djmvfb@rc04xcs213:~/cs2300proj$ python initialize_database.py
```

Your empty SQLite database with its necessary table should now exist as a file in your project's directory
 named `data.db`.


## Open up Firefox running on the Linux machine

Remember that if you are working on a Windows computer connecting to a Linux machine, you need to fire up Xming and enable X forwarding in PuTTY.

Within PuTTY, open an instance of `firefox` by typing the following command:

```
    (venv) djmvfb@rc04xcs213:~/cs2300proj$ firefox &
```

A bunch of text output will be thrown to your PuTTY console.
You can simply press `Enter` a few times to give you back the shell prompt.
So long as a Firefox window pops up, you're good.
If not, something wasn't set up properly.


## Running Your Flask Server

Execute the `run.sh` script to fire up your `Flask` server.

```
    (venv) djmvfb@rc04xcs213:~/cs2300proj$ ./run.sh
```

Your server should now be listening in on some port on the Linux machine.
Read the output from the `run.sh` script to figure out which port.
To open your project's home page, type `http://localhost:PORT/` into your `Firefox` window and press `Enter`.
You should see the sample project's home page.

