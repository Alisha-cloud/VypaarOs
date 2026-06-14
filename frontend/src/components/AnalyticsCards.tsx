type Props = {
  analytics: {
    total_sales: number;
    total_revenue: number;
    average_order_value: number;
  };
};

export default function AnalyticsCards({
  analytics,
}: Props) {
  return (
    <div className="grid grid-cols-3 gap-4">

      <div className="p-4 border rounded">
        <h3>Revenue</h3>
        <p className="text-2xl font-bold">
          ₹{analytics.total_revenue}
        </p>
      </div>

      <div className="p-4 border rounded">
        <h3>Sales</h3>
        <p className="text-2xl font-bold">
          {analytics.total_sales}
        </p>
      </div>

      <div className="p-4 border rounded">
        <h3>AOV</h3>
        <p className="text-2xl font-bold">
          ₹{analytics.average_order_value}
        </p>
      </div>

    </div>
  );
}