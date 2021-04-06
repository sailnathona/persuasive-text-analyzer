import React from "react";
import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Legend,
} from "recharts";

function PieChartPer({ uncommon }) {
  const data01 = [{ name: "% uncommon words", value: uncommon }];
  let b = { name: "common words", value: 100 - uncommon };
  data01.push(b);

  const COLORS = ['#C21460', '#E3D4FD'];

  return (
    <div>
      <PieChart width={350} height={350}>
        <Legend />
        <Pie
          data={data01}
          dataKey="value"
          cx={180}
          cy={100}
          innerRadius={70}
          outerRadius={90}
          paddingAngle={5}
          >
            {
      data01.map((entry, index) => (
        <Cell key={`cell-${index}`} fill={COLORS[index]}/>
      ))
    }
        </Pie>
        {/* <Legend /> */}
      </PieChart>
    </div>
  );
}

export default PieChartPer;
