
# Decentralized, Self-Learning Intrusion Prevention System

A research-oriented cybersecurity project combining network intrusion detection, machine learning, controlled prevention, and blockchain-based security auditing.

**Project status:** Development in progress.

The project aims to detect suspicious network activity, classify attacks using machine learning, evaluate prevention decisions, and maintain an auditable record of security events. The system is intended to be developed and evaluated in an isolated laboratory environment.

> The architecture described below is the planned design. Individual components will be marked as implemented only after their functionality has been tested.

## 1. Project Overview

Traditional intrusion detection systems identify suspicious traffic, while intrusion prevention systems can take additional action to restrict malicious activity. This project explores how machine learning, controlled enforcement, and decentralized audit logging can be combined in a reproducible experimental environment.

The initial research uses the CIC-IDS2017 dataset to investigate binary network-traffic classification and generalization across attack families.

The project will progressively integrate network monitoring, an ML inference service, a decision service, a validated rule engine, and Hyperledger Fabric for security-event auditing.

## 2. Objectives

- Detect suspicious network traffic using network monitoring tools.
- Train and evaluate machine-learning models for attack classification.
- Explore anomaly detection for potentially unfamiliar attacks.
- Evaluate predictions through a controlled decision service.
- Apply validated prevention rules through a controlled enforcement component.
- Record security events and prevention outcomes in Hyperledger Fabric.
- Evaluate detection performance, false positives, false negatives, processing time, and system overhead.
- Document experimental limitations and make evaluation procedures reproducible.

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
     Hyperledger Fabric
```

This is the target architecture, not a representation of a fully operational system.

The intended responsibilities are:

| Component | Responsibility |
|---|---|
| Suricata | Monitor network traffic and generate security events |
| ML service | Classify supported traffic records and return predictions |
| Decision service | Evaluate predictions and apply decision policies |
| Rule engine | Validate proposed prevention actions |
| Enforcement layer | Apply approved actions in the isolated lab |
| Hyperledger Fabric | Maintain an auditable record of selected events and decisions |

## 4. Technology Stack

| Component | Technology |
|---|---|
| Development environment | Ubuntu 24.04 on WSL2 |
| Containerization | Docker and Docker Compose |
| Network monitoring | Suricata |
| ML implementation | Python, pandas, NumPy, scikit-learn |
| Initial classifier | Random Forest |
| Planned anomaly detection | Isolation Forest |
| Initial dataset | CIC-IDS2017 |
| Planned blockchain audit | Hyperledger Fabric |
| Version control | Git and GitHub |

Additional components may be introduced as implementation requirements become clearer.

## 5. Current Research Progress

### Dataset

The CIC-IDS2017 CSV archive has been downloaded, integrity-checked, and extracted. Initial preprocessing and label-distribution analysis have been performed.

The processed dataset contains approximately 2.83 million rows across eight capture files.

### Machine learning

An initial binary Random Forest baseline has been trained and evaluated. Further experiments investigate capture-separated evaluation and attack-family generalization.

An important preliminary finding is that the capture-holdout model performed poorly on the held-out Thursday Morning WebAttacks capture. It detected only 5 of 2,180 attack records in that evaluation.

This result is a limitation of the current experimental baseline, not evidence that the complete proposed IPS is effective or ineffective. Additional controlled experiments are required.

### Evaluation methodology

The research investigates:

- Binary classification metrics.
- Per-family precision, recall, and F1-score.
- False-positive and false-negative behavior.
- Feature distributions across captures.
- Duplicate feature vectors and inconsistent labels.
- Data leakage risks and generalization limitations.

The experimental reports and research decisions are documented in `docs/research-log.md`.

## 6. Repository Structure

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

Directories represent the project organization and planned components; their presence does not imply that every component has been implemented.

## 7. Development Environment

The project is developed using Ubuntu 24.04 under WSL2, with Docker Desktop providing container support.

### Clone the repository

```bash
git clone https://github.com/Ak7865/immunet-ips.git
cd immunet-ips
```

### Create a Python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

Install dependencies from the project's dependency files when available. If no dependency file exists for a component, establish and document its dependencies before installing them.

Avoid installing project dependencies globally.

## 8. Dataset

The initial dataset is **CIC-IDS2017**, used for supervised network intrusion classification.

The dataset contains benign traffic and multiple attack families recorded in different network captures.

Dataset files are stored locally under `data/` and are excluded from Git. They are not bundled with this repository.

Preprocessing, class-distribution analysis, training/test separation, model training, and evaluation are documented as the research progresses.

## 9. Security and Testing Scope

All attack simulations and prevention experiments must remain inside the isolated project laboratory.

- Generate attack traffic only against systems owned by the project or explicitly authorized for testing.
- Do not target public IP addresses, third-party systems, or production networks.
- Validate proposed prevention rules before applying them.
- Use controlled, reversible enforcement actions in the laboratory.
- Keep credentials and API keys in local environment files; never commit secrets.
- Treat ML predictions as inputs to a controlled decision process, not as unquestionable instructions.
- Record test conditions, limitations, and relevant configuration changes.

## 10. Development Roadmap

- [x] Establish the development environment and Git repository.
- [x] Download and extract the CIC-IDS2017 CSV archive.
- [x] Perform initial CSV schema and sample inspection.
- [x] Establish an initial binary Random Forest baseline.
- [x] Evaluate the initial model on a capture-held-out dataset.
- [x] Investigate attack-family performance and duplicate feature vectors.
- [ ] Finalize reproducible preprocessing and grouped evaluation.
- [ ] Investigate and improve attack-family generalization.
- [ ] Integrate Suricata with the ML service.
- [ ] Implement the decision service and validated prevention workflow.
- [ ] Test detection and prevention in the isolated container laboratory.
- [ ] Integrate Hyperledger Fabric for security-event auditing.
- [ ] Evaluate end-to-end performance, overhead, and limitations.

Checklist items should be updated only after the corresponding milestone has been verified.

## 11. Research Documentation

Development decisions, environment changes, dataset handling, experiments, evaluation results, and limitations are recorded in [`docs/research-log.md`](docs/research-log.md).

## 12. License and Dataset Attribution

A license for this project has not yet been selected.

Before redistributing the project, select an appropriate software license and verify the dataset provider's applicable terms, attribution requirements, and redistribution restrictions.

The CIC-IDS2017 dataset is associated with the Canadian Institute for Cybersecurity at the University of New Brunswick. Consult the original provider's documentation for dataset information and usage requirements.
