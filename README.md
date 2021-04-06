# persuasive-text-analyzer

<img width="1440" alt="Screen Shot 2021-04-06 at 3 25 02 PM" src="https://user-images.githubusercontent.com/13419675/113769121-e4e6a300-9720-11eb-8c2f-18777baf9bcb.png">
<img width="1440" alt="Screen Shot 2021-04-06 at 3 25 17 PM" src="https://user-images.githubusercontent.com/13419675/113769128-e748fd00-9720-11eb-8d7c-fe3e3a18e5a5.png">

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
The Persuasive Text Analyzer is a web application that takes in a piece of argumentative text, such as from a panel discussion or a debate, and uses text analytics to determine how persuasive it is based on Aristotle’s three modes of persuasion: Pathos (emotional connection), Logos (logical reasoning), and Ethos (credibility of the person making persuasive arguments).

The inspiration for this project comes from a love of panel debates and the variety and richness in speakers available online to listen to who speak publicly about their ideas about the future, their worldview or ideologies. I stumbled upon an article about Aristotle’s Art of Rhetoric and realized that some of the best speakers I had listened were using a combination of his three modes of persuasion and so this is my attempt to measure something of this.


The text is run through a number of natural language processing algorithms and the results from this analysis visually displayed in a dashboard. The dashboard shows several metrics including end scores for pathos, logos, ethos calculated using various text analytics including the computation of polarity of opinions expressed using Azure Sentiment Analysis API at the document level; overall subjectivity score; displays key phrases from the text which are extracted using the Azure Key Phrases API to give an instant insight into which topics stood out; and displays other metrics such as the average length of sentence, number of questions posed by the speaker, flow of speech, and metrics relating to the speaker’s use of language.
	
## Technologies
The backend API was built using Flask and python, http requests using axios library, and the application UI was built using ReactJS, React charting library, Recharts, for the pie and bar charts, and TextBlob library to gauge subjectivity of the text.

The application uses the Text Analytics API from Azure Cognitive Services specifically sentiment analysis, and key phrases extraction.
	
## Setup
To run the server, clone the repository and make sure you have npm and node installed. 

```
$ npm install
$ npm start
open http://localhost:3000/
```

To run the backend server, make sure to have python and Flask installed.

```
$ git clone "https://www.github.com/sailnathona/persuasive-text-analyzer" 
$ cd persuasive-text-analyzer
$ [activate your virtualenv]
$ pip install -r requirements.txt
$ python app.py
open http://localhost:5000/
```


