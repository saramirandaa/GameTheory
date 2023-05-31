from sympy import *
import time


# Agente que calcule equilibrio por estrategia mixta para Cubilete
class Matrix:
    def __init__(self, p="p", q="q", cols=2, rows=2):
        self.matrix = []
        self.cols = cols
        self.rows = rows
        self.p = p
        self.q = q
        self.P1function = ""
        self.P2function = ""

        for row in range(rows):
            self.matrix.append([])
            for col in range(cols):
                self.matrix[row].append(dict())

    def calculate_polynomial(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if row == 0 and col == 0:
                    self.P1function += str(self.matrix[row][col]["PAYOFFS"][0]) + " * " + str(self.p) + " * " + str(
                        self.q)
                    self.P2function += str(self.matrix[row][col]["PAYOFFS"][1]) + " * " + str(self.p) + " * " + str(
                        self.q)
                elif row == 0 and col == 1:
                    self.P1function += " + " + str(self.matrix[row][col]["PAYOFFS"][0]) + " * " + str(
                        self.p) + " * (1 - " + str(self.q) + ")"
                    self.P2function += " + " + str(self.matrix[row][col]["PAYOFFS"][1]) + " * " + str(
                        self.p) + " * (1 - " + str(self.q) + ")"
                elif row == 1 and col == 0:
                    self.P1function += " + " + str(self.matrix[row][col]["PAYOFFS"][0]) + " * (1 - " + str(
                        self.p) + ") * " + str(self.q)
                    self.P2function += " + " + str(self.matrix[row][col]["PAYOFFS"][1]) + " * (1 - " + str(
                        self.p) + ") * " + str(self.q)
                elif row == 1 and col == 1:
                    self.P1function += " + " + str(self.matrix[row][col]["PAYOFFS"][0]) + " * (1 - " + str(
                        self.p) + ") * (1 - " + str(self.q) + ")"
                    self.P2function += " + " + str(self.matrix[row][col]["PAYOFFS"][1]) + " * (1 - " + str(
                        self.p) + ") * (1 - " + str(self.q) + ")"
        print("\nPAYOFFS POLYNOMIALS")
        print("P1: ", self.P1function)
        print("P2: ", self.P2function)

    def compute(self):
        p, q = symbols('p, q')

        P1 = sympify(self.P1function)
        P2 = sympify(self.P2function)
        P1 = P1.expand()
        P2 = P2.expand()
        P1 = P1.subs({p: self.p, q: self.q})
        P2 = P2.subs({p: self.p, q: self.q})
        print("\nSIMPLIFIED POLYNOMIALS")
        print("P1: ", P1)
        print("P2: ", P2)
        print("\nFactored polynomials")
        P1 = factor(P1, p)
        P2 = factor(P2, q)
        print("P1: ", P1)
        print("P2: ", P2)

        P1 = str(P1)
        P2 = str(P2)

        P1 = P1.replace(" ", "")
        P2 = P2.replace(" ", "")

        upper = P1.find(")")
        P1 = P1.replace(P1[upper + 1:], "")

        lower = P2.find("(")
        P2 = P2.replace(P2[:lower], "")

        print("\nExtracted polynomials")
        print("P1: ", P1)
        print("P2: ", P2)

        lower = P1.find("(")
        P1 = P1.replace(P1[:lower + 1], "")
        upper = P1.find(")")
        P1 = P1.replace(P1[upper:], "")

        lower = P2.find("(")
        P2 = P2.replace(P2[:lower + 1], "")
        upper = P2.find(")")
        P2 = P2.replace(P2[upper:], "")

        print("\nParenthesis sub-polynomials")
        print("P1: ", P1)
        print("P2: ", P2)

        P1 = sympify(P1)
        P2 = sympify(P2)

        P1 = P1.subs({p: self.p, q: self.q})
        P2 = P2.subs({p: self.p, q: self.q})

        print("\nProbability results")
        print("P: ", solve(P2, p))
        print("Q: ", solve(P1, q))

        print("\nNash Equilibrium for mixed strategies is: ", end=" ")
        print(f"{solve(P2, p)[0]} A + {1 - solve(P2, p)[0]} B, "
              f"{solve(P1, q)[0]} X + {1 - solve(P1, q)[0]} Y")

    def view(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.matrix[row][col], end=" ")
            print()


print("MIXED STRATEGIES NASH EQUILIBRIUM")
NASH = Matrix()
player1 = ["A", "B"]
player2 = ["X", "Y"]

for row in range(NASH.rows):
    for col in range(NASH.cols):
        print("Please enter payoffs values for strategy", player1[row], player2[col], ": ")
        strategy = player1[row] + player2[col]
        NASH.matrix[row][col].update({"STRATEGIES": strategy})
        value1 = int(input("Player 1: "))
        value2 = int(input("Player 2: "))
        NASH.matrix[row][col].update({"PAYOFFS": [value1, value2]})

NASH.view()
NASH.calculate_polynomial()
NASH.compute()

