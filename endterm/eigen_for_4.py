import cmath

def roots(a, b, c, d, e):
    A = -(3*b**2)/(8*a**2) + c/a
    B = (b**3)/(8*a**3) - (b*c)/(2*a**2) + d/a
    C = -(3*b**4)/(256*a**4) + (c*b**2)/(16*a**3) - (b*d)/(4*a**2) + e/a

    if B == 0:
        x1 = -b/(4*a) + cmath.sqrt(((-A) + cmath.sqrt(A**2 - 4*C)) / 2)
        x2 = -b/(4*a) + cmath.sqrt(((-A) - cmath.sqrt(A**2 - 4*C)) / 2)
        x3 = -b/(4*a) - cmath.sqrt(((-A) + cmath.sqrt(A**2 - 4*C)) / 2)
        x4 = -b/(4*a) - cmath.sqrt(((-A) - cmath.sqrt(A**2 - 4*C)) / 2)
    else:
        P = -(A**2)/12 - C
        Q = -(A**3)/108 + (A*C)/3 - (B**2)/8
        R = -Q/2 + cmath.sqrt((Q**2)/4 + (P**3)/27)

        U = R**(1/3)
        if U == 0:
            y = -5*A/6 - Q**(1/3)
        else:
            y = -5*A/6 + U - P/(3*U)
        
        W = cmath.sqrt(A + 2*y)

        x1 = -b/(4*a) + (W + cmath.sqrt(-(3*A + 2*y + 2*B/W)))/2
        x2 = -b/(4*a) + (W - cmath.sqrt(-(3*A + 2*y + 2*B/W)))/2
        x3 = -b/(4*a) + (-W + cmath.sqrt(-(3*A + 2*y + 2*B/W)))/2
        x4 = -b/(4*a) + (-W - cmath.sqrt(-(3*A + 2*y + 2*B/W)))/2

    return x1, x2, x3, x4

print(roots(1, -6, 11, -6, 1))