def print_multiplication_table(start=1, end=9):
    """주어진 범위의 구구단을 출력하는 함수"""
    for i in range(start, end + 1):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")
        print("-" * 15)  # 단 구분선


# 실행
if __name__ == "__main__":
    print("구구단 출력 (1단부터 9단까지):")
    print_multiplication_table()
