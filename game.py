from flask import Flask
from model import Player
from model.cards import Card
import cPickle as pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World'

@app.route('/start_game')
def start_game():
  player1 = Player('player1')
  player2 = Player('player2')

  deck = pickle.load(open('deck','rb'))
  deck = shuffle(deck)

  return player1.get_name() + " " + player2.get_name()


if __name__ == '__main__':
  app.run(debug=True)
