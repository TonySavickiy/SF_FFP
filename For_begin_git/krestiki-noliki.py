# Создаем пустое поле 4x4
board = [[' ' for _ in range(4)] for _ in range(4)]

# Заполняем первую строку числами от 0 до 3
for i in range(4):
    board[0][i] = str(i)

# Заполняем первый столбец числами от 0 до 3
for i in range(4):
    board[i][0] = str(i)

# Функция для отображения поля
def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 9)

# Функция для проверки выигрышной комбинации
def check_win(player):
    for i in range(1,4):
        if board[i][1] == board[i][2] == board[i][3] == player:
            return True
        if board[1][i] == board[2][i] == board[3][i] == player:
            return True
    if board[1][1] == board[2][2] == board[3][3] == player:
        return True
    if board[1][3] == board[2][2] == board[3][1] == player:
        return True
    return False

# Функция для хода игрока
def make_move(player):
    while True:
        row = int(input('Введите номер строки (1-3): '))
        col = int(input('Введите номер столбца (1-3): '))
        if row < 1 or row > 3 or col < 1 or col > 3 or board[row][col] != ' ':
            print('Некорректный ход. Попробуйте еще раз.')
        else:
            board[row][col] = player
            break

# Основной игровой цикл
def play_game():
    print('Добро пожаловать в игру "КРЕСТИКИ-НОЛИКИ, для теста SF. В игре 2 игрока: Игрок(X) и Игрок(O) \n Да будет битва!')
    current_player = 'X'
    while True:
        display_board()
        print(f'Ходит игрок {current_player}')
        make_move(current_player)
        if check_win(current_player):
            display_board()
            print(f'Игрок {current_player} выиграл!')
            break
        if all(board[i][j] != ' ' for i in range(1,4) for j in range(1,4)):
            display_board()
            print('Ничья!')
            break
        current_player = 'O' if current_player == 'X' else 'X'

# Запуск игры
play_game()