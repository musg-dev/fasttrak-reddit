import js_regex as re


def parse_vote(x, y):
    if re.compile("(Aye)").search(x):
        print("Core::Reddit::Parser::Vote // [AYE] " + y)
        return 1
    elif re.compile("(Yea)").search(x):
        print("Core::Reddit::Parser::Vote // [AYE] " + y)
        return 1
    elif re.compile("(Yay)").search(x):
        print("Core::Reddit::Parser::Vote // [AYE] " + y)
        return 1
    elif re.compile("(Nay)").search(x):
        print("Core::Reddit::Parser::Vote // [NAY] " + y)
        return 0
    elif re.compile("(Abstain)").search(x):
        print("Core::Reddit::Parser::Vote // [ABSTAIN] " + y)
        return 2
    elif re.compile("(FastTRAK)").search(x):
        print("Core::Reddit::Parser::Vote // [IGNORE] " + y)
        return 10


def parse_title(title):
    if re.compile("(S.Res.)").search(title):
        return 3
    elif re.compile("(H.Res.)").search(title):
        return 4
    elif re.compile("(S.Con.Res.)").search(title):
        return 5
    elif re.compile("(H.Con.Res.)").search(title):
        return 6
    elif re.compile("(S.J.Res.)").search(title):
        return 7
    elif re.compile("(H.J.Res.)").search(title):
        return 8
    elif re.compile("(S.)").search(title):
        return 1
    elif re.compile("(H.R.)").search(title):
        return 2
    else:
        return 0


def parse_bill_num(title, bill_type):
    if bill_type == 3:
        raw_bill_num = title[5:8]
        bill_num = [int(word) for word in raw_bill_num.split() if word.isdigit()]
        return bill_num
    if bill_type == 4:
        raw_bill_num = title[5:8]
        bill_num = [int(word) for word in raw_bill_num.split() if word.isdigit()]
        return bill_num
    if bill_type == 5:
        raw_bill_num = title[9:12]
        bill_num = [int(word) for word in raw_bill_num.split() if word.isdigit()]
        return bill_num
    if bill_type == 6:
        raw_bill_num = title[9:12]
        bill_num = [int(word) for word in raw_bill_num.split() if word.isdigit()]
        return bill_num
    if bill_type == 7:
        raw_bill_num = title[7:10]
        bill_num = [int(word) for word in raw_bill_num.split() if word.isdigit()]
        return bill_num
    if bill_type == 8:
        raw_bill_num = title[7:10]
        bill_num = [int(word) for word in raw_bill_num.split() if word.isdigit()]
        return bill_num
    if bill_type == 1:
        raw_bill_num = title[1:4]
        bill_num = [int(word) for word in raw_bill_num.split() if word.isdigit()]
        return bill_num
    if bill_type == 2:
        raw_bill_num = title[3:6]
        bill_num = [int(word) for word in raw_bill_num.split() if word.isdigit()]
        return bill_num

def parse_sub(sub_name):
    if sub_name == "ModelUSHouse":
        return 1
    elif sub_name == "ModelUSSenate":
        return 2
    elif sub_name == "ModelSenateJudiciCom":
        return 3
    elif sub_name == "ModelSenateEnviroCom":
        return 4
    elif sub_name == "ModelSenateFinanceCom":
        return 5
    elif sub_name == "ModelSenateFACom":
        return 6
    elif sub_name == "ModelUSHouseFACom":
        return 7
    elif sub_name == "ModelUSHouseBudgetCom":
        return 8
    elif sub_name == "ModelUSHouseESTCom":
        return 9
    elif sub_name == "ModelUSHouseELECom":
        return 10
    elif sub_name == "ModelUSHouseGOIII":
        return 11
    elif sub_name == "ModelUSHouseJudicial":
        return 12
    elif sub_name == "ModelUSHouseRulesCom":
        return 13
    elif sub_name == "ModelUSHouseIntelCom":
        return 14
    elif sub_name == "MUSGFastTRAKSandbox":
        return 15
    else:
        return 0