# input
n = 3 # try different values for n

# your code
if n%2 != 0:
  print("Weird")
elif n%2 == 0 and 2 <= n <=5:
  print("Not Weird")
elif n%2 == 0 and 6 <= n <=20:
  print("Weird")
elif n > 20:
  print("Not Weird")
