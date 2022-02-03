from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config["CORS_HEADERS"] = "*"


from nltk.tokenize import sent_tokenize
import persuade_algos

app.debug = True


@app.route("/process", methods=["POST", "OPTIONS"])
@cross_origin(origin="*", supports_credentials=True)
def process_text():
    input_text = request.json.get("text")
    parsed_text = sent_tokenize(input_text)
    (
        i_versus_we,
        count_and,
        repeats,
        uncommon_percent,
        avg_len,
        phrases_array,
        question_count,
        subj,
        pathos,
        logos,
        ethos,
    ) = persuade_algos.main(parsed_text)

    dict = {
        "i_versus_we": i_versus_we,
        "count_and": count_and,
        "repeats": repeats,
        "uncommon_percent": uncommon_percent,
        "avg_len": avg_len,
        "phrases": phrases_array,
        "num_questions": question_count,
        "subj_score": subj,
        "pathos": pathos,
        "logos": logos,
        "ethos": ethos,
    }

    return dict


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
