# main.py

import os
import uuid
import mimetypes
import falcon
import gevent
from gevent import socket

from controller.bbuser import *

app = falcon.API()

app.add_route('/bbuser',bbUser())
app.add_route('/logar/{login}/{senha}',bbUserLogin())
