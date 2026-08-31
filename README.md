# FraudSim Lab

> Privacy-safe synthetic fraud scenarios for testing detection systems.

[![Status: Design](https://img.shields.io/badge/status-design--phase-f59e0b)](#project-status)
[![License: MIT](https://img.shields.io/badge/license-MIT-0ea5e9)](LICENSE)
[![Data: Synthetic](https://img.shields.io/badge/data-synthetic%20only-22c55e)](SECURITY.md)

FraudSim Lab will generate explainable, labeled fraud scenarios for rules engines, graph analytics and machine-learning models—without exposing customer data.

## Why this matters

Fraud teams struggle with rare labels, privacy restrictions, concept drift and unrealistic toy datasets. A useful simulator must generate not just rows, but coherent actors, devices, merchants, accounts, transactions and attack campaigns over time.

## Planned capabilities

- Scenario packs for account takeover, mule networks, card-not-present abuse, invoice fraud and laundering typologies.
- Tabular, temporal and graph outputs with configurable class imbalance.
- Ground-truth event lineage and reason codes for every generated label.
- Baseline rules and models with precision-recall, calibration and cost-sensitive metrics.
- Drift, adversarial adaptation and analyst-capacity simulation.
- Reproducible seeds, dataset cards and privacy/safety guardrails.

## Differentiator

FraudSim Lab will connect **scenario generation → ground truth → detection benchmark → explanation**. Users should be able to change an attacker behavior, regenerate data and see exactly which detectors fail and why.

## Project status

**Design phase.** Current materials define the product and MVP; no validated dataset or performance claim is made yet.

## First release target

```bash
fraudsim generate --scenario account-takeover --events 100000 --seed 42
fraudsim benchmark ./output/events.parquet
```

The alpha will ship one end-to-end scenario, Parquet/CSV export, graph edges, dataset card and simple rule/model baselines.

## Documentation

- [Roadmap](ROADMAP.md)
- [Reference projects and gap analysis](docs/REFERENCE_PROJECTS.md)
- [Contributing](CONTRIBUTING.md)
- [Security and synthetic-data policy](SECURITY.md)

## Author

**Dr. Ahmed Mohamed El Sayed** — OSINT, digital forensics, cybercrime investigation and AI-powered investigation systems.

[Website](https://drahmedelsayed.com/) · [LinkedIn](https://www.linkedin.com/in/eldoctorams/) · [GitHub](https://github.com/eldoctorams)

## License

MIT. Synthetic data must not be represented as real-world evidence.
