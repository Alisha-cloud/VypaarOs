type Props = {
  tasks: string[];
};

export default function AgentFlow({
  tasks,
}: Props) {
  return (
    <div className="border rounded p-4">

      <h2 className="font-bold mb-4">
        Agent Execution
      </h2>

      <div className="flex gap-3 flex-wrap">

        {tasks.map((task) => (
          <div
            key={task}
            className="
    bg-emerald-600
    text-white
    px-4
    py-2
    rounded-full
    font-medium
  "
          >
            ✓ {task}
          </div>
        ))}

      </div>

    </div>
  );
}