TEST_CASE_FORMAT = """
case = Test %d
input = %s
output = "%s"
"""


def to_postfix(infix):

    # TODO: What to do about precedence?
    precedence = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    opStack = list()

    postfix = []

    for token in infix:

        if (token.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or
                token in "0123456789"):

            postfix.append(token)

        elif token == '(':
            opStack.append(token)

        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfix.append(topToken)
                topToken = opStack.pop()

        else:
            while (opStack) and \
                    (precedence[opStack[-1]] >= precedence[token]):
                postfix.append(opStack.pop())

            opStack.append(token)

    while opStack:
        postfix.append(opStack.pop())

    return "".join(postfix)


if __name__ == '__main__':

    INPUTS = [
        "4+3*5",
        "(4+3)*5",
        "4+3^5",
        "4^3*5",
        "A+B*C",
        "(A+B)*C",
        "A*B+C*D",
        "(A+B)*(C+D)",
        "A/B^C+D*E-A*C",
        "(A+B)*C-(D-E)*(F+G)",
        "(B^2-4*A*C)^(1/2)",
        "A*(B+C-D/E)/F"
    ]

    for i, inp in enumerate(INPUTS):

        out = to_postfix(inp)

        print(TEST_CASE_FORMAT % (i + 1, inp, out))


# print(to_postfix("A * B + C * D"))
# print(to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
# print(to_postfix("( A + B ) * ( C + D )"))
# print(to_postfix("( A + B ) * C"))
# print(to_postfix("A + B * C"))
