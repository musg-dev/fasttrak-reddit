import os

CLIENT_ID = "xyz"
CLIENT_SECRET = "123"
USERNAME = "xyz"
PASSWORD = "123"

SENTRY_URL= "abc" # URL for Sentry Errors

TRIGGER = "./FastTRAK" # Word to get the bot's attention.

MOD_SUB = "MUSGFastTRAK" # Sub to which draw the list of authorized users.


if os.environ("FT_DEVEL") == "1":
    WATCH_SUBS = "MUSGFastTRAKSandbox"
    DATABASE_URI = 'postgresql+psycopg2://fasttrak:password@localhost:5432/devel'
else:
    WATCH_SUBS = "ModelUSHouseFACom+ModelUSHouseBudgetCom+ModelUSHouseESTCom+ModelUSHouseELECom+ModelUSHouseGOIII+ModelUSHouseJudicial+ModelUSHouseRulesCom+ModelUSHouseIntelCom+ModelSenateJudiciCom+ModelSenateEnviroCom+ModelSenateFinanceCom+ModelSenateFACom+ModelUSSenate+ModelUSHouse"
    DATABASE_URI = 'postgresql+psycopg2://fasttrak:password@localhost:5432/prod'