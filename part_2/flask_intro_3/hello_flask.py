#!/usr/bin/env python

import flask


# Create the application.
APP = flask.Flask(__name__)


@APP.route('/hello/<name>/')
def hello(name):
    """
    Displays the page and greets whoever comes to visit it.
    """
    return flask.render_template('hello.html', name=name)


if __name__ == '__main__':
    APP.debug = True
    APP.run()
