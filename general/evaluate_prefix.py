"""
function that evaluates prefix notation string

things to have in mind:
* strings are maybe not in prefix notation (if more than one element is 
left on the stack or we don't have enough operands on stack- return false)
* we can encounter division by zero or overflow 
    - how likely are those things to acure
    - what will be their impact on system if they occure
    - is it too time consuming to chech if o2 is 0 if we have 
      division or do we have overflow after multiplying 
* think about setting some length restrictions
"""

def evaluate_prefix(string):
    if string is None or len(string) < 3:
        return False

    stack = []
    string = string.split(' ')

    # reading from right to left
    for symbol in string[::-1]:
        if symbol.isdigit():
            stack.append(symbol)
        else:
            if len(stack) >= 2:
                op1 = stack.pop()
                op2 = stack.pop()
                result = 0
                # check for zero division
                if symbol == '/':
                    if op2 == '0':
                        raise ZeroDivisionError('cannot divide by zero')
                    result = eval(" ".join([op1, symbol, op2]))
                # value overflow
                elif symbol == '*':
                    result = eval(" ".join([op1, symbol, op2]))
                    if str(result) == op1 or str(result) == op2:
                        raise OverflowError('cannot multiply - overflow error')
                else:
                    result = eval(op1 + symbol + op2)
                stack.append(str(result))
            else:
                raise ValueError('wrong input - check prefix notation')

    if len(stack) == 1:
        return stack.pop()
    else:
        raise ValueError('wrong input - check prefix notation')


try:
    # test cases
    # zero division
    # string = "/ 2 0"

    # normal 
    string = "- * / 15 - 7 + 1 1 3 + 2 + 1 1"
    print evaluate_prefix(string)

except ZeroDivisionError as e:
    print e
except OverflowError as e:
    print e
except ValueError as e:
    print e
