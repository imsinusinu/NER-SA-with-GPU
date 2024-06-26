from flask import Flask, render_template, request
import json
import pandas as pd

from sentence_split import spliter
from model_inference import ner_go, sa_go
from result_setting import sa_organizer, ner_organizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text')
        
        df = pd.DataFrame(columns=["본문"])
        df = df._append({'본문': text}, ignore_index=True)
        sentence_list = spliter(df)

        df1 = ner_go(sentence_list)
        df2 = sa_go(df1)

        ner_result = ner_organizer(df2)
        sa_result, sa_positive, sa_negative = sa_organizer(df2)
        
        return json.dumps({'ner_result': ner_result, 'sa_result': sa_result
                           , 'sa_positive': sa_positive, 'sa_negative': sa_negative}
                           , ensure_ascii = False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')