import re

def exclamation_marks(s):
    newlist = re.findall("\d\D*!{1,3}\D*\d", s)
    #If newlist is not empty, search for all cases where the condition of the project indicates a "False" should be returned.
    if newlist:
        for x in newlist:
            if x.count("!") == 3:
                sum = int(x[0]) + int(x[-1])
                if sum != 10:
                    return False
            else:
                return False
    #If newlist is empty, then we automatically know we should return a "False" 
    else:
        return False
    #If no conditions return a "False" result, then the string is automatically "True"
    return True

# Simple example
assert exclamation_marks("9!!!1a8!!!b") == True

# Missing third exclamation mark between first pair
assert exclamation_marks("9!!1a8!!!b") == False

# Exactly 3 exclamation marks between 6 and 4, and 3 exclamation marks between 5 and 5 at the end of the string.
assert exclamation_marks("arrb6!!!4xxbl5!!!eee5") == True

# No pairs add up to 10
assert exclamation_marks("dsmb7!!!1s3cr8t!!!efe3fy5!!!rw3") == False

# Second pair has only two exclamation marks
assert exclamation_marks("qsdb9!!!1darwxbl5!!erge5") == False

# Second pair has four exclamation marks
assert exclamation_marks("8!a!b!a2qn9!!!!1") == False

# Additional cases
assert exclamation_marks("b2!!q!8dbl3!!er!7l8q!e!r!2kj") == True
assert exclamation_marks("k9j!!l1ngco8!!a!2") == False
assert exclamation_marks("wd!o!!d9") == False
assert exclamation_marks("asd9!akb!b!anb!2") == False
assert exclamation_marks("r!z!e!d8!r!!2x9!w!va!1z3wq!e!wz!7zj!") == True
