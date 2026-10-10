**# Research and Implementation Log**



**## Project Title**

**\*\*Decentralized, Self-Learning Intrusion Prevention System\*\***



**## Development Environment**



\- Host operating system: Windows 11

\- Linux environment: Ubuntu 24.04.5 LTS under WSL2

\- IDE: Visual Studio Code connected to WSL

\- Container platform: Docker 29.0.1

\- Container orchestration: Docker Compose v2.40.3

\- Available host memory: approximately 11.8 GB

\- Configured WSL memory limit: 7 GB

\- Configured WSL processors: 4

\- Initial Ubuntu filesystem report: approximately 952 GB available

\- Project directory: \`/home/ah076/decentralized-ips\`



**## Research Objective**



The project aims to develop a modular intrusion prevention system that combines network intrusion detection, machine-learning-based attack classification, deterministic prevention-rule generation, propagation of validated rules to connected nodes, and blockchain-based auditing.



The initial implementation will use a controlled Docker lab. Later stages will investigate detection of previously unseen attacks and deployment across multiple physical machines.



**## Progress Record**



**### Step 1 — Environment Verification**



**\*\*Status:\*\*** Completed.



Ubuntu 24.04.5 LTS was verified under WSL2. Docker and Docker Compose were available, and a test container ran successfully using the \`hello-world\` image.



The Ubuntu filesystem reported approximately 952 GB available. The Ubuntu virtual disk was located under the Windows user's local WSL storage directory.



**### Step 2 — Project Structure**



**\*\*Status:\*\*** Completed.



A modular directory structure was created for container definitions, application services, machine-learning workflows, blockchain components, configuration, scripts, tests, and documentation.



The project is stored in the Ubuntu Linux filesystem at \`/home/ah076/decentralized-ips\`.



**### Step 3 — Resource Configuration and Development Tools**



**\*\*Status:\*\*** Completed.



WSL was configured with a 7 GB memory limit and four processors. Subsequent verification reported approximately 6.8 GiB of visible memory and four processors.



Visual Studio Code was connected to the Ubuntu environment, and the Linux Git executable was verified.



**### Step 4 — Version Control and Research Log**



**\*\*Status:\*\*** In progress.



Git repository initialization and creation of this research log are the current tasks.



**## Planned Experimental Methodology**



1\. Prepare and clean CIC-IDS2017 flow CSV files.

2\. Train and evaluate a Random Forest classifier.

3\. Capture controlled normal and attack traffic in the Docker lab.

4\. Configure Suricata to detect the initial attack.

5\. Compare Suricata alerts with machine-learning classifications.

6\. Introduce a deterministic decision service and validated prevention rules.

7\. Test propagation of rules to multiple lab nodes.

8\. Integrate Hyperledger Fabric for auditable records.

9\. Evaluate detection and prevention performance on both the public dataset and lab-generated traffic.

10\. Extend the system to additional attack categories and unknown-attack anomaly detection.



**## Experimental Reporting Rules**



\- Record actual measurements rather than planned or estimated outcomes.

\- Report accuracy, precision, and recall for each evaluated dataset.

\- Record false positives, false negatives, and prevention latency when measured.

\- Document dataset limitations and differences between public and laboratory traffic.

\- Do not claim that blockchain consensus, decentralized propagation, or unknown-attack detection works until corresponding tests pass.



**## Results**



No attack-detection or machine-learning performance results have been collected yet.





**## steps**

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



**## Environment Update — Internal Storage**



\- **\*\*Decision:\*\*** Keep active project development and dataset preparation on the internal Linux filesystem.

\- **\*\*Project location:\*\*** \`/home/ah076/decentralized-ips\`

\- **\*\*Storage verification:\*\*** Ubuntu reports 951 GB available on \`/\`.

\- **\*\*External SSD:\*\*** Optional only; the project must remain usable when it is disconnected.

\- **\*\*Rationale:\*\*** Avoid runtime and development dependencies on removable storage.

\- **\*\*Status:\*\*** Storage verified; dataset download has not started.



**## Dataset Preparation Plan — CIC-IDS2017**



\- **\*\*Source:\*\*** Canadian Institute for Cybersecurity, University of New Brunswick.

\- **\*\*Official page:\*\*** https\://www\.unb.ca/cic/datasets/ids-2017.html

\- **\*\*Initial dataset:\*\*** Machine-learning flow CSV archive only.

\- **\*\*Raw PCAP files:\*\*** Deferred until a specific experiment requires them.

\- **\*\*Storage:\*\*** Internal Linux filesystem under \`data/cicids2017/\`.

\- **\*\*Planned model:\*\*** Random Forest for supervised benign-versus-attack classification.

\- **\*\*Current status:\*\*** Dataset not yet downloaded; no training or evaluation results exist.



**## Dataset Download — Integrity Verification**



\- **\*\*Dataset:\*\*** CIC-IDS2017 MachineLearningCSV.zip

\- **\*\*Source:\*\*** Official CIC dataset browser at https\://cicresearch.ca/CICDataset/CIC-IDS-2017/

\- **\*\*Archive size:\*\*** Approximately 225 MB

\- **\*\*Integrity check:\*\*** Passed; copied archive is byte-for-byte identical to the downloaded archive.

\- **\*\*Expected and calculated MD5:\*\*** 4f83860afbf29cac8163854095bf6cf7

\- **\*\*Checksum-file caveat:\*\*** The supplied MD5 file references MachineLearningCVE.zip; the matching hash was verified explicitly against MachineLearningCSV.zip.

\- **\*\*Storage:\*\*** Internal Linux filesystem, under data/cicids2017/raw/.

\- **\*\*Current status:\*\*** Archive verified and copied; extraction, preprocessing, model training, and evaluation have not started.



**## Dataset Extraction — CIC-IDS2017**



\- **\*\*Archive:\*\*** MachineLearningCSV.zip

\- **\*\*Extracted directory:\*\*** data/cicids2017/raw/MachineLearningCVE/

\- **\*\*CSV files extracted:\*\*** 8

\- **\*\*Reported extracted size:\*\*** 844 MiB

\- **\*\*Extraction status:\*\*** Completed without visible errors.

\- **\*\*Integrity status:\*\*** Archive MD5 was verified before extraction; individual extracted CSV contents have not yet been independently validated.

\- **\*\*Current status:\*\*** Dataset extracted; schema inspection and preprocessing have not started.





**## ML Environment and Initial Schema Inspection**



\- **\*\*Python:\*\*** 3.12.3 in the project virtual environment \`.venv\`.

\- **\*\*Installed libraries:\*\*** pandas 3.0.6, NumPy 2.5.3, scikit-learn 1.9.1.

\- **\*\*CSV files inspected:\*\*** 8.

\- **\*\*Observed schema:\*\*** 79 columns per file, with a \`Label\` column.

\- **\*\*Inspection method:\*\*** At most 5,000 rows sampled per CSV using Python CSV streaming.

\- **\*\*Sample integrity:\*\*** No malformed-width rows observed in the inspected samples; this does not establish full-file integrity.

\- **\*\*Sample labels:\*\*** Most sampled rows were BENIGN; the Friday PortScan sample contained 7 PortScan rows among its first 5,000 rows.

\- **\*\*Data-cleaning consideration:\*\*** Column names contain inconsistent spacing and will require normalization.

\- **\*\*Current status:\*\*** Dependencies installed and initial schema inspection complete; full preprocessing, training, and evaluation have not started.


---

## CIC-IDS2017 Full Audit and Preprocessing

**Status: Preprocessing completed; output validation and model preparation are the next tasks.**

### Input dataset and audit

- **Dataset:** CIC-IDS2017 `MachineLearningCSV.zip`, extracted to `data/cicids2017/raw/MachineLearningCVE/`.
- **CSV files audited:** 8.
- **Total records read:** 2,830,743.
- **Original schema:** 79 columns per CSV, including the label column.
- **Label column:** `Label` (the source header contained leading whitespace in some files).
- **Full-file structure audit:** No malformed-width rows or missing labels were found in the audit.
- **Duplicate feature:** `Fwd Header Length` occurred twice, at original column indices 34 and 55. A full comparison found the two columns identical across all 2,830,743 rows. The duplicate at index 55 was removed.
- **Output schema:** 78 columns per CSV: 77 features plus one `Label` column.
- **Column names:** Leading/trailing and repeated whitespace was normalized.

### Label normalization and numeric cleanup

- Three source labels in the Web Attacks CSV contained the Unicode replacement character (`\ufffd`). The preprocessing script maps them to `Web Attack Brute Force`, `Web Attack Sql Injection`, and `Web Attack XSS`.
- Positive and negative infinity values in feature columns were replaced with missing values (`NaN`).
- Feature columns were converted to numeric values; the preprocessing run completed without conversion errors.
- **Total missing feature values after infinity handling:** 5,734.
- Missing feature values by input file:
  - Friday DDoS: 68
  - Friday PortScan: 742
  - Friday Morning: 244
  - Monday: 874
  - Thursday Infiltration: 414
  - Thursday Web Attacks: 270
  - Tuesday: 528
  - Wednesday: 2,594
- **Processed outputs:** `data/cicids2017/processed/cleaned_*.csv`, with a local `preprocessing_report.txt`.
- Raw CSV files were not modified. The dataset directory is excluded from Git, so the large raw and processed data files are not committed.

### Important class imbalance

The full audit found very rare classes, including Heartbleed (11 rows), SQL Injection (21 rows), and Infiltration (36 rows). These counts make an unexamined stratified split or per-class performance claim risky. The split design and metrics must explicitly account for rare classes.

### Current limitations and next steps

- The preprocessing script has not performed missing-value imputation.
- No train/test split has been finalized.
- No Random Forest model has been trained or evaluated.
- No model-performance claims are made at this stage.
- Before model training, validate the processed CSV schemas, row counts, labels, and remaining missing/non-finite values. Then design a leakage-aware split and fit imputation only on training data.

## Processed Dataset Validation

**Status: Completed.**

The validation script `ml/preprocessing/validate_processed_dataset.py` checked all eight processed CIC-IDS2017 CSV files using chunked reading.

- **Total records:** 2,830,743; matched the audited source counts.
- **Schema:** 78 columns per file, comprising 77 features and one `Label` column.
- **Missing feature values:** 5,734.
- **Infinite feature values:** 0.
- **Missing labels:** 0.
- **Labels containing the Unicode replacement character:** 0.
- **Label distributions:** Inspected for all eight files.
- **Validation outcome:** PASS.

The processed files retain missing feature values; imputation has not been applied. No train/test split, model training, or model evaluation has been performed.

**Next step:** Design a leakage-aware evaluation split, accounting for the severe class imbalance and rare attack categories in CIC-IDS2017. Fit preprocessing transformations using training data only and evaluate on held-out data.

