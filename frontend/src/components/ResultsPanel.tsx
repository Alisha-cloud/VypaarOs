"use client";

import ReactMarkdown from "react-markdown";
import { api } from "@/lib/api";

type Props = {
  report: string;
};

export default function ResultsPanel({
  report,
}: Props) {

  const exportPdf = async () => {

    try {

      const response = await api.post(
        "/export",
        {
          report,
        },
        {
          responseType: "blob",
        }
      );

      const url =
        window.URL.createObjectURL(
          new Blob([response.data])
        );

      const link =
        document.createElement("a");

      link.href = url;

      link.download =
        "VyapaarOS_Report.pdf";

      document.body.appendChild(
        link
      );

      link.click();

      link.remove();

      window.URL.revokeObjectURL(
        url
      );

    } catch (error) {

      console.error(
        "PDF Export Failed",
        error
      );

    }
  };

  return (
    <div className="border border-zinc-700 rounded-xl p-5 overflow-hidden">

      <div className="flex items-center justify-between mb-4">

        <h2 className="text-2xl font-bold">
          AI Advisor Report
        </h2>

        <button
          onClick={exportPdf}
          className="
  bg-green-600
  text-white
  px-4
  py-2
  rounded-lg
  hover:bg-green-700
  transition
"
        >
          Export PDF
        </button>

      </div>

      <div
  className="
    prose
    max-w-none
    max-h-[700px]
    overflow-y-auto
    overflow-x-hidden
    break-words
  "
>

  <ReactMarkdown>
    {report}
  </ReactMarkdown>

</div>

    </div>
  );
}