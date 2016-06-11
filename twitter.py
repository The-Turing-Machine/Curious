from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import pprint
import json

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

# CONSUMER_KEY = "rcPzx7rJtywQMk0VmdGLCAxjb"
# CONSUMER_SECRET = "DE3J8NLlSVSnGJuQ0U3GKCBjrIo7vBxQCEeCOj1HoS2bP74NPv"

CONSUMER_KEY = "N8CefcBhNEgLLzj5C5NTkwk7I"
CONSUMER_SECRET = "XvalzhATRiMwtRmz5g6jrU4yI9VrMvGRbPYpWaXYtPEofMYyMT"

# CONSUMER_KEY="XX254OwNWCuctNrlo29GW2Ihx"
# CONSUMER_SECRET = "KDTb6Q4swNH1ThMO13SH9vzhOQecP9705wFXw6qPg90S52ISZU"



# OAUTH_TOKEN = "4653955494-jbxlbxolDzQv16TA6astzszHOT7HHJbtZTy5HNV"
# OAUTH_TOKEN_SECRET = "3ndOvcdpb79OR73BfJtJ64i9Qg6X8qWIpcI4SAcnIfKSB"

OAUTH_TOKEN ="4653955494-Cbul45ZQvzsK16aELSN2O6ecVaT4UbSDujfCkqx"
OAUTH_TOKEN_SECRET = "8CwjuAi7ctdJQIfW4a835IdLYcap8cl5V2ZPaG0rm7exW"

# OAUTH_TOKEN="4653955494-VRs3MN2aPRhiQFBIdPyMs8S68X1cxaBT81s0bY7"
# OAUTH_TOKEN_SECRET="2eAn9kfBofZpuFHuYaakbwbNqrpeesInMas1AAdkxQKb1"


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
        # for i in woeid:
        #     # try:
        #     b = requests.get(url="https://api.twitter.com/1.1/trends/place.json?id="+i+"", auth=oauth)
        #     c = b.json()
        #     d = []
        #     d = c
        #     print d[0]
        #
        #     #
        #     # with open('data.txt', 'w') as outfile:
        #     #     json.dump(c, outfile)
        #     pp.pprint(b.json())
        #     # except:
        #     #     print "not available"
        b = requests.get(url="https://api.twitter.com/1.1/trends/place.json?id=23424848", auth=oauth)
        for i in b.json()[0]['trends']:
            print i["query"]







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


# [{u'created_at': u'2016-06-11T10:41:02Z', u'trends': [{u'url': u'http://twitter.com/search?q=%23%D8%A8%D8%B9%D8%AF_%D8%A7%D9%84%D9%81%D8%B7%D8%A7%D8%B1_%D8%A8%D8%AA%D8%B9%D9%85%D9%84_%D8%A7%D9%8A%D9%87', u'query': u'%23%D8%A8%D8%B9%D8%AF_%D8%A7%D9%84%D9%81%D8%B7%D8%A7%D8%B1_%D8%A8%D8%AA%D8%B9%D9%85%D9%84_%D8%A7%D9%8A%D9%87', u'tweet_volume': None, u'name': u'#\u0628\u0639\u062f_\u0627\u0644\u0641\u0637\u0627\u0631_\u0628\u062a\u0639\u0645\u0644_\u0627\u064a\u0647', u'promoted_content': None}, {u'url': u'http://twitter.com/search?q=%23%D8%A7%D9%83%D8%AA%D8%A8_%D8%AA%D9%88%D9%8A%D8%AA%D9%87_%D8%AD%D9%84%D9%88%D9%87', u'query': u'%23%D8%A7%D9%83%D8%AA%D8%A8_%D8%AA%D9%88%D9%8A%D8%AA%D9%87_%D8%AD%D9%84%D9%88%D9%87', u'tweet_volume': 33310, u'name': u'#\u0627\u0643\u062a\u0628_\u062a\u0648\u064a\u062a\u0647_\u062d\u0644\u0648\u0647', u'promoted_content': None}, {u'url': u'http://twitter.com/search?q=%23%D9%81%D9%84%D8%B3%D8%B7%D9%8A%D9%86', u'query': u'%23%D9%81%D9%84%D8%B3%D8%B7%D9%8A%D9%86', u'tweet_volume': None, u'name': u'#\u0641\u0644\u0633\u0637\u064a\u0646', u'promoted_content': None}, {u'url': u'http://twitter.com/search?q=%23%D8%AF%D8%B9%D9%88%D9%87_%D8%AD%D8%A8', u'query': u'%23%D8%AF%D8%B9%D9%88%D9%87_%D8%AD%D8%A8', u'tweet_volume': 21448, u'name': u'#\u062f\u0639\u0648\u0647_\u062d\u0628', u'promoted_content': None}, {u'url': u'http://twitter.com/search?q=%23%D8%B3%D9%85%D8%B1%D9%82%D9%86%D8%AF', u'query': u'%23%D8%B3%D9%85%D8%B1%D9%82%D9%86%D8%AF', u'tweet_volume': None, u'name': u'#\u0633\u0645\u0631\u0642\u0646\u062f', u'promoted_content': None}, {u'url': u'http://twitter.com/search?q=%23HBDAnis', u'query': u'%23HBDAnis', u'tweet_volume': None, u'name': u'#HBDAnis', u'promoted_content': None}, {u'url': u'http://twitter.com/search?q=%23%D9%86%D8%B5_%D9%8A%D9%88%D9%85', u'query': u'%23%D9%86%D8%B5_%D9%8A%D9%88%D9%85', u'tweet_volume': None, u'name': u'#\u0646\u0635_\u064a\u0648\u0645', u'promoted_content': None}, {u'url': u'http://twitter.com/search?q=%23%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D9%87', u'query': u'%23%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D9%87', u'tweet_volume': 101106, u'name': u'#\u0627\u0644\u0633\u0639\u0648\u062f\u064a\u0647', u'promoted_content': None}, {u'url': u'http://twitter.com/search?q=%23%D8%A7%D9%84%D9%85%D8%BA%D8%B1%D8%A8', u'query': u'%23%D8%A7%D9%84%D9%85%D8%BA%D8%B1%D8%A8', u'tweet_volume': None, u'name': u'#\u0627\u0644\u0645\u063a\u0631\u0628', u'promoted_content': None}, {u'url': u'http://twitter.com/search?q=%23%D8%A7%D9%84%D9%85%D8%B4%D8%A7%D9%87%D9%8A%D8%B1', u'query': u'%23%D8%A7%D9%84%D9%85%D8%B4%D8%A7%D9%87%D9%8A%D8%B1', u'tweet_volume': None, u'name': u'#\u0627\u0644\u0645\u0634\u0627\u0647\u064a\u0631', u'promoted_content': None}, {u'url': u'http://twitter.com/search?q=%23%D8%AF%D8%A7%D8%B9%D8%B4', u'query': u'%23%D8%AF%D8%A7%D8%B9%D8%B4', u'tweet_volume': 28934, u'name': u'#\u062f\u0627\u0639\u0634', u'promoted_content': None}, {u'url': u'http://twitter.com/search?q=%23%D8%A7%D9%84%D8%AF%D9%85%D8%B9%D9%87_%D8%A7%D9%84%D8%AD%D9%85%D8%B1%D8%A7%D8%A1', u'query': u'%23%D8%A7%D9%84%D8%AF%D9%85%D8%B9%D9%87_%D8%A7%D9%84%D8%AD%D9%85%D8%B1%D8%A7%D8%A1', u'tweet_volume': None, u'name': u'#\u0627\u0644\u062f\u0645\u0639\u0647_\u0627\u0644\u062d\u0645\u0631\u0627\u0621', u'promoted_content': None}], u'as_of': u'2016-06-11T10:46:11Z', u'locations': [{u'woeid': 23424740, u'name': u'Algeria'}]}]
