import unittest
import tic_tac_toe
from unittest.mock import patch

# Game testing


class TicTacToeTest(unittest.TestCase):
    def test_check_winner_vertical(self):
        grid = [[-1] * 3 for _ in range(3)]
        grid[0][0] = 1
        grid[1][0] = 1
        grid[2][0] = 1
        self.assertEqual(tic_tac_toe.TicTacToeGame().check_winner(grid), 1)
        grid = [[-1] * 3 for _ in range(3)]
        grid[1][0] = 0
        grid[1][1] = 0
        grid[1][2] = 0
        self.assertEqual(tic_tac_toe.TicTacToeGame().check_winner(grid), 1)
        grid = [[-1] * 3 for _ in range(3)]
        grid[0][0] = 1
        grid[1][1] = 1
        grid[2][2] = 1
        self.assertEqual(tic_tac_toe.TicTacToeGame().check_winner(grid), 1)

    @patch('builtins.input', return_value='1 2')
    def test_valid_input(self, mock_input):
        grid = [[-1] * 3 for _ in range(3)]
        grid[1][1] = 1
        self.assertEqual(None, tic_tac_toe.TicTacToeGame().valid_input(grid))


if __name__ == '__main__':
    unittest.main()
