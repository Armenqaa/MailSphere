class ValidInputException(Exception):
    pass


class TicTacToeGame:
    """Classic tic tac toe game"""
    def __init__(self, x_max=3, y_max=3):
        self.x_max = x_max
        self.y_max = y_max
        self.x_coord = 0
        self.y_coord = 0
        self.player1 = 1
        self.player2 = 2
        self.counter = 0
        self.score_board = [0, 0]

    def print_field(self, grid):
        """Print tic tac toe game's field"""
        print_list = [[' '] * self.x_max for _ in range(self.y_max)]
        for i in range(self.x_max):
            for j in range(self.y_max):
                if grid[i][j] == 0:
                    print_list[i][j] = 'O'
                elif grid[i][j] == 1:
                    print_list[i][j] = 'X'

        field = []
        for i in range(self.x_max):
            line = []
            for j in range(self.y_max):
                line.insert(j, print_list[i][j])
            field.append(' | '.join(line))

        print(('\n' + '———' * self.y_max + '\n').join(field))

    def show_board(self):
        """Print player's statistic"""
        print(f"{self.player1}: {self.score_board[0]}")
        print(f"{self.player2}: {self.score_board[1]}")

    def valid_input(self, grid):
        """Correct coordinate input"""
        print('Type x and y separated by a space')
        while 1:
            try:
                coord_str = input()
                if len(coord_str) != 3:
                    raise ValidInputException('Input is too long')
                if coord_str[1] != ' ':
                    raise ValidInputException('Wrong input')
            except ValidInputException as VIE:
                print(VIE)
                continue
            try:
                x_coord = int(coord_str[0])
                y_coord = int(coord_str[2])
            except ValueError:
                print('Not integer')
                continue
            try:
                if x_coord > 3 or x_coord < 1 or y_coord > 3 or y_coord < 1:
                    raise ValidInputException('Input coordinates should be between 1 and 3')
            except ValidInputException as VIE:
                print(VIE)
                continue
            try:
                if grid[x_coord - 1][y_coord - 1] != -1:
                    raise ValidInputException('Occupied field')
            except ValidInputException as VIE:
                print(VIE)
                continue
            break
        self.x_coord = x_coord
        self.y_coord = y_coord

    def start_game(self):
        """Tic tac toe start"""
        print('The game is starting. Please type your names:')
        print('Player one:')
        self.player1 = input()
        print('Player two:')
        self.player2 = input()
        print("Let's go")
        grid = [[-1] * 3 for _ in range(3)]
        while 1:
            self.counter += 1
            self.valid_input(grid)
            if self.counter % 2 == 1:
                print('X placed')
                grid[self.x_coord - 1][self.y_coord - 1] = 1
            else:
                print('O placed')
                grid[self.x_coord - 1][self.y_coord - 1] = 0
            self.print_field(grid)
            if self.check_winner(grid) == 1 or\
                    self.counter == self.x_max * self.y_max:
                if self.end_game() == 0:
                    break
                grid = [[-1] * 3 for _ in range(3)]

    def check_winner(self, grid):
        """Scrolling through the field chooses the winner"""
        for x in range(3):
            if grid[x][1] >= 0 and grid[x][1] == grid[x][0] \
                    and grid[x][1] == grid[x][2]:
                if grid[x][1] == 0:
                    print(f'The winner is {self.player2}')
                    self.score_board[1] += 1
                else:
                    print(f'The winner is {self.player1}')
                    self.score_board[0] += 1
                return 1

        for y in range(3):
            if grid[1][y] >= 0 and grid[1][y] == grid[0][y] \
                    and grid[1][y] == grid[2][y]:
                if grid[1][y] == 0:
                    print(f'The winner is {self.player2}')
                    self.score_board[1] += 1
                else:
                    print(f'The winner is {self.player1}')
                    self.score_board[0] += 1
                return 1

        if grid[1][1] >= 0 and grid[1][1] == grid[2][0]\
                and grid[1][1] == grid[0][2]:
            if grid[1][1] == 0:
                print(f'The winner is {self.player2}')
                self.score_board[1] += 1
            else:
                print(f'The winner is {self.player1}')
                self.score_board[0] += 1
            return 1

        if grid[1][1] >= 0 and grid[1][1] == grid[0][0] \
                and grid[1][1] == grid[2][2]:
            if grid[1][1] == 0:
                print(f'The winner is {self.player2}')
                self.score_board[1] += 1
            else:
                print(f'The winner is {self.player1}')
                self.score_board[0] += 1
            return 1

        return 0

    def end_game(self):
        """Some prints after the end of the game"""
        self.show_board()
        print('Game over. One more? y/n:')
        if input() == 'y':
            self.counter = 0
            return 1
        return 0


if __name__ == '__main__':
    game = TicTacToeGame()
    game.start_game()
