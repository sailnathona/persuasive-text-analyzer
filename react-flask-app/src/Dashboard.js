import Gauge from './Gauge.js';
import MainChart from './MainChart.js';
import WordCloud from './WordCloud.js';
import Card from './Card.js';
import PieChartPer from './PieChartPer.js';
import './grid.css';



function Dashboard({pathos, logos, ethos, subj_score, num_questions, phrases_array, avg_len, uncommon, repeats, count_ands, i_versus_we}) {
    return (
        <div className="grid-1">
                <div className="nav">Dashboard</div>
                <MainChart className="main" pathosval={pathos} logosval={logos} ethosval={ethos}/>
                <div className="side-area">
                    <Gauge className="gauge" value={subj_score} min="0" max="1" label='Subjectivity' units="0-1"/>
                    <WordCloud className="wordcloud" phrases={phrases_array}/>
                </div>
                <div className="cards">
                    <Card className="card1" number={num_questions} text="Questions posed"/>
                    <Card className="card2" number={avg_len} text="Average length of sentence"/>
                    <Card className="card3" number={i_versus_we} text="Ratio of 'I' to 'We'"/>
                    <Card className="card4" number={count_ands} text="% words beginning with 'And'"/>
                </div>
                <div className="pie">
                    <PieChartPer uncommon={uncommon}/>
                </div>
        </div>
    );
}

export default Dashboard;

