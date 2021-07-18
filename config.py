import os

CLIENT_ID = "t9GWKFQdyQ10UQ"
CLIENT_SECRET = "DGji9UkwuOZV-8uWUfrLqIZkG9g"
USERNAME = "MUSGFastTRAK"
PASSWORD = "C0wsg0m00"
USER_AGENT = "MUSGFastTRAK/0.1"

SENTRY_URL = "https://606009b6ca8248659f66cff16254dc6b@o336575.ingest.sentry.io/5686160"  # URL for Sentry Errors

TRIGGER = "./FastTRAK"  # Word to get the bot's attention.

MOD_SUB = "MUSGFastTRAK"  # Sub to which draw the list of authorized users.


if os.getenv("FT_DEVEL") == "1":
    WATCH_SUBS = "MUSGFastTRAKSandbox"
    DATABASE_URI = 'postgresql://fasttrak:password@127.0.0.1:5432/ft_devel'
else:
    WATCH_SUBS = "ModelUSHouseFACom+ModelUSHouseBudgetCom+ModelUSHouseESTCom+" \
                 "ModelUSHouseELECom+ModelUSHouseGOIII+ModelUSHouseJudicial+ModelUSHouseRulesCom+" \
                 "ModelUSHouseIntelCom+ModelSenateJudiciCom+ModelSenateEnviroCom+ModelSenateFinanceCom+" \
                 "ModelSenateFACom+ModelUSSenate+ModelUSHouse"
    DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost:5432/ft_prod'
