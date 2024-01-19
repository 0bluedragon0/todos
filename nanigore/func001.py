def sample():
    return 10

# 나이를 입력받아 성년/미성년을 판단
def is_major(nai:int) -> bool:
    return nai >= 18

def is_palace(nai:int):
    if nai>=25 and nai<=64:
        pay_palace = 3000
        return pay_palace
    else:
        pay_palace = 0
        return pay_palace
    
def is_discount(inwon:int):
    pay_in = 3000
    discount_in = 2400
    if inwon >= 10:
        pay_fee = discount_in*inwon
        return pay_fee
    pay_fee = pay_in * inwon
    return pay_fee