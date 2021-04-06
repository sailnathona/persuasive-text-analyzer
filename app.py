from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)

import persuade_algos
import re

from nltk.tokenize import sent_tokenize

@app.route('/process', methods=['POST'])
def process_for_persuasiveness():
        input_text = request.json.get('text') 
        print("raw input", input_text)
        sent_text = sent_tokenize(input_text)
        print("text parsed into sentences", sent_text)
        # process input text
        # values 1,2,3 respective totals for pathos, logos and ethos
        i_versus_we, count_and, repeats, uncommon_percent, avg_len, phrases_array, question_count, subj, value1, value2, value3 = persuade_algos.main(sent_text)
        dict = {"i_versus_we": i_versus_we, "count_and": count_and, "repeats": repeats, "uncommon_percent": uncommon_percent, "avg_len": avg_len, "phrases": phrases_array, "num_questions": question_count, "subj_score": subj, "pathos": value1, "logos": value2, "ethos": value3}
        
        return dict



if __name__ == '__main__':
    app.run(host='localhost', port=5000)




