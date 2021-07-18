from bot import config


def list_mods(reddit):
	mods = []
	for moderator in reddit.subreddit(config.MOD_SUB).moderator():
		mods.append(str(moderator))
		return mods
