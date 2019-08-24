import logging
from operator import itemgetter

import requests
from flask import Flask
from flask_ask import Ask, statement


REPOSITORY = 'johnwheeler/flask-ask'
ENDPOINT = 'https://api.github.com/repos/{}'.format(REPOSITORY)

app = Flask(__name__)
ask = Ask(app, '/')
logger = logging.getLogger()


@ask.launch
def launch():
    return stats()


@ask.intent("StatsIntent")
def stats():
    r = requests.get(ENDPOINT)
    repo_json = r.json()

    if r.status_code == 200:
        repo_name = ENDPOINT.split('/')[-1]
        keys = ['stargazers_count', 'subscribers_count', 'forks_count']
        stars, watchers, forks = itemgetter(*keys)(repo_json)
        speech = "{} has {} stars, {} watchers, and {} forks. " \
            .format(repo_name, stars, watchers, forks)
    else:
        message = repo_json['message']
        speech = "There was a problem calling the GitHub API: {}.".format(message)

    logger.info('speech = {}'.format(speech))
    return statement(speech)