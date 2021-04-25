from core import config

def list_mods():
		mods = []
		for moderator in reddit.subreddit(config.MOD_SUB).moderator():
			mods.append(str(moderator))
		return mods