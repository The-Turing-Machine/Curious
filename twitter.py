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

woeid=['23424739', '23424742', '23424740', '23424744', '23424745', '23424737', '23424747', '23424743', '23424748', '23424750', '23424741', '23424758', '23424753', '23424759', '23424754', '23424765', '23424757', '23424760', '23424764', '23424770', '23424762', '23424761', '23424755', '23424768', '23424773', '23424771', '23424978', '23424774', '23424794', '23424776', '23424785', '23424775', '23424792', '837054', '23424782', '23424971', '23424787', '23424786', '23424779', '879050', '23424843', '23424793', '26812346', '23424810', '23424868', '2480268', '23424796', '2345158', '23424798', '23424800', '23424801', '23424802', '23424807', '23424835', '23424806', '23424805', '23424808', '23424813', '23424812', '23424819', '1329894', '1259029', '2347569', '23424829', '23424824', '23424833', '2414888', '83123', '23424835', '1559861', '23424836', '23424839', '23424841', '23424844', '23424845', '23424848', '23424846', '23424851', '2124082', '23424803', '23424852', '23424853', '23424858', '23424856', '2429994', '23424871', '23424863', '23424867', '1940631', '23424864', '23424874', '2437673', '23424880', '23424876', '23424882', '23424879', '23424875', '979721', '2443718', '23424883', '23424889', '23424901', '23424899', '23424891', '23424897', '23424932', '23424896', '23424894', '23424900', '24865720', '483301', '23424887', '20069817', '23424893', '23424902', '23424763', '23424987', '23424912', '23424911', '23424909', '23424916', '23424906', '23424908', '29145317', '23424898', '23424922', '23424927', '159386', '12491802', '23424917', '23424919', '23424934', '23424923', '23424925', '28395013', '23424868', '23424885', '23424933', '23424936', '23424937', '23424940', '1325621', '2347676', '23424992', '532373', '1441680', '29125356', '23424943', '20069818', '23424941', '1062844', '1062617', '23424877', '23424945', '23424766', '23424949', '24865670', '23424952', '23424950', '12467072', '905958', '23424913', '23424993', '23424954', '23424957', '23424956', '23424961', '23424960', '23424968', '1048627', '23424964', '23424958', '23424967', '23424969', '23424972', '23424970', '1301134', '23424976', '23424738', '20070563', '23424973', '23424977', '23424979', '23424980', '23424907', '23424982', '23424984', '23425002', '23425003', '23425004']

def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print 'Please go here and authorize: ' + authorize_url

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret

pp = pprint.PrettyPrinter(indent=4)

def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

def get_trend_hashtags(woeid):
        for i in woeid:
            try:
                b = requests.get(url="https://api.twitter.com/1.1/trends/place.json?id="+i+"", auth=oauth)
                pp.pprint(b.json())
            except:
                print "not available"




if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    else:
        oauth = get_oauth()
        get_trend_hashtags(woeid)
        # r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=messi&count=100", auth=oauth)
        # a = r.json()
        # print len(a)
        # for i in range(0,100):
        #
        #     print "tweet="+a['statuses'][i]['text']
        #     print "place="+str(a['statuses'][i]['place'])
        #     print "coordibnates="+str(a['statuses'][i]['coordinates'])
            # print a['statuses'][0]['text']
            # print "tweet="+a['statuses'][1]['text']
            # print "place="+a['statuses'][1]['place']
        # pp.pprint(r.json())
