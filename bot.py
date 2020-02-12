print(f"""Welcome to TotalRandom™ !

---   .     . .-.         .         
 |.-.-|-.-. | |-'.-. .-..-| .-..-.-.
 '`-' '-`-`-'-'`-`-`-' '`-'-`-'' ' '

""")

try:
    import nekos, os, tweepy, time, logging
    print('All modules successfully imported.')
except ImportError:
    print('Failed to import one or more libraries.')
    sys.exit()

logging.basicConfig(level='INFO') # enable logging

def get_fact(): # get a random fact from nekos.life
    FACTS = nekos.fact()
    return FACTS

# env vars
# access credentials in the twitter dev dashboard
# set vars in the heroku dashboard

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

# end env vars

TIMER = 2 * 60 * 60 # wait two hours

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    FACT = get_fact()
    api.update_status(FACT)
    time.sleep(TIMER)
