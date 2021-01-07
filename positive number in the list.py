myList=[]
a = eval(input("enter the no. of elements in the list:\n"))                                 
for i in range(0,a):
    print("enter the element no.\n",i)
    i+=1
    element=int(input())
    myList.append(element)

print("\nPositive Numbers in this List are : ")
for j in range(a):
    if(myList[j] >= 0):
        print(myList[j], end = '   ')
