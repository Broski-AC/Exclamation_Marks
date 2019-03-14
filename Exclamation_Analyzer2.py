import re

def exclamation_marks(s):

    #So this only handles if the exclamation points are right next to each other
    #Apparently we can also have it so that there are characters between the points.
    '''
    substr = re.findall('!+', s)
    if substr is not None:
        if any(len(straight) != 3 for straight in substr):
            print("We're looking okay")
            return False
        else:
    '''
            #I think if I include the \D* between the exclamation points, we
            #should be on the right track. I think if I play with the above section
            #and work it into this code I should have the whole thing figured out.
    newlist = re.findall("\d\D*!{1,3}\D*\d", s)
                #Would need to be able to count how many times ! appears in the single strings
                #There is quite literally a count function that I can use 
                    #Example: string = "Hi" string.count("i")
    print(newlist)
    sumlist = []
    for x in newlist:
      print(x.count("!"))
      if x.count("!") == 3:
                #May want to put a while loop here to account for the last of
                #testing the string as a whole
        sum = int(x[0]) + int(x[-1])
                    #In this section, could I theoretically make it so that any spaces
                    #where it does = 10 get replaced by a zero, and if the total of the 
                    #list = 0, then we return true
        print(sum) 
        #Once we pass the first test of determining if there actually exists 3 exclamation points, then we need to check that the digits add up to 10
        if sum != 10:
          sumlist.append(1)
          print(sumlist)
        else:
          sumlist.append(0)
          print(sumlist)
    #So, if sumlist = 0, then we can return a True. If it doesn't equal 0, we can say False
    sum_numbers = 0
    for x in sumlist:
      sum_numbers += x
    if sum_numbers != 0:
      return False
    else:
      return True

exclamation_marks("9!!!1a8!!!b")
exclamation_marks("9!!1a8!!!b")
exclamation_marks("arrb6!!!4xxb15!!!eee5")
exclamation_marks("dsmb7!!!1s3cr8t!!!efe3fy5!!!rw3")
exclamation_marks("r!z!e!d8!r!!2x9!w!va!1z3wq!e!wz!7zj!")
'''
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
'''
