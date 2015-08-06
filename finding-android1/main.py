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
    user_first_name = ndb.StringProperty()
    user_last_name = ndb.StringProperty()
    level = ndb.IntegerProperty()
    attempts = ndb.IntegerProperty()

# # user1 = UserModel (currentUser = "James", level = 1, attempts = 1)
# user1.put()

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            pass
        else:
            self.redirect(users.create_login_url(self.request.url))

        welcome_template = JINJA_ENVIRONMENT.get_template("templates/welcome.html")
        self.response.out.write(welcome_template.render())


class Level_1_Handler(webapp2.RequestHandler):
    def get (self):
        artist_interest = self.request.get ("level_entry")
        level_1_template = JINJA_ENVIRONMENT.get_template("templates/level1.html")
        self.response.out.write(level_1_template.render())

    def post(self):
        # user_first_name = self.response.get('user_first_name')
        # user_last_name = self.response.get('user_last_name')
        user = users.get_current_user()


        user1 = UserModel(currentUser=user.user_id(), user_first_name = self.request.get('user_first_name'), user_last_name =  self.request.get('user_last_name'), attempts = 0)
        user1.put()
        artist_interest = self.request.get ("level_entry")
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
        #self.response.write('Hello world!')
        # template = JINJA_ENVIRONMENT.get_template('index.html')
        # self.response.write(template.render())

class Congratulations_Handler(webapp2.RequestHandler):
    def get (self):
        congratulations_template = JINJA_ENVIRONMENT.get_template("templates/congratulations.html")
        self.response.out.write(congratulations_template.render())

class About_Us_Handler(webapp2.RequestHandler):
    def get (self):
        about_us_template = JINJA_ENVIRONMENT.get_template("templates/about_us.html")
        self.response.out.write(about_us_template.render())

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/level_1', Level_1_Handler),
    ('/level_2', Level_2_Handler),
    ('/level_3', Level_3_Handler),
    ('/level_4', Level_4_Handler),
    ('/level_5', Level_5_Handler),
    ('/congratulations', Congratulations_Handler),
    ('/about_us', About_Us_Handler)
], debug=True)
