export default function CompetitorCard({
  competitor,
}: any) {

  return (
    <div className="border rounded p-5">

      <h2 className="text-2xl font-bold mb-4">
        Competitor Analysis
      </h2>

      <div className="space-y-4">

        {competitor.competitors.map(
          (item: any) => (

            <div
              key={item.name}
              className="border rounded p-3"
            >
              <h3 className="font-semibold">
                {item.name}
              </h3>

              <p>
                Strength:
                {" "}
                {item.strength}
              </p>

              <p>
                Weakness:
                {" "}
                {item.weakness}
              </p>

            </div>

          )
        )}

      </div>

      <div className="mt-4 p-3 bg-gray-50 rounded">
        {competitor.recommendation}
      </div>

    </div>
  );
}