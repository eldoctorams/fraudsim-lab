from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
import hashlib
import random


@dataclass(frozen=True)
class ForgeConfig:
    events: int = 250
    fraud_rate: float = 0.08
    seed: int = 42
    scenario: str = "account-takeover"

    def validate(self) -> None:
        if self.events < 10:
            raise ValueError("events must be at least 10")
        if not 0 <= self.fraud_rate <= 1:
            raise ValueError("fraud_rate must be between 0 and 1")
        if self.scenario not in {"account-takeover", "mule-network", "card-abuse"}:
            raise ValueError("unsupported scenario")


def _event_id(seed: int, index: int) -> str:
    return hashlib.sha256(f"maat:{seed}:{index}".encode()).hexdigest()[:16]


def forge_campaign(config: ForgeConfig) -> dict:
    """Generate a deterministic, labeled campaign with ground-truth lineage."""
    config.validate()
    rng = random.Random(config.seed)
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    fraud_indices = set(rng.sample(range(config.events), round(config.events * config.fraud_rate)))
    actors = [f"ACC-{i:04d}" for i in range(max(12, config.events // 8))]
    devices = [f"DEV-{i:03d}" for i in range(max(6, config.events // 20))]
    mules = actors[-max(3, len(actors) // 10):]
    rows = []

    for index in range(config.events):
        fraudulent = index in fraud_indices
        account = rng.choice(actors)
        device = rng.choice(devices)
        amount = round(rng.lognormvariate(3.4, 0.8), 2)
        channel = rng.choice(["mobile", "web", "card"])
        reason = "baseline-activity"

        if fraudulent:
            if config.scenario == "account-takeover":
                device = "DEV-NEW-ATO"
                amount = round(amount * 8 + 250, 2)
                channel, reason = "mobile", "new-device-velocity"
            elif config.scenario == "mule-network":
                account = rng.choice(mules)
                amount = round(amount * 5 + 120, 2)
                reason = "fan-in-mule-convergence"
            else:
                channel = "card"
                amount = round(amount * 4 + 80, 2)
                reason = "merchant-burst-card-abuse"

        rows.append({
            "event_id": _event_id(config.seed, index),
            "timestamp": (start + timedelta(minutes=index * 7)).isoformat(),
            "account_id": account,
            "device_id": device,
            "channel": channel,
            "amount": amount,
            "is_fraud": fraudulent,
            "scenario": config.scenario if fraudulent else "legitimate",
            "ground_truth_reason": reason,
        })

    total_amount = round(sum(row["amount"] for row in rows), 2)
    fraud_count = sum(row["is_fraud"] for row in rows)
    digest = hashlib.sha256(repr(rows).encode()).hexdigest()
    return {
        "manifest": {
            "engine": "MAAT FORGE",
            "version": "0.1.0",
            "config": asdict(config),
            "dataset_sha256": digest,
            "synthetic_only": True,
        },
        "metrics": {
            "events": len(rows),
            "fraud_events": fraud_count,
            "realized_fraud_rate": round(fraud_count / len(rows), 4),
            "total_amount": total_amount,
        },
        "events": rows,
    }
