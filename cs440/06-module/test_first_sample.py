def test_upper():
    assert 'cityu'.upper() == 'CITYU'
    assert 'computer science'.upper() == 'COMPUTER SCIENCE'

def test_isupper():
    assert 'CITYU'.isupper()
    assert 'CS'.isupper()

def test_number_equal():
    assert 1.0 == 1
