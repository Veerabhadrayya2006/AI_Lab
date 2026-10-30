
import random

def heuristic(board):
    n = len(board)
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (board[i] == board[j] or
                abs(board[i] - board[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


def print_board(board):
    n = len(board)
    for row in range(n):
        print(" ".join(
            "Q" if board[col] == row else "."
            for col in range(n)
        ))


def hill_climbing(n):
    board = [random.randint(0, n - 1) for _ in range(n)]
    iteration = 0

    while True:
        current_h = heuristic(board)

        print(f"\nIteration {iteration}")
        print("Board:", board)
        print("Heuristic:", current_h)
        print_board(board)

        if current_h == 0:
            print("\nSolution found!")
            return board

        best_board = board[:]
        best_h = current_h

        # Try moving each queen to every other row
        for col in range(n):
            for row in range(n):
                if row != board[col]:
                    neighbor = board[:]
                    neighbor[col] = row
                    h = heuristic(neighbor)

                    if h < best_h:
                        best_h = h
                        best_board = neighbor

        # Stop if no better move exists
        if best_h >= current_h:
            print("\nLocal optimum reached. Restarting...")
            board = [
                random.randint(0, n - 1)
                for _ in range(n)
            ]
            iteration += 1
            continue

        print("Next heuristic:", best_h)
        board = best_board
        iteration += 1


n = int(input("Enter number of queens: "))
solution = hill_climbing(n)

print("\nFinal Solution:")
print_board(solution)
