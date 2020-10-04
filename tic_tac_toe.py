class TicTacGame:
    m = 3
    x = 0
    y = 0
    n = 3
    grid = [[-1] * 3 for i in range(3)]
    player1 = ''
    player2 = ''
    counter = 0
    score_board = [0, 0]

    def grid_size(self):
        print('Type size of field. First number - x size, second - y size:')
        self.m = int(input())
        self.n = int(input())
        self.grid = [[-1] * self.m for i in range(self.n)]

    def print_field(self):
        p = [[' '] * self.m for i in range(self.n)]
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    p[i][j] = 'O'
                elif self.grid[i][j] == 1:
                    p[i][j] = 'X'
        for i in range(self.m):
            summary_list = []
            for j in range(self.n):
                summary_list.insert(j, p[i][j])
            print('  '.join(summary_list))

    def show_board(self):
        print(f"{self.player1}: {self.score_board[0]}")
        print(f"{self.player2}: {self.score_board[1]}")

    def valid_input(self):
        coord_str = input()
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
            if self.grid[x - 1][y - 1] != -1:
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
        while 1:
            self.counter += 1
            print('Type x and y separated by a space')
            ret = self.valid_input()
            while ret == 0 or ret == 2 or self.x > self.m or self.x < 1 or self.y > self.n or self.y < 1:
                if ret == 0:
                    print('Wrong input!')
                else:
                    print('Occupied field!')
                ret = self.valid_input()
            if self.counter % 2 == 1:
                print('X placed')
                self.grid[self.x - 1][self.y - 1] = 1
            else:
                print('O placed')
                self.grid[self.x - 1][self.y - 1] = 0
            self.print_field()
            if self.check_winner() == 1 or self.counter == self.m * self.n:
                if self.end_game() == 0:
                    break

    def check_winner(self):
        for x in range(self.m):
            if self.grid[x][1] >= 0 and self.grid[x][1] == self.grid[x][0] and self.grid[x][1] == self.grid[x][2]:
                if self.grid[x][1] == 0:
                    print(f'The winner is {self.player2}')
                    self.score_board[1] += 1
                else:
                    print(f'The winner is {self.player1}')
                    self.score_board[0] += 1
                return 1

        for y in range(self.n):
            if self.grid[1][y] >= 0 and self.grid[1][y] == self.grid[0][y] and self.grid[1][y] == self.grid[2][y]:
                if self.grid[1][y] == 0:
                    print(f'The winner is {self.player2}')
                    self.score_board[1] += 1
                else:
                    print(f'The winner is {self.player1}')
                    self.score_board[0] += 1
                return 1

        if self.grid[1][1] >= 0 and self.grid[1][1] == self.grid[2][0] and self.grid[1][1] == self.grid[0][2]:
            if self.grid[1][1] == 0:
                print(f'The winner is {self.player2}')
                self.score_board[1] += 1
            else:
                print(f'The winner is {self.player1}')
                self.score_board[0] += 1
            return 1

        if self.grid[1][1] >= 0 and self.grid[1][1] == self.grid[0][0] and self.grid[1][1] == self.grid[2][2]:
            if self.grid[1][1] == 0:
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
            self.grid = [[-1] * 3 for i in range(3)]
            return 1
        return 0


game = TicTacGame()
game.start_game()