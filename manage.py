#!/usr/bin/env python
import os
import subprocess

from flask.ext.script import Manager, Server

from sunshine.wsgi import app


manager = Manager(app)
manager.add_command("runserver", Server())


def call_command(cmd, verbose=False):
    if verbose:
        print cmd
    subprocess.call(cmd)


if __name__ == '__main__':
    manager.run()
