# FastTRAK
FastTRAK is a software suite for automating common tasks of r/ModelUSGov clerks, but in theory can be expanded to any Reddit-based polisim. It consists of a Reddit bot, a Discord bot, a Google Sheets client, and a web-based report engine.
## Reddit Bot
The Reddit bot is the part that most people in the sim will interact with. It has the job of monitoring legislation and updating the status of things in its database such as the status of the thread and how people voted on it. 
### Installation
FastTRAK requires Python 3 or higher and PostgreSQL 10 or higher. We recommend running this on an Enterprise Linux distro such as AlmaLinux or Rocky Linux.

Clone the repo, create a virtualenv, then drop into it and install the requirements using pip3. Modify the config to match your setup, including Sentry.
### Usage
(venv) python3 bot.py
### Credits
Chance Callahan | u/hyp3rdriv3
### Partners
r/ModelUSGov