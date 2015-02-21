from google.appengine.ext import ndb

class Configuration(ndb.Model):
	key = ndb.StringProperty()
	value = ndb.StringProperty()

class ContentSummary(ndb.Model):
	url = ndb.StringProperty(required=True)
	headline = ndb.StringProperty(required=True)
	standfirst = ndb.TextProperty(required=True)