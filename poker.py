import time
from treys import Card, Deck, Evaluator

# Define hole cards (A♥ K♠)
hole_cards = [Card.new('7h'), Card.new('4s')]
evaluator = Evaluator()


def calculateHandStrength():
    deck = Deck()
    deck.cards.remove(hole_cards[0])
    deck.cards.remove(hole_cards[1])

    # Deal a random board (flop, turn, river)
    board = deck.draw(5)

    # Evaluate hand strength
    hand_strength = evaluator.evaluate(board, hole_cards)
    hand_class = evaluator.get_rank_class(hand_strength)

    # Print results

    return hand_class

total = 100000

from collections import defaultdict

d = defaultdict(int)
start_time = time.time()
for i in range(total):
    hs = calculateHandStrength()
    d[hs] += 1
    if i % 1000 == 0:
        print(f"on the {i}th iteration")

end_time = time.time()
print(f"Total time for {total} iterations: {end_time - start_time} seconds")
print(d)

for key, value in sorted(d.items()):
    print(f"{evaluator.class_to_string(key)}: {value / total * 100:.2f}%")

print(sum(value for _, value in d.items()))
