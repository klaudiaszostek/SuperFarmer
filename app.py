from flask import Flask, render_template, jsonify, request
from game_logic.player import Player
from game_logic.dice import roll_dice

app = Flask(__name__)
player = Player()

@app.route('/')
def index():
    return render_template('game.html', animals=player.get_animals(), turn=player.turn)


@app.route('/roll', methods=['POST'])
def roll():
    results = roll_dice()

    event = player.apply_roll(results)
    return jsonify({
        'dice': results,
        'animals': player.get_animals(),
        'event': event,
        'turn': player.turn,
        'trades': player.get_possible_trades(),
        'can_trade': not player.exchanged_this_turn,
        'victory': player.check_victory()
    })

@app.route('/trade', methods=['POST'])
def trade():
    data = request.json
    success, message = player.exchange(data['from'], data['to'])
    return jsonify({
        'success': success,
        'message': message,
        'animals': player.get_animals(),
        'trades': player.get_possible_trades(),
        'can_trade': not player.exchanged_this_turn
    })

@app.route('/reset', methods=['POST'])
def reset():
    global player
    player = Player()
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(debug=True)
