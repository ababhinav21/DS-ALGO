def issorted(a):
    le=len(a)
    if le==0 or le==1:
        return True
    elif a[0]>a[1]:
        return False
    smallerList=a[1:]
    issmallerListSorted= issorted(smallerList)
    if issmallerListSorted:
        return True
    else:
        return False  
    
a=[1,2,3,4,5,6,8]
print(issorted(a))