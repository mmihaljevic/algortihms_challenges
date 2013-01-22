"""
parse number range 1, 2-7, 11 = 1, 2, 3, 4, 5, 6, 7, 11
- check if range is valid
- do we need to support negatives? for this case not
"""

def parse_number(string):
    """ string with given ranges"""
    if string is None or len(string) < 1:
        return False

    result = []
    # tokenize by ,
    tokens = string.split(',')
    for token in tokens:
        token = token.strip()
        # wrong format
        if len(token) == 0:
            return False
        # only one number - could be positive or negative
        elif len(token) < 3:
            if len(result) > 0 and int(result[-1]) > int(token):
                return False
            result.append(token)
        # range 
        elif '-' in token:
            range = token.split('-')
            # check if range is valid
            if len(result) and (int(result[-1]) > int(range[0]) or int(range[0]) >= int(range[1])):
                return False
            result.extend(str(i) for i in xrange(int(range[0]), int(range[1]) + 1))                    
        else:
            return False
    return result

s1 = "1"
s2 = "1-5"
s3 = "1, 3-5, 8"
s4 = "-1, 3, -4"
s5 = "-1, 4-5, 7"
s6 = "1-5, 6-8, 9-13"
s = [s1, s2, s3, s4, s5, s6]

for string in s:
    print parse_number(string) 
