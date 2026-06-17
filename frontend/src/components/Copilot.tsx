"use client";

import { useState } from "react";
import { api } from "@/lib/api";

export default function Copilot() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState<
  {
    role: string;
    content: string;
  }[]
>([]);
  const [loading, setLoading] = useState(false);

  const askCopilot = async () => {
    if (!question.trim()) return;

    try {
      setLoading(true);

      const response = await api.post(
        "/chat",
        {
          question,
        }
      );

      setMessages((prev) => [
  ...prev,
  {
    role: "user",
    content: question,
  },
  {
    role: "assistant",
    content: response.data.answer,
  },
]);

setQuestion("");

    }  catch (error) {
  console.error(error);

  setMessages((prev) => [
    ...prev,
    {
      role: "assistant",
      content: "Unable to get response.",
    },
  ]);

} finally {
  setLoading(false);
}
  };

  return (
    <div className="border rounded p-5 space-y-4">

      <h2 className="text-2xl font-bold">
        AI Business Copilot
      </h2>

      <div className="flex flex-wrap gap-2">

  {[
    "Increase sales",
    "Pricing strategy",
    "Marketing plan",
    "Forecast revenue",
    "Inventory advice",
  ].map((prompt) => (

    <button
      key={prompt}
      onClick={() =>
        setQuestion(prompt)
      }
      className="
  border
  border-zinc-700
  px-3
  py-2
  rounded-lg
  hover:bg-zinc-800
  transition
"
    >
      {prompt}
    </button>

  ))}

</div>

      <input
        type="text"
        placeholder="Ask a business question..."
        value={question}
        onChange={(e) =>
          setQuestion(
            e.target.value
          )
        }
        className="w-full border rounded p-3"
      />

      <button
        onClick={askCopilot}
        className="
  bg-blue-600
  hover:bg-blue-700
  text-white
  px-5
  py-3
  rounded-lg
  transition
"
      >
        {loading
          ? "Thinking..."
          : "Ask Copilot"}
      </button>

      <div
  className="
    h-[400px]
    overflow-y-auto
    space-y-3
    border
    border-zinc-700
    rounded-lg
    p-3
    bg-zinc-950
  "
>
  {messages.map(
    (msg, index) => (

      <div
  key={index}
  className={`border border-zinc-700 rounded-lg p-4 ${
  msg.role === "user"
    ? "bg-blue-900 text-white ml-10"
    : "bg-zinc-900 text-white mr-10"
}`}
>

        <strong>
          {msg.role === "user"
            ? "You"
            : "AI"}
          :
        </strong>

        <p className="mt-1 whitespace-pre-wrap break-words leading-relaxed">
  {msg.content}
</p>

      </div>

    )
  )}

</div>

    </div>
  );
}