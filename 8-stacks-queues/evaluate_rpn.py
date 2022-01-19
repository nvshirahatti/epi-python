from functools import reduce
from inspect import stack


# O(n) time | O(n) space
def evaluate_rpn(rpn_expression):
    stack = []
    DELIMITER = ","
    OPERATORS = {
        "+": lambda y, x: x + y,
        "-": lambda y, x: x - y,
        "*": lambda y, x: x * y,
        "/": lambda y, x: int(x / y),
    }

    for token in rpn_expression.split(DELIMITER):
        if token in OPERATORS:
            stack.append(OPERATORS[token](stack.pop(), stack.pop()))
        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == "__main__":
    assert evaluate_rpn("3,4,+,2,*,1,+") == 15
    assert evaluate_rpn("4,13,5,/,+") == 6
    assert evaluate_rpn("10,6,9,3,+,-11,*,/,*,17,+,5,+") == 22
    print("All tests passed!")
