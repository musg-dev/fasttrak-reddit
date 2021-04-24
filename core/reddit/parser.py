import re

def parse_vote(x):
    if re.match(x, "/(Aye)/i") == True:
		print("Core::Reddit::Parser::Vote // [AYE] " + i.author.name)
        return 1
	if re.match(x, "/(Yea)/i") == True:
	    print("Core::Reddit::Parser::Vote // [AYE] " + i.author.name)
        return 1
	if re.match(x, "/(Nay)/i") == True:
	    print("Core::Reddit::Parser::Vote // [NAY] " + i.author.name)
        return 0
	if re.match(x, "/(Abstain)/i") == True:
		print("Core::Reddit::Parser::Vote // [ABSTAIN] " + i.author.name)
        return 2

