from flask import Response
import simplejson

def response(status_code, message = None, mime = 'application/json'):
    if not message:
        if status_code == 200:
            message = "OK"
        elif status_code == 400:
            message = "Bad Request"
        elif status_code == 401:
            message = "Unauthorized"
        elif status_code == 403:
            message = "Forbidden"
        elif status_code == 404:
            message = "Not Found"
        else:
            message = "No Message"

    res = simplejson.dumps(dict(
        message = message,
        status = status_code
    ), for_json = True)

    return Response(res, status = status_code, mimetype = mime)