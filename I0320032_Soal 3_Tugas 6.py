#rentang nilai
for i in range (10, 25):

    #hasil
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print("%i bukan prima" % i)
        i +=1
    else:
        print("%i adalah bilangan prima" % i)