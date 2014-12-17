# My first Reddit bot, used to comment on everything Jack has posted.

import praw
import os
from config import *

user_agent = "Jack lolbot 1.0"
r = praw.Reddit(user_agent=user_agent)

r.login(REDDIT_USERNAME, REDDIT_PASS)

if not os.path.isfile('jack_comments.txt'):
	replied = []
else:
	with open('jack_comments.txt') as f:
		replied = f.read()
		replied = replied.split('\n')
		replied = filter(None, replied)

jack = r.get_redditor('searchin4sanity')
comments = jack.get_comments(limit=5)

for submission in comments:
	if submission.id not in replied:
		submission.reply("Whatever you say, J.")
		print 'Bot replied to comment', submission.id
		replied.append(submission.id)

with open('jack_comments.txt', 'w') as f:
	for post_id in replied:
		f.write(post_id + '\n')







