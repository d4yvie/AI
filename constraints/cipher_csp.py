from constraint import *


class Cryptarithmetic:

    def two_plus_two_is_four(self):
        """
            TWO
        +   TWO
            FOUR
        :return: the parameters for the solution
        """
        problem = Problem()
        problem.addVariables(["T", "W", "O", "F", "U", "R"], [x for x in range(10)])
        problem.addConstraint(AllDifferentConstraint())
        problem.addConstraint(
            lambda t, w, o, f, u, r: (t * 100 + w * 10 + o) * 2 == f * 1000 + o * 100 + u * 10 + r,
            ["T", "W", "O", "F", "U", "R"])
        return problem.getSolutions()

    def aal_plus_aal_is_fang(self):
        """
            AAL
        +   AAL
            FANG
        :return: the parameters for the solution
        """
        problem = Problem()
        problem.addVariables(["T", "W", "O", "F", "U", "R"], [x for x in range(10)])
        problem.addConstraint(AllDifferentConstraint())
        problem.addConstraint(
            lambda t, w, o, f, u, r: (t * 100 + w * 10 + o) * 2 == f * 1000 + o * 100 + u * 10 + r,
            ["T", "W", "O", "F", "U", "R"])
        return problem.getSolutions()


if __name__ == "__main__":
    c = Cryptarithmetic()
    print(c.two_plus_two_is_four())
