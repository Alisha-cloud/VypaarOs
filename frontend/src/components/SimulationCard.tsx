type Props = {
  simulation: {
    current_price: number;
    new_price: number;
    price_reduction: number;
    estimated_sales_growth: string;
    projected_revenue: number;
    revenue_change: number;
    recommendation: string;
  };
};

export default function SimulationCard({
  simulation,
}: Props) {
  return (
    <div className="border rounded p-5">

      <h2 className="text-2xl font-bold mb-4">
        Price Simulation
      </h2>

      <div className="grid grid-cols-2 gap-4">

        <div>
          <p className="text-gray-400">
            Current Price
          </p>

          <p className="text-xl font-bold">
            ₹{simulation.current_price}
          </p>
        </div>

        <div>
          <p className="text-gray-400">
            New Price
          </p>

          <p className="text-xl font-bold">
            ₹{simulation.new_price}
          </p>
        </div>

        <div>
          <p className="text-gray-400">
            Price Reduction
          </p>

          <p className="text-xl font-bold">
            ₹{simulation.price_reduction}
          </p>
        </div>

        <div>
          <p className="text-gray-400">
            Sales Growth
          </p>

          <p className="text-xl font-bold text-green-500">
            {simulation.estimated_sales_growth}
          </p>
        </div>

        <div>
          <p className="text-gray-400">
            Projected Revenue
          </p>

          <p className="text-xl font-bold">
            ₹{simulation.projected_revenue}
          </p>
        </div>

        <div>
          <p className="text-gray-400">
            Revenue Change
          </p>

          <p className="text-xl font-bold text-green-500">
            +₹{simulation.revenue_change}
          </p>
        </div>

      </div>

      <div className="mt-6 p-4 border rounded">

        <h3 className="font-semibold mb-2">
          Recommendation
        </h3>

        <p>
          {simulation.recommendation}
        </p>

      </div>

    </div>
  );
}