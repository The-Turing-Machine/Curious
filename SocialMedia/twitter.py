from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import pprint
import json

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CK=["N8CefcBhNEgLLzj5C5NTkwk7I","XX254OwNWCuctNrlo29GW2Ihx","gcLU6rXGwRHUaWOSl9J648bkp","JlchYZFCVgx0cPrjxtUPumZaO","BzKONSSMBFeqtbHZbMZNU5XC3","yWOim0eBDzMrN8FlOilcRTVCK","9u8p3OjDgDvFjTQQQ5XYQqB8v"]
CS=["XvalzhATRiMwtRmz5g6jrU4yI9VrMvGRbPYpWaXYtPEofMYyMT","KDTb6Q4swNH1ThMO13SH9vzhOQecP9705wFXw6qPg90S52ISZU","JQ5E8Wn0XutYqslBdjGRJxi5snbh2bDmGAeq3mI8bXnmyYVVAn","2Y5s28O5Mt4Ti5i24WG05fkUPkQV5LPJYLktBPzXx1OrZtgZaz","SvhHxNdwb2X4bXL6UnUrkqEZbPUxqDeFEnfhMQLhpx45sU4fTi","4iGTjaL0r9slwCtU5jcQDdqIxvfYsp62Si71128eCJpd3jRJnw","sy82wTf1VlTiCPtdM2BDOYNGRX9aTzrssi9M0IqeNX1lmUBK2M"]

# CONSUMER_KEY = "N8CefcBhNEgLLzj5C5NTkwk7I"
# CONSUMER_SECRET = "XvalzhATRiMwtRmz5g6jrU4yI9VrMvGRbPYpWaXYtPEofMYyMT"

# CONSUMER_KEY="XX254OwNWCuctNrlo29GW2Ihx"
# CONSUMER_SECRET = "KDTb6Q4swNH1ThMO13SH9vzhOQecP9705wFXw6qPg90S52ISZU"

# CONSUMER_KEY="gcLU6rXGwRHUaWOSl9J648bkp"
# CONSUMER_SECRET = "JQ5E8Wn0XutYqslBdjGRJxi5snbh2bDmGAeq3mI8bXnmyYVVAn"

# CONSUMER_KEY="JlchYZFCVgx0cPrjxtUPumZaO"
# CONSUMER_SECRET = "2Y5s28O5Mt4Ti5i24WG05fkUPkQV5LPJYLktBPzXx1OrZtgZaz"

# CONSUMER_KEY="BzKONSSMBFeqtbHZbMZNU5XC3"
# CONSUMER_SECRET = "SvhHxNdwb2X4bXL6UnUrkqEZbPUxqDeFEnfhMQLhpx45sU4fTi"

# CONSUMER_KEY="yWOim0eBDzMrN8FlOilcRTVCK"
# CONSUMER_SECRET = "4iGTjaL0r9slwCtU5jcQDdqIxvfYsp62Si71128eCJpd3jRJnw"

# CONSUMER_KEY="9u8p3OjDgDvFjTQQQ5XYQqB8v"
# CONSUMER_SECRET = "sy82wTf1VlTiCPtdM2BDOYNGRX9aTzrssi9M0IqeNX1lmUBK2M"

CONSUMER_KEY=CK[0]
CONSUMER_SECRET = CS[0]




OT =["4653955494-Cbul45ZQvzsK16aELSN2O6ecVaT4UbSDujfCkqx","4653955494-VRs3MN2aPRhiQFBIdPyMs8S68X1cxaBT81s0bY7","4653955494-2z4klWrjEk8PhV1HCT9QFvibjPouDuj0z2YIQh6","4653955494-7OzM7jwuYoAxVFDAiICYRf4yQP0y5XGItr1G6ii","4653955494-PeENb05JJcTnWJ251V0CmonDCTR0w97hSX6WeN3","4653955494-HI5zQDkJD384A1kq0aXKLtcMFtdsQmtob7pcqgU","4653955494-vi3R1KMecUKtKu27mmqMfAuMwGpYjEcKvXawSfy"]
OTS = ["8CwjuAi7ctdJQIfW4a835IdLYcap8cl5V2ZPaG0rm7exW","2eAn9kfBofZpuFHuYaakbwbNqrpeesInMas1AAdkxQKb1","Kb01dB5abJyhW7to5rYRB9CTW0LwDwG6F4mOUMEQlTxYw","haXwpryYzHoPrOLxNVjGAhRuImvhPdjcw3KfBlQlyIc8R","pNkTXHJ8YiehkdUvXaMzHc3PeKOQyZs18PbpoNef44lUH","g7d049GSwqmAEBI0aSsBTXpWGfweOYIpTt1ktW8j1ZbhU","esHifHRZcQgGJPGfgaZmGcjlUd23IbdjuvbdOSko3CJub"]

# OAUTH_TOKEN = "4653955494-Cbul45ZQvzsK16aELSN2O6ecVaT4UbSDujfCkqx"
# OAUTH_TOKEN_SECRET ="8CwjuAi7ctdJQIfW4a835IdLYcap8cl5V2ZPaG0rm7exW"

# OAUTH_TOKEN="4653955494-VRs3MN2aPRhiQFBIdPyMs8S68X1cxaBT81s0bY7"
# OAUTH_TOKEN_SECRET="2eAn9kfBofZpuFHuYaakbwbNqrpeesInMas1AAdkxQKb1"

# OAUTH_TOKEN= "4653955494-2z4klWrjEk8PhV1HCT9QFvibjPouDuj0z2YIQh6"
# OAUTH_TOKEN_SECRET="Kb01dB5abJyhW7to5rYRB9CTW0LwDwG6F4mOUMEQlTxYw"

# OAUTH_TOKEN = "4653955494-7OzM7jwuYoAxVFDAiICYRf4yQP0y5XGItr1G6ii"
# OAUTH_TOKEN_SECRET ="haXwpryYzHoPrOLxNVjGAhRuImvhPdjcw3KfBlQlyIc8R"

# OAUTH_TOKEN = "4653955494-PeENb05JJcTnWJ251V0CmonDCTR0w97hSX6WeN3"
# OAUTH_TOKEN_SECRET = "pNkTXHJ8YiehkdUvXaMzHc3PeKOQyZs18PbpoNef44lUH"

# OAUTH_TOKEN =  "4653955494-HI5zQDkJD384A1kq0aXKLtcMFtdsQmtob7pcqgU"
# OAUTH_TOKEN_SECRET = "g7d049GSwqmAEBI0aSsBTXpWGfweOYIpTt1ktW8j1ZbhU"

# OAUTH_TOKEN =  "4653955494-vi3R1KMecUKtKu27mmqMfAuMwGpYjEcKvXawSfy"
# OAUTH_TOKEN_SECRET =  "esHifHRZcQgGJPGfgaZmGcjlUd23IbdjuvbdOSko3CJub"



OAUTH_TOKEN = OT[0]
OAUTH_TOKEN_SECRET = OTS[0]
s = requests.session()






coun = ["Afghanistan","Argentina","Armenia","Australia","Austria","Bahrain","Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo","Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","North Korea","Democratic Republic of the Cong","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Kuwait","Kyrgyzstan","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Republic of Korea (South Korea)","Republic of Moldova","Romania","Russian Federation","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syrian Arab Republic","Tajikistan","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom of Great Britain and Northern Ireland","United Republic of Tanzania","United States of America","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]

woeid =[u'23424740', u'23424747', u'23424748', u'23424750', u'23424775', u'23424782', u'23424787', u'23424868', u'23424796', u'23424800', u'23424801', u'23424802', u'23424819', u'23424829', u'23424824', u'23424833', u'83123', u'23424848', u'23424846', u'23424803', u'23424852', u'23424853', u'23424856', u'23424874', u'23424900', u'23424909', u'23424908', u'23424898', u'23424922', u'23424919', u'23424934', u'23424923', u'23424925', u'23424868', u'23424936', u'1062617', u'23424950', u'23424954', u'23424957', u'23424969', u'23424976', u'23424738', u'23424982', u'23424984']






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

def get_oauth(CONSUMER_KEY,CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET):
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    print CONSUMER_KEY
    print "chaneg agaib"
    return oauth

dic = {}
def get_trend_hashtags(woeid,oauth):
        c = 0
        for i in woeid:
            # try:
            b = s.get(url="https://api.twitter.com/1.1/trends/place.json?id="+i+"", auth=oauth)
            # print b.json()
            tag =[]
            try:
            # pp.pprint(b.json())
                loc = b.json()[0]['locations']
                for k in b.json()[0]['trends']:

                    vol = k['tweet_volume']
                    print loc
                    print vol
                    # print pp.pprint(b.json())
                    tag.append(k['query'])

                    # print k['query']
                # print tag[0:10]
                dic[i] = tag[0:10]
                print dic
            except:
                pass
                print "error"
                # CONSUMER_KEY="9u8p3OjDgDvFjTQQQ5XYQqB8v"
                # CONSUMER_SECRET = "sy82wTf1VlTiCPtdM2BDOYNGRX9aTzrssi9M0IqeNX1lmUBK2M"
                # OAUTH_TOKEN =  "4653955494-vi3R1KMecUKtKu27mmqMfAuMwGpYjEcKvXawSfy"
                # OAUTH_TOKEN_SECRET =  "esHifHRZcQgGJPGfgaZmGcjlUd23IbdjuvbdOSko3CJub"
                print c
                if c!=6:

                    CONSUMER_KEY=CK[c+1]
                    CONSUMER_SECRET = CS[c+1]
                    OAUTH_TOKEN = OT[c+1]
                    OAUTH_TOKEN_SECRET =  OTS[c+1]
                    print "changed"
                    oauth = get_oauth(CONSUMER_KEY,CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
                    c = c+1
                else:
                    c=0









if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    else:
        oauth = get_oauth(CONSUMER_KEY,CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
        get_trend_hashtags(woeid,oauth)
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
