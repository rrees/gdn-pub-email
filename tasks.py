import webapp2
import jinja2
import os
import json
import logging

from urllib import quote, urlencode

from google.appengine.api import urlfetch
from google.appengine.ext import ndb

import content_api
import models

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))

def summarise_tags(content):
	tags = content.get('tags')
	keywords = [t for t in tags if t['type'] == 'keyword']
	contributors = [t for t in tags if t['type'] == 'contributor']

	return [k['webTitle'] for k in keywords]

def summarise_content(content):
	#logging.info(content)
	summary = models.ContentSummary(
		id=content['id'],
		url=content['webUrl'],
		headline=content['fields']['headline'],
		link_text=content['fields']['trailText'],
		tags=summarise_tags(content),
		)

	for field in ['byline', 'standfirst']:
		if field in content['fields']:
			setattr(summary, field, content['fields'][field])

	return summary

class LatestContent(webapp2.RequestHandler):
	def get(self):
		
		required_fields='headline,trailText,byline,standfirst'
		required_tags='keyword'
		result = content_api.search({'show-fields': required_fields,
			'show-tags': required_tags,
			})

		if not result:
			self.response.out.write("Read of CAPI failed")
			return
		
		data = json.loads(result)
		content = [summarise_content(c) for c in data.get('response', {}).get('results', [])]
		#logging.info(content)

		new_content = [c.put() for c in content if not models.ContentSummary.get_by_id(c.key.id())]
		logging.info(new_content)

		self.response.out.write("{0} new items found".format(len(new_content)))

app = webapp2.WSGIApplication([webapp2.Route(r'/tasks/latest', handler=LatestContent)],
                              debug=True)