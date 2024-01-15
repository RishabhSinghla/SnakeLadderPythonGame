from board import Board
from dice import Dice
from player import Player

class SnakesAndLaddersGame:
    def __init__(self, num_players=2):
        self.board = Board()
        self.dice = Dice()
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.winner = None

    def move_player(self, player, steps):
        new_position = player.position + steps

        if new_position in self.board.snakes:
            print(f"{player.name} landed on a snake! Going down to position {self.board.snakes[new_position]}")
            player.position = self.board.snakes[new_position]
        elif new_position in self.board.ladders:
            print(f"{player.name} found a ladder! Going up to position {self.board.ladders[new_position]}")
            player.position = self.board.ladders[new_position]
        elif new_position > self.board.size:
            player.position = self.board.size - (new_position - self.board.size)
        else:
            player.position = new_position

    def display_board(self):
        print("\nCurrent Board:")
        for player in self.players:
            print(f"{player.name} is at position {player.position}")
        print()

    def play(self):
        while not self.winner:
            for player in self.players:
                try:
                    input(f"{player.name}, press Enter to roll the dice...")
                except KeyboardInterrupt:
                    print("\nGame aborted. Exiting...")
                    return

                dice_result = self.dice.roll()
                print(f"{player.name} rolled a {dice_result}")
                self.move_player(player, dice_result)
                self.display_board()

                for other_player in self.players:
                    if other_player != player and other_player.position == player.position:
                        print(f"{other_player.name} is on the same position as {player.name}! {other_player.name} goes back to the start.")
                        other_player.position = 0

                if player.position == self.board.size:
                    self.winner = player
                    break

        print(f"\nCongratulations! {self.winner.name} is the winner!")

if __name__ == "__main__":
    num_players = 2
    game = SnakesAndLaddersGame(num_players)
    game.play()
