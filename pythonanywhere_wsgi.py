#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WSGI configuration for PythonAnywhere deployment.

This file is specifically for PythonAnywhere deployment.
Copy this file content to your PythonAnywhere WSGI file.
"""

import os
import sys

# Add your project directory to the Python path
project_home = '/home/Bikal/PORTFOLIO'  # Updated with actual username
if project_home not in sys.path:
    sys.path.append(project_home)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'myportfolio.settings'
os.environ.setdefault('DEBUG', 'False')

# Import Django and your application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
