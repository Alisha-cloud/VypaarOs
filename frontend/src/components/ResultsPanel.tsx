import ReactMarkdown from "react-markdown";

type Props = {
  report: string;
};

export default function ResultsPanel({
  report,
}: Props) {
  return (
    <div className="border rounded p-5">

      <h2 className="text-2xl font-bold mb-4">
        AI Advisor Report
      </h2>

      <div className="prose prose-invert max-w-none">
        <ReactMarkdown>
          {report}
        </ReactMarkdown>
      </div>

    </div>
  );
}