def remove_target(s: str, target: str) -> str:
    stack = []
    t_len = len(target)

    for c in s:
        stack.append(c)
        # 스택 끝부분이 target과 일치하는지 확인
        if len(stack) >= t_len and ''.join(stack[-t_len:]) == target:
            # 일치하면 해당 부분 삭제
            del stack[-t_len:]

    result = ''.join(stack)
    return result if result else "FRULA"

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    s = input().rstrip()
    target = input().rstrip()
    print(remove_target(s, target))
