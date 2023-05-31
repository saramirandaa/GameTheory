import time


class Matrix:
    def __init__(self, cols, rows):
        self.matrix = []
        self.cols = cols
        self.rows = rows

        for row in range(rows):
            self.matrix.append([])
            for col in range(cols):
                self.matrix[row].append(dict())

    def search_greater1(self):
        strategies = []
        for row in range(self.rows):
            for col in range(self.cols):
                if row == self.rows - 1:
                    break

                if self.matrix[row][col]["PAYOFFS"][0] > self.matrix[row + 1][col]["PAYOFFS"][0]:
                    strategies.append(self.matrix[row][col]["STRATEGIES"])
                elif self.matrix[row][col]["PAYOFFS"][0] == self.matrix[row + 1][col]["PAYOFFS"][0]:
                    strategies.append(self.matrix[row][col]["STRATEGIES"])
                    strategies.append(self.matrix[row + 1][col]["STRATEGIES"])
                else:
                    strategies.append(self.matrix[row + 1][col]["STRATEGIES"])
        print("Player 1 choosed: ", strategies)
        return strategies

    def search_greater2(self):
        strategies = []
        for row in range(self.rows):
            for col in range(self.cols):
                if col == self.cols - 1:
                    break
                if self.matrix[row][col]["PAYOFFS"][1] > self.matrix[row][col + 1]["PAYOFFS"][1]:
                    strategies.append(self.matrix[row][col]["STRATEGIES"])
                elif self.matrix[row][col]["PAYOFFS"][1] == self.matrix[row][col + 1]["PAYOFFS"][1]:
                    strategies.append(self.matrix[row][col]["STRATEGIES"])
                    strategies.append(self.matrix[row][col + 1]["STRATEGIES"])
                else:
                    strategies.append(self.matrix[row][col + 1]["STRATEGIES"])
        print("Player 2 choosed: ", strategies)
        return strategies

    def compare_cells(self, cells1, cells2):
        flag = False
        strategy = ""
        for cell in cells1:
            if cell in cells2:
                print("Nash equilibrium is: ", cell, end=" ")
                flag = True
                strategy = cell
                for row in range(self.rows):
                    for col in range(self.cols):
                        if self.matrix[row][col]["STRATEGIES"] == strategy:
                            print("with payoffs: ", end=" ")
                            print(self.matrix[row][col]["PAYOFFS"])
        if not flag:
            print("No Nash equilibrium found")



    def view(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.matrix[row][col], end=" ")
            print()


print("PURE STRATEGIES NASH EQUILIBRIUM")
strategies = int(input("Please enter the number of strategies for players: "))
NASH = Matrix(strategies, strategies)
player1 = ["A", "B", "C", "D", "E"]
player2 = ["X", "Y", "Z", "V", "W"]

for row in range(NASH.rows):
    for col in range(NASH.cols):
        print("Please enter payoffs values for strategy", player1[row], player2[col], ": ")
        strategy = player1[row] + player2[col]
        NASH.matrix[row][col].update({"STRATEGIES": strategy})
        value1 = int(input("Player 1: "))
        value2 = int(input("Player 2: "))
        NASH.matrix[row][col].update({"PAYOFFS": [value1, value2]})

NASH.view()

NASH_J1 = NASH.search_greater1()
NASH_J2 = NASH.search_greater2()

NASH.compare_cells(NASH_J1, NASH_J2)
time.sleep(3000)
