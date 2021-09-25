

i = 0
test_str = "mississippi"
most_frequency = {}
for i in test_str:
    if i in  most_frequency:
         most_frequency[i] += 1
    else:
         most_frequency[i] = 1
  

print ("Count of all characters in GeeksforGeeks is :\n "+  str( most_frequency))
