import pytest
import random
import string
import session4
import os
import decimal
from decimal import Decimal
import cmath
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
        '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_add_100_times():
    tot_sum = Decimal('0')
    q = Decimal(str(session4.Qualean(1)))
    for _ in range(100):
        tot_sum += q
    assert tot_sum == 100 * q, "q + q + ... 100 times is not equal to 100 * q"

def test_sqrt_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q = session4.Qualean(val)
        assert (q.__sqrt__()) == cmath.sqrt(q), f"sqrt is not working"

def test_decimalsqrt_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q = session4.Qualean(val)
        sqrt_complex_num = q.__sqrt__()
        sqrt_fun = round(Decimal(sqrt_complex_num.real),10)
        if(sqrt_complex_num.real>0):
            decimal_sqrt = round(q.__decimal__().sqrt(),10)
            assert (sqrt_fun) == decimal_sqrt, f"sqrt decimal precision not matching!"

def test_sum_million():
    for _ in range(50):
        q_sum = session4.Qualean(0)
        for _ in range(1000000):
            q1 = session4.Qualean(random.sample([1,0,-1], 1)[0])
            q_sum += q1
            assert math.isclose(round(q_sum, 10), 0, rel_tol=1e-09, abs_tol=1e3), f"sum of 1 million different qs is not very close to zero"

def test_or_short_circuit():
    for _ in range(50):
        value = random.choice([-1,0,1])
        s = session4.Qualean(value)
        s2 = session4.Qualean(value) 
        if bool(s) == True:
            assert (s.__or__(s2)) == True, f"OR is not giving right output"
            assert (s.__or__()) == True, f"OR is not giving desired output"
            assert (s.__and__()) == False, f"Q2 not defined"
        else:
            assert (s.__or__()) == False, f"Q2 not defined"
            assert (s.__and__(s2)) == False, f"AND function not giving desired output"
            assert (s.__and__()) == False, f"AND function not giving desired output"


def test_bool_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        s = session4.Qualean(val)
        assert (s.__bool__()) == bool(s), f"Bool is not giving desired output please re-check"

def test_float_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        s = session4.Qualean(val)
        assert (type(s.__float__())) == float, f"YWrong float conversion"

def test_mul_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        s1 = session4.Qualean(val)
        s2 = session4.Qualean(val)
        assert (s1.__mul__(s2)) == s1*s2, f"Wrong multiplication"

def test_lt_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        s1 = session4.Qualean(val)
        s2 = session4.Qualean(val)
        assert (s1.__lt__(s2)) == (s1<s2), f"Wrong < comparison"

def test_lte_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        s1 = session4.Qualean(val)
        s2 = session4.Qualean(val)
        assert (s1.__le__(s2)) == (s1<=s2), f"Wrong <= comparison"

def test_gt_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        s1 = session4.Qualean(val)
        s2 = session4.Qualean(val)
        assert (s1.__gt__(s2)) == (s1>s2), f"Wrong > comparison"

def test_gte_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        s1 = session4.Qualean(val)
        s2 = session4.Qualean(val)
        assert (s1.__ge__(s2)) == (s1>=s2), f"Wrong >= comparison"

def test_eq_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        s1 = session4.Qualean(val)
        s2 = session4.Qualean(val)
        assert (s1.__eq__(s2)) == (s1==s2), f"Wrong == comparison"

