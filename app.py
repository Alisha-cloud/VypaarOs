from workflow.graph import workflow

result = workflow.invoke(
    {
        "goal":
        "Increase sales by 30%"
    }
)

print("\nPLAN\n")
print(result["plan"])

print("\nFINAL REPORT\n")
print(result["advisor_report"])