import cmath

def roots(a, b, c, d):
    Q=(a**2 - 3*b)/9
    R=(2*a**3 - 9*a*b +27*c)/54
    S=Q**3 - R**2
    if S>0:
        phi=(1/3)*cmath.acos(R/cmath.sqrt(Q**3)) 
        x1 = (-2 * cmath.sqrt(Q) * cmath.cos(phi)) - a/3
        x2 = (-2 * cmath.sqrt(Q) * cmath.cos(phi + (2*cmath.pi)/3)) - a/3
        x3 = (-2 * cmath.sqrt(Q) * cmath.cos(phi - (2*cmath.pi)/3)) - a/3
    elif S<0:
        phi = (1/3) * cmath.acosh(abs(R)/cmath.sqrt(Q**3))
        x1=-2 * cmath.sgn
print(roots(1, -6, -6, 1))