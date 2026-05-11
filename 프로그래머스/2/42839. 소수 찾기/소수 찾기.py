from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    unique_numbers = set()
    
    # 모든 순열을 만들어서 숫자로 변환
    for n in range(1, len(numbers) + 1):
        for number in permutations(numbers, n):
            num = int(''.join(number))  # 리스트를 문자열로 합친 후 정수로 변환
            unique_numbers.add(num)     # 중복된 숫자를 제거하기 위해 set 사용

    # 소수 판정
    count = 0
    for num in unique_numbers:
        if is_prime(num):
            count += 1
    
    return count
