import webapp2
import jinja2
import os
import json
import logging
from urllib import quote, urlencode
from google.appengine.api import urlfetch

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))

class LatestContent(webapp2.RequestHandler):
	def get(self):
		

		self.response.out.write("Hello world")

app = webapp2.WSGIApplication([webapp2.Route(r'/tasks/latest', handler=LatestContent)],
                              debug=True)