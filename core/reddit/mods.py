import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def list_mods(reddit):
		mods = []
		for moderator in reddit.subreddit(config.MOD_SUB).moderator():
			mods.append(str(moderator))
		return mods