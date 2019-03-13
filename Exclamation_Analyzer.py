import re

def exclamation_marks(s):
    # Alright, so this can search for all instances of 
    # ! points within a string. I can then use a for loop to go 
    # through each instance and see if any are <> 3. If so, the string 
    # won't work, and we can automatically return a false value.
    '''
    substr = re.findall('!+',s)

    #If we find actual substrings
    if substr is not None:
        #IF there are any number of exclamation points not equal to 3, then we know
        #that we have an automatic Flase
        if any(len(straight) != 3 for straight in substr):
            print("We'll exit here")
            return False
        else:
            #If we get to this point, we now need to check:
                #1) to see if there are numbers on either side of the split
                #2) what those two number add up to.
            #So since we know that the 3 exclamation points are there, we can
            #split along those lines. That may leave us with more of a mess than before.
    '''
    print(s)
        #Better idea: Try and split so that we can still get the variables on either side of the exclamation points.
        #I quite literally think I can use just this next part as the entire code
    check = re.search("\d!!!\d",s)
    if check is None:
        return False
    else:
        #I wonder if I can just use this, and get right of the first check
        newlist = re.findall("\d\!!!\D*\d",s)
            #Also, need to edit the above.
        print(newlist)
        for x in newlist:
            if x[0].isdigit() and x[-1].isdigit():
                sum = int(x[0]) + int(x[-1])
                    #issue here is that it will only tackle one 
                    #instance in the list. 
                    #I need it so that if all the cases are true, 
                    #then we can submit a final true result
                if sum != 10:
                    return False
                else:
                    return True
            else:
                pass
                    
        print("We'll continue here")
                
assert exclamation_marks("9!!!1a8!!!b") == True
assert exclamation_marks("dsmb7!!!1s3cr8t!!!efe3fy5!!!rw3") == False
assert exclamation_marks("9!!!sdfsd!!!asdfasdf!!!") == False

'''
#Test case to begin checking items
z = exclamation_marks("He!!!oo0")
if z == False:
    print("Hello!")
'''
