from constraint import *


class Cryptarithmetic:

    def two_plus_two_is_four(self):
        """
             TWO
        +    TWO
            FOUR
        possible solution: {'F': 1, 'O': 4, 'R': 8, 'T': 7, 'U': 6, 'W': 3}
        :return: the parameters for the solution
        """
        problem = Problem()
        variables = ["T", "W", "O", "F", "U", "R"]
        problem.addVariables(variables, [x for x in range(10)])
        problem.addConstraint(AllDifferentConstraint())
        problem.addConstraint(
            lambda t, w, o, f, u, r: (t * 100 + w * 10 + o) * 2 == f * 1000 + o * 100 + u * 10 + r,
            variables)
        return problem.getSolutions()

    def aal_plus_aal_is_fang(self):
        """
             AAL
        +    AAL
            FANG
        possible solution: {'A': 9, 'F': 1, 'G': 4, 'L': 2, 'N': 8}
        :return: the parameters for the solution
        """
        problem = Problem()
        variables = ["A", "L", "F", "N", "G"]
        problem.addVariables(variables, [x for x in range(10)])
        problem.addConstraint(AllDifferentConstraint())
        problem.addConstraint(
            lambda a, l, f, n, g: (a * 100 + a * 10 + l) * 2 == f * 1000 + a * 100 + n * 10 + g,
            variables)
        return problem.getSolutions()

    def send_plus_more_is_money(self):
        """
             SEND
        +    MORE
            MONEY
        possible solution: {'D': 9, 'E': 8, 'M': 0, 'N': 1, 'O': 3, 'R': 6, 'S': 2, 'Y': 7}
        :return: the parameters for the solution
        """
        problem = Problem()
        variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
        problem.addVariables(variables, [x for x in range(10)])
        problem.addConstraint(AllDifferentConstraint())
        problem.addConstraint(
            lambda s, e, n, d, m, o, r, y: (s * 1000 + e * 100 + n * 10 + d) + (
                    m * 1000 + o * 100 + r * 10 + e) == m * 10000 + o * 1000 + n * 100 + e * 10 + y,
            variables)
        return problem.getSolutions()


if __name__ == "__main__":
    c = Cryptarithmetic()
    print(c.two_plus_two_is_four())
    print(c.aal_plus_aal_is_fang())
    print(c.send_plus_more_is_money())

