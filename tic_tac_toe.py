
class TicTacGame:

    def __init__(self, m=3, n=3):
        self.m = 3
        self.n = 3
        self.x = 0
        self.y = 0
        self.player1 = ''
        self.player2 = ''
        self.counter = 0
        self.score_board = [0, 0]

    # def grid_size(self):
    #    print('Type size of field. First number - x size, second - y size:')
    #    self.m = int(input())
    #    self.n = int(input())
    #    self.grid = [[-1] * self.m for i in range(self.n)]

    def print_field(self, grid):
        p = [[' '] * self.m for i in range(self.n)]
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    p[i][j] = 'O'
                elif grid[i][j] == 1:
                    p[i][j] = 'X'

        field = []
        for i in range(self.m):
            line = []
            for j in range(self.n):
                line.insert(j, p[i][j])
            field.append(' | '.join(line))

        print(('\n' + '———' * self.n + '\n').join(field))

    def show_board(self):
        print(f"{self.player1}: {self.score_board[0]}")
        print(f"{self.player2}: {self.score_board[1]}")

    def valid_input(self, grid, coord_str):
        if len(coord_str) != 3:
            return 0
        else:
            if coord_str[1] != ' ':
                return 0
            try:
                x = int(coord_str[0])
                y = int(coord_str[2])
            except ValueError:
                return 0
            if grid[x - 1][y - 1] != -1:
                return 2
            self.x = x
            self.y = y
            return 1

    def start_game(self):
        print('The game is starting. Please type your names:')
        print('Player one:')
        self.player1 = input()
        print('Player two:')
        self.player2 = input()
        print("Let's go")
        grid = [[-1] * 3 for i in range(3)]
        while 1:
            self.counter += 1
            print('Type x and y separated by a space')
            coord_str = input()
            ret = self.valid_input(grid, coord_str)
            while ret == 0 or ret == 2 or self.x > self.m \
                    or self.x < 1 or self.y > self.n or self.y < 1:
                if ret == 0:
                    print('Wrong input!')
                else:
                    print('Occupied field!')
                coord_str = input()
                ret = self.valid_input(grid, coord_str)
            if self.counter % 2 == 1:
                print('X placed')
                grid[self.x - 1][self.y - 1] = 1
            else:
                print('O placed')
                grid[self.x - 1][self.y - 1] = 0
            self.print_field(grid)
            if self.check_winner(grid) == 1 or self.counter == self.m * self.n:
                if self.end_game() == 0:
                    break
                grid = [[-1] * 3 for i in range(3)]

    def check_winner(self, grid):
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
        self.show_board()
        print('Game over. One more? y/n:')
        if input() == 'y':
            self.counter = 0
            return 1
        return 0


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
