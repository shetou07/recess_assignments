# FILE HANDLING
filename = "afternoon.txt"
f = open(filename,"wt")
# We are going to write on the file
f.write("Now our file has some data or information")

# We then close our file
f.close()



# Exception Handling
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
