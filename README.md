# UOPY demo

UniObjects for Python (UOPY) is a Python package by Rocket Software.

## Installation

### Install from PyPI

```bash
$ pip install uopy
```

## Quick start

**Before using UOPY to connect to an MV Database, you must be running either a UniVerse or UniData server.** 

The following example uses UOPY to connect to [UniVerse](https://www.rocketsoftware.com/products/rocket-universe-0/rocket-universe) on Windows.

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

1. Intro to UOPY, UniObjects for Python
    - [video link](https://www.rocketsoftware.com/resource/intro-uopy-uniobjects-python)
2. UOPY GUI examples
    - [video link](https://www.rocketsoftware.com/resource/uopy-gui-examples)
    - [code link](https://github.com/RocketSoftware/uopy-demo/tree/master/examples/uopy_tkexample)
3. Webserver app demo
    - [video link](https://www.rocketsoftware.com/resource/webserver-app-demo)
    - [code link](https://github.com/RocketSoftware/uopy-demo/tree/master/examples/uopy_web)

## API Reference

* [Docs site](https://rocketsoftware.github.io/uopy-demo/docs/uopy.html)
