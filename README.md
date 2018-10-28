# Speedport Smart 3 Utility
It's a little straight forward tool to gather statistics from the info page of a _Telekom Speedport Smart 3_ Router. to circumvent any complicated login and decoding mechanisms, it just uses a headless firefox, parses the output of http://speedport.ip/html/login/status.html and sends it to an InfluxDB. It doesn't make use of the *secret* engineering page http://speedport.ip/engineer/html/version.html

The tool was tested on Linux and Windows, the latter might need you to install some additional SW to run it.

For other Router Models (i.e. Telekom Speedport Hybrid), you might also have a look at https://github.com/melle/l33tport

1. Installation
2. Build
3. Copyright and Disclaimer

---

## 1. Installation

1. Download this Project as a zip and extract it or clone it via git
2. Open a shell in the Folder
3. Type

```bash
pip3 install -r requirements.txt
python3 setup.py -I y
```

### setup.py Arguments

- *-I*, *--install*: Install the geckodriver
- *-i*, *--interval*: The interval in which it will push to the database

## 2. Copyright and Disclaimer

MIT License

Copyright (c) [2018] [Herobone@herobone.de]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
