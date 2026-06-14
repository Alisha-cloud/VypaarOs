type Props = {
  report: string;
};

export default function ResultsPanel({
  report,
}: Props) {
  return (
    <div className="border rounded p-5">

      <h2 className="text-xl font-bold mb-3">
        AI Advisor Report
      </h2>

      <pre className="whitespace-pre-wrap">
        {report}
      </pre>

    </div>
  );
}