import copy
from node import Node


def simulate_1(word_length, alphabet, word):
    from ato_game import AtoGame
    game = AtoGame()
    game.alph_count = len(alphabet)
    game.word_length = word_length
    from players.player_rng import PlayerRng
    game.p1 = PlayerRng
    game.p2 = PlayerRng
    game.alphabet = alphabet
    game.word = copy.deepcopy(word)
    word_analisys = {}
    while True:
        if len(game.word) != 0:
            move1 = game.p1.make_move_1(self=game.p1, word=game.word, alphabet=game.alphabet, word_analisys=word_analisys, separator=game.separator, word_length=word_length)
        else:
            move1 = 0
        move2 = game.p2.make_move_2(self=game.p2, word=game.word, alphabet=game.alphabet, position=move1, word_analisys=word_analisys,
                                    separator=game.separator, word_length=word_length)
        game.word.insert(move1, move2)
        from utility import analyse_word
        is_rep, game.repetition, word_analisys = analyse_word(game.word)
        if is_rep:
            return 1
        elif len(game.word) == game.word_length:
            return 2


def simulate_2(word_length, alphabet, move1, word):
    from ato_game import AtoGame
    game = AtoGame()
    game.alph_count = len(alphabet)
    game.word_length = word_length
    from players.player_rng import PlayerRng
    game.p1 = PlayerRng
    game.p2 = PlayerRng
    game.alphabet = alphabet
    game.word = copy.deepcopy(word)
    word_analisys = {}
    move2 = game.p2.make_move_2(self=game.p2, word=game.word, alphabet=game.alphabet, position=move1, word_analisys=word_analisys,
                                separator=game.separator, word_length=word_length)
    game.word.insert(move1, move2)
    from utility import analyse_word
    is_rep, game.repetition, word_analisys = analyse_word(game.word)
    if is_rep:
        return 1
    elif len(game.word) == game.word_length:
        return 2

    while True:
        if len(game.word) != 0:
            move1 = game.p1.make_move_1(self=game.p1, word=game.word, alphabet=game.alphabet, word_analisys=word_analisys, separator=game.separator, word_length=word_length)
        else:
            move1 = 0
        move2 = game.p2.make_move_2(self=game.p2, word=game.word, alphabet=game.alphabet, position=move1, word_analisys=word_analisys,
                                    separator=game.separator, word_length=word_length)
        game.word.insert(move1, move2)
        is_rep, game.repetition, word_analisys = analyse_word(game.word)
        if is_rep:
            return 1
        elif len(game.word) == game.word_length:
            return 2


def get_value_by_mcts(node, word_length, alphabet):
    if node.Type == 1:
        return simulate_2(word_length, alphabet, node.Place, node.Word)
    if node.Type == 2:
        return simulate_1(word_length, alphabet, node.Word)


def descend_by_uct(node, alphabet: [str]):
    not_used_move = node.get_not_used_move()
    word = copy.deepcopy(node.Word)
    if not_used_move != -1:
        if node.Type == 1:
            word.insert(node.Place, not_used_move)
            new_node = Node(word, -1, not_used_move, 2, alphabet)
            node.Children.append(new_node)
            return new_node, True
        if node.Type == 2:
            new_node = Node(word, not_used_move, "", 1, alphabet)
            node.Children.append(new_node)
            return new_node, True
    return node.get_best_child(), False


def play_one_game(node, alphabet: [str], word_length: int):
    used_nodes = [node]
    first_visited = False
    while not first_visited:
        (node, first_visited) = descend_by_uct(node, alphabet)
        used_nodes.append(node)
    winner = get_value_by_mcts(node, word_length, alphabet)
    if winner == used_nodes[0].Type:
        score = 0
    else:
        score = 1
    for used_node in used_nodes:
        used_node.update_score(score)