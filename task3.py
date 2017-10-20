file1 = open('running-config.cfg', 'r')
file2 =open('newrunning-config.cfg','w')
n=1

for line in file1:
    for word in line:
        if word == '172':
            file2.write(word.replace('172','192'))
            n+=1
        else:
            file2.write(word)


file1.close()

