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

def redirect_play():
    self.redirect("/play")

class UserModel(ndb.Model):
    currentUser = ndb.StringProperty()
    level = ndb.IntegerProperty()
    attempts = ndb.IntegerProperty()
    text = ndb.StringProperty()
    
# # user1 = UserModel (currentUser = "James", level = 1, attempts = 1)
# user1.put()

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            #self.response.write(user)
            user = UserModel(currentUser = user.user_id())
            user.put()
        else:
            self.redirect(users.create_login_url(self.request.url))

        welcome_template = JINJA_ENVIRONMENT.get_template("templates/welcome.html")
        self.response.out.write(welcome_template.render())

class Level_1_Handler(webapp2.RequestHandler):
    def get (self):
        level_1_template = JINJA_ENVIRONMENT.get_template("templates/level1.html")
        self.response.out.write(level_1_template.render())


class Level_2_Handler(webapp2.RequestHandler):
    def get (self):
        level_2_template = JINJA_ENVIRONMENT.get_template("templates/level2.html")
        self.response.out.write(level_2_template.render())

class Level_3_Handler(webapp2.RequestHandler):
    def get (self):
        level_3_template = JINJA_ENVIRONMENT.get_template("templates/level3.html")
        self.response.out.write(level_3_template.render())

class Level_4_Handler(webapp2.RequestHandler):
    def get (self):
        level_4_template = JINJA_ENVIRONMENT.get_template("templates/level4.html")
        self.response.out.write(level_4_template.render())

class Level_5_Handler(webapp2.RequestHandler):
    def get (self):
        level_5_template = JINJA_ENVIRONMENT.get_template("templates/level5.html")
        self.response.out.write(level_5_template.render())

<<<<<<< HEAD


        #self.response.write('Hello world!')
        # template = JINJA_ENVIRONMENT.get_template('index.html')
        # self.response.write(template.render())
#>>>>>>> 4a0eeab248790272d9c8361a6dfda1212a5d7347

=======
>>>>>>> 1f318b56de110cd33e90b4b62f2d8de8eb9ec6bc
app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/level_1', Level_1_Handler),
    ('/level_2', Level_2_Handler),
    ('/level_3', Level_3_Handler),
    ('/level_4', Level_4_Handler),
    ('/level_5', Level_5_Handler)
], debug=True)
