a = input("enter your world\n")
if type(world)!=type(str):
def world(a):
    if len(a)<7:
        print("your world should be len 7")
        return"false"
    elif len(a)%2==0:
            return"please insert an odd world len then 7"

    else:
        c=len(a)//2-1
        d=c+3
        return(a[c:d]) 
        
print(world(a)) 
