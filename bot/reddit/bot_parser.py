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
    if re.compile("(S.)").search(title):
        return 1
    elif re.compile("(H.R.)").search(title):
        return 2
    elif re.compile("(S.Res.").search(title):
        return 3
    elif re.compile("(H.Res.)").search(title):
        return 4
    elif re.compile("(S.Con.Res.)").search(title):
        return 5
    elif re.compile("(H.Con.Res.").search(title):
        return 6
    elif re.compile("(S.J.Res.)").search(title):
        return 7
    elif re.compile("(H.J.Res.)").search(title):
        return 8
    else:
        return 0


def parse_bill_num(title, bill_type):
    if bill_type == 3 or 4:
        raw_bill_num = title[5:8]
        bill_num = [int(word) for word in raw_bill_num.split() if word.isdigit()]
        return bill_num
    if bill_type == 5 or 6:
        raw_bill_num = title[9:12]
        bill_num = [int(word) for word in raw_bill_num.split() if word.isdigit()]
        return bill_num
    if bill_type == 7 or 8:
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
