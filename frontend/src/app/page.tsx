import GoalForm from "@/components/GoalForm";

export default function Home() {
  return (
    <main className="max-w-4xl mx-auto p-10">

      <h1 className="text-4xl font-bold mb-6">
        VyapaarOS
      </h1>

      <p className="mb-8">
        AI Business Operating System
      </p>

      <GoalForm />
    </main>
  );
}