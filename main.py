"""Functions to simulate the Coins Circle problem"""


class Player():
    def __init__(self, player_name: int):
        self.coins = 1
        self.player = player_name

    def receive(self, n_coins):
        self.coins += n_coins

    def give(self, n_coins):
        self.coins -= n_coins

    def is_in_game(self):
        return self.coins > 0

    def __repr__(self):
        return f'Player {self.player} ({self.coins})'


def coins_move(N_players):
    # Create list with the Players
    players = [Player(player) for player in (range(1, N_players + 1))]
    step = 1
    index = 0
    # print(f'Starting to play with {N_players} circle\n----\n')
    while len(players) > 1:
        # use of % to make it circular index
        receiver_index = (index + 1) % len(players)
        coins_to_move = (step + 1) % 2 + 1
        # print(f'Step {step}: Movement of coins ({coins_to_move}): {players[index]} -> {players[receiver_index]}')

        # update player who gives coins and receives
        players[index].give(coins_to_move)
        players[receiver_index].receive(coins_to_move)
        # if player who gives has 0 coins, then remove from the list.
        if not players[index].is_in_game():
            # print(f'Player {players[index].player} is out of coins')
            players.pop(index)
            # reduce the index in 1 because the lenght of the list was decreased
            index -= 1
        # print(f'Step {step} - Players: {[player for player in players]}\n-----\n')
        step += 1
        index += 1
        index = index % len(players)  # use a circular index
        # to avoid ininity loops
        if step > N_players * 4:
            break
    return players


if __name__ == '__main__':
    circles_with_winner = []
    for N_players in range(4, 1500):
        winner = coins_move(N_players)
        if len(winner) == 1:
            print(f'With {N_players}, the winner is {winner}')
            circles_with_winner.append((N_players, winner[0].player))
    print('List with (N_player, winner) for the Coins Circle game')
    print(circles_with_winner)
