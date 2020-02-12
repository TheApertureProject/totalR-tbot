print(f"""Welcome to TotalRandom™ !

---   .     . .-.         .         
 |.-.-|-.-. | |-'.-. .-..-| .-..-.-.
 '`-' '-`-`-'-'`-`-`-' '`-'-`-'' ' '

""")

try:
    import nekos, os, sys, tweepy, time, logging, random, requests, json
    print('All modules successfully imported.')
except ImportError:
    print('Failed to import one or more libraries.')
    sys.exit()

logging.basicConfig(level='INFO') # Enable logging

def get_fact(): # Get a random fact from nekos.life
    FACTS = nekos.fact()
    return FACTS

def get_why(): # Get a random question from nekos.life
    WHYYY = nekos.why()
    WHYY = WHYYY.capitalize() # Uppercase the first letter of the question
    return WHYY

#def get_vine(): # Get a random example of def from ud.com
#    r = requests.get(url="http://api.urbandictionary.com/v0/random")
#    if type(r) == int:
#        return 1
#    else:
#        r2 = json.loads(r.text)
#        r3 = r2["list"][0]["example"]
#if len(r3) > 281:
#            while len(r3) > 281:
#                r = requests.get(url="http://api.urbandictionary.com/v0/random")
#                r2 = json.loads(r.text)
#                r3 = r2["list"][0]["example"]
#            r4 = r3.replace('[', '')
#            r5 = r4.replace(']', '')
#            return r5

# Environment vars
# Access your app's credentials in the Twitter developer dashboard
# Set vars in the heroku dashboard

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

# End of environment vars

TIMER = 60 * 60 # Wait time between two tweets

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    FACT = get_fact()
    WHY = get_why()
    #VINE = get_vine()
    XLIST = [FACT, WHY]
    FINAL = random.choice(XLIST)
    #    if FINAL == VINE:
    #        if VINE != 1:
    #            api.update_status(random.choice(FINAL))
    #    else:
    #        XLIST = [FACT, WHY]
    #        FINAL = random.choice(XLIST)
    #        api.update_status(random.choice(FINAL))
    api.update_status(random.choice(FINAL))
    time.sleep(TIMER)
