print "Hey! What's your name?"

name = raw_input("> ")

print """
Hey %s, I'm thinking of a number
between 1 and 100. Try to guess my number!
""" % name

my_num = 34
not_won = True
i = 1

def check(guess):
    global i
    global not_won
    number = int(guess)
    
    print "The number I'm checking is %s" % number

    if number < 34:
        print "Too low. Try again."
        i += 1
    elif number > 34:
        print "Too high. Try again."
        i += 1
    else:
        print "Congratulations! You got it in %s times!" % i
        not_won = False 

def check_char(char):
    global i
    if ord(char) >= 0 and ord(char) <= 127:

        if ord(char) >= 48 and ord(char) <= 57:
            return False
        else: 
            return True 
    else: 
        return False


def check_input(input):
    for char in input:
        if check_char(char):
            return False
    return True

while not_won:

    number = raw_input("> ")

    if check_input(number):
        check(number)
    else: 
        i += 1
        print "You suck! Don't try to break my game! Try again."