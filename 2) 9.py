def sum_thrice(w,x, y, z):

     sum = w + x + y + z
  
     if w == x == y == z:
      sum = sum * 4
     return sum

print(sum_thrice(1, 2, 3 ,4))
print(sum_thrice(3, 3, 3 ,4))
