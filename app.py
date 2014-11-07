#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv as argv
from bottle import route, run, static_file


@route('/')
def index():
    return static_file('index.html', root='public')


@route('/<filepath:path>')
def hello(filepath):
    return static_file(filepath, root='public')

run(host='0.0.0.0', port=argv[1])
