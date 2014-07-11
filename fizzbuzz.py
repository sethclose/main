
# Get a valid number to count to
while True:
    try:
        n = int(raw_input("Please enter an integer of at least 1: "))
        if n <= 0:
          print "Must be at least 1"
        else:
          break
    except ValueError  as (strerror):
        print "No valid integer! Please try again ... {}" .format (strerror)

# Print numbers or substitutes
print "Fizz buzz counting up to n"
result = ""
for i in range(n):
  j = i + 1
  if j % 3 == 0 and j % 5 == 0:
    result += "fizz buzz"
  elif j % 3 == 0:
    result += "fizz"
  elif j % 5 == 0:
    result += "buzz"
  else:
    result += str(j)
  if j != n:
    result += ", "
print result