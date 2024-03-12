from django.test import TestCase
from chess.models import Game


class GameModelTest(TestCase):

    def setUp(self):

        self.board_state_initial = {
            "a1": "Rook_White", "a2": "Pawn_White", "a7": "Pawn_Black", "a8": "Rook_Black",
            "b1": "Knight_White", "b2": "Pawn_White", "b7": "Pawn_Black", "b8": "Knight_Black",
            "c1": "Bishop_White", "c2": "Pawn_White", "c7": "Pawn_Black", "c8": "Bishop_Black",
            "d1": "Queen_White", "d2": "Pawn_White", "d7": "Pawn_Black", "d8": "Queen_Black",
            "e1": "King_White", "e2": "Pawn_White", "e7": "Pawn_Black", "e8": "King_Black",
            "f1": "Bishop_White", "f2": "Pawn_White", "f7": "Pawn_Black", "f8": "Bishop_Black",
            "g1": "Knight_White", "g2": "Pawn_White", "g7": "Pawn_Black", "g8": "Knight_Black",
            "h1": "Rook_White", "h2": "Pawn_White", "h7": "Pawn_Black", "h8": "Rook_Black"
        }
        self.move_log_initial = [
            {"from": "e2", "to": "e4", "piece": "Pawn", "color": "White", "time": "2024-03-10T12:00:00"},
            {"from": "e7", "to": "e5", "piece": "Pawn", "color": "Black", "time": "2024-03-10T12:02:00"}
        ]

        self.game = Game.objects.create(
            board_state=self.board_state_initial,
            game_status='IN_PROGRESS',
            current_turn='WHITE',
            move_log=self.move_log_initial,
        )

    def test_game_creation(self):

        self.assertEqual(self.game.board_state, self.board_state_initial)
        self.assertEqual(self.game.game_status, 'IN_PROGRESS')
        self.assertEqual(self.game.current_turn, 'WHITE')
        self.assertEqual(self.game.move_log, self.move_log_initial)

    def test_game_str(self):

        expected_game_str = f"Game {self.game.pk}: IN_PROGRESS"
        self.assertEqual(str(self.game), expected_game_str)
