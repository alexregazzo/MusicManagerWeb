import traceback
from functools import wraps

from flask import Response


def log_response(f: callable):
    @wraps(f)
    def function_wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return function_wrapper


def ensure_response(f: callable):
    @wraps(f)
    def function_wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(e)
            print(type(e))
            print(traceback.print_exc())
            return Response("{}", status=500, content_type='application/json')

    return function_wrapper


def authorize(f: callable):
    @wraps(f)
    def function_wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return function_wrapper


def logout(f: callable):
    @wraps(f)
    def function_wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return function_wrapper
