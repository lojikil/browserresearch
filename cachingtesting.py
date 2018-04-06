#!/usr/bin/env python

from bottle import route, run, response
import uuid

uuids = {
    'blank': uuid.uuid4(),
    'public': uuid.uuid4(),
    'private': uuid.uuid4(),
    'no-cache': uuid.uuid4(),
    'no-store': uuid.uuid4(),
    'must-revalidate': uuid.uuid4(),
    'max-age=0': uuid.uuid4(),
    'private, no-cache': uuid.uuid4(),
    'private, no-store': uuid.uuid4(),
    'private, no-cache, no-store': uuid.uuid4(),
    'public, no-cache': uuid.uuid4(),
    'public, no-store': uuid.uuid4(),
    'public, no-cache, no-store': uuid.uuid4(),
    'no-cache, no-store, must-revalidate': uuid.uuid4(),
    'no-cache, no-store, must-revalidate, max-age=0': uuid.uuid4(),
    'no-cache, no-store, max-age=0': uuid.uuid4()
}

@route('/dest/<path>')
def public(path):
    if path != 'blank' and path in uuids:
        response.set_header('Cache-Control', path)
    return str(uuids[path])

@route('/')
def index():

    t = "<html><head><title>Cache Test</title></head><body>{0}</body></html>"
    data = []
    for k, v in uuids.items():
        data.append("<a href='/dest/{0}'>{0} UUID: {1}</a>".format(k, v))

    return t.format('<br>'.join(data))


if __name__ == "__main__":
    run(host='0.0.0.0', port=8085)
