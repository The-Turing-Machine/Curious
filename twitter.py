from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import pprint

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "rcPzx7rJtywQMk0VmdGLCAxjb"
CONSUMER_SECRET = "DE3J8NLlSVSnGJuQ0U3GKCBjrIo7vBxQCEeCOj1HoS2bP74NPv"

OAUTH_TOKEN = "4653955494-jbxlbxolDzQv16TA6astzszHOT7HHJbtZTy5HNV"
OAUTH_TOKEN_SECRET = "3ndOvcdpb79OR73BfJtJ64i9Qg6X8qWIpcI4SAcnIfKSB"
