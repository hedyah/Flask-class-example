
from flask import Flask, jsonify, request
from flask_cors import CORS
import sys

app = Flask(__name__)


tweets = [
"kinda rude when I spend money and it actually leaves my bank account but ok", 
"Does anyone else get the random urges at midnight to get their life together lol", 
"I was having problems with my work computer so I called my IT guy and he was like, 'You really need to stop calling me when Im at school, Mom.", 
"I don't think it's a coincidence that diet has the word die in it.", 
"My dog sighs a lot for somebody who doesn't contribute to this house or know what a government is",
"It's called the weekend yet weeks keep happening lol", 
"I've been alive 20 years and still haven't found the right thing to say when someone knocks on the door of the public bathroom you're in.",
"You ever accidentally make eye contact with someone 10 + times?", 
"When you're both typing so you erase the message to let them speak first, but they do the same thing lol." 
]

@app.get('/api/tweets')
def tweets_get():
    args = request.args
    #tweetId
    tweet_id = args.get('tweetId')
    #if not tweet_id (alternative way)
    if tweet_id == None:
        return jsonify(tweets), 200
    else:
        return jsonify(tweets[tweet_id]), 200

if len(sys.argv) > 1:
    mode = sys.argv[1]
    print (sys.argv[0])
    print (sys.argv[1])
else:
    print("missing requriement argument: testing")
    exit()
    
if mode == "testing":
    CORS(app)
    app.run(debug=True)
elif mode == "production":
    import bjoern
    print("running production mode")
    bjoern.run(app, "0.0.0.0", 5000)
else:
    print("invalid mode, please chose either 'testing' or 'prodction'")
