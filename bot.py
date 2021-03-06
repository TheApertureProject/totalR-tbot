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

def get_vine(): # Get a random example of def from ud.com
    try:
        r = requests.get(url="http://api.urbandictionary.com/v0/random")
        r2 = json.loads(r.text)
        r3 = r2["list"][0]["example"]
        if len(r3) > 281:
            while len(r3) > 281:
                r = requests.get(url="http://api.urbandictionary.com/v0/random")
                r2 = json.loads(r.text)
                r3 = r2["list"][0]["example"]
        r4 = r3.replace('[', '')
        r5 = r4.replace(']', '')
        return r5
    except Exception as e:
        print(e)
        return 1

def get_definition(): # Get a random word & its definition from ud.com
    try:
        r = requests.get(url="http://api.urbandictionary.com/v0/random")
        down = 0
        r2 = json.loads(r.text)
        word1 = r2["list"][0]["word"]
        definition1 = r2["list"][0]["definition"]
        full = f"\"{word1}\" — {definition1}"
        if len(full) > 281:
            while len(full) > 281:
                r = requests.get(url="http://api.urbandictionary.com/v0/random")
                r2 = json.loads(r.text)
                word1 = r2["list"][0]["word"]
                definition1 = r2["list"][0]["definition"]
                full = f"{word1} — {definition1}"
            full = full.replace('[', '')
            full = full.replace(']', '')
            return full
        else:
            full = full.replace('[', '')
            full = full.replace(']', '')
            return full
    except Exception as e:
        print(e)
        return 1

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
    VINE = get_vine()
    DEF = get_definition()
    XLIST = [FACT, WHY, VINE, DEF]
    FINAL = random.choice(XLIST)
    if FINAL == VINE:
        if VINE != 1:
            api.update_status(FINAL)
    elif FINAL == DEF:
        if DEF != 1:
            api.update_status(FINAL)    
    else:
        XLIST = [FACT, WHY]
        FINAL = random.choice(XLIST)
        api.update_status(FINAL)
    time.sleep(TIMER)
