from google.appengine.ext import ndb

class Configuration(ndb.Model):
	key = ndb.StringProperty()
	value = ndb.StringProperty()

class ContentSummary(ndb.Model):
	url = ndb.StringProperty(required=True)
	headline = ndb.StringProperty(required=True)
	byline = ndb.StringProperty()
	standfirst = ndb.TextProperty()
	trail_text = ndb.StringProperty(required=True)
	tags = ndb.StringProperty(repeated=True)
	production_office = ndb.StringProperty(required=True, default="UK")
	sent = ndb.BooleanProperty(required=True, default=False)