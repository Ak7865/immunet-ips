# Decentralized, Self-Learning Intrusion Prevention System

A research-oriented cybersecurity project that combines network intrusion detection, machine learning, automated prevention, and blockchain-based audit logging.

## 1. Project Overview

This project aims to develop a decentralized Intrusion Prevention System (IPS) that detects suspicious network activity, classifies known attacks using machine learning, evaluates prevention decisions, and records security events in a blockchain-based audit trail.

The system is intended to be developed and evaluated in an isolated laboratory environment using containerized services.

**Project status:** Development in progress. The architecture and implementation roadmap are being established. Features will be marked as implemented only after testing.

## 2. Objectives

- Detect suspicious network traffic using network monitoring tools.
- Train and evaluate machine-learning models for network attack classification.
- Explore anomaly detection for potentially unknown attacks.
- Evaluate detection results using a decision service.
- Apply validated prevention rules through a controlled rule engine.
- Record security events and prevention outcomes in a Hyperledger Fabric ledger.
- Evaluate detection performance, false positives, processing time, and system overhead.

## 3. Planned Architecture

```text
Attacker Container
        |
        v
Victim Web Application
        |
        v
Network Monitoring (Suricata)
        |
        v
Machine-Learning Service
        |
        v
Decision Service
        |
        v
Validated Rule Engine
        |
        v
Prevention / Enforcement

Security Events and Decisions
        |
        v
Blockchain Audit Layer
(Hyperledger Fabric)
```

This diagram represents the planned architecture, not a claim that every component is already operational.

## 4. Technology Stack

| Component | Planned Technology |
|---|---|
| Development environment | Ubuntu 24.04 on WSL2 |
| Containerization | Docker and Docker Compose |
| Network monitoring | Suricata |
| Machine learning | Python, pandas, NumPy, scikit-learn |
| Initial classifier | Random Forest |
| Anomaly detection | Isolation Forest |
| Initial dataset | CIC-IDS2017 |
| Blockchain audit layer | Hyperledger Fabric |
| Version control | Git and GitHub |

Additional components may be introduced as the implementation and evaluation progress.

## 5. Repository Structure

```text
decentralized-ips/
├── blockchain/
│   ├── chaincode/
│   ├── client/
│   └── network/
├── config/
├── docker/
│   ├── attacker/
│   ├── compose/
│   ├── suricata/
│   └── victim-web/
├── docs/
│   └── research-log.md
├── ml/
│   ├── evaluation/
│   ├── models/
│   ├── preprocessing/
│   └── training/
├── scripts/
├── services/
│   ├── decision-service/
│   ├── ml-service/
│   ├── rule-engine/
│   └── sync-agent/
├── tests/
├── .gitignore
└── README.md
```

The repository may evolve as implementation requirements become clearer.

## 6. Development Environment

The project is developed on Ubuntu 24.04 under WSL2, with Docker Desktop providing container support.

Clone the repository:

```bash
git clone https://github.com/Ak7865/immunet-ips.git
cd immunet-ips
```

Create and activate a Python virtual environment for machine-learning development:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies when the project's dependency files are established. Avoid installing packages globally.

## 7. Dataset

The initial dataset is **CIC-IDS2017**, intended for supervised network intrusion classification.

Dataset files are stored locally under `data/` and are excluded from Git. The dataset is not bundled with this repository.

Preprocessing, class-distribution analysis, train/test separation, model training, and evaluation will be documented as they are completed.

## 8. Security and Testing Scope

- Generate attack traffic only inside the isolated project lab.
- Do not target public IP addresses, third-party systems, or production networks.
- Validate prevention rules before applying them.
- Keep API keys and credentials in local environment files; never commit secrets.
- Treat model predictions as inputs to a controlled decision process, not as unquestionable instructions.
- Record test conditions and limitations so experimental results can be reproduced.

## 9. Development Roadmap

- [x] Establish the development environment and Git repository.
- [x] Download and extract the initial CIC-IDS2017 CSV archive.
- [x] Perform initial CSV schema and sample inspection.
- [ ] Build reproducible dataset preprocessing.
- [ ] Train and evaluate the initial Random Forest classifier.
- [ ] Integrate Suricata with the machine-learning service.
- [ ] Implement the decision service and validated prevention-rule workflow.
- [ ] Test detection and prevention in the isolated container lab.
- [ ] Integrate Hyperledger Fabric for security-event auditing.
- [ ] Evaluate performance, limitations, and reproducibility.

Checklist items indicate project milestones and should be updated only when their completion has been verified.

## 10. Research Documentation

Development decisions, environment changes, dataset handling, experiments, and evaluation results are recorded in [`docs/research-log.md`](docs/research-log.md).

## 11. License and Dataset Attribution

A license for this project has not yet been selected. Dataset use and redistribution must follow the original dataset provider's terms and attribution requirements.