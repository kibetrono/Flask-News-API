from flask import  render_template
from . import main

@main.app_errorhandler(404)
def allErrors(error):
    """Function that handles wrong urls"""
    render_template("errors.html"),404
