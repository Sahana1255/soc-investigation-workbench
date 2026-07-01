from services.soc_engine import SOCEngine

engine = SOCEngine()

result = engine.investigate(
    title="Windows Investigation",
    evidence_files=[
        "data/sample_logs/Security.evtx"
    ]
)

print("=" * 50)
print("Incident:", result["incident"].title)
print("Events:", len(result["incident"].events))
print("IOCs:", len(result["incident"].iocs))
print("=" * 50)