import argparse
import csv
import json
from pathlib import Path

from .engine import ForgeConfig, forge_campaign


def main() -> None:
    parser = argparse.ArgumentParser(prog="maat", description="Forge explainable synthetic fraud campaigns")
    parser.add_argument("--scenario", default="account-takeover", choices=["account-takeover", "mule-network", "card-abuse"])
    parser.add_argument("--events", type=int, default=250)
    parser.add_argument("--fraud-rate", type=float, default=0.08)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", default="maat-output")
    args = parser.parse_args()
    result = forge_campaign(ForgeConfig(args.events, args.fraud_rate, args.seed, args.scenario))
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    (output / "manifest.json").write_text(json.dumps({"manifest": result["manifest"], "metrics": result["metrics"]}, indent=2), encoding="utf-8")
    with (output / "events.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=result["events"][0])
        writer.writeheader()
        writer.writerows(result["events"])
    print(json.dumps(result["metrics"], indent=2))


if __name__ == "__main__":
    main()
