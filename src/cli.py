import argparse
from pathlib import Path
from .engine import assess
from .ingest import load_case, load_events
from .reporting import to_markdown


def main() -> int:
    parser = argparse.ArgumentParser(description="Assess a synthetic incident-response case")
    parser.add_argument("--case", required=True)
    parser.add_argument("--events", required=True)
    parser.add_argument("--output", default="reports/generated-assessment.md")
    args = parser.parse_args()

    assessment = assess(load_case(args.case), load_events(args.events))
    report = to_markdown(assessment)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(f"case={assessment.case.case_id} score={assessment.risk_score} findings={len(assessment.findings)} containment_ready={assessment.containment_ready}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
