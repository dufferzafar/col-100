from expression import *
from infix import to_postfix

TEST_CASE_FORMAT = """
case = Test %d
input = %s
output = "%s"
"""


INPUTS = [
    "4+3*5",
    "A+B",
    "(A+B)*(Z+1)",
    "(4+3)*5",
    "4+3^5",
    "4^3*5",
    "A+B*C",
    "1",
    "Z",
    "A+Z",
    "(A+B)*C",
    "A*B+C*D",
    "(A+B)*(C+D)",
    "1+5*2+D-2",
    "(A+B)*C-(D-E)*(F+G)",
    "3-C+D-4",
    "0*1",
    "1*0",
    "0*0+0-0/1",
    # "1/0",
    # "A/B^C+D*E-A*C",
    # "(B^2-4*A*C)^(1/2)",
    # "A*(B+C-D/E)/F"
]

if __name__ == '__main__':

    for i, inf in enumerate(INPUTS):

        pre = infix_to_prefix(inf)
        post1 = infix_to_postfix(inf)
        post2 = to_postfix(inf)

        assert post1 == post2

        val1 = evaluate_prefix(pre)
        val2 = evaluate_postfix(post1)

        # print(type(val1))

        assert val1 == val2

        if val1 // 1 == val1:
            val1 = int(val1)

        inp = pre
        out = post1 + "\n" + str(val1)

        print(TEST_CASE_FORMAT % (i + 1, inp, out))
