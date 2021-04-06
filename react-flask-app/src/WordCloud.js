import React from "react";
import TagCloud from "react-tag-cloud";
import randomColor from "randomcolor";

function randomIntFromInterval(min, max) {
  // min and max included
  return Math.floor(Math.random() * (max - min + 1) + min);
}

function WordCloud({ phrases }) {
  if (phrases) {
    return (
      <div>
        <TagCloud
          style={{
            fontFamily: "sans-serif",
            fontSize: randomIntFromInterval(),
            fontWeight: "bold",
            fontStyle: "italic",
            color: () => randomColor(),
            padding: 5,
            width: "100%",
            height: "100%",
            marginTop: "20px",
            marginRight: "10px",
            marginLeft: "10px",
            marginBotton: "0px",
          }}
        >
          {phrases.map((string) => (
            <div>{string}</div>
          ))}
        </TagCloud>
      </div>
    );
  }
}

export default WordCloud;
