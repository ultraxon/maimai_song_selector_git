from flask import Flask, request, jsonify, render_template
import json
import pandas as pd

from what_to_play_today import MDZZ

app = Flask(__name__)
data_info = pd.read_csv('./csv_file/maimai_full_list_edited.csv')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def handle_post():
    request_data = json.loads(request.get_data(as_text=True))
    print('Received: ', request_data)
    category = request_data['Category']
    difficulty = request_data['Difficulty']
    starsLowerBound = request_data['starsLowerBound']
    starsUpperBound = request_data['starsUpperBound']

    selector = MDZZ()
    result = selector.random_select_sqlite(lower_bound=starsLowerBound, upper_bound=starsUpperBound, difficulty=difficulty, category=category)

    json_return = {
        'ret_type': 0,
        'Category': None,
        'MusicName': None,
        'Difficulty': None,
        'Stars': None,
    }

    if result == -1:
        json_return['ret_type'] = -1
    else:
        json_return['Category'] = result[0]
        json_return['MusicName'] = result[1]
        json_return['Difficulty'] = result[2]
        json_return['Stars'] = result[3]
        
    print(result)
    return jsonify(json_return), 201


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)