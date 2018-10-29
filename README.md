# Speedport 3 Smart Utils

It's a little straight forward tool to gather statistics from the info page of a _Telekom Speedport Smart 3_ Router. to circumvent any complicated login and decoding mechanisms, it just uses a headless firefox, parses the output of http://speedport.ip/html/login/status.html and sends it to an InfluxDB. It doesn't make use of the *secret* engineering page http://speedport.ip/engineer/html/version.html

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
python3 setup.py -I y
```

### setup.py Arguments

- *-I*, *--install*: Install/Reinstall the geckodriver (Default: n)
- *-i*, *--interval*: Update Interval in seconds to read data and push to the DB (Default: 3600)
- *-H*, *--host*: Hostname of the InfluxDB server (Default: localhost)
- *-p*, *--port*: Port of the InfluxDB server (Default: 8086)
- *-d*, *--database*: Set the default database (Default: iobroker)

## 2. Usage

To run this programm periodically (in the interval you defined at setup), you have to start it as a service (Only Linux). This will start it in the background. Now it will display some debug messages and a process ID (eg. *[1] 72*). To stop it again just write *kill PID* where PID is the given process ID (here 72).

```bash
python3 postSpeedToDB.py &
```

## 3. Copyright and Disclaimer

Copyright (C) <2018>  <Herobone>

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