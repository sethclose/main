while True:
    try:
        n = int(raw_input("Please enter an integer of at least 1: "))
        if n <= 0:
          print "Must be at least 1"
        else:
          break
    except ValueError  as (strerror):
        print "No valid integer! Please try again ... {}" .format (strerror)
        
print "Fizz buzz counting up to n"

for i in range(n):
  result = ""
  j = i + 1
  if j % 3 == 0 and j % 5 == 0:
    print "fizz buzz",
  elif j % 3 == 0:
    print "fizz",
  elif j % 5 == 0:
    print "buzz",
  else:
    print str(j),
  if j != n:
    print ",", 