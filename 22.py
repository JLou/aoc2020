from collections import deque
from itertools import islice

example_input = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

infinite_loop_input = """Player 1:
43
19

Player 2:
2
29
14"""

with open('inputs/22.txt') as f:
    myinput = f.read()


def parse_input(data) -> tuple[deque, deque]:
    def parse_player(player_data):
        return deque(map(int, player_data.split('\n')[1:]))
    players = data.split('\n\n')
    return list(map(parse_player, players))


def format_deck(deck):
    return ", ".join(map(str, deck))


def compute_score(deck):
    deck.reverse()
    return sum([(i+1)*e for i, e in enumerate(deck)])


def play(deck1, deck2, game_id):
    i = 1
    print(f'== Game {game_id} ==')

    while len(deck1) > 0 and len(deck2) > 0:

        print(f'-- Round {i} (Game {game_id} --')
        print(f'Player 1\'s deck: {format_deck(deck1)}')
        print(f'Player 2\'s deck: {format_deck(deck2)}')
        card1 = deck1.popleft()
        card2 = deck2.popleft()

        print(f'Player 1 plays: {card1}')
        print(f'Player 2 plays: {card2}')
        if card2 > card1:
            print('Player 2 wins')
            deck2.append(card2)
            deck2.append(card1)
        else:
            print('Player 1 wins')
            deck1.append(card1)
            deck1.append(card2)
        i += 1
    print('== Post-game results ==')
    print(f'Player 1\'s deck: {format_deck(deck1)}')
    print(f'Player 2\'s deck: {format_deck(deck2)}')

    winning_deck = deck1 if len(deck1) > 0 else deck2
    print(f'Final score: {compute_score(winning_deck)}')


def happened_before(deck1, deck2, prev_rounds):
    d1, d2 = (list(deck1), list(deck2))
    if (d1, d2) in prev_rounds:
        return True
    else:
        prev_rounds.append((d1, d2))
        return False


def play_recur(deck1, deck2, game_id):
    i = 1
    #print(f'== Game {game_id} ==')
    prev_rounds = []

    while len(deck1) > 0 and len(deck2) > 0:

        #print(f'-- Round {i} (Game {game_id}) --')

        #print(f'Player 1\'s deck: {format_deck(deck1)}')
        #print(f'Player 2\'s deck: {format_deck(deck2)}')

        if happened_before(deck1, deck2, prev_rounds):
            winner = 1
            #print(f'I\'ve seen that before... back to game {game_id-1}')
            return 1
        else:
            card1 = deck1.popleft()
            card2 = deck2.popleft()

            #print(f'Player 1 plays: {card1}')
            #print(f'Player 2 plays: {card2}')

            winner = 1
            if len(deck1) >= card1 and len(deck2) >= card2:
                #print("Playing a sub-game to determine the winner...\n")
                copy_deck1 = deque(islice(deck1, card1))
                copy_deck2 = deque(islice(deck2, card2))
                winner = play_recur(copy_deck1, copy_deck2, game_id+1)
            else:
                if card2 > card1:
                    winner = 2
                else:
                    winner = 1

        if winner == 1:
            #print(f'Player 1 wins round {i} of game {game_id}!\n')
            deck1.append(card1)
            deck1.append(card2)
        else:
            #print(f'Player 2 wins round {i} of game {game_id}\n')
            deck2.append(card2)
            deck2.append(card1)

        i += 1
    # if game_id > 1:
        #print(f'...anyway, back to game {game_id-1}.\n')

    return 1 if len(deck1) > 0 else 2


def play_game(data):
    deck1, deck2 = parse_input(data)
    play(deck1, deck2, 1)


def play_game2(data):
    deck1, deck2 = parse_input(data)
    winner = play_recur(deck1, deck2, 1)

    print('== Post-game results ==')
    print(f'Player 1\'s deck: {format_deck(deck1)}')
    print(f'Player 2\'s deck: {format_deck(deck2)}')
    winning_deck = deck1 if len(deck1) > 0 else deck2
    print(f'Final score: {compute_score(winning_deck)}')


# play_game2(example_input)
# play_game2(infinite_loop_input)
play_game2(myinput)
