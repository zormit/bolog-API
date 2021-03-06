# bolog API

[![Build Status](https://travis-ci.org/zormit/bolog-API.svg?branch=master)](https://travis-ci.org/zormit/bolog-API)

This is a book catalog written in Flask. It's only an API + backend.

## Contributing

Currently the API is not used in any way. The data that is currently published on http://zormit.github.io/bolog-API/ on a prototype-basis via the `gh-pages` branch.

## development

### bootstrap / installation

* clone the repository
* `requirements.dev.txt` contains all the requirements for running a development environment. Install them with `pip install -r requirements.dev.txt`.


### run tests

```
PYTHONPATH=. pytest
```

Because of problems with [not having the module in the path](http://stackoverflow.com/a/34140498), we're calling `pytest` that way.

### running it


```
export FLASK_APP=`pwd`/devapp.py
export FLASK_DEBUG=1
flask run
```

See [here](http://flask.pocoo.org/docs/0.12/cli/#factory-functions) for more information on this technique.
