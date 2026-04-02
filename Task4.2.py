# global variables
x = 300

print("Find the closest number to", x)

# get input from user
a = int(input(
"Enter your first number: "))
b = int(input(
"Enter your second number: "))
c = int(input(
"Enter your third number: "))

# calculate absolute distances
da = abs(x - a)
db = abs(x - b)
dc = abs(x - c)

# find the smallest distance
smallest = min(da, db, dc)

# check results
if da == db == dc:
    print(
"All numbers are equally closest to", x
)
else:
    if da == smallest:
        print("A", a,
"is the closest to", x)
    if db == smallest:
        print("B", b,
"is the closest to", x)
    if dc == smallest:
        print("C", c,
"is the closest to", x)
