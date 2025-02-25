# 사칙연산 함수
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b


# 연산자 매핑
def calculate(a, b, operator):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }
    if operator not in operations:
        raise ValueError(f"잘못된 연산자입니다. 지원되는 연산자: {', '.join(operations.keys())}")

    operation = operations[operator]
    return operation(a, b)


# 입력 및 실행
if __name__ == "__main__":
    try:
        a = float(input("첫 번째 숫자를 입력하세요: "))
        b = float(input("두 번째 숫자를 입력하세요: "))
        operator = input("수행할 연산을 선택하세요 (+, -, *, /): ")
        result = calculate(a, b, operator)
        print(f"결과: {result}")
    except ValueError as e:
        print(f"오류: {e}")
