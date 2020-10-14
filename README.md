# UOPY demo

UniObjects for Python demo programs.

## Installation

### Install from PyPI

```bash
$ pip install uopy
```

## Quick start

**Before use UOPY to connect requires a running Universe/UniData server.** 

The following example use UOPY to connect to [UniVerse](https://www.rocketsoftware.com/products/rocket-universe-0/rocket-universe) on Windows.

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
### Examples code

* UOPY GUI [link](https://github.com/RocketSoftware/uopy-demo/tree/master/examples/uopy_tkexample)
* UOPY Web App [link](https://github.com/RocketSoftware/uopy-demo/tree/master/examples/uopy_web)

## API Reference

* [Docs site](https://rocketsoftware.github.io/uopy-demo/docs/uopy.html)
