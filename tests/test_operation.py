from src.math_operation import add,subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, -2) == -3
    assert add(0, 0) == 0
    
    print("All tests passed!")

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 2) == -3
    assert subtract(0, -5) == 5
    assert subtract(2, -1) ==1
    assert subtract(0,0)==0
    
    print("All tests passed!")
