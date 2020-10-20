# UOPY demo

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

1. UOPY: Intro to UOPY, UniObjects for Python
    - [video link](https://www.rocketsoftware.com/resource/intro-uopy-uniobjects-python)
2. UOPY: GUI examples
    - [video link](https://www.rocketsoftware.com/resource/uopy-gui-examples)
    - [code link](https://github.com/RocketSoftware/uopy-demo/tree/master/examples/uopy_tkexample)
3. UOPY: Webserver app demo
    - [video link](https://www.rocketsoftware.com/resource/webserver-app-demo)
    - [code link](https://github.com/RocketSoftware/uopy-demo/tree/master/examples/uopy_web)
4. UOPY: Android Demo
    - [video link](https://www.rocketsoftware.com/resource/uopy-android-demo)

## API Reference

* [Docs site](https://rocketsoftware.github.io/uopy-demo/docs/uopy.html)
