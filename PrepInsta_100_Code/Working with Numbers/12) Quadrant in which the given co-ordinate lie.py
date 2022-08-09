# Quadrant in which the given co-ordinate lie

#     II     |      I
#   (-x,y)   |    (x,y)
#            |
# |||||||||||||||||||||||||
#            |
#    III     |      IV
#  (-x,-y)   |    (x,-y)

def quadrant(x,y):
    if(x==0 and y==0):
        print("At Origin.")
    elif(x==0):
        print("On Y-axis.")
    elif(y==0):
        print("On X-axis.")
    elif(x>0 and y>0):
        print(x,"and",y,"is in I Quadrant.")
    elif(x<0 and y>0):
        print(x,"and",y,"is in II Quadrant.")
    elif(x<0 and y<0):
        print(x,"and",y,"is in III Quadrant.")
    else:
        print(x,"and",y,"is in IV Quadrant.")

x,y=map(int,input("Enter the cordinates: ").split())
quadrant(x,y)
