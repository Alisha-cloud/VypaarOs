type Props = {
  knowledge: string[];
};

export default function KnowledgePanel({
  knowledge,
}: Props) {
  return (
    <div className="border border-zinc-700 rounded-xl p-5 overflow-hidden">

      <h2 className="text-2xl font-bold mb-4">
        Retrieved Knowledge
      </h2>

      <div className="space-y-3">

        {knowledge.map(
          (item, index) => (

            <div
              key={index}
              className="
                border
                border-zinc-700
                rounded-lg
                p-3
                bg-zinc-900
                text-white
                whitespace-pre-wrap
                break-words
              "
            >
              {item}
            </div>

          )
        )}

      </div>

    </div>
  );
}