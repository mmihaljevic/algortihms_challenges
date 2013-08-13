"""
Write a function that converts numbers to words. Separate each word by a dash character.

Example: The number 125 will be converted in:

one-hundred-twenty-five
Input 
List of numbers. Read from the stdin.

Output 
For each number, print out the english words
"""

numbers_single = {
    "1" : "one", "2" : "two", "3" : "three", "4" : "four",
    "5" : "five", "6" : "six", "7" : "seven", "8" : "eight",
    "9" : "nine", "0" : "zero" 
}

numbers_double = {
    "10" : "ten", "11" : "eleven", "12" : "twelve", "13" : "thirteen", 
    "20" : "twenty", "30" : "thirty", "40" : "fourty", "50" : "fifty",     
    "60" : "sixty", "70" : "seventy", "80" : "eighty", "90": "ninety",
    "2" : "twenty", "3" : "thirty", "4" : "fourty", "5" : "fifty", 
    "6" : "sixty", "7" : "seventy", "8" : "eighty", "9": "ninety"
}

number_decimals = {
    3 : "hundred", 4 : "thousand"}

def number_to_word(number):
    decimals = len(number)
    # special cases
    if decimals == 0:
        return
    if decimals == 1:
        return numbers_single[number]
    if decimals == 2:
        if number[0] == "0":
            return number_to_word(number[1:])
        if numbers_double.has_key(number):
            return numbers_double[number]
        else:
            return numbers_double[number[0]] + "-" + number_to_word(number[1:])
    if decimals == 3 or decimals == 4:
        if number[0] == "0" :
            return  number_to_word(number[1:])
        return numbers_single[number[0]] + "-"+ number_decimals[decimals] +"-" + number_to_word(number[1:])



print number_to_word("1")
print number_to_word("20")
print number_to_word("21")
print number_to_word("13")
print number_to_word("123")
print number_to_word("110")
print number_to_word("101")
print number_to_word("506")
print number_to_word("1034") 
