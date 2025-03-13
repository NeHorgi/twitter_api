Here is a test task for The Soul Publishing.
This script likes a tweet in Twitter by given id of tweet.

For using it just copy all of these files in your work directory.

1) Install requirements by using command:

       'pip install -r requirements.txt'

2) Activate venv in you work directory

    For Windows (Git Bash):

       python -m venv venv
       venv/Scripts/activate

    For Linux/macOS:

       python -m venv venv
       venv/bin/activate
3) Create ".env" file in the root of directory and fill it with following data:

    You can find all of these parameters on the page of your developer Twitter account.

       TWITTER_BEARER_TOKEN - Twitter API bearer token.
       TWITTER_USER_ID - Twitter API user id.
       TWITTER_CONSUMER_KEY - Twitter API consumer key.
       TWITTER_CONSUMER_SECRET - Twitter API consumer secret.
       TWITTER_ACCESS_TOKEN - Twitter API access token.
       TWITTER_ACCESS_TOKEN_SECRET - Twitter API access token secret.

4) In file like_tweet.py change variable "tweet_id" on any existing tweet you would like to like.
5) In cmd in you work directory run command

       python .\like_tweet.py
    
    or start manually from the module.

