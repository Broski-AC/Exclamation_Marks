import re

def exclamation_marks(s):

    substr = re.findall('!+', s)
    if substr is not None:
        if any(len(straight) != 3 for straight in substr):
            print("We're looking okay")
            return False
        else:
            newlist = re.findall("\d\D*!!!\D*\d", s)
            print(newlist)
            for x in newlist:
                if x[0].isdigit() and x[-1].isdigit():
                    sum = int(x[0]) + int(x[-1])
                    if sum != 10:
                        return False
                    else:
                        return True
                else:
                    pass
    else:
        pass


assert exclamation_marks("qsdb9!!!1darwxbl5!!erge5") == False