import re

def exclamation_marks(s):
    # Alright, so this can search for all instances of 
    # ! points within a string. I can then use a for loop to go 
    # through each instance and see if any are <> 3. If so, the string 
    # won't work.

    substr = re.findall('!+',s)

    if substr is not None:
        if any(len(straight) != 3 for straight in substr):
            print("We'll exit here")
            return False
        else:
            print("We'll continue here")

#Test case to begin checking items
z = exclamation_marks("He!!!oo0")
if z == False:
    print("Hello!")

