# 사칙연산 클래스
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        return a / b


# 상수로 연산 매핑 정의
OPERATIONS = {
    '+': MathOperations.add,
    '-': MathOperations.subtract,
    '*': MathOperations.multiply,
    '/': MathOperations.divide,
}


# 유효한 연산자인지 확인하는 함수
def validate_operator(operator):
    if operator not in OPERATIONS:
        raise ValueError(f"잘못된 연산자입니다. 지원되는 연산자: {', '.join(OPERATIONS.keys())}")


# 계산 함수
def calculate(a, b, operator):
    validate_operator(operator)
    operation = OPERATIONS[operator]
    return operation(a, b)


# 입력 및 실행
if __name__ == "__main__":
    try:
        first_number = float(input("첫 번째 숫자를 입력하세요: "))
        second_number = float(input("두 번째 숫자를 입력하세요: "))
        operator = input("수행할 연산을 선택하세요 (+, -, *, /): ")
        result = calculate(first_number, second_number, operator)
        print(f"결과: {result}")
    except ValueError as e:
        print(f"오류: {e}")
