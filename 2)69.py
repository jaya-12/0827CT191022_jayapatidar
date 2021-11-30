def checknumber(A, val):
# traverse in the list
   for i in A:
     if val>= i:
      return False
      return True
   # Driver code
     A=list()
     n1=int(input("Enter the size of the List ::"))
     print("Enter the Element of List ::")
   for i in range(int(n1)):
     k=int(input(""))
   A.append(k)
   val = int(input("Enter the checking value"))
   if(checknumber(A, val)):
       print("All the values are greater than ",val)
   else:
       print("Values are not greater than ",val)
