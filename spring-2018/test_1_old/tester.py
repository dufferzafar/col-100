"""

"""

import random

from subprocess import Popen, PIPE, TimeoutExpired

SOURCE_FILE_NAME = "code.m"

# This ensures that same test cases are generated for everyone
random.seed(9001003)


##############################################################################

# VPL Stuff, don't touch!
def print_comment(s):
    print('Comment :=>> ' + s)


def print_grade(num):
    print('Grade :=>> ' + str(num))

##############################################################################

# TODO: Deal with code involving plots?


# We can add all our source code checks here
with open(SOURCE_FILE_NAME) as f:
    src = f.read()
    if src.count("printf") > 10:
        print_comment("This has >10 printfs")


##############################################################################

def run_code(src, inpt, timeout=0.5):
    """
    Run user's src file with given input.
    """

    cmd = ["octave", "-q", src]
    process = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    try:
        stdout, stderr = process.communicate(
            input=inpt.encode(),
            timeout=timeout
        )
        stdout = stdout.decode().strip()
        stderr = stderr.decode().strip()
    except TimeoutExpired:
        print("Program timed out")

    return stdout, stderr

##############################################################################


if __name__ == '__main__':

    inp = "Shadab\nZafar"
    stdout, stderr = run_code(SOURCE_FILE_NAME, inp)
    print("STDOUT:", repr(stdout))
    print("STDERR:", repr(stderr))
