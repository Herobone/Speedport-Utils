# Speedport 3 Smart Utils

It's a little straight forward tool to gather statistics from the info page of a _Telekom Speedport Smart 3_ Router. to circumvent any complicated login and decoding mechanisms, it just uses a headless firefox, parses the output of http://speedport.ip/html/login/status.html and sends it to an InfluxDB. It doesn't make use of the *secret* engineering page http://speedport.ip/engineer/html/version.html

You can find more information about this tool on my **[website](https://herobone.de/project/speedport-3-smart-utils/)**

The tool was tested on Linux and Windows, the latter might need you to install some additional SW to run it.
For other Router Models (i.e. Telekom Speedport Hybrid), you might also have a look at https://github.com/melle/l33tport

1. Installation
2. Usage
3. Copyright and Disclaimer

---

## 1. Installation

### Requirements

- Linux (eg. Ubuntu 18.04) or Windows (can be headless)
- Firefox
- Python (minimal Version: 3.6)
- Pip (using python3)

1. Download this Project as a zip and extract it or clone it via git
2. Open a shell in the Folder
3. Type

```bash
pip3 install -r requirements.txt
python3 setup.py -I
```

### setup.py Arguments

- *-I*, *--install*: Install/Reinstall the geckodriver
- *-i*, *--interval*: Update Interval in seconds to read data and push to the DB (Default: 3600)
- *-H*, *--host*: Hostname of the InfluxDB server (Default: localhost)
- *-p*, *--port*: Port of the InfluxDB server (Default: 8086)
- *-d*, *--database*: Set the default database (Default: iobroker)

## 2. Usage

### Arguments

- *-v*, *--verboose*: Output debug/information messages
- *-q*, *--quiet*: No output to the console
- *-t*, *--type*: Set the type of execution (multi/single)
- *-a*, *--action*: Set the action it should do (DB/TXT/CSV/LOG)
- *-f*, *--format*: Set the format for dump to TXT file. Default: {} {} {} (First {} is Timestamp, Second {} is Up, Third {} is Down)

### Methods to run

#### Method 1: Service

To run this programm periodically (in the interval you defined at setup), you have to start it as a service (Only Linux). This will start it in the background. Now it will display some debug messages and a process ID (eg. *[1] 72*). To stop it again just write *kill PID* where PID is the given process ID (here 72).

```bash
python3 speedread.py &
```

#### Method 2: Crontab

The other method to get the data regularly is using crontab (Only Linux). To run this every hour you have to add it to your crontab. To do this type

```bash
crontab -e
```

Now you should write in the file:

```bash
59 * * * * /usr/bin/python3 <path to root of speedport utils>/speedread.py -t single -q
```

This will execute every hour at 59 minutes the command *postSpeedToDB.py -t single -q*. In this case the argument *-q* tells the program to be silent (or *quiet*) and the *-t single* tells the program to make a single measurement

## 3. Copyright and Disclaimer

Copyright (C) 2018 Herobone

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
