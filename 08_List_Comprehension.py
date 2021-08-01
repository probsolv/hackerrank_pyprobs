# inputs. Try different values.
x = 1
y = 1
z = 2
n = 3

# Alternative 1: your code with list comprehension

l = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k]) != n]
print(l)

# Alternative 2: your code with loops

resultslist = []
for i in range(0,x+1):
  for j in range(0,y+1):
    for k in range(0,z+1):
      if i+j+k != n:
        resultslist.append([i,j,k])

print(resultslist)
