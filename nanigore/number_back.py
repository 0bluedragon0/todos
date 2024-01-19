# 데이터 자체는 원래 백이 아니라 database에서 관리
numbers = []

def save(num:int) -> bool:
    if isinstance(num,int) == False:
        return False
    numbers.append(num)
    return True

def find_all()->list:
    return numbers

def delete(num:int)->bool:
    if isinstance(num,int)==False:
        return False
    for item in numbers:
        if item==num:
            list.remove(item)
            return True
    return False