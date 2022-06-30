
''' operations on numbers '''
# casting
toFloat = float(x)
toInt = int(y)
toComplex = complex(x)

print(toFloat, toInt, toComplex)

# different presentition of numbers
print(1000000, 1_000_000, 1e-5)
print(200000000000000000.0)

# arthmetic operations
print(2+4.0)
print(1--3, 1 - -3, 2-(-4))
print(5 // 3)
# print(4.6 / 0)
print(-5 % 3)  # r = x - (y * (x // y))

# maths functions
print(round(2.5), round(3.5))  # rounding ties to even
print(abs(-5.4))
# with 3 arguments (power(x, y, z) => (x ** y) % z)
print(pow(4, 3), pow(2, 3, 2))

# displaying formatted numbers
print(f"this is {3.23}")
print(f"this is {3.4253:.2f}")
print(f"The value of n is {1000000:,}")
print(f"percentage of 0.433 is {0.433:.2%}")
