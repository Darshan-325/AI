def solve_n_queens_single(n):
    board = [-1] * n
    solution = []

    def backtrack(row, cols, diag1, diag2):
        if row == n:
            solution.append(board[:])
            return True  # stop after finding the first solution
        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue
            board[row] = col
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)
            if backtrack(row + 1, cols, diag1, diag2):
                return True
            # Backtrack
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)
        return False

    backtrack(0, set(), set(), set())
    return solution[0] if solution else None

# Example usage
n = 4
sol = solve_n_queens_single(n)
if sol:
    for i in sol:
        print(". " * i + "Q " + ". " * (n - i - 1))
else:
    print("No solution found.")

