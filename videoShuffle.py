import os
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
    	

application = webapp2.WSGIApplication([
	('/', MainPage),	
], debug=True)