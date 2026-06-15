"use client";

import { useState } from "react";

import { api } from "@/lib/api";

import AnalyticsCards from "@/components/AnalyticsCards";
import AgentFlow from "@/components/AgentFlow";
import ResultsPanel from "@/components/ResultsPanel";
import SimulationCard from "@/components/SimulationCard";
import FileUpload from "@/components/FileUpload";

export default function GoalForm() {
  const [goal, setGoal] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const analyze = async () => {
    try {
      setLoading(true);

      const response = await api.post(
        "/analyze",
        {
          goal,
        }
      );

      setResult(response.data);

    } catch (error) {
      console.error(error);

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-8">

        <FileUpload />

      {/* Goal Input */}

      <div className="space-y-4">

        <input
          className="border p-3 w-full rounded"
          placeholder="Enter business goal..."
          value={goal}
          onChange={(e) =>
            setGoal(e.target.value)
          }
        />

        <button
          onClick={analyze}
          className="bg-black text-white px-5 py-3 rounded"
        >
          {loading
            ? "Analyzing..."
            : "Analyze"}
        </button>

      </div>


      {/* Goal Card */}

{result?.goal && (

  <div className="border rounded p-5">

    <h3 className="text-sm text-gray-400">
      Goal
    </h3>

    <p className="text-xl font-semibold">
      {result.goal}
    </p>

  </div>

)}

      {/* Analytics */}

      {result?.analytics_data && (

        <AnalyticsCards
          analytics={
            result.analytics_data
          }
        />

      )}

      {result?.simulation_data && (

  <SimulationCard
    simulation={
      result.simulation_data
    }
  />

)}

      {/* Agent Flow */}

      {result?.plan?.tasks && (

        <AgentFlow
          tasks={
            result.plan.tasks
          }
        />

      )}

      {/* Advisor Report */}

      {result?.advisor_report && (

        <ResultsPanel
          report={
            result.advisor_report
          }
        />

      )}

    </div>
  );
}