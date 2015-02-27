#!/usr/bin/env python

""" A simple web server to test how IE deals with cookie paths.

   Usage:

   `python cookietesting.py`

   and then, from within your browser go to: http://localhost:8082/gateway

   and the other URLs.
"""

from bottle import route, run, response, request

tmpl = None


@route('/gateway')
def gateway():
    foo = request.get_cookie("foo")
    print "in /gateway, foo = {0}".format(foo)
    if foo is None:
        response.set_cookie("foo", "foo-gateway", path="/gateway")
    return "{0}".format(foo)

@route('/gateway-backend')
def gateway():
    foo = request.get_cookie("foo")
    print "in /gateway-backend, foo = {0}".format(foo)
    if foo is None:
        response.set_cookie("foo", "foo-gateway-backend", path="/gateway-backend")
    return "{0}".format(foo)

@route('/g')
def gateway():
    foo = request.get_cookie("foo")
    print "in /g, foo = {0}".format(foo)
    if foo is None:
        response.set_cookie("foo", "foo", path="/g")
    return "{0}".format(foo)

@route('/')
def index():
    global tmpl
    if tmpl is None:
        with file('cookietesting.html') as fh:
            tmpl = fh.read()
    return tmpl

run(port=8082)
