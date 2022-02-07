rz = IntegerRing()

p = rz(0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab)
k = GF(0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab, 'I')
q = p ^ 2
Z = -(2+I)
A = 240*I
B = 1012*(1+I)

if q % 4 == 3 or q % 8 == 5:
    raise RuntimeError("Use an optimized routine")
    
qP = rz(q - 1)
c1 = 0
while qP % 2 == 0:
    c1+= 1
    qP /= 2
print('c1 =', c1)

c2 = (q - 1) / (2^c1)        # Integer arithmetic
print('c2 =', c2)

c3 = (c2 - 1) / 2            # Integer arithmetic
print('c3 =', c3)

c4 = 2^c1 - 1                # Integer arithmetic
print('c4 =', c4)

c5 = 2^(c1 - 1)              # Integer arithmetic
print('c5 =', c5)

c6 = Z^rz(c2)
print('c6 =', c6)

c7 = Z^rz((c2 + 1) / 2)
print('c7 =', c7)
