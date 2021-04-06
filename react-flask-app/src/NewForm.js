import React, { useState } from "react";
import axios from "axios";
import Dashboard from "./Dashboard";
import LoadingSpinner from "./LoadingSpinner";

import "./form.css";
import { FaGithub } from "react-icons/fa";

function NewForm() {
  const [text, setText] = useState("");
  const [fetchedData, setFetchedData] = useState("");
  const [isSubmitted, setSubmitted] = useState(false);
  const [isLoading, setLoading] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
    setLoading(true);

    console.log("button clicked");

    const config = {
      headers: { "Access-Control-Allow-Origin": "*" },
    };

    axios
      .post(
        "http://localhost:5000/process",
        {
          text: text,
        },
        config
      )
      .then((res) => {
        console.log("res", res);
        setFetchedData(res.data);
        setLoading(false);
      })
      .catch((er) => {
        console.log(er.response.data);
        setLoading(false);
      });
  };

  function displayLength() {
    return (
      <div>
        <p>{text.length} characters!</p>
      </div>
    );
  }

  return !isSubmitted ? (
    <div className="main-div">
      <div className="form-header">
        <p>Persuasive Text Analyzer</p>
        <a className="gitbox" href="https://github.com/sailnathona/persuasive-text-analyzer">
          <FaGithub />
          GitHub
        </a>
      </div>
      <div className="container-box">
        <div className="box">
          <form onSubmit={handleSubmit} method="post">
            <label className="mainlabel"><strong>Input text:</strong></label>
            <textarea
              name="text"
              value={text}
              onChange={(e) => setText(e.target.value)}
              cols={60}
              rows={7}
              placeholder="Enter min 300 -> max 5000 chars"
            ></textarea>
            <br />
            <input
              id="sb"
              disabled={text.length <= 300 | text.length >= 5000 }
              style={{
                opacity: `${text.length <= 300 ? "0.7" : "1"}`,
                cursor: `${text.length <= 300 | text.length >= 5000 ? "not-allowed" : "pointer"}`,
                }}
              type="submit"
              name="Submit"
              value="SUBMIT"
            />
          </form>
          {displayLength()}
        </div>
      </div>
    </div>
  ) : isLoading ? (
    <LoadingSpinner />
  ) : (
    <Dashboard
      pathos={fetchedData.pathos}
      logos={fetchedData.logos}
      ethos={fetchedData.ethos}
      subj_score={fetchedData.subj_score}
      num_questions={fetchedData.num_questions}
      phrases_array={fetchedData.phrases}
      avg_len={fetchedData.avg_len}
      uncommon={fetchedData.uncommon_percent}
      repeats={fetchedData.repeats}
      count_ands={fetchedData.count_and}
      i_versus_we={fetchedData.i_versus_we}
    />
  );
}

export default NewForm;