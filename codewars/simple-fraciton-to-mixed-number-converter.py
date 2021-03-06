

from fractions import Fraction
import re


def mixed_fraction(s):
    if s.count('-') > 1:
        s = s.replace('-', '')
    pattern = re.compile(r'(-?\d+)/(-?\d+)$')
    result = re.match(pattern, s)
    if not result:
        return 'not valid s'
    numer, deno = int(result.group(1)), int(result.group(2))

    # zero
    if deno == 0:
        raise ZeroDivision("zero devision error happend!")
    if numer == 0:
        return '0'

    # simple
    fractions = Fraction(numer, deno)
    output = ''
    if fractions < 0:
        output += '-'
        fractions *= -1
    numer, deno = fractions.numerator, fractions.denominator
    int_part, new_numer = divmod(numer, deno)

    # print int_part, new_numer, deno, fractions
    fract_part = '{}/{}'.format(new_numer, deno)
    if new_numer == 0:
        return output + str(int_part)
    if int_part == 0:
        return output + fract_part
    return output + str(int_part) + ' ' + fract_part

for t in ['42/9', '6/3', '4/6', '0/188', '-10/7', '-3988791/5992333', '9309376/-4654688', '-5389358/9955676', '0/-1110']:
    print mixed_fraction(t)


# Input: 42/9, expected result: 4 2/3.
# Input: 6/3, expedted result: 2.
# Input: 4/6, expected result: 2/3.
# Input: 0/18891, expected result: 0.
# Input: -10/7, expected result: -1 3/7.
# Inputs 0/0 or 3/0 must raise a zero division error.
