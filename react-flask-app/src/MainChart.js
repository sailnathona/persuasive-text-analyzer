import React from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";
import RightItem from './RightItem';

const MainChart = ({ pathosval, logosval, ethosval }) => {
  const data = [
    { name: "Pathos", value: pathosval },
    { name: "Logos", value: logosval },
    { name: "Ethos", value: ethosval },
  ];

  const total = pathosval + logosval + ethosval;

  return (
    <>
      <div>
        <BarChart
          width={400}
          height={300}
          data={data}
          margin={{
            top: 30,
            right: 30,
            left: 10,
            bottom: 5,
          }}
          barSize={40}
        >
          <XAxis
            dataKey="name"
            scale="point"
            padding={{ left: 20, right: 20 }}
          />
          <YAxis />
          <Tooltip />
          <CartesianGrid strokeDasharray="3 3" />
          <Bar dataKey="value" fill="#8884d8" background={{ fill: "#eee" }} />
        </BarChart>
      </div>
      {/* <div style={{ marginLeft: "100px", marginTop: "20px" }}>
        Overall Score: {total}
        Pathos: {pathosval}
        Logos: {logosval}
        Ethos: {ethosval}
      </div> */}
      <RightItem pathos={pathosval} logos={logosval} ethos={ethosval}/>
    </>
  );
};

export default MainChart;
