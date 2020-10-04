import unittest
import tic_tac_toe


class TicTacToeTest(unittest.TestCase):
    def test_check_winner_vertical(self):
        grid = [[-1] * 3 for i in range(3)]
        grid[0][0] = 1
        grid[1][0] = 1
        grid[2][0] = 1
        self.assertEqual(tic_tac_toe.TicTacGame().check_winner(grid), 1)
        grid = [[-1] * 3 for i in range(3)]
        grid[1][0] = 1
        grid[1][1] = 1
        grid[1][2] = 1
        self.assertEqual(tic_tac_toe.TicTacGame().check_winner(grid), 1)
        grid = [[-1] * 3 for i in range(3)]
        grid[0][0] = 1
        grid[1][1] = 1
        grid[2][2] = 1
        self.assertEqual(tic_tac_toe.TicTacGame().check_winner(grid), 1)

    def test_valid_input(self):
        grid = [[-1] * 3 for i in range(3)]
        grid[1][1] = 1
        coord_str = '123'
        self.assertEqual(tic_tac_toe.TicTacGame()
                         .valid_input(grid, coord_str), 0)
        coord_str = 'a b'
        self.assertEqual(tic_tac_toe.TicTacGame()
                         .valid_input(grid, coord_str), 0)
        coord_str = '1 a'
        self.assertEqual(tic_tac_toe.TicTacGame()
                         .valid_input(grid, coord_str), 0)
        coord_str = '2 2'
        self.assertEqual(tic_tac_toe.TicTacGame()
                         .valid_input(grid, coord_str), 2)


if __name__ == '__main__':
    unittest.main()
