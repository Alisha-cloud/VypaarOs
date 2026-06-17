export default function ForecastCard({
  forecast,
}: any) {
  return (
    <div className="border rounded p-5">

      <h2 className="text-2xl font-bold mb-4">
        Sales Forecast
      </h2>

      <div className="space-y-2">

        <p>
          Current Sales:
          {" "}
          {forecast.current_sales}
        </p>

        <p>
          Projected Sales:
          {" "}
          {forecast.projected_sales}
        </p>

        <p>
          Current Revenue:
          ₹{forecast.current_revenue}
        </p>

        <p>
          Projected Revenue:
          ₹{forecast.projected_revenue}
        </p>

        <p>
          Growth:
          {" "}
          {forecast.growth}
        </p>

      </div>

    </div>
  );
}