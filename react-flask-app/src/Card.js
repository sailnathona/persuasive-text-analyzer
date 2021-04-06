import React from 'react';


function Card({number, text}) {
    return (
            <div style={{fontFamily: 'Inter'}}>
                <h1>{number}</h1>
                <p>{text}</p>
            </div>
    );
}

export default Card;
