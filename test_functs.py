import divisor_master

def test_f_1():
    assert divisor_master.is_prime(7)
    assert not divisor_master.is_prime(6)

def test_f_2():
    assert divisor_master.all_divs(7) == [1,7]
    assert divisor_master.all_divs(8) == [1,2,4,8]

def test_f_3():
    assert divisor_master.big_prive_div(7) == 7