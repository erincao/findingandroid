#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#<<<<<<< HEAD
def redirect_play():
    self.redirect("/play")

#=======
#>>>>>>> 4a0eeab248790272d9c8361a6dfda1212a5d7347
class Player(ndb.Model):
    user = ndb.StringProperty(required = True)
    level = ndb.IntegerProperty(required = True)
    attempts = ndb.IntegerProperty(required = True)

player1 = Player (user = "James", level = 1, attempts = 1)
player1.put()

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
#<<<<<<< HEAD
        welcome_template = JINJA_ENVIRONMENT.get_template("templates/welcome.html")
        self.response.out.write(welcome_template.render())


class PlayHandler(webapp2.RequestHandler):
    def get (self):
        play_template = JINJA_ENVIRONMENT.get_template("templates/play.html")
        self.response.out.write(play_template.render())

#
# class LoginHandler(webapp2.RequestHandler):
#     def get(self):
#         user = users.get_current_user()
#         if user:
#             greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
#                         (user.nickname(), users.create_logout_url('/')))
#         else:
#             greeting = ('<a href="%s">Sign in or register</a>.' %
#                         users.create_login_url('/'))
#
#         self.response.out.write('<html><body>%s</body></html>' % greeting)
#=======
        #self.response.write('Hello world!')
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())
#>>>>>>> 4a0eeab248790272d9c8361a6dfda1212a5d7347



app = webapp2.WSGIApplication([
    ('/play', PlayHandler),
    ('/', WelcomeHandler)
], debug=True)
