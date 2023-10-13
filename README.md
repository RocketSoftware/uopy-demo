# UOPY demo

[![UOPY Forum](https://img.shields.io/badge/UOPY-Forum-brightgreen)](https://community.rocketsoftware.com/forums/multivalue?CommunityKey=dd45d00d-59db-4884-b3eb-2b0647af231b)
[![UOPY API Docs](https://img.shields.io/badge/UOPY-%20API%20Docs-brightgreen)](https://rocketsoftware.github.io/uopy-demo/docs/uopy.html)
[![PyPI](https://img.shields.io/pypi/v/uopy)](https://pypi.org/project/uopy/)
![PyPI - Downloads](https://img.shields.io/pypi/dw/uopy)


UniObjects for Python (UOPY) is a Python package by Rocket Software. It is a client API that allows Python applications to access Rocket MV Databases over the network.

## Installation

### Install from PyPI

```bash
$ pip install uopy
```

## Quick start

**Before using UOPY to connect to an MV Database, you must be running either a [UniVerse](https://www.rocketsoftware.com/products/rocket-universe-0/rocket-universe) or [UniData](https://www.rocketsoftware.com/products/rocket-unidata-0/rocket-unidata) server.** 

The following example uses UOPY to connect to UniVerse on Windows.

```python
>>> import uopy
>>> ses = uopy.connect(host='localhost', user='username', password='password', account='XDEMO')
>>> cmd = uopy.Command("LIST LOCATIONS")
>>> cmd.run()
>>> print(cmd.response)

LIST LOCATIONS 01:58:07pm  13 Oct 2020  PAGE    1
LOCATIONS.    Location Name............

WHSE1         Main warehouse
WHSE2         Secondary warehouse
WHSE3         Tertiary Warehouse

3 records listed.
```

## Resources

| Name | Link  |
|---|---|
| GitHub UOPY examples repository | [home](https://github.com/RocketSoftware/uopy-demo)  |
| UOPY: Intro to UOPY, UniObjects for Python | [video](https://www.rocketsoftware.com/resource/intro-uopy-uniobjects-python) |
| UOPY: GUI examples | [video](https://www.rocketsoftware.com/resource/uopy-gui-examples), [code](https://github.com/RocketSoftware/uopy-demo/tree/master/examples/uopy_tkexample) |
| UOPY: Webserver app demo |  [video](https://www.rocketsoftware.com/resource/webserver-app-demo), [code](https://github.com/RocketSoftware/uopy-demo/tree/master/examples/uopy_web) |
| UOPY: Android Demo | [video](https://www.rocketsoftware.com/resource/uopy-android-demo) |

## API Reference

* [Docs site](https://rocketsoftware.github.io/uopy-demo/docs/uopy.html)
