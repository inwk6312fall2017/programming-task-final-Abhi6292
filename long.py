
"""
l=0
for word in open('Book2.txt').read().split():
    longg = ''
    if len(word)>len(longg):
        longg = word

   # for w in open('book2.txt').read().split():
    #    if
print(longg)
"""

def Words():
    file1 = open('Book1.txt', 'r')
    file2 =open('Book2.txt','r')
    file3 = open('Book3.txt', 'r')
    longg1 = ''
    for line in file1:
        for word in line.split():
            if len(word) > len(longg1):
                longg1 = word
           #     print(longg1)
                for l in file2:
                    for w in l.split():
                        if len(w)> len(longg1):
                            longg1=w
                     #       print(longg1)
                            for li in file3:
                                for wo in l.split():
                                    if len(wo) > len(longg1):
                                        longg1 = wo

    print (longg1)


Words()
