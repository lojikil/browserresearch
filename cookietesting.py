#!/usr/bin/env python

""" A simple web server to test how IE deals with cookie paths.

   Usage:

   `python cookietesting.py`

   and then, from within your browser go to: http://localhost:8082/gateway

   and the other URLs.
"""

from bottle import route, run, response, request

@route('/gateway')
def gateway():
    foo = request.get_cookie("foo")
    print "in /gateway, foo = {0}".format(foo)
    if foo is None:
        response.set_cookie("foo", "foo-gateway", path="/gateway")
    return "current cookies: {0}".format(foo)

@route('/gateway-backend')
def gateway():
    foo = request.get_cookie("foo")
    print "in /gateway-backend, foo = {0}".format(foo)
    if foo is None:
        response.set_cookie("foo", "foo-gateway-backend", path="/gateway-backend")
    return "current cookies: {0}".format(foo)

@route('/g')
def gateway():
    foo = request.get_cookie("foo")
    print "in /g, foo = {0}".format(foo)
    if foo is None:
        response.set_cookie("foo", "foo", path="/g")
    return "current cookies: {0}".format(foo)

run(port=8082)
