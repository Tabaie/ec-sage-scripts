from sage.all import *
import argparse, sys

parser = argparse.ArgumentParser('Compute stuff for hash to curve')
parser.add_argument('--stop_at', type=str, default='not-provided')
parser.add_argument('--c6', type=str, default='not-provided')
parser.add_argument('--test', nargs='+', default=[])
parser.add_argument('--nosageexp', default='not-provided')

args = parser.parse_args()

rz = IntegerRing()

p = rz(0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab)
k = GF(0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab, 'I')
q = p ** 2
Z = -(2+I)
A = 240*I
B = 1012*(1+I)

if q % 4 == 3 or q % 8 == 5:
    raise RuntimeError("Use an optimized routine")
    
#why is this necessary?
#seems like sagemath does a poor job with large powers of field extension elements
def exp_nosage(base, pw):
    
    res = k(1)
    baseP2i = k(1)
    p = pw

    while p != 0:
        if p % 2 == 1:
            res *= baseP2i
        baseP2i *= 2
    
    return res

def exp(base, pw):
    if args.nosageexp == 'not-provided':
        return base ** pw
    return exp_nosage(base,pw)

def check_stop_flag(c):
    if args.stop_at == c:
        sys.exit(0)

if len(args.test) > 0:
    print('Test flag provided. Only performing test.')

    for test in args.test:
        if test != 'exp':
            raise RuntimeError('unknown test ' + test)

        inp = [rz(2), rz(583)]
        for e in inp:
            correct = Z ** e
            observed = exp_nosage(Z, e)
            if observed != correct:
                raise RuntimeError('Test failed')
        print('Tests successful')
        os.exit(0)
        


qP = rz(q - 1)
c1 = 0
while qP % 2 == 0:
    c1+= 1
    qP /= 2
print('c1 =', c1)

c2 = (q - 1) / (2**c1)        # Integer arithmetic
print('c2 =', c2)

c3 = (c2 - 1) / 2        # Integer arithmetic
print('c3 =', c3)

c4 = 2**c1 - 1                # Integer arithmetic
print('c4 =', c4)

c5 = 2**(c1 - 1)              # Integer arithmetic
print('c5 =', c5)

check_stop_flag('c6')
if args.c6 == 'not-provided':
    #c6 = Z**rz(c2)
    c6 = exp(Z, rz(c2))
else:
    c6 = rz(args.c6)
print('c6 =', c6)

check_stop_flag('c7')
c7 = exp(Z,rz((c2 + 1) / 2))
print('c7 =', c7)
