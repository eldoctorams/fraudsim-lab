# Reference projects and clean-room decisions

| Project | Useful pattern | MAAT FORGE decision |
|---|---|---|
| [IBM AMLSim](https://github.com/IBM/AMLSim) | Synthetic transaction networks and laundering patterns | Generate coherent actors and campaign lineage, not isolated rows |
| [SynthCity](https://github.com/vanderschaarlab/synthcity) | Extensible synthetic-data plugins and evaluation | Keep scenario engines modular and measurement-driven |
| [SDV](https://github.com/sdv-dev/SDV) | Multi-table synthetic data workflows | Preserve referential coherence across account/device/event records |
| [Fraud Detection Handbook](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook) | Reproducible fraud evaluation | Couple each dataset with seed, manifest and ground truth |

These projects were studied as references. No source code, assets or model weights are copied or bundled. MAAT FORGE is an independent MIT-licensed implementation.
