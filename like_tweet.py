import os
import logging

import requests
import tweepy
from dotenv import load_dotenv
from tweepy import TooManyRequests, Client

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Put there id of any existing tweet in Tweeter.
tweet_id = '1896695607542284632'


class TwitterAPI:
    """
    Class for working with Twitter API.

    Attributes:
        bearer_token (str): Twitter API bearer token.
        consumer_key (str): Twitter API consumer key.
        consumer_secret (str): Twitter API consumer secret.
        access_token (str): Twitter API access token.
        access_token_secret (str): Twitter API access token secret.
        user_id (str): Twitter API user id.
    """
    def __init__(self):
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        self.consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
        self.consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
        self.access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        self.access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        self.user_id = os.getenv("TWITTER_USER_ID")

        if not all(
                [self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret, self.user_id]):
            logging.error("Missing API credentials. Make sure to set all required environment variables in .env file.")
            raise ValueError("API credentials are missing, check your credentials in .env file.")

        self._client = tweepy.Client(self.bearer_token, self.consumer_key, self.consumer_secret, self.access_token,
                                     self.access_token_secret)
        auth = tweepy.OAuth1UserHandler(
            self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)
        self._api = tweepy.API(auth, wait_on_rate_limit=True)

        try:
            self._api.verify_credentials()
            logging.info("Authentication successful.")
        except tweepy.TweepyException as e:
            logging.error(f"Authentication failed: {e}")
            raise ValueError("Invalid Twitter API credentials, check your credentials in .env file.")

    @property
    def session(self) -> Client:
        """
        Property for collecting Twitter API session.

        :return: Twitter API v2 Client
        """
        return self._client

    def like_tweet(self, post_id: str) -> requests.Response:
        """
        Method for liking post by given post_id.

        :param post_id: id of post to like.
        :return: response from Twitter API.
        """
        logging.info(f"Trying to like a tweet with id {post_id}.")
        try:
            response = self.session.like(post_id)
            response.raise_for_status()
            return response
        except TooManyRequests:
            logging.info("Sorry, looks like you are using free limit endpoint. Try again later.")
        except Exception as e:
            logging.error(f"Something went wrong: {e}")


if __name__ == '__main__':
    twitter = TwitterAPI()
    twitter.like_tweet(tweet_id)
