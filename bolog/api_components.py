from functools import update_wrapper

from flask import Flask, json, Response, request
from voluptuous import Invalid


class ApiResult(object):

    def __init__(self, value, status=200):
        self.value = value
        self.status = status

    def to_response(self):
        return Response(json.dumps(self.value),
                        status=self.status,
                        mimetype='application/json')


class ApiException(Exception):

    def __init__(self, message, status=400):
        self.message = message
        self.status = status

    def to_result(self):
        return ApiResult({'message': self.message},
                         status=self.status)


class ApiFlask(Flask):

    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        # mimetype: text/html
        return Flask.make_response(self, rv)


def dataschema(schema):
    def decorator(f):
        def new_func(*args, **kwargs):
            try:
                kwargs.update(schema(request.get_json()))
            except Invalid as e:
                # TODO: nicer error message?
                raise ApiException('Invalid data: %s (path: "%s")'
                                   % (e.msg, e.path))
            return f(*args, **kwargs)
        return update_wrapper(new_func, f)
    return decorator
