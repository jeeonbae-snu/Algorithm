# [level 2] 전화번호 목록 (프로그래머스 42577)

def solution(phone_book):
    # 해시 테이블 생성
    phone_dict = {}

    # 모든 전화번호를 해시 테이블에 저장
    for number in phone_book:
        phone_dict[number] = True

    # 각 전화번호의 접두어가 해시 테이블에 있는지 확인
    for number in phone_book:
        prefix = ""
        for digit in number[:-1]:  # 마지막까지는 볼 필요 없음
            prefix += digit
            if prefix in phone_dict:  # 접두어가 해시 테이블에 있다면
                return False

    return True
