from func001 import sample, is_major, is_palace, is_discount

# 테스트하는 함수를 작성
# 테스트 하는 함수는 pytest로 실행이 가능

# def test_sample1():
#     assert sample() == 10
# 
# def sample():
#     assert round(2.5) == 3

# def test_is_major():
#     assert is_major(20) is True
#     assert is_major(18) is True
#     assert is_major(15) is False

# 나이를 입력받아 입장료를 리턴하는 함수
# 25 ~ 64세면 3000원, 기타는 무료
    
def test_is_palace():
    assert is_palace(30) == 3000
    assert is_palace(65) == 0
    assert is_palace(35) == 3000
    assert is_palace(15) == 0

# 입장료는 3000원이다. 10명이면 1인당 2400원이다.
# 인원수를 입력받아 요금을 출력
def test_is_discount():
    assert is_discount(10) == 24000
    assert is_discount(9) == 27000
