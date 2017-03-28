# bolog API

This is a book catalog written in Flask. It's only an API + backend.


## development

### bootstrap / installation

* clone the repository
* `requirements.dev.txt` contains all the requirements for running a development environment. Install them with `pip install -r requirements.dev.txt`.


### run tests

```
python -m pytest tests
```

Because of problems with [not having the module in the path](http://stackoverflow.com/a/34140498), we're calling `pytest` that way.

### running it


```
export FLASK_APP=`pwd`/devapp.py
export FALSK_DEBUG=1
flask run
```

See [here](http://flask.pocoo.org/docs/0.12/cli/#factory-functions) for more information on this technique.
