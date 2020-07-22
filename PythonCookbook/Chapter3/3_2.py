from decimal import Decimal
a = 4.2
b = 2.1

print(a+b)

print(a+b == 6.3)


a = Decimal('4.2')
b = Decimal('2.1')

print(a+b)

print(a+b == Decimal('6.3'))
print(a+b == 6.3)
