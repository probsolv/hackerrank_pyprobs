# input
n = int(input())

# your code
for x in range(1,n+1):
  print(x, end = "")
  
#if you wanted to get the number you could try something like this:

n = 90
s = 0
exp = 0
e2 = n-99
e1 = n-9
if n < 100:
    e2 = 0
if n < 10:
    e1 = 0
l = [i for i in range(n, 0, -1)]

for i in l:
    if i >= 100:
        val = int(i * 10 ** (3*exp))
    elif i >= 10:
        val = int(i * 10 ** (2*(exp-e2)) * 10**(3*e2))
    else:
        val = int(i * 10 ** (exp-e1-e2) * 10**(2*e1) * 10**(3*e2))

    s = s + val
    exp = exp + 1
    #print(val)

print(int(s))
