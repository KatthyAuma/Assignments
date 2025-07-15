

def isleap(year:int=0)->None:
    year = int(input("Enter year: "))
    if ((year%4)==0) & ((year%100)!=0) or ((year%400)== 0):
        print (f"{year} is Leap")

    else:
        print (f"{year} is NOT Leap")

isleap()
