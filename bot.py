print(f"""Welcome to TotalRandom™ !

---   .     . .-.         .         
 |.-.-|-.-. | |-'.-. .-..-| .-..-.-.
 '`-' '-`-`-'-'`-`-`-' '`-'-`-'' ' '

""")

try:
    import nekos, os, sys, tweepy, time, logging, random
    print('All modules successfully imported.')
except ImportError:
    print('Failed to import one or more libraries.')
    sys.exit()

logging.basicConfig(level='INFO') # enable logging

def get_fact(): # get a random fact from nekos.life
    FACTS = nekos.fact()
    return FACTS

def get_why(): # get a random question from nekos.life
    WHYY = nekos.why()
    return WHY

# env vars
# access credentials in the twitter dev dashboard
# set vars in the heroku dashboard

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

# end env vars

TIMER = 10 # wait time between two tweets

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    FACT = get_fact()
    WHY = get_why()
    XLIST = [FACT, WHY]
    CHOICE = random.choice
    api.update_status(FACT)
    time.sleep(TIMER)
