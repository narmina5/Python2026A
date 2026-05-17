"""
1. virtual environment yaradin (venv adli)
2. onu aktiv edin
3. deaktiv edin
4. yeniden aktiv edin
5. iki paket yukleyin: numpy ve requests
6. pip list ile paketleri listele
7. pip freeze istifade ederek requirements.txt yarat
8. venv-i deaktiv et ve 2ci venv yarat (venv2 adli)
9. paketleri listele (pip list) - venv-le eyni olmadigini goruruk
10. hemin venv2-ye requirements.txt-deki paketleri yukle - pip install -r requirements.txt
11. Paketlerin dogru yuklendiyini yoxlayin
12. Yeni versiyalari olan paketleri gormek ucun pip list --outdated
13. numpy-in versiyasini gosterin
"""

"""
cowsay kitabxanasi yukleyin
cowsay.cow() funksiyasini icherisine 1 ədəd string (uzunluq fərq etmir) argumenti vererek ishledin
"""
import cowsay
cowsay.cow("Möööö!!!")


import random
import os
import time


def initialize_board(size, num_mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mines = random.sample(range(size * size), num_mines)  # Randomly place mines

    for mine in mines:
        row, col = divmod(mine, size)
        board[row][col] = 'X'

    # Generate numbers for safe cells
    for row in range(size):
        for col in range(size):
            if board[row][col] == 'X':
                continue
            board[row][col] = str(count_surrounding_mines(board, row, col, size))

    return board


def count_surrounding_mines(board, row, col, size):
    mine_count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < size and 0 <= nc < size and board[nr][nc] == 'X':
            mine_count += 1
    return mine_count


def display_board(board, size, revealed):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen (Windows/Linux/Mac)

    for row in range(size):
        row_display = ""
        for col in range(size):
            if revealed[row][col]:
                row_display += f"{board[row][col]} "
            else:
                row_display += "_ "
        print(row_display)
    print("\n")


def play_game(size=5, num_mines=5):
    board = initialize_board(size, num_mines)
    revealed = [[False for _ in range(size)] for _ in range(size)]

    while True:
        display_board(board, size, revealed)
        print("Enter row and column to reveal (e.g., '2 3'):")

        try:
            row, col = map(int, input().split())
            if not (0 <= row < size and 0 <= col < size):
                print("Invalid input. Try again.")
                continue
        except ValueError:
            print("Please enter two numbers.")
            continue

        if board[row][col] == 'X':
            display_board(board, size, revealed)
            print("Game Over! You hit a mine!")
            break

        revealed[row][col] = True

        # Check if the player has won
        if all(revealed[row][col] or board[row][col] == 'X' for row in range(size) for col in range(size)):
            display_board(board, size, revealed)
            print("Congratulations, you won!")
            break

        time.sleep(0.5)  # Pause briefly for better visual experience


if __name__ == "__main__":
    play_game()