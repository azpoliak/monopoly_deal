class Player:

  MAX_HAND_COUNT = 7
  _private_hand = []
  _public_hand = []
  __name = ""

  def __init__(self, name):
    self.name = name

  def get_name(self):
    return self.name

  def get_hand(self):
    return _private_hand  
		
  def add_cards(self, cards):
  	for card in cards:
  		_private_hand.append(card)