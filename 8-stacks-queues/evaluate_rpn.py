from functools import reduce


# O(n) time | O(n) space
def evaluate_rpn(rpn_expression):
    sln = []
    DELIMITER = ","
    OPERATORS = {
        "+": lambda acc, cur: acc + cur,
        "-": lambda acc, cur: acc - cur,
        "*": lambda acc, cur: acc * cur,
        "/": lambda acc, cur: acc / cur,
    }

    for token in RPN_expression.split(DELIMITER):
        if token in OPERATORS:
            sln = [reduce(OPERATORS[token], sln)]
        else:
            sln.append(int(token))

    return sln[-1]


if __name__ == "__main__":
    rpn_expression = "3,4,5,+,2,*,1,+"
    sln = evaluate_rpn(rpn_expression)
    print(sln)
