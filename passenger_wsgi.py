#!/usr/bin/python3

import os
import sys

# Add the project directory to the Python path
project_dir = os.path.dirname(__file__)
sys.path.insert(0, project_dir)

# Import the Flask application
from app_production import app

# This is the WSGI application object that Passenger (used by most shared hosting) will use
application = app

if __name__ == "__main__":
    app.run()
