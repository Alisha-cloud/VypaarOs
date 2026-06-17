"use client";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function RevenueChart({
  analytics,
}: any) {

  const data = [
    {
      name: "Current Revenue",
      revenue: analytics.total_revenue,
    },
    {
      name: "Projected Revenue",
      revenue: Math.round(
        analytics.total_revenue * 1.2
      ),
    },
  ];

  return (
    <div className="border border-zinc-700 rounded-xl p-5 overflow-hidden">

      <h2 className="text-2xl font-bold mb-4">
        Revenue Forecast
      </h2>

      <div className="w-full h-[300px]">

        <ResponsiveContainer
          width="100%"
          height="100%"
        >

          <BarChart data={data}>

            <XAxis
              dataKey="name"
              stroke="#a1a1aa"
            />

            <YAxis
              stroke="#a1a1aa"
            />

            <Tooltip
              contentStyle={{
                background: "#18181b",
                border: "1px solid #27272a",
                color: "white",
              }}
            />

            <Bar
              dataKey="revenue"
              fill="#2563eb"
              radius={[8, 8, 0, 0]}
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}