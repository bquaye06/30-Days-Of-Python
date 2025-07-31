import math
# Introduction
# Day 1 - 30DaysOfPython Challenge

print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool

print(type('Michael Quaye'))
print(type(4+3j))

# FINDONG EUCLIDIAN DISTANCE
p1q1 = (2-10)**2
p2q2 = (3-8)**2
d = math.sqrt(p1q1 + p2q2)
print(d)