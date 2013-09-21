#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import urllib2
import urllib
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class MainPage(webapp2.RequestHandler):

    def get(self):        
    	greeting = 'Welcome to uShuf: revolutionizing the way you watch TV'
        template_values = {
            'greeting': greeting,           
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("Thanks for liking!")        
        #print "Hello"

class LikeVideo(webapp2.RequestHandler):
    def post(self):        
        videoID = self.request.get('videoID')
        #self.request.body = 'videoID=vid'        
        #print videoID;
        self.response.write("Thanks for liking! "+videoID)        

class unLikeVideo(webapp2.RequestHandler):
    def post(self):
        #self.body = 'videoID=vid'
        #videoID = self.POST['videoID']
        self.response.write("We will find you a better pick!")# + videoID)       
    	

application = webapp2.WSGIApplication([
	('/', MainPage),
    ('/like', LikeVideo),
    ('/unlike', unLikeVideo),
], debug=True)