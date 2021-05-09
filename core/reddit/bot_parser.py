import js_regex as re


def parse_vote(x, y):
    if re.compile("(Aye)").search(x):
        print("Core::Reddit::Parser::Vote // [AYE] " + y)
        return 1
    if re.compile("(Yea)").search(x):
        print("Core::Reddit::Parser::Vote // [AYE] " + y)
        return 1
    if re.compile("(Yay)").search(x):
        print("Core::Reddit::Parser::Vote // [AYE] " + y)
        return 1
    if re.compile("(Nay)").search(x):
        print("Core::Reddit::Parser::Vote // [NAY] " + y)
        return 0
    if re.compile("(Abstain)").search(x):
        print("Core::Reddit::Parser::Vote // [ABSTAIN] " + y)
        return 2
    if re.compile("(FastTRAK)").search(x):
        print("Core::Reddit::Parser::Vote // [AYE] " + y)
        return 10
