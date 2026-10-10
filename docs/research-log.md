# Research and Implementation Log

## Project Title
**git **

## Development Environment

- Host operating system: Windows 11
- Linux environment: Ubuntu 24.04.5 LTS under WSL2
- IDE: Visual Studio Code connected to WSL
- Container platform: Docker 29.0.1
- Container orchestration: Docker Compose v2.40.3
- Available host memory: approximately 11.8 GB
- Configured WSL memory limit: 7 GB
- Configured WSL processors: 4
- Initial Ubuntu filesystem report: approximately 952 GB available
- Project directory: `/home/ah076/decentralized-ips`

## Research Objective

The project aims to develop a modular intrusion prevention system that combines network intrusion detection, machine-learning-based attack classification, deterministic prevention-rule generation, propagation of validated rules to connected nodes, and blockchain-based auditing.

The initial implementation will use a controlled Docker lab. Later stages will investigate detection of previously unseen attacks and deployment across multiple physical machines.

## Progress Record

### Step 1 — Environment Verification

**Status:** Completed.

Ubuntu 24.04.5 LTS was verified under WSL2. Docker and Docker Compose were available, and a test container ran successfully using the `hello-world` image.

The Ubuntu filesystem reported approximately 952 GB available. The Ubuntu virtual disk was located under the Windows user's local WSL storage directory.

### Step 2 — Project Structure

**Status:** Completed.

A modular directory structure was created for container definitions, application services, machine-learning workflows, blockchain components, configuration, scripts, tests, and documentation.

The project is stored in the Ubuntu Linux filesystem at `/home/ah076/decentralized-ips`.

### Step 3 — Resource Configuration and Development Tools

**Status:** Completed.

WSL was configured with a 7 GB memory limit and four processors. Subsequent verification reported approximately 6.8 GiB of visible memory and four processors.

Visual Studio Code was connected to the Ubuntu environment, and the Linux Git executable was verified.

### Step 4 — Version Control and Research Log

**Status:** In progress.

Git repository initialization and creation of this research log are the current tasks.

## Planned Experimental Methodology

1. Prepare and clean CIC-IDS2017 flow CSV files.
2. Train and evaluate a Random Forest classifier.
3. Capture controlled normal and attack traffic in the Docker lab.
4. Configure Suricata to detect the initial attack.
5. Compare Suricata alerts with machine-learning classifications.
6. Introduce a deterministic decision service and validated prevention rules.
7. Test propagation of rules to multiple lab nodes.
8. Integrate Hyperledger Fabric for auditable records.
9. Evaluate detection and prevention performance on both the public dataset and lab-generated traffic.
10. Extend the system to additional attack categories and unknown-attack anomaly detection.

## Experimental Reporting Rules

- Record actual measurements rather than planned or estimated outcomes.
- Report accuracy, precision, and recall for each evaluated dataset.
- Record false positives, false negatives, and prevention latency when measured.
- Document dataset limitations and differences between public and laboratory traffic.
- Do not claim that blockchain consensus, decentralized propagation, or unknown-attack detection works until corresponding tests pass.

## Results

No attack-detection or machine-learning performance results have been collected yet.


## steps
This preparation stage establishes the reproducible development environment and modular project structure. The system is designed to separate detection, classification, decision-making, prevention, synchronization, and audit logging into independent components. Experimental performance remains unmeasured at this stage.

Completed: The project has a Git repository for source-code history. The research log will document implementation decisions, test conditions, and measured results throughout development. No model training or attack-detection experiments have been performed yet.

Preparation milestone: The project now has a Linux-based development environment, Docker support, version control on the main branch, and a dedicated documentation directory. The project structure separates machine learning, detection, decision-making, rule enforcement, synchronization, and blockchain auditing.
No attack detection or model performance results have been claimed yet.

Preparation is complete. The development environment, version-control repository, project structure, and research log are established. The next stage will prepare the CIC-IDS2017 flow data for Random Forest training, with memory-conscious preprocessing suitable for the laptop.

Part 1 preparation: The project will separate active computation from archival storage. Dataset archives, raw packet captures, and backups will be stored on the external SSD, while application code, Docker data, and active blockchain data remain on internal storage.

The development environment and storage inventory are documented. The external dataset and backup location remains pending verification; no dataset has been downloaded and no experiment has started.

Storage verification status: pending. The host exposes an NVMe disk and a separate 1 TB disk. The intended external SSD has not yet been positively identified, so dataset and backup directories will not be assigned to a drive until its identity and capacity are confirmed.

Storage identification: Windows detects the external device as Cablet MD202 over USB. The drive's capacity, filesystem, available space, and WSL mount path remain unverified.

Storage identification: The external USB device is confirmed as a 240,057,409,536-byte disk with a primary NTFS partition assigned to F:. Its volume label suggests possible Windows installation media, so its contents and available space must be verified before assigning it as the archival destination.

The external SSD has approximately 130.3 GB free, sufficient in principle for dataset archives and backups. Its existing contents must be preserved, and Linux access has not yet been established. No data has been written to the external drive.

## Environment Update — Internal Storage

- **Decision:** Keep active project development and dataset preparation on the internal Linux filesystem.
- **Project location:** `/home/ah076/decentralized-ips`
- **Storage verification:** Ubuntu reports 951 GB available on `/`.
- **External SSD:** Optional only; the project must remain usable when it is disconnected.
- **Rationale:** Avoid runtime and development dependencies on removable storage.
- **Status:** Storage verified; dataset download has not started.

## Dataset Preparation Plan — CIC-IDS2017

- **Source:** Canadian Institute for Cybersecurity, University of New Brunswick.
- **Official page:** https://www.unb.ca/cic/datasets/ids-2017.html
- **Initial dataset:** Machine-learning flow CSV archive only.
- **Raw PCAP files:** Deferred until a specific experiment requires them.
- **Storage:** Internal Linux filesystem under `data/cicids2017/`.
- **Planned model:** Random Forest for supervised benign-versus-attack classification.
- **Current status:** Dataset not yet downloaded; no training or evaluation results exist.
