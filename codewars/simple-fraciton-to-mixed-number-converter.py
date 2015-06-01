

from fractions import Fraction

def mixed_fraction(s):
    if s.count('-') > 1:
        s = s.replace('-', '')
    if '-' not in s:
        numer, deno = s.split('/')
        print numer, deno
        if deno == '0':
            raise ZeroDivisionError()

        if numer == '0':
            return '0'

        left, numer = divmod(int(numer), int(deno))
        lala = Fraction(numer, int(deno))
        numer, deno = lala.numerator, lala.denominator
        if numer == 0:
            return '%d' % left
        return '{left} {numer}/{deno}'.format(left=left, numer=numer, deno=deno).lstrip('0  ')

    if '-' in s:
        return '-' + mixed_fraction(s.replace('-', ''))

for t in ['42/9', '6/3', '4/6', '0/188', '-10/7', '-3988791/5992333', '9309376/-4654688', '-5389358/9955676']:
    print mixed_fraction(t)
# print mixed_fraction('42/9')