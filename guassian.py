from math import pi, sqrt, exp
m = 0
s = 2
x = 1

oneBySqrt_TwoPi_S = 1/(sqrt(2 * pi )*s)


xMinus_M_By_S_powerTwo = (( x - m )/ s)**2


f_of_x= oneBySqrt_TwoPi_S * exp(-0.5* xMinus_M_By_S_powerTwo)

print("f(x) = %f " %f_of_x)

