#Problem: Print 3-D coordinates such that sum of them is less than or equal to 3


for x in range(0,3):
    for y in range(0,3):
        for z in range(0,3):
            if x+y+z<=3:
                print (x,y,z)
