import praw
import config
import time
import os

def bot_login():
	print("loading... " + config.catch_phrase)
	r = praw.Reddit(username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = "n00b90's special bot v1a")
	print("READY!!!!! " + config.catch_phrase)
	return r

def run_bot(r, comments_replied_to):
	print("Obtaining 1000 comments. " + config.catch_phrase)
	for comment in r.subreddit('teenagers').comments(limit=1000):
		if "u/ReqostSleuthBott" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me() or "u/reqostsleuthbott" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
			print("String found in comment: " + comment.id + " " + config.catch_phrase)
			comment.reply("Looks like a repost. I've seen this image 3 times.\n\nFirst seen [Here](https://youtu.be/dQw4w9WgXcQ) on 2019-12-09 98.44% match. Last seen [Here](https://youtu.be/dQw4w9WgXcQ) on 2020-02-26 96.88% match\n\n__Searched Images:__ 124,094,822 | __Indexed Posts:__ 518,905,752 | __Search Time:__ 1.00131s\n\n_Feedback? Hate? Visit_ r/repostsleuthbot - _I'm not perfect, but you can help. Report [ [False Positive](https://www.reddit.com/message/compose/?to=ReqostSleuthBott&subject=False%20Positive&message={%22post_id%22:%20%22hbbnaw%22,%20%22meme_template%22:%20null}) ]_")
			print("Replied to comment! " + config.catch_phrase)
			comments_replied_to.append(comment.id)
			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")
	print("Sleeping for 3 seconds... " + config.catch_phrase)
	# My lovely bot is sleeping
	time.sleep(3)

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open ("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = list(filter(None, comments_replied_to))

	return comments_replied_to

r = bot_login()

comments_replied_to = get_saved_comments()
#print(comments_replied_to)

while True:
	run_bot(r, comments_replied_to)
