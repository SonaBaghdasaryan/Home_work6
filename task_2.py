# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть
# ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
# число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from random import randint as rndit

def check_queens(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i][0] == arr[j][0] or arr[i][1] == arr[j][1] or abs(arr[i][0] - arr[j][0]) == abs(
                    arr[i][1] - arr[j][1]):
                return False

    return True


def generate_board():
    board = []
    for i in range(8):
        row = rndit(1, 8)
        board.append((i + 1, row))
    return board

if __name__ == '__main__':
    successful_boards = []

    while len(successful_boards) < 4:
        board = generate_board()
        if check_queens(board):
            successful_boards.append(board)

    for board in successful_boards:
        print(board)