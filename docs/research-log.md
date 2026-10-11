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

## Baseline Random Forest Evaluation and Diagnostic Analysis

### Experimental Setup

The CIC-IDS2017 dataset was used to develop an initial binary classification baseline for the proposed decentralized intrusion prevention system. The processed dataset contained 2,830,743 flow records, with 77 numerical features and one target label per record. The original multiclass labels were mapped to two classes: BENIGN and ATTACK, where every non-BENIGN, non-missing label was assigned to ATTACK.

A capture-day holdout strategy was used. Monday through Thursday captures were assigned to the training partition, while the three Friday captures were reserved for evaluation. A fixed-seed sample of 300,000 records was selected from the training partition. Median imputation was fitted using the training sample only.

The baseline classifier was a Random Forest with 100 trees, a maximum depth of 20, a minimum of two samples per leaf, and random seed 42. The model was implemented using a scikit-learn pipeline containing median imputation and classification.

### Baseline Results

Evaluation on the 703,245 Friday records produced an accuracy of 70.46%. The ATTACK class achieved a precision of 99.72%, recall of 28.18%, and F1-score of 0.4394.

The confusion matrix contained 414,094 true negatives, 228 false positives, 207,518 false negatives, and 81,405 true positives. Consequently, the model missed a substantial proportion of attack records despite producing few false-positive predictions.

These results indicate that the baseline is insufficient to demonstrate effective intrusion prevention. High attack precision alone is not evidence of effective prevention when attack recall is low.

### Capture-Level Diagnostic Evaluation

Separate evaluations of the Friday morning, DDoS, and PortScan captures revealed substantial differences in performance. The model failed to identify the sampled Bot attack family and detected only approximately 0.10% of PortScan attacks in the earlier capture-level evaluation. DDoS attack recall was approximately 63.46%.

The results suggest that aggregate metrics conceal important differences between traffic captures and attack families. Potential explanations include differences in traffic-feature distributions and the absence of some attack families from the training captures. These explanations remain hypotheses and require further controlled experiments.

### Feature Distribution Analysis

A diagnostic analysis compared selected feature distributions between Monday–Thursday training captures and Friday diagnostic captures. Differences were observed in features including Destination Port, backward packet length statistics, packet-length variance, forward inter-arrival-time variability, maximum flow inter-arrival time, and initial forward TCP window size.

The analysis used sampled records and summary statistics, including medians and quartiles. The observed differences establish distributional differences within the examined samples but do not establish causation or identify a single reason for classification errors. Feature importance values are model-dependent and should not be interpreted as causal evidence.

### Limitations and Next Steps

Friday has already been examined during baseline evaluation and diagnostic analysis. It must therefore not be described as an untouched final test set after subsequent model selection or threshold tuning.

The next experiment will establish a separate, reproducible validation procedure using the Monday–Thursday data. The validation design will document partition membership, random seed, class counts, and preprocessing boundaries. Imputation and model fitting must use training data only.

Random row-level validation will be interpreted as an estimate of performance on similar traffic, not as proof of generalization to unseen capture days or attack families. Generalization to unseen attack families and the effectiveness of actual prevention actions require separate evaluation.

No claim of successful distributed rule propagation, blockchain auditing, or real-time attack prevention is made on the basis of these classifier results.

### Validation Protocol Design

A separate validation experiment is planned using the Monday–Thursday portion of CIC-IDS2017. The purpose is to support reproducible model comparison without using the previously examined Friday captures for model selection.

The proposed experiment will use a stratified 80:20 random row-level split with a fixed random seed. Stratification will preserve the approximate proportions of the BENIGN and ATTACK classes across the training and validation partitions. The validation manifest will record the split configuration, partition sizes, class counts, and source files.

This protocol is intended to estimate performance on traffic drawn from the same capture collection. Since records from an individual capture may occur in both partitions, the results will not establish generalization to unseen capture days or attack families. The previously examined Friday data will remain diagnostic data and will not be used to select model settings or classification thresholds.

This section describes the planned protocol. The split has not yet been generated or validated, and no validation metrics are available at this stage.

### Validation Manifest Implementation

The next implementation task is to create a separate script for generating a reproducible validation manifest from the Monday–Thursday CIC-IDS2017 captures. The script will use a fixed random seed and an 80:20 stratified row-level split of the available records.

The manifest will record the experiment configuration, source captures, partition sizes, and BENIGN/ATTACK class counts. It will be stored separately from the original Friday-held-out manifest to preserve the baseline experiment.

The script will validate that the training and validation partitions are disjoint and that their combined record count matches the source dataset. The manifest-generation result remains pending until the script has been executed and its checks have passed.

### Validation Manifest Generation — Results

**Status: Completed.**

The script `ml/preprocessing/create_validation_manifest.py` was compiled and executed successfully. It scanned all five Monday–Thursday processed CIC-IDS2017 captures, covering 2,127,498 records, and generated a reproducible 300,000-row sample using random seed 42.

The sampled records were partitioned using stratified random sampling, with 80% assigned to training and 20% to validation.

| Partition | Total records | BENIGN | ATTACK |
|---|---:|---:|---:|
| Training | 240,000 | 209,871 | 30,129 |
| Validation | 60,000 | 52,468 | 7,532 |
| Total sample | 300,000 | 262,339 | 37,661 |

The manifest was saved as `data/cicids2017/processed/binary_validation_manifest.json`. The script verified that the partitions were disjoint and that their combined record count matched the sample size. The original processed CSV files were not modified, and no model training was performed during this step.

**Limitations:** The validation partition contains randomly sampled records from the same Monday–Thursday capture collection as the training partition. Consequently, it estimates performance on similarly sampled traffic and does not establish generalization to unseen capture days or attack families. The experiment also uses a 300,000-row sample rather than the complete training-period dataset.

The next stage is to train a candidate Random Forest using only the training partition, fit imputation exclusively on training data, and evaluate the candidate on the validation partition. Friday diagnostic data will not be used for model selection.

### Validation-Only Random Forest Training — Planned Experiment

The next experiment will train a candidate binary Random Forest classifier using the training partition recorded in `data/cicids2017/processed/binary_validation_manifest.json`. The corresponding validation partition will be used to assess performance without incorporating validation records into model fitting.

The candidate will use the existing baseline configuration: 100 trees, maximum depth 20, minimum leaf size of two, and random seed 42. Median imputation will be fitted exclusively on the training partition through a scikit-learn pipeline.

Evaluation will report the confusion matrix, precision, recall, F1-score, accuracy, false positives, and false negatives for the BENIGN and ATTACK classes. The candidate model and evaluation report will be stored separately from the original baseline artifacts to preserve reproducibility.

This experiment will measure performance on a stratified random row-level validation sample from the Monday–Thursday captures. It will not establish generalization to unseen capture days or attack families. Results are pending until training and validation complete successfully.

### Validation Candidate — Implementation Preparation

The validation manifest has been generated successfully using a reproducible 300,000-row sample from the Monday–Thursday CIC-IDS2017 captures. The sample contains 240,000 training records and 60,000 validation records.

The next implementation will create a separate training script, `ml/training/train_binary_validation.py`, to evaluate the existing Random Forest configuration on this partition. The script will reproduce the sampling and split procedure, verify the resulting class counts against the saved manifest, and stop if the reconstructed partition does not match the recorded configuration.

Median imputation will be fitted exclusively on training records. The candidate model and validation report will be saved separately from the original baseline artifacts. Evaluation will include the confusion matrix, accuracy, precision, recall, F1-score, false positives, and false negatives.

**Status:** Implementation pending. No validation-candidate model has been trained, and no validation metrics have been collected.

### Random Forest Validation Experiment — Results

**Status: Completed.**

The validation-training script, `ml/training/train_binary_validation.py`, reconstructed the 300,000-row sample using random seed 42 and verified its training and validation class counts against the saved validation manifest. The experiment used 240,000 training records and 60,000 validation records.

A Random Forest classifier with 100 trees, maximum depth 20, minimum leaf size of two, and random seed 42 was trained using a scikit-learn pipeline. Median imputation was fitted exclusively on the training partition.

The validation confusion matrix was:

| Actual class | Predicted BENIGN | Predicted ATTACK |
|---|---:|---:|
| BENIGN | 52,457 | 11 |
| ATTACK | 32 | 7,500 |

The model achieved 99.93% accuracy. The ATTACK class achieved 99.85% precision, 99.58% recall, and an F1-score of 0.9971. There were 11 false positives and 32 false negatives among the 60,000 validation records.

The candidate model was saved as `ml/models/binary_random_forest_validation.joblib`, and its evaluation report was saved as `data/cicids2017/processed/binary_validation_report.json`. The original baseline artifacts were preserved.

### Interpretation and Limitations

The random row-level validation metrics were substantially higher than the earlier Friday diagnostic metrics, for which attack recall was 28.18%. The validation and Friday evaluations represent different generalization conditions. The random validation partition contains records sampled from the same capture collection as the training partition, whereas Friday contains traffic from separate captures and includes attack families absent from the training captures.

Consequently, the random validation results should not be interpreted as evidence of reliable detection of unseen attacks. Shared capture sources between the training and validation partitions may contribute to optimistic performance. The difference between random validation and Friday diagnostic results motivates further investigation using capture-level evaluation and carefully controlled experiments.

These results concern binary classification only. They do not establish the effectiveness of real-time blocking, distributed rule propagation, or blockchain auditing.

The next stage will examine the reproducibility and limitations of the validation experiment before selecting any model settings or classification thresholds.

### Validation Reliability and Generalization Investigation — Planned Work

The initial random row-level validation experiment achieved 99.93% accuracy and 99.58% ATTACK recall on 60,000 validation records. These results were substantially higher than those obtained during the earlier Friday diagnostic evaluation, where ATTACK recall was 28.18%.

This difference warrants further investigation before the random-validation results are used to support conclusions about the proposed intrusion prevention system. The current validation design allows records from the same source captures to occur in both training and validation partitions. Consequently, the experiment does not independently establish generalization to unseen capture days or attack families.

The next investigation will verify the reproducibility of the generated validation sample and split, review the data-processing and evaluation boundaries, and determine whether the existing metrics are consistent with the saved model and report. The original baseline artifacts will be preserved.

Any subsequent generalization experiment will be designed and reported separately from the random row-level validation experiment. Friday diagnostic results will not be used to select model parameters or classification thresholds.

**Status:** Investigation planned; no additional tests or conclusions have been produced yet.

#### Saved Experiment Artifact Verification

The existence of the four principal experiment artifacts was verified in the project workspace:

- `binary_baseline_report.json` — original Friday-held-out baseline metrics.
- `binary_validation_manifest.json` — sampled dataset and training/validation partition metadata.
- `binary_validation_report.json` — random row-level validation metrics.
- `binary_random_forest_validation.joblib` — serialized validation model.

All four files were present. Their filesystem timestamps were consistent with the recorded experiment sequence. This check establishes artifact availability only; it does not yet verify that the report contents match the manifest or saved model.

**Status:** Artifact existence verified; metric and metadata consistency checks pending.

#### Validation Metadata and Metric Consistency Audit — Planned

The baseline report, validation manifest, validation report, and serialized validation model have been confirmed to exist. The next audit will examine the contents of the JSON artifacts to verify consistency between the documented sampling procedure, dataset partition counts, model configuration, and reported evaluation metrics.

The expected validation experiment uses a 300,000-record sample, partitioned into 240,000 training records and 60,000 validation records. The reported validation confusion matrix contains 52,457 true negatives, 11 false positives, 32 false negatives, and 7,500 true positives.

These values are reference results from the earlier training run, not independently reverified findings. The audit will determine whether the saved artifacts contain matching values and whether their metadata adequately documents the experiment's limitations.

**Status:** Audit planned; saved JSON contents have not yet been inspected in this step.

#### Validation Metadata and Metric Consistency Audit — Results

The saved baseline report, validation manifest, and validation report were inspected. Their principal dataset counts, class counts, model configuration, confusion matrix, and evaluation metrics were consistent with the previously recorded experiments.

The validation experiment used 300,000 sampled records from Monday–Thursday captures, with 240,000 records for training and 60,000 for validation. The validation confusion matrix contained 52,457 true negatives, 11 false positives, 32 false negatives, and 7,500 true positives. The resulting accuracy was 99.93%, with an ATTACK recall of 99.58%.

In contrast, the Friday diagnostic evaluation achieved 70.46% accuracy and 28.18% ATTACK recall, with 207,518 false negatives. This substantial performance difference demonstrates that the random row-level validation score is not sufficient evidence of generalization to different network captures.

The validation manifest explicitly acknowledges that records from the same capture can appear in both partitions and that the experiment does not establish unseen-capture or unseen-attack-family generalization. Friday data was excluded from fitting and validation selection.

**Conclusion:** The saved experiment metadata and metrics are internally consistent with the recorded results. However, the high random-validation score must be interpreted within the limitations of its split strategy. The cause of the performance gap remains under investigation.

**Status:** Metadata and metric consistency audit completed.

#### Capture-Level Generalization Experiment — Dataset Coverage Audit

The preceding experiments revealed a substantial difference between random row-level validation and Friday diagnostic performance. A capture-level evaluation is therefore needed to investigate generalization beyond records drawn from familiar captures.

Before defining this evaluation, the class distribution of each available Monday–Thursday capture will be examined. The audit will identify benign and attack record counts, attack-family coverage, and classes that occur in only one capture or have very few records.

The split strategy will be selected only after reviewing these distributions. The objective is to evaluate generalization to held-out capture sources while documenting any limitations caused by missing attack classes, rare classes, or insufficient training examples.

No new model will be trained during this coverage audit, and the existing baseline and validation artifacts will remain unchanged.

**Status:** Dataset coverage audit planned; capture-level split not yet selected.

#### Capture-Level Class Coverage Audit — Results

The eight processed CIC-IDS2017 captures were inspected using chunked label-only reads. Their observed row counts and class distributions matched the previously documented dataset counts.

Monday contained only BENIGN records. Tuesday contained FTP-Patator and SSH-Patator; Wednesday contained multiple DoS families and Heartbleed; Thursday morning contained Web Attack Brute Force, Web Attack XSS, and SQL Injection; and Thursday afternoon contained Infiltration. Friday contained Bot, DDoS, and PortScan traffic in separate captures.

The audit identified substantial differences in attack-family coverage and severe class scarcity for Heartbleed (11 records), SQL Injection (21 records), and Infiltration (36 records). Consequently, a capture-level split may exclude some attack families from training, and reliable per-class estimates may not be possible for rare attacks.

The proposed next experiment is to hold out the Thursday morning WebAttacks capture from model training and evaluate on its records. This will assess generalization to one excluded capture, but will not establish universal unseen-attack generalization. Existing models and Friday diagnostic results will remain unchanged.

**Status:** Capture-level class coverage audited; the proposed holdout experiment has not yet been executed.

#### Thursday WebAttacks Capture Holdout — Experiment Design

The proposed experiment will use `cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv` as a held-out evaluation capture. Its 170,366 records comprise 168,186 BENIGN records and 2,180 attack records: 1,507 Web Attack Brute Force, 652 Web Attack XSS, and 21 Web Attack Sql Injection.

The model will be trained exclusively on the other Monday–Thursday captures, excluding the held-out WebAttacks capture. The evaluation will therefore test performance on a capture source not used for fitting, while recognizing that the same attack families may be represented elsewhere in the training data only if the dataset actually contains them.

Before training, the class coverage of the remaining captures will be verified. Evaluation metrics will include the confusion matrix, per-class precision and recall, and false-positive and false-negative counts. Rare-class metrics, particularly for SQL Injection, will be interpreted cautiously because the held-out class contains only 21 records.

This experiment will be reported separately from the existing random row-level validation and Friday diagnostic evaluation. No model or threshold changes will be made to the existing experiments.

**Status:** Experiment design documented; training and evaluation have not started.

#### Training-Capture Coverage Verification — Planned

The Thursday morning WebAttacks capture has been designated as the held-out evaluation source. The remaining Monday–Thursday captures will be audited to establish the attack-family coverage available for model training.

The audit will verify the number of records and class labels in the eligible training captures, confirm that the held-out capture is excluded, and identify any classes that are absent from the training data. This check is necessary to distinguish evaluation on a new capture containing previously observed attack families from evaluation on genuinely unseen attack families.

No model will be trained and no existing model artifacts will be modified during this verification.

**Status:** Training-capture coverage verification planned; results pending.

#### Training-Capture Coverage Verification — Results

The audit examined the eligible Monday–Thursday captures after excluding the Thursday morning WebAttacks capture and all Friday captures. The eligible data contained 1,957,132 records: 1,690,589 BENIGN and 266,543 ATTACK records. No missing labels were found, and the exclusion checks passed.

The eligible training captures contained DoS GoldenEye, DoS Hulk, DoS Slowhttptest, DoS slowloris, FTP-Patator, SSH-Patator, Infiltration, and Heartbleed. The held-out Thursday morning capture contained Web Attack Brute Force, Web Attack XSS, and Web Attack Sql Injection, none of which appeared in the eligible training captures.

Therefore, the proposed experiment will evaluate both capture-level separation and generalization to attack families absent from the training data. Because the classifier is binary, it will evaluate BENIGN-versus-ATTACK detection rather than attack-family identification. The small number of SQL Injection records (21) limits the reliability of its class-specific performance estimate.

**Status:** Training-capture coverage verified; holdout model training has not started.

#### Capture-Level Holdout Model Implementation — Planned

A separate training script will be developed to evaluate binary intrusion detection on the excluded Thursday morning WebAttacks capture. The script will use the eligible Monday–Thursday captures while excluding both the held-out WebAttacks capture and all Friday captures.

The experiment will use the existing binary-label mapping, where BENIGN is encoded as 0 and every attack family as 1. Median imputation will be fitted only on training data. The Random Forest configuration will initially match the existing baseline to support a controlled comparison.

The script will save its model and evaluation report under distinct filenames to avoid overwriting previous experiment artifacts. Evaluation will include the confusion matrix, accuracy, precision, recall, F1-score, and false-positive and false-negative counts.

Because the held-out capture contains attack families absent from training, this experiment will provide evidence about generalization to those families within this dataset. It will not, by itself, establish generalization to all unseen attacks or real-world production traffic.

**Status:** Implementation planned; no model has been trained for this experiment.

#### Holdout Script Compilation and Resource Review

The new script, `ml/training/train_binary_capture_holdout.py`, passed Python syntax compilation using `python -m py_compile`. Git confirmed that the script exists as a new, untracked file.

Before training, two implementation concerns were identified. First, the current implementation accumulates all training features in memory, which may be unsuitable for the 7 GB WSL memory limit. Second, the evaluation report hardcodes the feature count rather than deriving it from the loaded dataset.

The script will be revised to reduce memory pressure and validate the feature schema before training. No holdout model has been trained, and no new performance results have been produced.

**Status:** Syntax verified; memory and feature-schema safeguards pending.

#### Revised Holdout Script — Compilation Verification

The revised `ml/training/train_binary_capture_holdout.py` passed Python syntax compilation. Git confirmed that the script exists as an untracked file, and the existing baseline and random-validation artifacts remain separate.

The revised implementation includes feature-schema checks, a fixed 300,000-record training sample, chunked evaluation of the held-out capture, and separate output paths for the new model and report. However, the sampling implementation can temporarily allocate additional memory when combining the retained sample with an incoming data chunk.

Training has therefore been deferred until the sampling implementation is reviewed for memory efficiency. No holdout performance results are available at this stage.

**Status:** Compilation verified; memory-efficiency review

#### Memory-Efficient Training Sample Selection — Planned Improvement

The holdout training script passed syntax verification, but its sampling procedure can temporarily allocate substantial additional memory when combining retained samples with incoming chunks.

The next revision will reduce unnecessary allocations while preserving a reproducible sampling procedure with a fixed random seed and a maximum sample size of 300,000 records. Feature schema validation and capture exclusion checks will remain in place.

The sampling procedure, random seed, selected sample size, and any limitations introduced by sampling will be recorded in the experiment report. Training will begin only after the revised implementation passes syntax and preliminary consistency checks.

**Status:** Memory-efficient sampling improvement planned; no model training performed.

#### Memory-Efficient Sampling Revision — Verification Results

The sampling block in `ml/training/train_binary_capture_holdout.py` was revised to retain a bounded sample of 300,000 records using a fixed random seed. The script passed Python syntax compilation, and `git status` confirmed that the new script remains present as an untracked file.

The revised implementation reduces repeated concatenation of the full retained sample with each incoming chunk. However, it still creates temporary candidate and combined arrays, so peak memory consumption has not yet been measured or established to fit within the available WSL memory limit.

No training was performed, and no new evaluation results are available.

**Status:** Syntax verified; sampling correctness and peak-memory suitability still require review.

#### Sampling Algorithm Unit Test — Planned

A small synthetic-data test will be conducted before running the capture-level holdout experiment. The test will verify that the sampling algorithm retains the requested number of records, maintains the alignment of feature rows and labels, and produces a reproducible sample when the random seed and input data remain unchanged.

The test will not load the CIC-IDS2017 dataset or fit a classifier. Passing this test will establish basic sampling correctness, but will not establish peak-memory suitability for the full dataset.

**Status:** Synthetic sampling test planned; no test results produced yet.

#### Sampling Algorithm Unit Test — Results

The sampling algorithm was tested using 500 synthetic records distributed across four chunks. With a requested sample size of 100 and random seed 42, the test retained exactly 100 records.

The test passed checks for sample size, feature and label dimensions, reproducibility across repeated runs, and feature-label alignment. All checks completed without errors.

These results establish basic functional correctness of the tested sampling procedure on synthetic data. They do not establish peak-memory suitability or validate the full-dataset training and evaluation pipeline.

**Status:** Synthetic sampling test passed; full-dataset experiment not yet executed.

### End-of-Session Checkpoint — 11 October 2026

#### Completed
- Audited class distributions across all eight processed CIC-IDS2017 captures.
- Verified that the Thursday morning WebAttacks capture contains 170,366 records, including 168,186 BENIGN records and 2,180 attack records.
- Confirmed that the remaining eligible Monday–Thursday captures contain 1,957,132 records, including 1,690,589 BENIGN and 266,543 ATTACK records.
- Created `ml/training/train_binary_capture_holdout.py` for a separate capture-level holdout experiment.
- Verified Python syntax compilation and tested the sampling algorithm on synthetic data. The test retained exactly 100 of 500 records and passed reproducibility and feature-label alignment checks.

#### Current Limitations
- The capture-holdout training script has not been executed on CIC-IDS2017.
- Peak memory usage has not been measured.
- The holdout model's performance remains unknown.
- Existing random-validation and Friday diagnostic results remain unchanged.

#### Next Session
1. Verify the holdout script's sampling correctness and memory requirements.
2. Run the capture-level holdout experiment only after the implementation passes the required checks.
3. Inspect the confusion matrix and per-class metrics.
4. Continue documenting findings without overstating generalization or production effectiveness.

**Session status:** Implementation and preliminary tests completed; capture-holdout training pending.

### Research Session Resume — 11 October 2026

#### Previous Session Checkpoint
The previous session's source code and research-log changes were committed and pushed to the GitHub `main` branch in commit `90d7163`. The local working tree was clean after the push.

The capture-level dataset audit identified Thursday morning WebAttacks as a suitable holdout candidate. The synthetic sampling test passed checks for exact sample size, reproducibility, and feature-label alignment.

#### Work Remaining
1. Remove trailing whitespace reported during the previous Git checks.
2. Review the holdout sampler for correctness and memory efficiency.
3. Verify feature schema and sampling behavior before training.
4. Execute the holdout experiment only after the implementation passes these checks.
5. Record actual evaluation results without changing the existing baseline or Friday diagnostic results.

The holdout model has not been trained, and its performance remains unknown.

**Status:** Project resumed; implementation review is the next task.

#### Source Formatting and Static Verification — Planned

The previous Git commit reported trailing whitespace in the research log and two Python scripts. These formatting issues will be removed without changing the experimental logic.

After cleanup, the affected scripts will be checked for Python syntax errors, and Git whitespace checks will be rerun. The capture-holdout model will remain untrained during this step.

**Status:** Formatting cleanup and static verification planned; results pending.

#### Source Formatting and Static Verification — Results

Trailing whitespace was removed from the research log, prediction-confidence evaluation script, and capture-holdout training script. Both affected Python scripts passed syntax compilation. The Git whitespace check completed without reporting errors in the tracked changes.

The research log and two Python scripts are modified in the working tree. These changes have not yet been committed or pushed.

**Status:** Formatting cleanup and syntax verification completed; capture-holdout training remains pending.

#### Capture-Holdout Sampler Review — Planned

The source formatting cleanup and Python syntax checks completed successfully. The next step is to review the capture-holdout sampler for statistical correctness, reproducibility, feature-schema consistency, and peak-memory requirements.

The current implementation retains a fixed-size sample by selecting records with the smallest random keys. Its synthetic test passed, but the full-dataset implementation has not yet been validated against an independent reference sample or measured for peak memory consumption.

The review will also verify that the held-out Thursday morning WebAttacks capture is excluded from training and that preprocessing is fitted exclusively on training data. No model training will occur during this review.

**Status:** Sampler review planned; holdout experiment not yet executed.

#### Capture-Holdout Script Review — Findings

The capture-holdout training script and WSL memory availability were inspected. The environment reported approximately 5.6 GiB of available memory at the time of inspection.

The code review identified suspicious formatting and variable-name inconsistencies in the saved script, including the feature-column list construction and a variable name in the sampling cleanup block. These issues must be resolved before the script can be considered ready for execution.

The key-based sampling strategy remains a candidate for selecting a reproducible, fixed-size sample, but the implementation has not yet passed a complete runtime check on the actual project script. Peak memory usage also remains unmeasured.

No model training was performed, and no new evaluation results were produced.

**Status:** Code review identified corrections required before training.

### Capture-Holdout Script: Static Verification

The capture-level holdout training script was reviewed and corrected for feature-schema validation, variable naming, and report-description consistency. Python bytecode compilation is used as a syntax check. This check does not establish that the script is free of runtime errors or that the sampling and training pipeline produces valid experimental results. A full-data training run has not yet been performed.

### Capture-Holdout Script Review

A source review confirmed that the proposed experiment separates the Thursday morning WebAttacks capture from the eligible training captures, uses a reproducible key-based training sample, fits median imputation within the training pipeline, and evaluates the held-out capture in chunks. The evaluation code will be strengthened by validating confusion-matrix totals against the observed test-row and class counts and by simplifying classification-report generation. These are pre-experiment code-review findings; no capture-holdout model has been trained and no performance results are available yet.

### Capture-Holdout Preflight Verification — 11 October 2026

The capture-holdout training script passed Python bytecode compilation and `git diff --check`. All five required processed CSV files were confirmed to exist: Monday, Tuesday, Wednesday, Thursday afternoon Infiltration, and Thursday morning WebAttacks. The model and processed-data output directories also exist. The working tree contains modifications to the research log, prediction-confidence inspection script, and capture-holdout training script. No capture-holdout training or performance evaluation has been completed at this checkpoint.

### Capture-Holdout Experiment Readiness — 11 October 2026

The capture-holdout script passed Python bytecode compilation. All required input captures and output directories were verified, and the model and report paths are distinct from the existing baseline artifacts. The configured experiment uses a reproducible 300,000-row sample, a median imputer, a 100-tree Random Forest with maximum depth 20 and two parallel jobs, and chunked evaluation of the complete Thursday morning WebAttacks capture. Available memory before launch was approximately 5.3 GiB. Training has not yet started; performance results remain pending.

### Capture-Holdout Experiment Results — 11 October 2026

**Status:** Completed successfully.

**Experimental setup**
- Training captures: Monday, Thursday afternoon Infiltration, Tuesday, and Wednesday.
- Held-out capture: Thursday morning WebAttacks.
- Eligible training rows: 1,957,132.
- Training sample: 300,000 rows, comprising 259,291 BENIGN and 40,709 ATTACK.
- Features: 77.
- Model: median imputation and RandomForestClassifier with 100 trees, maximum depth 20, minimum leaf size 2, random seed 42, and two parallel jobs.
- Held-out records evaluated: 170,366.
- Runtime: 80.11 seconds.

**Observed results**

Confusion matrix, with actual classes as rows and predicted classes as columns:

| Actual class | Predicted BENIGN | Predicted ATTACK |
|---|---:|---:|
| BENIGN | 168,130 | 56 |
| ATTACK | 2,175 | 5 |

Overall accuracy was 0.9869 (98.69%). BENIGN precision was 0.9872, recall 0.9997, and F1-score 0.9934. ATTACK precision was 0.0820, recall 0.0023, and F1-score 0.0045.

The model detected only 5 of 2,180 attack records and missed 2,175. It generated 56 false positives. The high overall accuracy therefore does not reflect effective attack detection.

**Interpretation and limitations**

The held-out WebAttacks capture contains attack families absent from the eligible training captures. The very low attack recall indicates poor generalization in this experiment. These results do not establish performance on all unseen attack families or production traffic. The experiment is evidence that the current model is not suitable for deployment as an intrusion prevention system without further investigation and improvement.

**Artifacts**

- Model: `ml/models/binary_random_forest_capture_holdout.joblib`
- Report: `data/cicids2017/processed/binary_capture_holdout_report.json`
- Script: `ml/training/train_binary_capture_holdout.py`

The model and report are local experimental artifacts; no claim of production effectiveness is made.

### Comparison of Friday Diagnostic and Thursday WebAttacks Holdout — 11 October 2026

Both experiments used a Random Forest with 100 trees, maximum depth 20, minimum leaf size 2, median imputation, and a 300,000-row training sample. The evaluation sets differed in capture source, size, and attack composition.

| Metric | Friday diagnostic | Thursday WebAttacks holdout |
|---|---:|---:|
| Test records | 703,245 | 170,366 |
| Accuracy | 70.46% | 98.69% |
| ATTACK precision | 99.72% | 8.20% |
| ATTACK recall | 28.18% | 0.23% |
| ATTACK F1-score | 43.94% | 0.45% |
| False negatives | 207,518 | 2,175 |

The Friday diagnostic was previously examined and is not an untouched final test set. The Thursday WebAttacks capture was held out from model fitting and contains attack families absent from the eligible training captures.

The Thursday result demonstrates that high overall accuracy can coexist with extremely poor attack detection when benign traffic dominates the test set. Attack recall decreased substantially between these two evaluation settings. Because capture source and attack-family composition differ simultaneously, the comparison does not establish which factor caused the performance difference.

**Conclusion:** The current baseline does not meet the requirements for a dependable intrusion prevention system. Further investigation should focus on capture-level generalization, attack-family coverage, and class-specific detection performance. No production-effectiveness claim is justified by these experiments.

### Diagnostic Investigation Plan — 11 October 2026

Following the capture-holdout experiment, the next investigation will examine the existing feature-importance, prediction-confidence, and feature-distribution diagnostic scripts and their available outputs.

The investigation will focus on:
1. Identifying which features the current Random Forest relies on most heavily.
2. Examining the prediction confidence associated with missed attacks, where saved diagnostic outputs permit.
3. Reviewing differences in feature distributions between training data and the held-out capture.
4. Distinguishing observed evidence from hypotheses about why attack detection failed.

The Friday diagnostic and Thursday WebAttacks holdout results will be treated as diagnostic evidence, not as unbiased final-test estimates. The held-out capture will not be used to tune the model and then presented as an untouched final test set.

No new model configuration has been selected. The next experiment will be chosen only after reviewing the available diagnostic evidence.

### Initial Feature-Importance and Confidence Findings — 11 October 2026

The existing diagnostic artifacts were inspected. These artifacts primarily describe the original Friday-diagnostic baseline model and should not be confused with diagnostics from the newer Thursday capture-holdout model.

**Feature importance:** The five highest impurity-based feature-importance scores were Destination Port (0.087714), Bwd Packet Length Std (0.070899), Packet Length Variance (0.066286), Bwd Packet Length Mean (0.051191), and Avg Bwd Segment Size (0.049015). These scores describe the baseline Random Forest's use of features; they do not establish causality or generalization.

**Prediction confidence:** In the existing sampled diagnostics, the baseline predicted all 2,000 sampled PortScan attack records as BENIGN and all 1,966 sampled Bot attack records as BENIGN. Median attack probability was 0.0000 for both groups. These observations indicate severe detection failures for those sampled records. They do not establish the full probability distribution for every record or prove that threshold adjustment cannot help in other cases.

**Data inspection note:** The confidence CSV uses `True_Label`, not `ActualLabel`; an attempted summary grouped by the nonexistent column and raised a `KeyError`. The file itself was readable. Feature-distribution and label-specific shift reports exist and require further examination.

**Current interpretation:** Feature-distribution differences and low attack probabilities are plausible investigation leads, not established causes of the Thursday holdout failure. No model changes or threshold tuning have been performed as part of this diagnostic review.

### Feature-Distribution Comparison Findings — 11 October 2026

**Reports examined**
- `top_feature_distributions_binary.csv`
- `feature_shift_by_label.csv`

**Scope:** The inspected distribution summaries compare Mon–Thu training captures with Friday diagnostic captures. They do not directly compare the Thursday WebAttacks holdout against the training set.

**Observed differences**
- The sampled median `Destination Port` for ATTACK records was 80 in the training group and 8,080 in the Friday diagnostic group.
- The sampled median `Destination Port` for BENIGN records was 443 in the training group and 3,268 in the Friday diagnostic group.
- The sampled median `Packet Length Variance` for ATTACK records was 65.33 in training and 12 in the Friday diagnostic group.
- The displayed medians for `Bwd Packet Length Std` were zero for ATTACK records in both groups, despite different third quartiles.

**Interpretation and limitations**

These summaries provide evidence of differences between sampled training and Friday diagnostic feature distributions. They do not establish that feature shift caused the model's errors. The datasets also differ in attack-family composition, and the capture-holdout experiment cannot isolate capture effects from unseen attack-family effects.

The Thursday WebAttacks holdout result remains a separate evaluation: 5 of 2,180 attacks detected, with attack recall of approximately 0.23%. The inspected CSV summaries are not direct measurements of that holdout's feature shift.

**Decision:** Do not change model parameters or claim a causal explanation based on these summaries alone. Further analysis should quantify feature differences by dataset and label, while clearly separating observations from hypotheses.

### Feature-Shift Report Coverage Audit — 11 October 2026

**Report:** `data/cicids2017/processed/feature_shift_by_label.csv`

**Structure:** 208 rows, with columns `Label`, `Dataset`, `Feature`, `Sample_Count`, `Missing_Count`, `Median`, `Mean`, and `Std`. The report summarizes 13 selected features for each recorded label and dataset combination.

**Coverage findings**
- BENIGN has summaries for all 13 selected features in both `Mon-Thu training` and `Friday diagnostic`.
- DDoS, PortScan, and Bot have summaries only in the Friday diagnostic group.
- DoS GoldenEye, DoS Hulk, DoS Slowhttptest, DoS slowloris, FTP-Patator, Heartbleed, Infiltration, and SSH-Patator have summaries only in the Mon–Thu training group.
- Web Attack Brute Force, Web Attack Sql Injection, and Web Attack XSS have no entries in this particular report, because these attack families belong to the separately held-out Thursday WebAttacks capture.

**Interpretation**

The current report supports a feature-distribution comparison for BENIGN records only. It does not support a same-attack-family distribution comparison between the training and Friday diagnostic groups, because no attack family appears in both groups in this report.

The absence of matching attack labels is a limitation of the report's grouping and dataset composition; it is not evidence that the model cannot generalize to all attack families. The separate Thursday WebAttacks holdout result provides evidence of poor detection on that held-out capture, but it does not isolate the cause.

**Next action:** Inspect the existing report-generation scripts and determine whether a more appropriate binary-label comparison can be produced from the available data without changing the trained model. Keep any new analysis explicitly separate from the held-out Thursday evaluation.

### Review of Feature-Shift Report Generator — 11 October 2026

**Script reviewed:** `ml/evaluation/inspect_feature_shift_by_label.py`

The script samples up to 2,000 records per original label per capture using random priorities and a fixed random seed of 42. It summarizes 13 selected numeric features using sample count, missing count, median, mean, and standard deviation.

The script preserves original multiclass labels rather than mapping records to binary `BENIGN` and `ATTACK` labels. The training capture list includes the Thursday morning WebAttacks capture, while the Friday captures form the diagnostic group. This report therefore represents the original Mon–Thu versus Friday diagnostic comparison, not the later Thursday WebAttacks capture-holdout experiment.

Because most attack labels appear in only one group, the existing report supports a same-label distribution comparison only for BENIGN. The per-label sampling also means its summaries are not complete-dataset statistics.

**Planned next step:** Develop a separate, reproducible binary feature-shift diagnostic that compares BENIGN and ATTACK samples from the existing Mon–Thu training and Friday diagnostic groups. Preserve the original report and script. Interpret pooled ATTACK results cautiously because different attack families may have different feature distributions. Do not retrain or tune the model as part of this diagnostic step.

### Binary Feature-Shift Diagnostic — Script Validation — 11 October 2026

Created `ml/evaluation/inspect_binary_feature_shift.py` as a separate diagnostic script. It maps the original `BENIGN` label to `BENIGN` and all other labels to `ATTACK`, then samples each binary class independently within each capture. Sampling uses a fixed random seed of 42 and a maximum of 2,000 records per binary class per capture.

The script uses chunked CSV reading and summarizes 13 numeric features. Its intended output is `data/cicids2017/processed/binary_feature_shift_by_label.csv`. The script passed Python syntax validation using `python -m py_compile`.

No dataset, trained model, or existing diagnostic script was modified as part of this validation. The diagnostic has not yet been executed; its output and runtime remain unverified.

### Binary Feature-Shift Diagnostic Results — 11 October 2026

**Script:** `ml/evaluation/inspect_binary_feature_shift.py`

**Output:** `data/cicids2017/processed/binary_feature_shift_by_label.csv`

The diagnostic completed successfully across the eight configured capture files. It used chunked CSV reading, random-priority sampling, and seed 42, with up to 2,000 records per binary class per capture.

**Sample counts**
- Mon–Thu training: 10,000 BENIGN and 6,036 ATTACK records.
- Friday diagnostic: 6,000 BENIGN and 5,966 ATTACK records.

These counts describe the diagnostic sample, not the complete datasets.

**Selected median comparisons**

| Feature | Binary label | Mon–Thu training | Friday diagnostic |
|---|---|---:|---:|
| Flow Duration | BENIGN | 30,802 | 49,184.5 |
| Flow Duration | ATTACK | 5,618,066 | 63,608 |
| Flow Packets/s | BENIGN | 128.09 | 78.44 |
| Flow Packets/s | ATTACK | 1.20 | 113.98 |
| Init_Win_bytes_forward | BENIGN | 122 | 139.5 |
| Init_Win_bytes_forward | ATTACK | 29,200 | 8,192 |

**Interpretation and limitations**

The sampled feature distributions differ between Mon–Thu training and Friday diagnostic data, particularly for ATTACK records. However, the binary ATTACK group combines different attack families. The observed differences may reflect attack-family composition, capture conditions, or both; this analysis does not establish causation.

Friday remains diagnostic data, not an untouched final test set. These results do not directly measure feature shift in the Thursday WebAttacks capture-holdout experiment.

**Next action:** Validate the generated CSV's structure, class coverage, sample counts, and missing-value summaries before drawing further conclusions. No model retraining or tuning was performed.

### Binary Feature-Shift Report Validation — 11 October 2026

**Validated file:** `data/cicids2017/processed/binary_feature_shift_by_label.csv`

The report passed the structural validation checks.

- Total rows: 52, corresponding to 13 features across two datasets and two binary labels.
- All four dataset/label combinations contain all 13 expected features.
- Recorded sample counts match the expected values: 10,000 training BENIGN, 6,036 training ATTACK, 6,000 Friday BENIGN, and 5,966 Friday ATTACK.
- No missing median, mean, or standard-deviation values were found.
- No negative missing counts or missing counts greater than sample counts were found.

Some feature observations are missing. For example, the Friday ATTACK sample has 10 missing values each for `Flow Packets/s` and `Flow Bytes/s`. The report records these through `Missing_Count`.

**Conclusion:** The report is structurally consistent with the expected sampling counts and feature coverage. This validation does not establish model generalization, prove that feature shift caused detection errors, or validate the Thursday capture-holdout result.

No model retraining or tuning was performed.

### Capture-Holdout Metric Formula Verification — 11 October 2026

**Script checked:** `ml/training/train_binary_capture_holdout.py`

Python syntax validation passed. A reference calculation using scikit-learn's `confusion_matrix` and `classification_report` reproduced the previously recorded confusion matrix:

`[[168130, 56], [2175, 5]]`

The reference classification metrics were:

- BENIGN precision: 0.987229; recall: 0.999667; F1-score: 0.993409; support: 168,186.
- ATTACK precision: 0.081967; recall: 0.002294; F1-score: 0.004462; support: 2,180.
- Accuracy: 0.986905.

These values agree with the formulas implemented in the staged capture-holdout script. The model misses 2,175 of 2,180 attacks in this evaluation. High accuracy therefore does not imply effective attack detection.

**Limitation:** This check reconstructs the previously recorded confusion matrix; it does not rerun model training or independently verify the original predictions. The result supports the conclusion that the evaluated model is inadequate for the tested holdout, not a claim that every possible model or configuration will fail.

No model retraining or tuning was performed.

### Repository Checkpoint — Binary Feature-Shift Diagnostic — 11 October 2026

The current project changes were committed and pushed successfully to the GitHub repository `Ak7865/immunet-ips`.

- Commit: `ddce58e`
- Branch: `main`
- Commit message: `Add binary feature shift diagnostics and document evaluation`
- Push result: successful; local `main` and `origin/main` point to the same commit.
- Working tree: clean at the time of verification.

The commit includes the research-log updates, the new binary feature-shift diagnostic script, a minor cleanup in the prediction-confidence inspection script, and changes to the capture-holdout evaluation script.

**Next task:** Review `ml/evaluation/inspect_binary_feature_shift.py` for correctness and code quality before designing another experiment. Do not modify the model or start a new training run until that review is complete.

### Binary Feature-Shift Script Code Review — 11 October 2026

**Script reviewed:** `ml/evaluation/inspect_binary_feature_shift.py`

The script reads configured CIC-IDS2017 captures in chunks of 50,000 rows and retains up to 2,000 records per binary label per capture. Sampling uses random priorities and a fixed seed of 42. This bounds memory use and supports reproducibility when inputs and processing order remain unchanged.

**Findings**
1. The summary's selected-feature list includes `Destination Port`, but this feature is absent from `FEATURES`. A later filter silently excludes it, leaving three displayed features rather than four.
2. The label mapping converts `BENIGN` to `BENIGN` and every other value to `ATTACK`. Unexpected labels are not explicitly validated.
3. Sampling is capped separately for each binary class within each capture. Consequently, the pooled samples are not a globally uniform sample of the combined dataset.

**Planned corrections:** Align the displayed feature list with the actual selected features, and validate original labels against the expected CIC-IDS2017 labels before binary mapping. Preserve the existing report and trained models. These changes are intended to improve diagnostic correctness and transparency, not model performance.

**Limitation:** This code review does not establish whether the observed feature differences caused the capture-holdout model's low attack recall.

### Binary Label-Validation Tests — 11 October 2026

The label-validation logic in `ml/evaluation/inspect_binary_feature_shift.py` was tested independently.

- `BENIGN` maps to `BENIGN`.
- Known CIC-IDS2017 attack labels map to `ATTACK`.
- An unexpected label raises `ValueError` and is not silently accepted.
- Python syntax validation and `git diff --check` passed.

The feature-selection summary was also corrected to list only the three selected features included in the report: `Flow Duration`, `Flow Packets/s`, and `Init_Win_bytes_forward`.

These tests validate the mapping logic and script formatting; they do not validate model performance or establish the cause of the capture-holdout failure.

**Next action:** Rerun the diagnostic with the label-validation correction, then compare its output with the previously recorded results. The model will not be retrained.

### Binary Feature-Shift Diagnostic Rerun — 11 October 2026

**Status:** Completed successfully.

Reran `ml/evaluation/inspect_binary_feature_shift.py` after correcting feature selection and adding validation for unexpected original labels. The script completed without errors and generated `data/cicids2017/processed/binary_feature_shift_by_label.csv`.

**Sample counts:**
- Mon–Thu training captures: 6,036 ATTACK and 10,000 BENIGN sampled rows.
- Friday diagnostic captures: 5,966 ATTACK and 6,000 BENIGN sampled rows.
- Sampling was capped at 2,000 records per capture and binary label where available. Consequently, counts are not fully balanced across all labels or captures.

**Selected feature observations:**
- Median `Flow Duration` for ATTACK rows was approximately 5.62 million in Mon–Thu training captures and 63,608 in Friday diagnostic captures.
- Median `Flow Packets/s` was approximately 1.20 in Mon–Thu ATTACK samples and 113.98 in Friday ATTACK samples.
- Median `Init_Win_bytes_forward` was 29,200 in Mon–Thu ATTACK samples and 8,192 in Friday ATTACK samples.
- Means substantially exceeded medians for several features, indicating skewed distributions and the need to interpret summary statistics cautiously.

**Interpretation and limitations:**
These results identify descriptive differences between the sampled dataset groups. They do not establish causation, statistical significance, or that feature shift alone explains the classifier's poor attack recall. The Friday data remains diagnostic rather than an untouched final test set. Binary ATTACK combines multiple attack families, and the capped sampling procedure does not preserve the natural class prevalence.

**Next action:** Continue investigating generalization and attack-family coverage without treating aggregate accuracy as sufficient evidence of intrusion-detection quality.

### Binary Feature-Shift Report Validation — 11 October 2026

**Status:** CSV structure validated.

The generated `binary_feature_shift_by_label.csv` contains 52 rows and 8 columns: `Dataset`, `Binary_Label`, `Feature`, `Sample_Count`, `Missing_Count`, `Median`, `Mean`, and `Std`. There are no duplicate rows and no missing values in the report fields.

The report covers 13 features, two binary labels, and two dataset groups. This gives 52 summary rows.

**Missing observations:** The `Flow Packets/s` and `Flow Bytes/s` summaries record missing observations in their samples. For example, Friday ATTACK has 10 missing observations for each feature; Mon–Thu ATTACK has 16. These counts describe the sampled data, not necessarily the complete source captures.

**Additional observation:** `Init_Win_bytes_backward` has a BENIGN Friday median of `-1`, while the Mon–Thu ATTACK median is `235`. Do not automatically convert `-1` to missing or zero without establishing the feature's meaning and the dataset's conventions.

**Interpretation:** The report is structurally consistent with 13 features × 2 labels × 2 dataset groups. Its summaries support further investigation of feature distributions but do not establish causality or statistical significance. Sampling is capped by capture and label, and differences in attack-family composition limit direct comparisons.

**Next action:** Review the diagnostic script and its feature-selection and sampling logic before deciding whether a more targeted evaluation is warranted.

### Binary Feature-Shift Script Review — 11 October 2026

**Objective:** Inspect `ml/evaluation/inspect_binary_feature_shift.py` for correctness and reproducibility before making further diagnostic changes.

**Review checklist:**
1. Verify that the selected feature list matches the intended 13 features.
2. Verify that the sampling procedure is deterministic and respects the per-capture, per-label limit.
3. Verify that unexpected original labels are rejected rather than silently classified as ATTACK.
4. Check how missing and non-finite feature values are handled when computing summary statistics.
5. Verify the definitions of `Sample_Count`, `Missing_Count`, `Median`, `Mean`, and `Std`.
6. Confirm that the script distinguishes descriptive feature-distribution differences from evidence of model generalization failure.

**Constraint:** This is a code review only. Do not modify the dataset, retrain the model, or change evaluation methodology during this step.

**Next action:** Inspect the current script and report any concrete correctness or reproducibility issues before proposing fixes.

### Feature-Shift Report Code Review — 11 October 2026

**Status:** Review completed; proposed correction not yet implemented.

Reviewed `ml/evaluation/inspect_binary_feature_shift.py`.

**Findings:**
1. The script uses a fixed random seed and caps sampling independently by binary label within each capture.
2. Unexpected original labels are rejected before binary mapping.
3. Sampling converts feature values to numeric and replaces positive and negative infinity with missing values.
4. Report generation counts all sampled rows in `Sample_Count`, counts missing values in `Missing_Count`, and computes descriptive statistics from non-missing values. It does not explicitly normalize non-finite values again during reporting.
5. The report would be clearer with a `Valid_Count` field showing the number of observations used for each feature's statistics.
6. The selected summary-feature filtering is redundant but does not affect the current results.
7. The diagnostic group includes the Thursday morning WebAttacks capture, so it must not be confused with the separate capture-holdout training experiment.

**Proposed next action:** Normalize non-finite values explicitly during report generation and add `Valid_Count`. Keep sampling, feature selection, model parameters, and source data unchanged. Validate the report schema and confirm that the new counts reconcile with the existing sample and missing counts.

**Limitation:** This correction improves reporting consistency; it does not resolve the classifier's generalization problem or establish the cause of low attack recall.

### Binary Feature-Shift Report Correction — 11 October 2026

**Status:** Report regenerated successfully.

Corrected the indentation of the report-generation loop in `ml/evaluation/inspect_binary_feature_shift.py`. The non-finite-value normalization and `Valid_Count` calculation now execute for each feature within each dataset and binary-label group.

**Validation results:**
- `python -m py_compile ml/evaluation/inspect_binary_feature_shift.py` completed successfully.
- `git diff --check` completed successfully.
- The diagnostic completed and regenerated `data/cicids2017/processed/binary_feature_shift_by_label.csv`.
- The CSV contains 52 rows, 13 unique features, and 9 columns, including `Valid_Count`.
- The report contains no missing values in its summary fields.
- The three selected features appear in the printed distribution summary again.

**Limitation:** The terminal paste for the final validation command appears partially corrupted. The output confirms the report dimensions and schema, but the reconciliation condition `Sample_Count = Missing_Count + Valid_Count` still requires a clean, independent check.

**Next action:** Verify the count relationship across all report rows, then review the final diff before deciding whether to commit and push the correction.

### Feature-Shift Report Count Reconciliation — 11 October 2026

**Status:** All validation assertions passed.

Independently checked `data/cicids2017/processed/binary_feature_shift_by_label.csv`.

- Total report rows: 52.
- Unique features: 13.
- Columns: 9, including `Valid_Count`.
- Count mismatches: 0.
- Verified invariant for every row: `Sample_Count = Missing_Count + Valid_Count`.
- The validation command completed with `All report validations passed.`

**Conclusion:** The regenerated report has the expected dimensions and internally consistent observation counts. This validates report structure and count arithmetic, not the model's detection performance or the causal explanation for its generalization failure.

**Next action:** Review the Git working-tree status and diffs before selecting files for a commit.

### Capture-Holdout Attack-Family Investigation — 11 October 2026

**Status:** Planned; no new evaluation executed.

**Motivation:** The capture-holdout binary classifier produced 2,175 false negatives among 2,180 attack records, with only 5 true positives and attack recall of approximately 0.23%. Aggregate binary metrics do not show whether the errors are concentrated in a particular attack family.

**Research question:** How does the existing capture-holdout model perform separately on Web Attack Brute Force, Web Attack XSS, and Web Attack Sql Injection in the held-out Thursday morning WebAttacks capture?

**Planned measurements for each original attack label:**
- Number of actual attack records.
- True positives and false negatives.
- Attack recall, calculated as `TP / (TP + FN)`.
- Number of records predicted BENIGN and ATTACK.

**Constraints:**
1. Reuse the existing capture-holdout model and its held-out capture.
2. Do not retrain or tune the model during this investigation.
3. Preserve the original attack labels for analysis rather than merging them into ATTACK.
4. Do not use Friday diagnostic data as an untouched final test set.
5. Report per-family counts alongside recall, because small classes can make metrics unstable.

**Interpretation limitation:** The held-out attack families are absent from the eligible training captures, and the entire capture is held out. Therefore, attack-family novelty and capture-level distribution shift remain confounded. This investigation can characterize the errors but cannot independently establish their cause.

**Next action:** Inspect the existing capture-holdout evaluation script and report to identify how predictions and original labels can be recovered without retraining.

### Per-Family Capture-Holdout Evaluation Design — 11 October 2026

**Status:** Design recorded; implementation not started.

Inspection of `binary_capture_holdout_report.json` confirms that the report stores aggregate binary metrics, not individual predictions or per-family results.

The existing `iter_csv_chunks()` function in `ml/training/train_binary_capture_holdout.py` converts original labels into binary values using `labels != "BENIGN"`. This is suitable for binary training and evaluation but does not preserve the original attack-family distinctions for per-family analysis.

**Planned approach:** Create a separate evaluation-only script that loads `ml/models/binary_random_forest_capture_holdout.joblib`, reads the held-out Thursday WebAttacks capture in chunks, retains the original `Label` values, and evaluates predictions separately for:
- `Web Attack Brute Force`
- `Web Attack XSS`
- `Web Attack Sql Injection`

**Measurements:** For each original attack family, report actual record count, TP, FN, predicted BENIGN count, predicted ATTACK count, and attack recall. Also report totals and verify reconciliation against the previously recorded aggregate attack counts.

**Constraints:**
1. Do not retrain or tune the model.
2. Do not modify the existing training script or model artifact.
3. Use only the already designated held-out capture for this investigation.
4. Preserve original labels and report small-family counts explicitly.
5. Do not treat this analysis as an independent final test, because attack-family novelty and capture-level distribution shift remain confounded.

**Next action:** Implement and validate the separate evaluation-only script, then compare its aggregate predictions with the recorded confusion matrix before interpreting per-family results.

### Saved Model Feature-Metadata Verification — 11 October 2026

**Objective:** Verify the saved binary capture-holdout model's feature metadata and the source evaluation report before running the per-family diagnostic.

**Reason:** The training pipeline may have been fitted using NumPy arrays rather than a pandas DataFrame. Consequently, the saved model may not expose `feature_names_in_`. The evaluation script must use a reliable feature schema and preserve the original feature order.

**Planned checks:**
1. Inspect the source report's recorded feature names and test-set counts.
2. Inspect the saved model's pipeline steps and available feature metadata.
3. Confirm the feature count and ordering expected by the model.
4. Correct the evaluation script if necessary before running predictions.

**Safety and validity:** This is an evaluation-only diagnostic. It must reuse the existing model, avoid retraining, and verify aggregate counts against the previously recorded evaluation report.

**Status:** Pending metadata inspection.

### Capture-Holdout Feature-Schema Correction — 11 October 2026

**Finding:** The saved model is a scikit-learn Pipeline with `imputer` and `classifier` steps. It expects 77 features, but `feature_names_in_` is unavailable.

**Correction:** The per-family evaluation script must obtain the expected feature names from `binary_capture_holdout_report.json`, verify that exactly 77 features are recorded, and compare the held-out CSV's feature names and ordering against that recorded schema.

**Validation requirements:**
- Preserve original attack-family labels.
- Reuse the saved model without retraining.
- Check aggregate attack counts and false negatives against the existing report.
- Do not run predictions until the schema correction is saved and syntax checks pass.

**Status:** Metadata inspected; script correction pending.

### Per-Family Capture-Holdout Evaluation — Execution Preparation — 11 October 2026

**Pre-execution checks:** The evaluation script passed Python syntax compilation and `git diff --check` after the feature-schema correction.

**Evaluation objective:** Measure how the existing binary Random Forest performs separately on Web Attack Brute Force, Web Attack XSS, and Web Attack Sql Injection in the held-out Thursday WebAttacks capture.

**Expected safeguards:**
- Reuse the existing saved model; do not retrain.
- Validate feature names and ordering against the source report.
- Reconcile total rows, attack rows, false negatives, and true positives against the existing aggregate results.
- Save a JSON report containing family-level counts and recall.
- Interpret results as diagnostic evidence, not proof that attack-family novelty alone caused the poor recall.

**Status:** Syntax and whitespace checks passed; evaluation pending.

### Evaluation Script Runtime Error — Feature Metadata — 11 October 2026

**Observed error:** `AttributeError: 'SimpleImputer' object has no attribute 'feature_names_in_'`.

**Cause:** The evaluation script still accesses `model.feature_names_in_`, even though the saved pipeline was fitted without retaining feature-name metadata.

**Impact:** Evaluation stopped during feature-schema validation, before the held-out capture was evaluated.

**Correction:** Replace the remaining old feature-metadata lookup with the feature list stored in `binary_capture_holdout_report.json`. Retain the 77-feature count and ordering checks.

**Status:** Runtime error identified; correction pending. No new evaluation results produced.

### Per-Family Capture-Holdout Results — 11 October 2026

**Experiment:** Existing binary Random Forest evaluated on the held-out Thursday Morning WebAttacks capture, retaining original attack-family labels.

**Aggregate reconciliation:**
- Total rows: 170,366
- Actual attack rows: 2,180
- Attacks predicted BENIGN: 2,175
- Attacks predicted ATTACK: 5
- Aggregate counts matched the existing evaluation report.

**Family-level results:**

| Family | Actual | TP | FN | Recall |
|---|---:|---:|---:|---:|
| Web Attack Brute Force | 1,507 | 0 | 1,507 | 0.00% |
| Web Attack XSS | 652 | 3 | 649 | 0.46% |
| Web Attack Sql Injection | 21 | 2 | 19 | 9.52% |

**Interpretation:** Detection performance is extremely poor on this held-out capture despite the high aggregate accuracy previously reported. SQL Injection recall is based on only 21 records and should be interpreted cautiously.

**Limitations:** This is a diagnostic evaluation, not an independent final test. Attack-family novelty and capture-level distribution shift remain confounded. The evaluation emitted scikit-learn warnings because feature names were supplied to an imputer fitted without feature names; the run nevertheless completed and aggregate reconciliation passed.

**Artifact:** `data/cicids2017/processed/binary_capture_holdout_by_family.json`

**Status:** Family-level diagnostic completed; further investigation pending.

### Saved Pipeline Preprocessing Inspection — 11 October 2026

**Pipeline:** `SimpleImputer(strategy='median')` followed by `RandomForestClassifier(max_depth=20, min_samples_leaf=2, n_jobs=2, random_state=42)`.

**Findings:**
- The imputer and classifier each expect 77 features.
- The imputer has no `feature_names_in_` attribute.
- The classifier's classes are `[0, 1]`, representing BENIGN and ATTACK in the binary experiment.
- The evaluation supplies named pandas DataFrames to a pipeline whose imputer was fitted without feature names, producing scikit-learn warnings.

**Planned correction:** Pass the validated feature matrix to the existing pipeline as a NumPy array in the exact feature order recorded in the source report. Do not retrain or modify the saved model.

**Validation:** Rerun the evaluation and confirm that warnings disappear and aggregate counts still reconcile with the existing report.

**Status:** Cause identified; correction pending.

### Verified Per-Family Evaluation and Warning Resolution — 11 October 2026

**Status:** Evaluation completed successfully after converting the validated feature matrix to NumPy before prediction.

**Validation results:**
- Python syntax check passed.
- `git diff --check` passed.
- Scikit-learn feature-name warnings no longer appeared.
- Total held-out rows: 170,366.
- Actual attacks: 2,180.
- False negatives: 2,175.
- True positives: 5.
- Aggregate counts reconciled with the original capture-holdout report.

**Attack-family results:**

| Attack family | Actual | TP | FN | Recall |
|---|---:|---:|---:|---:|
| Web Attack Brute Force | 1,507 | 0 | 1,507 | 0.00% |
| Web Attack XSS | 652 | 3 | 649 | 0.46% |
| Web Attack Sql Injection | 21 | 2 | 19 | 9.52% |

**Interpretation:** The saved model has extremely poor attack detection on this held-out capture. The results justify further investigation, but do not independently establish the cause of the performance failure.

**Artifact:** `data/cicids2017/processed/binary_capture_holdout_by_family.json`

**Next action:** Review the current working-tree changes and prepare a reproducible commit only after inspecting the diff and confirming that no unintended files are included.

### Git Change Review Preparation — 11 October 2026

**Objective:** Review the working tree after the per-family evaluation and warning-resolution changes.

**Checks:**
1. Identify modified and staged files.
2. Summarize tracked-file changes.
3. Check for whitespace errors.
4. Identify untracked files, including the new evaluation script and generated report if applicable.

**Safety:** No files will be staged, committed, or pushed during this inspection. Generated datasets, model artifacts, and unrelated files must not be included in a commit without explicit review.

**Status:** Review pending.

### Pre-Commit Content Review — 11 October 2026

**Git status:** One modified tracked file and one untracked Python script.

**Files under review:**
- `docs/research-log.md`
- `ml/evaluation/evaluate_capture_holdout_by_family.py`

**Review objectives:**
1. Confirm the research log documents the evaluation findings and validation steps.
2. Confirm the evaluation script uses feature names from the source report.
3. Confirm feature count and ordering are validated.
4. Confirm the feature matrix is converted to NumPy after numeric coercion and non-finite-value handling.
5. Confirm aggregate reconciliation checks remain present.

**Safety:** No staging, committing, or pushing until the review is complete.

**Status:** Content review pending.

### Feature-Schema Validation Review — 11 October 2026

**Finding:** The evaluation script obtains `expected_features` from the source report, but its empty-list validation checks `original_features` instead of `expected_features`.

**Risk:** If the source report lacks the feature list, the script may fail later with a less informative error instead of stopping at the schema-validation stage.

**Correction:** Change the guard to `if not expected_features:` and retain the feature-count and ordering checks.

**Other checks:** The script handles non-finite values before converting the feature matrix to NumPy, and aggregate row and prediction counts are reconciled against the existing report.

**Status:** One validation correction required before final review and commit.

### Final Pre-Commit Verification — 11 October 2026

**Validation correction:** The feature-schema guard now checks `expected_features`, the list loaded from the source evaluation report.

**Checks passed:**
- Python compilation completed without errors.
- `git diff --check` completed without errors.
- The corrected guard was confirmed in the evaluation script.

**Files expected to change:**
- `docs/research-log.md`
- `ml/evaluation/evaluate_capture_holdout_by_family.py`

**Next action:** Review the final diff, confirm the intended files only, then stage and commit the research log and evaluation script together. Do not include datasets, trained models, or generated evaluation reports.

**Status:** Validation correction complete; final review pending.

### Final Script and Research-Log Review — 11 October 2026

**Review outcome:**
- `docs/research-log.md` contains the evaluation findings and workflow notes.
- `ml/evaluation/evaluate_capture_holdout_by_family.py` uses the feature schema from the source report.
- The script validates feature count and ordering.
- Non-finite values are replaced before NumPy conversion.
- Aggregate row, attack, false-negative, and true-positive counts are reconciled against the original report.
- The evaluation completed without scikit-learn feature-name warnings.
- `git diff --check` passed.

**Pending files:** The research log is modified, and the evaluation script is untracked.

**Next action:** Stage only these two files, inspect the staged diff, and commit only after confirming that the staged content is correct.

**Status:** Review complete; staging pending.

### Evaluation Diagnostic Commit Preparation — 11 October 2026

**Final checks passed:**
- Staged whitespace validation completed without warnings.
- Python syntax compilation completed without errors.
- Exactly two files are staged:
  - `docs/research-log.md`
  - `ml/evaluation/evaluate_capture_holdout_by_family.py`

**Change purpose:** Add a reproducible evaluation-only diagnostic that reports held-out attack-family performance and documents the results.

**Scope:** No model retraining, model artifact changes, or dataset changes are included in the staged files.

**Status:** Ready for local commit; remote push pending.

### Post-Commit Working-Tree Review — 11 October 2026

**Latest local commit:** `2ff0a98` — `Add capture-holdout family evaluation`

**Observed status:**
- Local `main` is ahead of `origin/main` by one commit.
- `docs/research-log.md` has additional uncommitted changes.
- The evaluation script has been committed.

**Next action:** Inspect the remaining research-log diff to determine whether it contains a useful note added after the commit or an unintended change. Do not discard changes or push until the remaining diff is reviewed.

**Status:** Post-commit review pending.

### Capture-Holdout Evaluation Push Completed — 11 October 2026

**Pushed commits:**
- `2ff0a98` — Add capture-holdout family evaluation
- `20ecf45` — Document capture-holdout evaluation workflow

**Remote:** `origin/main`

**Push result:** Successful. The remote branch advanced from `1b6561c` to `20ecf45`.

**Next action:** Verify local and remote branch synchronization.

**Status:** Changes pushed; final synchronization check pending.

### Attack-Family Novelty vs Capture-Level Distribution Shift — 11 October 2026

**Background:** The existing binary Random Forest detected only 5 of 2,180 attacks in the held-out Thursday Morning WebAttacks capture. The family-level diagnostic reported 0% recall for Web Attack Brute Force, 0.46% for Web Attack XSS, and 9.52% for Web Attack Sql Injection.

**Research question:** To what extent can poor detection be associated with unfamiliar attack families versus capture-level distribution shift?

**Current limitation:** The held-out WebAttacks capture differs from the training data in both attack-family composition and capture characteristics. The existing experiment cannot isolate these effects.

**Next investigation:** Build a label-availability inventory across the processed CIC-IDS2017 captures. For each capture, record the original attack labels and their counts. Determine which attack families appear in multiple captures and which are restricted to a single capture.

**Constraints:**
1. Do not retrain or modify the existing model during this inventory step.
2. Preserve original attack labels rather than collapsing them into BENIGN and ATTACK.
3. Use the existing processed dataset and capture filenames.
4. Treat the inventory as descriptive evidence, not causal proof.

**Decision after inventory:** Use the observed label/capture overlap to determine whether a controlled evaluation can separate family novelty from capture-level shift.

**Status:** Dataset overlap inventory pending.

### Processed Dataset Inventory — 11 October 2026

**Objective:** Identify the processed CIC-IDS2017 CSV files, their capture filenames, and the existing code that handles labels.

**Checks:**
1. List processed CSV and JSON artifacts.
2. Inspect CSV file sizes to understand the scope of the inventory.
3. Review existing label and capture references in the training and evaluation scripts.

**Constraints:** Read-only inspection; no model retraining, data modification, or label remapping.

**Status:** File and label inventory pending.

### Processed Capture Inventory Findings — 11 October 2026

**Inventory result:** Eight processed CIC-IDS2017 capture CSVs are present in `data/cicids2017/processed/`.

**Capture files identified:**
- `cleaned_Monday-WorkingHours.pcap_ISCX.csv`
- `cleaned_Tuesday-WorkingHours.pcap_ISCX.csv`
- `cleaned_Wednesday-workingHours.pcap_ISCX.csv`
- `cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv`
- `cleaned_Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv`
- `cleaned_Friday-WorkingHours-Morning.pcap_ISCX.csv`
- `cleaned_Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`
- `cleaned_Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv`

**Relevant finding:** The existing binary capture-holdout training script converts original labels into BENIGN/ATTACK values. The separate family evaluation script preserves the original `Label` values for the held-out capture.

**Next investigation:** Count original labels by capture using chunked CSV reads. Report capture filename, original label, and row count. Verify that each capture's label counts sum to its total number of rows.

**Constraints:** Read-only analysis; no retraining, dataset modification, or binary label remapping.

**Status:** Capture filenames identified; label-overlap inventory pending.

### Capture-Level Original Label Inventory Results — 11 October 2026

**Status:** Inventory completed successfully across all eight processed CIC-IDS2017 captures.

| Capture | Rows | Distinct original labels |
|---|---:|---:|
| Monday Working Hours | 529,918 | 1 |
| Tuesday Working Hours | 445,909 | 3 |
| Wednesday Working Hours | 692,703 | 6 |
| Thursday Morning WebAttacks | 170,366 | 4 |
| Thursday Afternoon Infiltration | 288,602 | 2 |
| Friday Morning | 191,033 | 2 |
| Friday Afternoon DDoS | 225,745 | 2 |
| Friday Afternoon PortScan | 286,467 | 2 |

**Validation:** For all eight captures, the sum of original-label counts equalled the total row count.

**Initial observation:** The number of distinct labels varies substantially by capture. Monday has only one label, while Wednesday has six and Thursday Morning WebAttacks has four. This suggests label overlap must be examined explicitly before designing a controlled evaluation.

**Limitation:** Distinct-label counts alone do not identify the exact shared or capture-specific attack families and cannot establish the cause of model performance differences.

**Artifact:** `data/cicids2017/processed/capture_label_overlap_inventory.json`

**Next action:** Inspect the actual per-capture label counts and identify attack families present in multiple captures versus those restricted to one capture.

**Status:** Inventory complete; label-overlap analysis pending.

### Original Label Overlap Findings — 11 October 2026

**Status:** Capture-level label inventory inspected successfully.

#### 1. Original label distribution

| Capture | BENIGN rows | Attack families and counts |
|---|---:|---|
| Monday | 529,918 | None |
| Tuesday | 432,074 | FTP-Patator: 7,938; SSH-Patator: 5,897 |
| Wednesday | 440,031 | DoS GoldenEye: 10,293; DoS Hulk: 231,073; DoS Slowhttptest: 5,499; DoS slowloris: 5,796; Heartbleed: 11 |
| Thursday Morning — WebAttacks | 168,186 | Web Attack Brute Force: 1,507; Web Attack SQL Injection: 21; Web Attack XSS: 652 |
| Thursday Afternoon — Infiltration | 288,566 | Infiltration: 36 |
| Friday Morning | 189,067 | Bot: 1,966 |
| Friday Afternoon — DDoS | 97,718 | DDoS: 128,027 |
| Friday Afternoon — PortScan | 127,537 | PortScan: 158,930 |

#### 2. Initial interpretation

- Monday contains only BENIGN-labelled traffic.
- Tuesday and Wednesday contain multiple attack families.
- The Thursday Morning WebAttacks capture contains three web-attack labels.
- Infiltration, Bot, DDoS, and PortScan appear in their respective individual captures in this inventory.
- The label inventory establishes where labels occur, but it does not establish whether a family is intrinsically difficult to detect or whether capture-specific feature distributions explain model performance.

#### 3. Connection to the held-out evaluation

The binary Random Forest detected only 5 of 2,180 attack rows in the held-out Thursday Morning WebAttacks capture. Family-level recall was 0% for Brute Force, approximately 0.46% for XSS, and approximately 9.52% for SQL Injection.

These results motivate a more controlled investigation of capture-level and feature-distribution effects. They do not, by themselves, prove the cause of the poor recall.

**Artifact:** `data/cicids2017/processed/capture_label_overlap_inventory.json`

**Next action:** Compare the held-out capture's feature distributions with the training captures, beginning with a small, reproducible set of numeric features.

**Status:** Label inventory complete; feature-distribution comparison pending.

### Feature-Distribution Comparison — Planned Method — 11 October 2026

**Objective:** Investigate whether the held-out Thursday Morning WebAttacks capture differs from the eligible training captures in selected numeric feature distributions.

**Training captures:**
- Monday Working Hours
- Tuesday Working Hours
- Wednesday Working Hours
- Thursday Afternoon Infiltration

**Held-out capture:**
- Thursday Morning WebAttacks

**Preprocessing requirements:**
1. Use the existing 77 feature columns, excluding `Label`.
2. Apply numeric coercion consistently.
3. Treat positive and negative infinity as missing values.
4. Report missing-value rates rather than silently assuming all features are valid.
5. Compare robust summary statistics, including median and interquartile range, for selected features.
6. Do not retrain the model or alter the processed datasets.

**Interpretation limitation:** Differences in feature distributions can indicate covariate shift, but they do not establish its cause or prove that it explains poor attack recall. The held-out capture also contains attack families not represented in the training captures.

**Status:** Method planned; feature selection and implementation pending.

### Feature Selection for Capture-Distribution Analysis — 11 October 2026

**Status:** Feature schema verified.

The saved capture-holdout report contains 77 feature columns, excluding `Label`, and identifies the held-out capture as `cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv` with 170,366 rows.

**Initial features proposed for comparison:**

1. `Destination Port` — destination-port distribution.
2. `Flow Duration` — flow-duration distribution.
3. `Total Fwd Packets` — forward packet counts.
4. `Total Backward Packets` — backward packet counts.
5. `Flow Bytes/s` — flow byte rate.
6. `Flow Packets/s` — flow packet rate.
7. `Packet Length Mean` — average packet length.
8. `SYN Flag Count` — SYN flag counts.
9. `Init_Win_bytes_forward` — initial forward TCP window value.
10. `Idle Mean` — mean idle time.

These features cover ports, flow volume, rates, packet characteristics, TCP-related behavior, and timing. Their selection is exploratory, not a claim that they are the most important features for detecting web attacks.

**Planned comparison:** Compare the combined eligible training captures against the held-out capture using medians, interquartile ranges, missing-value rates, and selected quantiles. Preserve the original training/held-out separation and do not retrain the model.

**Limitation:** Summary-statistic differences are descriptive evidence of distribution differences, not proof of their cause or of their effect on model performance.

**Next action:** Implement a chunked, read-only feature-summary script and validate its output.

### Script Validation and Memory Review — 11 October 2026

**Validation results:**
- Python compilation produced no reported syntax error.
- `git diff --check` reported a trailing blank line at the end of `docs/research-log.md`.
- Git status showed the research log modified and two evaluation scripts untracked.

**Memory review:** The initial feature-distribution script reads CSV files in chunks but retains all valid values for each selected feature to calculate exact quantiles. Chunked input alone therefore does not guarantee low memory usage.

**Next action:** Remove the unnecessary trailing blank line from the research log and revise the comparison method to use bounded-memory summaries before executing the analysis.

**Status:** Syntax check appears successful; formatting and memory-efficiency improvements pending.


### Feature Analysis Memory Optimization — 11 October 2026

**Previous issue:** The initial comparison script read CSVs in chunks but retained every valid value for each selected feature. This could consume excessive RAM under the WSL memory limit.

**Planned improvement:**
- Continue reading CSVs in chunks of 50,000 rows.
- Calculate bounded-memory descriptive summaries.
- Report valid and missing counts, missing-value rates, minimum, maximum, mean, standard deviation, and approximate quantiles.
- Clearly document the quantile estimation method and its limitations.
- Preserve the same four training captures, held-out capture, and ten selected features.
- Do not retrain the model or modify processed CSV files.

**Status:** Research-log whitespace warning resolved; memory optimization pending.

### Reservoir-Sampling Correctness Review — 11 October 2026

**Status:** Revised feature-distribution script saved but not executed.

**Issue identified:** The current implementation combines the existing reservoir with incoming values and uses separate replacement logic depending on reservoir size. This complicates correctness verification and risks producing an incorrectly sampled population.

**Required correction:**
- Implement standard reservoir sampling with a clearly maintained count of valid observations.
- Keep no more than 100,000 sampled values per feature per capture.
- Ensure missing and non-finite values are excluded consistently.
- Make sampling reproducible using a fixed random seed.
- Verify the implementation with a small synthetic dataset before processing the CIC-IDS2017 captures.

**Safety of the experiment:** No model retraining or processed-dataset modification is intended.

**Next action:** Replace the sampling logic with a simpler, verifiable implementation and test it before running the full analysis.

### Synthetic Validation of Reservoir Sampling — 11 October 2026

**Objective:** Verify that the corrected feature-sampling algorithm respects the configured reservoir size and produces reproducible results.

**Checks planned:**
1. The reservoir never exceeds its configured capacity.
2. Every observation in a small synthetic stream is eligible for selection.
3. Repeated runs with the same random seed produce the same reservoir.
4. The sample size equals the population size when the population is smaller than the reservoir capacity.

**Scope:** Synthetic data only. No processed dataset is scanned, and no model is retrained.

**Status:** Sampling implementation revised; synthetic validation pending.

### Feature-Distribution Comparison Execution — 11 October 2026

**Status:** Analysis script executed successfully.

Five captures were scanned:

| Capture | Rows scanned |
|---|---:|
| Monday Working Hours | 529,918 |
| Thursday Afternoon Infiltration | 288,602 |
| Tuesday Working Hours | 445,909 |
| Wednesday Working Hours | 692,703 |
| Thursday Morning WebAttacks (held out) | 170,366 |
| **Total** | **2,127,498** |

The script completed each capture and reported that feature summaries were calculated.

**Output artifact:** `data/cicids2017/processed/capture_feature_distribution_comparison.json`

**Method:** Chunked CSV reading and bounded reservoir sampling for ten selected numeric features. Quantiles and sample-based statistics are approximate.

**Limitations:** Successful execution does not establish that the held-out capture differs significantly from the training captures. Distribution differences and their relationship to attack recall remain to be examined. The report is descriptive and does not represent model retraining.

**Next action:** Inspect the saved JSON report and compare the feature summaries between the combined training captures and the held-out capture.

**Status:** Analysis executed; interpretation pending.

### Feature-Distribution Report Inspection — 11 October 2026

**Objective:** Inspect the completed feature-distribution report and identify descriptive differences between the eligible training captures and the held-out Thursday Morning WebAttacks capture.

**Report:** `data/cicids2017/processed/capture_feature_distribution_comparison.json`

**Values to examine:**
- Median and interquartile range (Q1–Q3).
- Missing-value rates.
- Valid observation counts.
- Approximate sample-based statistics and their limitations.

**Interpretation rules:**
- Compare the held-out capture with individual training captures, not only a pooled summary.
- Large numerical differences are observations, not proof of causation.
- Do not infer feature importance from distribution differences alone.
- Do not modify the model or source datasets during inspection.

**Status:** Report generated; detailed inspection pending.

### Initial Feature-Distribution Findings — 11 October 2026

**Status:** The feature-distribution report has been inspected.

**Observations:**
- `Destination Port`, `Total Fwd Packets`, `Total Backward Packets`, `SYN Flag Count`, and `Idle Mean` have the same reported median in the held-out capture and the four eligible training captures.
- `Flow Duration`, `Flow Bytes/s`, `Flow Packets/s`, `Packet Length Mean`, and `Init_Win_bytes_forward` show differences in their reported medians across captures.
- The held-out capture has approximately 0.079% missing values in `Flow Bytes/s` and `Flow Packets/s`.
- These are descriptive observations based on reservoir-sample statistics; the reported quantiles are approximate.

**Interpretation limitation:** Similar medians do not imply identical distributions. Different medians do not establish causation or explain the model's low attack recall. The attack-family composition also differs between training and held-out captures.

**Next action:** Inspect whether the selected features contain extreme values or strongly skewed distributions that make median comparisons insufficient. Avoid attributing the recall failure to any single feature without further evidence.

**Status:** Initial comparison complete; distribution-shape investigation pending.

### Distribution Shape and Extreme Values — 11 October 2026

**Status:** Initial sample-based distribution-shape inspection completed.

**Observations:**
- `Flow Duration` has a held-out median of approximately 31,420 and a sample mean of approximately 12.57 million.
- `Flow Bytes/s` has a held-out median of approximately 4,764 and a sample mean of approximately 1.847 million.
- `Flow Packets/s` also shows a large difference between its median and sample mean.
- `Packet Length Mean` has a held-out median of approximately 57.8 and a sample mean of approximately 99.87.
- `Init_Win_bytes_forward` has a held-out median of 58 and a sample mean of approximately 6,263.
- The sampled extrema include negative values for `Flow Duration`, `Flow Bytes/s`, and `Flow Packets/s`.

**Interpretation:** These differences are consistent with strongly skewed distributions and possible extreme observations. Because the statistics are reservoir-sample estimates, they do not establish the exact full-dataset extrema or their frequencies.

**Next action:** Inspect the original processed CSVs for negative and non-finite values in the selected features, counting occurrences by capture without modifying any data.

**Status:** Distribution-shape inspection complete; value-quality investigation pending.

### Feature Value-Quality Check — 11 October 2026

**Status:** Read-only check completed across the five captures.

**Held-out Thursday Morning WebAttacks capture:**
- `Flow Duration`: 11 negative values out of 170,366 rows.
- `Flow Bytes/s`: 10 negative values and 135 missing values.
- `Flow Packets/s`: 11 negative values and 135 missing values.
- `Packet Length Mean`: no negative or missing values.
- `Init_Win_bytes_forward`: 81,911 negative values, approximately 48.08% of rows.

**Cross-capture observations:**
- Negative values in `Flow Duration` and `Flow Packets/s` are rare in every inspected capture.
- Missing values in `Flow Bytes/s` and `Flow Packets/s` vary by capture.
- Negative values in `Init_Win_bytes_forward` are common across all inspected captures and require interpretation using the feature's encoding conventions. They should not be removed or replaced without justification.

**Interpretation limitation:** These counts identify data characteristics but do not establish that any feature caused the held-out model's poor attack recall.

**Next action:** Inspect the distinct negative values in the selected features, especially `Flow Duration`, `Flow Bytes/s`, `Flow Packets/s`, and `Init_Win_bytes_forward`, without changing the dataset or model.

**Status:** Value-quality counts complete; negative-value interpretation pending.

### Distinct Negative-Value Patterns — 11 October 2026

**Status:** Distinct negative values inspected across five captures.

**Observations:**
- All observed negative values of `Init_Win_bytes_forward` are `-1`.
- Negative `Flow Duration` values are mostly `-1`, with a small number of `-2` and `-4` observations.
- Negative `Flow Packets/s` values are concentrated at `-2,000,000`, with a few other values.
- Negative `Flow Bytes/s` values are concentrated at `-12,000,000`, but the held-out capture contains one value of `-261,000,000`.

**Interpretation limitation:** Repeated negative values may reflect dataset encoding or flow-calculation behavior, but their cause has not yet been established. No values were changed or removed.

**Next action:** Inspect the affected records alongside their original labels and related flow features to investigate whether the negative rate and duration values occur together.

**Status:** Negative-value inventory complete; record-level investigation pending.

### Record-Level Investigation of Negative Flow Values — 11 October 2026

**Objective:** Inspect a small sample of records containing negative flow-duration or flow-rate values, preserving their original labels and related feature values.

**Fields to inspect:**
- `Label`
- `Destination Port`
- `Flow Duration`
- `Total Fwd Packets`
- `Total Backward Packets`
- `Flow Bytes/s`
- `Flow Packets/s`
- `Packet Length Mean`
- `Init_Win_bytes_forward`

**Method:** Read-only, chunked inspection of the processed captures. Print a maximum of five matching records per capture.

**Limitations:** A small sample can illustrate patterns but cannot establish the cause or prevalence of an anomaly beyond the previously calculated counts. No preprocessing changes or model retraining are planned.

**Status:** Record-level investigation planned.

### Record-Level Negative Flow Value Findings — 11 October 2026

**Status:** Read-only record inspection completed across five captures.

**Observed pattern:**
- The first five matching records in each capture were labelled `BENIGN`.
- These sampled records had `Flow Duration = -1`, one forward packet, and one backward packet.
- Negative `Flow Packets/s` values frequently occurred alongside negative flow duration.
- Negative `Flow Bytes/s` values were also observed in many matching records.
- One sampled record from the held-out Thursday Morning WebAttacks capture had `Flow Bytes/s = -261,000,000`.

**Interpretation limitation:** These records illustrate a recurring pattern but do not establish the cause of the values, their overall impact on predictions, or whether they explain poor attack recall. The sample was selected by a negative-value condition and is not representative of the full capture.

**Next action:** Quantify how often the negative-duration pattern occurs and determine whether its frequency differs between BENIGN and ATTACK records in the held-out capture.

**Status:** Example records inspected; label-conditioned frequency analysis pending.

### Label-Conditioned Negative Flow Duration Analysis — 11 October 2026

**Dataset:** Held-out Thursday Morning WebAttacks capture
**Method:** Read-only, chunked scan of `Label` and `Flow Duration`.

| Original label | Total rows | Negative Flow Duration | Percentage |
|---|---:|---:|---:|
| BENIGN | 168,186 | 11 | 0.006540% |
| ATTACK | 2,180 | 0 | 0.000000% |
| Total | 170,366 | 11 | 0.006456% |

**Validation:** The label-group totals reconcile to the 170,366 rows in the capture.

**Finding:** All 11 records with `Flow Duration < 0` are labelled BENIGN. No attack records in this capture have negative flow duration.

**Interpretation limitation:** Negative flow duration is rare in this capture. These counts do not explain the model's poor attack recall and do not establish the cause or predictive impact of the negative values.

**Next action:** Quantify negative `Flow Bytes/s` and `Flow Packets/s` values by original label in the same held-out capture.

**Status:** Label-conditioned negative-duration counts completed; rate-feature analysis pending.

### Label-Conditioned Rate-Feature Quality Analysis — 11 October 2026

**Dataset:** Held-out Thursday Morning WebAttacks capture
**Method:** Read-only, chunked scan of `Label`, `Flow Bytes/s`, and `Flow Packets/s`.

| Feature | BENIGN rows | BENIGN negative | BENIGN missing/non-numeric | ATTACK rows | ATTACK negative | ATTACK missing/non-numeric |
|---|---:|---:|---:|---:|---:|---:|
| Flow Bytes/s | 168,186 | 10 (0.005946%) | 135 (0.080268%) | 2,180 | 0 | 0 |
| Flow Packets/s | 168,186 | 11 (0.006540%) | 135 (0.080268%) | 2,180 | 0 | 0 |

**Validation:** The scan covered 170,366 records, comprising 168,186 BENIGN and 2,180 ATTACK records.

**Findings:** All observed negative and missing rate values occurred in BENIGN records. Negative values were rare, and missing values affected 135 BENIGN records for each feature. No ATTACK record had a negative or missing value in either feature.

**Interpretation limitation:** These counts do not establish why the values are negative or missing, whether they caused individual false positives, or whether they explain poor attack recall.

**Next action:** Review the current preprocessing and model-inference pipeline to verify how missing and negative feature values are handled before making any changes.

**Status:** Label-conditioned rate-feature quality counts completed; preprocessing review pending.

### Preprocessing Pipeline Review — 11 October 2026

**Status:** Initial source-code search completed; targeted code inspection pending.

**Observed from source search:**
- The capture-holdout training script replaces positive and negative infinity with missing values.
- The training pipeline uses `SimpleImputer(strategy="median")`.
- The family evaluation script also replaces positive and negative infinity with missing values before prediction.
- The source search does not establish whether negative finite values are transformed, rejected, or passed directly to the model.

**Next action:** Inspect the feature-loading, imputation, and prediction code in the capture-holdout training and family-evaluation scripts before proposing preprocessing changes.

### Preprocessing Source-Code Inspection — 11 October 2026

**Files inspected:**
- `ml/training/train_binary_capture_holdout.py`
- `ml/evaluation/evaluate_capture_holdout_by_family.py`

**Confirmed behavior:**
- Training converts feature columns to numeric values using `pd.to_numeric(errors="coerce")`.
- Training replaces positive and negative infinity with `NaN`.
- The saved model pipeline uses `SimpleImputer(strategy="median")` before the Random Forest classifier.
- Family evaluation converts feature columns to numeric values and replaces positive and negative infinity with `NaN` before prediction.
- The inspected code does not explicitly replace finite negative feature values.

**Interpretation:** Negative finite values can reach the imputer and classifier unchanged. Missing values are handled by the pipeline's median imputer, subject to the fitted imputer's behavior.

**Limitation:** Source inspection alone does not establish whether negative or missing values cause incorrect predictions. No model or dataset changes were made.

**Next action:** Inspect false-positive and false-negative records to determine whether the suspicious feature values occur in actual model errors.

**Status:** Preprocessing code inspected; prediction-error analysis pending.

### Prediction-Error Analysis Preparation — 11 October 2026

**Objective:** Determine whether suspicious feature values are associated with false-positive or false-negative predictions in the held-out capture.

**Existing evaluation results:**
- False positives: 56.
- False negatives: 2,175.
- True positives: 5.
- True negatives: 168,130.

**Approach:** Inspect the existing prediction-confidence and error-analysis implementation before adding new diagnostics. Preserve the saved model, current preprocessing, and dataset unchanged.

**Limitations:** The aggregate confusion matrix does not establish whether negative or missing feature values contribute to individual prediction errors.

**Next action:** Inspect `ml/evaluation/inspect_prediction_confidence.py` to identify its existing prediction, confidence, and output logic.

**Status:** Error-analysis preparation documented; source inspection pending.

### Prediction-Confidence Source Inspection — 11 October 2026

**Objective:** Inspect the existing prediction-confidence script before implementing additional error diagnostics.

**Target file:** `ml/evaluation/inspect_prediction_confidence.py`

**Questions to resolve:**
1. How are the saved model and held-out capture loaded?
2. How are missing and infinite feature values handled?
3. How are predictions and attack probabilities calculated?
4. Are false-positive and false-negative records identified and their feature values retained?
5. What output files and summary statistics are produced?

**Constraint:** This is a read-only source inspection. No model, dataset, or preprocessing changes are authorized at this stage.

**Status:** Inspection requested; findings pending.

### Prediction-Confidence Script Review — 11 October 2026

**File inspected:** `ml/evaluation/inspect_prediction_confidence.py`

**Findings:**
- The script loads `ml/models/binary_random_forest.joblib`, not the capture-holdout model.
- It samples up to 2,000 records per original label in each of three Friday captures.
- It converts infinite feature values to missing values and predicts using the loaded model.
- Its final results contain capture name, true label, predicted label, and attack probability, but not the original feature values.
- Its output is a summary grouped by capture and true label.

**Limitation:** This script evaluates a different model on different captures. Its results cannot be treated as direct evidence explaining the errors of the capture-holdout model.

**Next action:** Inspect the capture-holdout model's saved feature metadata and the existing error-analysis outputs before designing a record-level diagnostic for the correct model.

**Status:** Existing confidence script reviewed; dedicated capture-holdout error analysis still needed.

### Capture-Holdout Report Metadata Inspection — 11 October 2026

**Objective:** Verify the feature metadata recorded in the capture-holdout evaluation report before implementing record-level prediction-error diagnostics.

**Target report:** `data/cicids2017/processed/binary_capture_holdout_report.json`

**Checks:**
- Identify the report's top-level fields.
- Locate any recorded feature names and their ordering.
- Review available model, training, holdout, and imputation metadata.

**Constraint:** Read-only inspection; no model retraining, dataset modification, or preprocessing changes.

**Status:** Report metadata inspection pending.

### Capture-Holdout Report Metadata Verified — 11 October 2026

**Report:** `data/cicids2017/processed/binary_capture_holdout_report.json`

**Findings:**
- The report contains 77 feature names in the recorded feature order.
- The recorded training sample contains 300,000 rows.
- The report identifies median imputation fitted on the training sample only.
- The report records the held-out capture, training captures, confusion matrix, classification metrics, model configuration, and limitations.

**Implication:** Future record-level diagnostics should use the feature names and order recorded in this report and the corresponding capture-holdout model.

**Limitation:** The report does not provide individual false-positive or false-negative records with their original feature values.

**Next action:** Verify that the saved capture-holdout model's input feature names and ordering match the report metadata before running further error analysis.

**Status:** Report metadata inspected; model/report feature compatibility check pending.

### Model/Report Feature Compatibility Check — 11 October 2026

**Objective:** Verify that the saved capture-holdout model expects the feature count and ordering recorded in the evaluation report.

**Artifacts:**
- `ml/models/binary_random_forest_capture_holdout.joblib`
- `data/cicids2017/processed/binary_capture_holdout_report.json`

**Checks:** Compare input feature counts, compare feature names and ordering when stored by the model, and inspect the model classes and pipeline steps.

**Constraint:** Read-only artifact inspection; no retraining or data modification.

**Status:** Compatibility check pending.

### Model/Report Compatibility Check — 11 October 2026

**Artifacts inspected:**
- `ml/models/binary_random_forest_capture_holdout.joblib`
- `data/cicids2017/processed/binary_capture_holdout_report.json`

**Results:**
- Report feature count: 77.
- Model input feature count: 77.
- The saved model does not expose `feature_names_in_`, so direct name-and-order comparison was unavailable.
- Model classes are `[0, 1]`.
- Pipeline steps are `imputer` and `classifier`.

**Interpretation:** The feature counts and class encoding are consistent with the expected setup, but feature ordering remains unverified.

**Next action:** Inspect the capture-holdout training script to confirm how the training feature order is selected and recorded.

**Status:** Feature-count compatibility confirmed; feature-order verification pending.

### Training Feature-Order Source Inspection — 11 October 2026

**Objective:** Verify how `train_binary_capture_holdout.py` selects and orders model input features and records that order in the evaluation report.

**Checks:**
- Determine how the target `Label` column is excluded.
- Identify how feature names and column order are established.
- Verify how the training sample preserves the selected columns.
- Locate the report-generation logic for `feature_names`.

**Constraint:** Read-only source inspection; no model retraining or data modification.

**Status:** Training feature-order inspection pending.

### Training Feature-Order Source Inspection — 11 October 2026

**File:** `ml/training/train_binary_capture_holdout.py`

**Findings:**
- The training script reads the CSV header, strips column-name whitespace, and excludes `Label` to define `expected_features`.
- It checks that each training capture's feature names and ordering match `expected_features`.
- It converts features to NumPy arrays in that established order.
- It performs the same feature-schema check on the held-out capture before evaluation.
- The report records `expected_features` in its `feature_names` field.

**Interpretation:** The training script is designed to preserve a consistent feature order across training and evaluation.

**Limitation:** Source inspection alone does not prove that the currently saved model and report were generated together from the inspected source version.

**Next action:** Inspect the earlier portion of the training script where `expected_features` is established, then verify its consistency with the processed CSV header.

**Status:** Feature-order logic reviewed; artifact provenance and direct ordering verification pending.

### Direct Feature-Order Comparison — 11 October 2026

**Objective:** Compare the capture-holdout report's recorded feature list with the processed Monday CSV header.

**Method:** Read the CSV header only, strip column-name whitespace, exclude `Label`, and compare the resulting ordered list against the report's `feature_names`.

**Constraint:** Read-only comparison; no model or dataset modifications.

**Status:** Direct comparison pending.

### Direct Feature-Order Comparison — 11 October 2026

**Result:** Passed.

- Processed Monday CSV feature count: 77.
- Capture-holdout report feature count: 77.
- Ordered feature lists match exactly after trimming whitespace and excluding `Label`.
- The CSV contains exactly one `Label` column.

**Interpretation:** The report's feature list matches the processed Monday CSV header used as the reference schema by the training script.

**Limitation:** This comparison does not independently establish the saved model's historical training provenance or its original feature ordering.

**Next action:** Review the capture-holdout training source's initial schema-establishment code to complete the source-level feature-order audit before designing record-level prediction-error analysis.

**Status:** Report-to-header feature-order comparison passed.

### Training Schema Establishment Review — 11 October 2026

**Objective:** Inspect the initial schema-establishment section of the capture-holdout training script.

**Target:** `ml/training/train_binary_capture_holdout.py`, lines 65–125.

**Checks:**
- Identify the source of `expected_features`.
- Confirm how the target column is excluded.
- Confirm when feature-schema validation occurs.

**Constraint:** Read-only source inspection; no model retraining or dataset modification.

**Status:** Initial schema-establishment review pending.

### Training Schema Establishment Review — 11 October 2026

**File:** `ml/training/train_binary_capture_holdout.py`

**Findings:**
- The script establishes `expected_features` from the first configured training capture's CSV header.
- It strips column-name whitespace and excludes the `Label` target column.
- It checks feature names and ordering across all configured training captures and the held-out capture before sampling or fitting.
- It requires exactly 77 input features.
- During training, each chunk is checked against the established feature order before conversion to a NumPy array.

**Conclusion:** The source implements consistent feature-schema validation across the configured captures. Together with the successful report-to-Monday-header comparison, this supports schema consistency in the documented workflow.

**Limitation:** The saved model does not expose feature names, so its historical training order cannot be independently verified from model metadata alone.

**Next action:** Begin a record-level diagnostic using the correct capture-holdout model and held-out capture, retaining the original labels, predictions, and selected suspicious feature values.

**Status:** Source-level schema audit completed; record-level error analysis pending.

### False-Negative Record Diagnostic Preparation — 11 October 2026

**Objective:** Identify whether an existing evaluation script can support record-level investigation of false negatives from the capture-holdout experiment.

**Scope:**
- Use `binary_random_forest_capture_holdout.joblib`.
- Use the held-out Thursday Morning WebAttacks capture.
- Preserve original attack-family labels.
- Inspect selected feature values for actual false-negative records.
- Keep the analysis read-only.

**Constraint:** Do not retrain the model, alter feature handling, or modify the processed dataset.

**Next action:** Inventory the existing evaluation scripts and select the appropriate implementation path.

**Status:** Record-level diagnostic preparation pending.

### Existing Family-Evaluation Script Review — 11 October 2026

**File:** `ml/evaluation/evaluate_capture_holdout_by_family.py`

**Objective:** Determine whether the existing family-level evaluation can support record-level false-negative analysis.

**Checks:**
- Confirm the model and held-out capture used.
- Review label preservation and prediction logic.
- Determine whether individual misclassified records and selected feature values are retained.
- Identify any output-file side effects.

**Constraint:** Read-only source inspection; do not execute or modify the evaluation script during this review.

**Status:** Script review pending.

### Family-Evaluation Script Review — 11 October 2026

**File:** `ml/evaluation/evaluate_capture_holdout_by_family.py`

**Findings:**
- Loads `binary_random_forest_capture_holdout.joblib`.
- Uses the held-out Thursday Morning WebAttacks capture.
- Validates the held-out capture's feature names and ordering against the source report.
- Converts non-numeric values to missing values and replaces positive and negative infinity with missing values before prediction.
- Aggregates true positives and false negatives by original attack family.
- Validates the evaluated row count and attack/false-negative/true-positive counts against the source report.
- Writes aggregate results to `binary_capture_holdout_by_family.json`.
- Does not retain individual misclassified records or their feature values.

**Decision:** Preserve this evaluator unchanged and create a separate read-only diagnostic for individual false-negative records.

**Next action:** Define the diagnostic's output fields and sampling strategy before implementing it.

**Status:** Existing evaluator reviewed; dedicated record-level diagnostic selected.

### Record-Level Diagnostic Design — 11 October 2026

**Objective:** Investigate feature values in false-negative records from the held-out Thursday Morning WebAttacks capture.

**Input artifacts:**
- `ml/models/binary_random_forest_capture_holdout.joblib`
- `data/cicids2017/processed/binary_capture_holdout_report.json`
- The held-out Thursday Morning WebAttacks processed CSV.

**Proposed output:** A separate CSV containing every false-negative record, its original attack-family label, predicted label, attack probability, selected suspicious feature values, and flags for negative or missing values.

**Selected features:**
- `Flow Duration`
- `Flow Bytes/s`
- `Flow Packets/s`
- `Init_Win_bytes_forward`

**Method:** Perform chunked inference using the existing saved model and preprocessing pipeline. Preserve original labels, use the report's feature order, and validate the resulting false-negative count against the existing evaluation report.

**Safeguards:** Do not retrain the model, modify the dataset, or change preprocessing. Keep the existing family-evaluation script unchanged.

**Interpretation limitation:** Associations between suspicious feature values and false negatives do not establish causation.

**Status:** Diagnostic design proposed; implementation pending approval.

### False-Negative Diagnostic Implementation — 11 October 2026

**Script:** `ml/evaluation/inspect_capture_holdout_false_negatives.py`

**Implementation:**
- Loads the existing capture-holdout model and source report.
- Checks the expected capture, feature count, and feature ordering.
- Processes the held-out capture in chunks.
- Identifies records whose original label is non-BENIGN and whose prediction is BENIGN.
- Preserves original labels and records attack probabilities, selected feature values, and negative/missing-value flags.
- Writes results to `capture_holdout_false_negatives.csv`.
- Validates scanned row count and false-negative count against the existing report.

**Safeguards:** The script does not retrain the model or alter the source capture. The diagnostic output is separate from the existing evaluation report.

**Status:** Script created; syntax and whitespace checks pending; full diagnostic execution pending.

### False-Negative Diagnostic Initial Checks — 11 October 2026

**Script:** `ml/evaluation/inspect_capture_holdout_false_negatives.py`

**Initial results:**
- Python compilation completed without a reported syntax error.
- `git diff --check` reported trailing whitespace in `docs/research-log.md` at lines 1834 and 1855.

**Required follow-up:**
- Inspect the diagnostic script's ending to verify that the full file was saved correctly.
- Remove trailing whitespace from the research log.
- Rerun the syntax and whitespace checks.

**Constraint:** Do not execute the full diagnostic until the file-integrity and whitespace checks are clean.

**Status:** Initial syntax check passed; file-integrity inspection and whitespace cleanup pending.

### False-Negative Diagnostic Verification — 11 October 2026

**Script:** `ml/evaluation/inspect_capture_holdout_false_negatives.py`

**Results:**
- Python syntax compilation passed.
- The script's ending and entry point were inspected and are intact.
- `git diff --check` passed after removing trailing whitespace from the research log.

**Conclusion:** The script passes the initial syntax and whitespace checks.

**Next action:** Execute the diagnostic against the held-out capture and verify the scanned row count and false-negative count against the existing evaluation report.

**Status:** Initial verification passed; full diagnostic execution pending.

### False-Negative Diagnostic Execution — 11 October 2026

**Script:** `ml/evaluation/inspect_capture_holdout_false_negatives.py`

**Action:** Run the diagnostic using the existing capture-holdout model and held-out Thursday Morning WebAttacks capture.

**Expected validation targets:**
- Scanned rows: 170,366.
- False-negative records: 2,175.

**Output:** `data/cicids2017/processed/capture_holdout_false_negatives.csv`

**Constraint:** Do not retrain the model or modify the source dataset.

**Status:** Execution requested; actual counts and output validation pending.

### False-Negative Diagnostic Execution Results — 11 October 2026

**Script:** `ml/evaluation/inspect_capture_holdout_false_negatives.py`

**Results:**
- Capture rows scanned: 170,366.
- False-negative records extracted: 2,175.
- Both counts matched the existing capture-holdout report.
- Output written to `data/cicids2017/processed/capture_holdout_false_negatives.csv`.

**Warning observed:** Scikit-learn emitted warnings that the `SimpleImputer` was fitted without feature names while inference inputs contained feature names. The run completed successfully, but the warning's origin should be investigated before considering the workflow fully clean.

**Interpretation:** The record-level diagnostic reproduced the expected false-negative count. This validates the record count, not the causal explanation for the model's errors.

**Next action:** Inspect the generated CSV's columns, label distribution, and selected feature flags before drawing conclusions about false negatives.

**Status:** Diagnostic completed; count validation passed; warning investigation and output analysis pending.

### False-Negative Feature Summary — 11 October 2026

**Input:** `data/cicids2017/processed/capture_holdout_false_negatives.csv`

**Objective:** Summarize original attack-family labels, suspicious feature flags, selected feature-value ranges, and attack probabilities among the extracted false-negative records.

**Method:** Read the diagnostic CSV and calculate aggregate counts and descriptive statistics without rerunning predictions.

**Constraint:** Read-only analysis; no changes to the model, dataset, or diagnostic output.

**Status:** Summary command prepared; observed results pending.

### False-Negative Feature Summary Results — 11 October 2026

**Input:** `data/cicids2017/processed/capture_holdout_false_negatives.csv`

**Validation:**
- False-negative records: 2,175.
- Web Attack Brute Force: 1,507.
- Web Attack XSS: 649.
- Web Attack Sql Injection: 19.

**Selected-feature quality findings:**
- Negative `Flow Duration`: 0 records.
- Negative `Flow Bytes/s`: 0 records.
- Negative `Flow Packets/s`: 0 records.
- Missing `Flow Bytes/s` or `Flow Packets/s`: 0 records.
- Negative `Init_Win_bytes_forward`: 0 records.

**Attack probability:** Median approximately 0.062761; maximum approximately 0.487569.

**Interpretation:** The selected negative and missing feature-value patterns do not occur in the extracted false-negative records. Therefore, they do not directly explain these errors. The low attack probabilities are consistent with the classifier assigning BENIGN predictions to these attack records.

**Limitation:** This analysis covers only four selected features and the false-negative subset. It does not establish the underlying cause of poor attack recall or exclude other feature-distribution, representation, or model-generalization problems.

**Next action:** Compare selected feature distributions between the held-out BENIGN records and the missed attack families to identify potential areas for further investigation.

**Status:** False-negative feature summary completed; comparative analysis pending.

### BENIGN vs. Missed Brute Force Comparison — 11 October 2026

**Objective:** Compare selected feature distributions between BENIGN records and missed Web Attack Brute Force records in the held-out capture.

**Attack subset:** The 1,507 Brute Force records already identified as false negatives.

**Initial features:** `Destination Port`, `Flow Duration`, `Total Fwd Packets`, `Total Backward Packets`, `Flow Bytes/s`, `Flow Packets/s`, `Packet Length Mean`, and `Init_Win_bytes_forward`.

**Method:** Calculate chunk-based descriptive statistics for the held-out BENIGN group and compare them with the false-negative diagnostic records. Preserve the source data and saved model.

**Interpretation limitation:** Differences between these groups may suggest useful follow-up experiments but do not establish causation or prove that any single feature explains the model's errors.

**Status:** Comparative distribution analysis planned; results pending.

### BENIGN vs. Missed Brute Force Comparison — Execution — 11 October 2026

**Method:** Read the held-out capture in chunks, collect BENIGN feature values, and compare their descriptive distributions with the 1,507 missed Brute Force records.

**Features:** Destination Port, Flow Duration, Total Fwd Packets, Total Backward Packets, Flow Bytes/s, Flow Packets/s, Packet Length Mean, and Init_Win_bytes_forward.

**Statistics:** Median and interquartile range (25th–75th percentiles), with valid observation counts.

**Constraint:** Read-only analysis; no retraining or changes to the source capture.

**Status:** Comparison command prepared; observed distributions pending.

### Feature-Comparison Column Mismatch — 11 October 2026

**Attempted analysis:** Compare BENIGN and missed Brute Force records across eight selected features.

**Observed issue:** The diagnostic CSV contains only the four selected feature values, four flags, capture row, original label, predicted label, and attack probability. It does not contain `Destination Port`, `Total Fwd Packets`, `Total Backward Packets`, or `Packet Length Mean`.

**Cause:** The comparison attempted to select features from the diagnostic CSV that were never exported into it.

**Resolution plan:** Verify the saved diagnostic columns and row identifiers, then retrieve the missing features from the original held-out capture using the recorded capture row numbers.

**Constraint:** Do not alter the source dataset, model, or diagnostic output.

**Status:** Comparison stopped safely; source-row-based feature retrieval pending.

### Diagnostic Row-Identifier Verification — 11 October 2026

**Input:** `data/cicids2017/processed/capture_holdout_false_negatives.csv`

**Results:**
- Diagnostic records: 2,175.
- Minimum `Capture_Row`: 12,638.
- Maximum `Capture_Row`: 93,287.
- The diagnostic contains only the selected feature values and flags; four features needed for the planned comparison were not exported.

**Interpretation:** The saved row identifiers provide a way to retrieve omitted feature values from the original capture. These identifiers are 1-based data-row positions, excluding the CSV header.

**Next action:** Retrieve the four missing features for the false-negative rows from the original capture, then compare their distributions with the BENIGN group.

**Status:** Diagnostic row identifiers verified; source-feature retrieval pending.

### False-Negative Feature Retrieval and Summary — 11 October 2026

**Objective:** Retrieve four features omitted from the false-negative diagnostic CSV and summarize their values by original attack family.

**Source:** `cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv`, matched using the recorded `Capture_Row` identifiers.

**Results:**
- Successfully retrieved all 2,175 false-negative records.
- Brute Force: 1,507 records.
- XSS: 649 records.
- SQL Injection: 19 records.
- Destination Port was 80 for all 2,175 records.
- Median Total Fwd Packets was 3 for Brute Force and XSS.
- Median Total Backward Packets was 1 for Brute Force and XSS.
- Median Packet Length Mean was 0 for Brute Force and XSS.

**Interpretation:** The missed records frequently have low packet counts and a Packet Length Mean of zero. These are descriptive observations, not proof of the cause of misclassification. The small SQL Injection sample limits conclusions about that family.

**Next action:** Compare the feature distributions of missed attacks against correctly detected attacks and benign traffic before making causal claims.

**Status:** Source-feature retrieval and descriptive summaries completed.

### Three-Group Feature Comparison Plan — 11 October 2026

**Objective:** Compare missed attacks, detected attacks, and benign traffic in the held-out Thursday Morning WebAttacks capture.

**Groups:**
1. Missed attacks: actual attack, predicted benign.
2. Detected attacks: actual attack, predicted attack.
3. Benign traffic: actual benign, regardless of prediction.

**Features:**
- Destination Port
- Flow Duration
- Total Fwd Packets
- Total Backward Packets
- Flow Bytes/s
- Flow Packets/s
- Packet Length Mean
- Init_Win_bytes_forward

**Method:** Use the saved capture-holdout model and original capture labels. Summarize counts, medians, and quartiles for each group. Keep the original data and model unchanged.

**Limitation:** Distribution differences may identify useful hypotheses but cannot establish the cause of false negatives on their own.

**Status:** Comparison plan recorded; implementation pending.

### Three-Group Comparison Script — Syntax Validation — 11 October 2026

**Script:** `ml/evaluation/compare_capture_holdout_prediction_groups.py`

**Validation command:** `python -m py_compile ml/evaluation/compare_capture_holdout_prediction_groups.py`

**Result:** Passed with no syntax errors.

**Planned analysis:** Compare missed attacks, detected attacks, and benign traffic across eight selected features. Use the saved capture-holdout model, process the capture in chunks, and use bounded reservoir samples for feature summaries.

**Integrity constraint:** Do not retrain or modify the model or original capture.

**Status:** Syntax validated; execution pending.

### Three-Group Comparison Execution — 11 October 2026

**Script:** `ml/evaluation/compare_capture_holdout_prediction_groups.py`

**Result:** Execution completed successfully over 170,366 rows.

| Group | Records |
|---|---:|
| Missed attacks | 2,175 |
| Detected attacks | 5 |
| Benign traffic | 168,186 |
| **Total** | **170,366** |

The group totals match the previously established evaluation counts.

**Output:** `data/cicids2017/processed/capture_holdout_prediction_group_comparison.json`

**Interpretation:** The grouping reconciles with the existing evaluation. The results confirm that only five of 2,180 attacks were detected in this held-out capture. Feature summaries must be inspected before drawing further conclusions.

**Status:** Comparison completed; feature-summary interpretation pending.

### Three-Group Feature Summary Inspection Plan — 11 October 2026

**Input:** `data/cicids2017/processed/capture_holdout_prediction_group_comparison.json`

**Objective:** Inspect feature summaries for missed attacks, detected attacks, and benign traffic.

**Statistics:** Valid sample count, missing sample count, median, Q25, and Q75.

**Features:** Destination Port, Flow Duration, Total Fwd Packets, Total Backward Packets, Flow Bytes/s, Flow Packets/s, Packet Length Mean, and Init_Win_bytes_forward.

**Method:** Read the existing JSON report and display the saved statistics without rerunning predictions or modifying any files.

**Limitation:** Only five attacks were detected, so comparisons involving that group will be highly uncertain. Differences in descriptive statistics do not establish causation.

**Status:** Inspection plan recorded; report inspection pending.

### Three-Group Feature Summary — Initial Interpretation — 11 October 2026

**Source:** `capture_holdout_prediction_group_comparison.json`

**Observed group sizes:**
- Missed attacks: 2,175
- Detected attacks: 5
- Benign traffic: 168,186, represented by a 100,000-record reservoir sample in the feature summaries.

**Key median comparisons:**

| Feature | Missed attacks | Benign sample |
|---|---:|---:|
| Flow Duration | 5,476,931 | 31,173 |
| Total Fwd Packets | 3 | 2 |
| Total Backward Packets | 1 | 2 |
| Flow Bytes/s | 0 | 5,072.30736 |
| Flow Packets/s | 0.742031326 | 98.80934736 |
| Packet Length Mean | 0 | 58.6 |
| Init_Win_bytes_forward | 29,200 | 22 |
| Destination Port | 80 | 80 |

**Interpretation:** The missed-attack group differs substantially from the benign sample in several feature medians. These differences motivate further investigation but do not establish causation. Feature semantics, source records, and model decision behavior must be examined before drawing conclusions.

**Limitations:** The benign statistics are sample-based, and the detected-attack group contains only five records. The detected group is insufficient for stable population-level conclusions.

**Next action:** Investigate whether the saved model's predictions and feature-processing behavior are consistent with these observed differences.

**Status:** Descriptive comparison interpreted; decision-behavior investigation pending.

### Model Decision-Behavior Investigation Plan — 11 October 2026

**Objective:** Investigate the saved capture-holdout model's decision behavior on the held-out WebAttacks capture.

**Existing evidence:**
- The model missed 2,175 attacks and detected 5.
- Missed attacks had substantially different feature medians from the sampled benign group.
- The missed-attack probabilities had a previously measured mean of approximately 0.0658 and maximum of approximately 0.4876.

**Next checks:**
1. Inspect the saved classifier's class labels and probability output.
2. Verify how predicted classes relate to attack probabilities and the classification threshold.
3. Compare probability distributions for missed attacks, detected attacks, and benign traffic.
4. Avoid inferring causation from feature summaries alone.

**Integrity constraints:** Do not retrain the model, change the threshold, or modify the source dataset during this diagnostic step.

**Status:** Investigation plan recorded; model decision diagnostics pending.

### Saved Model Probability Diagnostics — 11 October 2026

**Model:** `binary_random_forest_capture_holdout.joblib`

**Configuration observed:**
- Classifier: RandomForestClassifier
- Trees: 100
- Maximum depth: 20
- Minimum samples per leaf: 2
- Input features: 77
- Class labels: `[0, 1]`
- Pipeline steps: median imputer and random forest classifier

**Missed-attack probability results:**
- Records: 2,175
- Mean attack probability: 0.065765
- Median: 0.062761
- 90th percentile: 0.067761
- 95th percentile: 0.150601
- 99th percentile: 0.230617
- Maximum: 0.487569
- Records with probability at least 0.50: 0
- Records with probability at least 0.10: 142
- Records with probability at least 0.01: 2,154

**Interpretation:** All missed attacks received attack probabilities below 0.50 and were classified as benign. Most have relatively low predicted attack probabilities. Threshold changes have not been tested and could increase false positives.

**Next action:** Inspect the training code to verify the binary label mapping and probability-column interpretation before any threshold analysis.

**Status:** Probability diagnostics completed; label-mapping verification pending.
### Binary Label Mapping Verification Plan — 11 October 2026

**Objective:** Confirm how the capture-holdout training script maps original CIC-IDS2017 labels to binary classes.

**Questions to verify:**
1. Is `BENIGN` mapped to class `0`?
2. Are all non-`BENIGN` labels mapped to class `1`?
3. Does the training script use the same feature order documented in the saved evaluation report?
4. How does the training pipeline handle non-finite feature values?

**Method:** Read the existing training script without modifying it or retraining the model.

**Status:** Verification plan recorded; source inspection pending.

### Binary Label Mapping and Preprocessing Verification — 11 October 2026

**Source inspected:** `ml/training/train_binary_capture_holdout.py`

**Verified findings:**
- `BENIGN` is mapped to class `0`.
- All non-`BENIGN` labels are mapped to class `1`.
- The training script validates feature names and order across training and held-out captures.
- Exactly 77 input features are expected.
- Numeric conversion is applied to feature columns.
- Positive and negative infinity are replaced with missing values.
- A median `SimpleImputer` and `RandomForestClassifier` are used in the saved pipeline.
- The evaluation report records confusion-matrix labels as `BENIGN`, `ATTACK`.

**Interpretation:** The training source supports the expected binary label mapping. The absent `attack_label` field in the report does not, by itself, indicate a model-label error.

**Next action:** Inspect the training script's sampling and class-distribution details to determine how representative the 300,000-row training sample was.

**Status:** Label mapping and preprocessing verified; training-sample investigation pending.

### Training-Sample Sampling Method Review — 11 October 2026

**Source:** `ml/training/train_binary_capture_holdout.py`

**Verified configuration:**
- Four eligible training captures.
- 1,957,132 eligible source rows.
- 300,000-row training sample.
- NumPy random generator seed: 42.
- Global key-based random sampling retains the 300,000 lowest random keys.
- Random Forest: 100 trees, maximum depth 20, minimum leaf size 2.
- `class_weight=None`; no explicit class weighting is applied.
- Median imputation is included in the training pipeline.

**Interpretation:** The sample is selected globally rather than through explicit class or attack-family stratification. Rare-family representation is not guaranteed by the sampling method.

**Limitation:** The sampling method alone does not establish the actual class balance or prove that any attack family was absent from the sample.

**Next action:** Inspect the saved evaluation report's eligible-source and training-sample class counts.

**Status:** Sampling method reviewed; saved class-count verification pending.

### Training Class-Balance Verification — 11 October 2026

**Source:** `binary_capture_holdout_report.json`

| Dataset | BENIGN | ATTACK |
|---|---:|---:|
| Eligible training source | 86.3809% | 13.6191% |
| Training sample | 86.4303% | 13.5697% |
| Held-out capture | 98.7204% | 1.2796% |

**Counts:**
- Eligible training source: 1,957,132 rows.
- Training sample: 300,000 rows, including 40,709 attacks.
- Held-out capture: 170,366 rows, including 2,180 attacks.

**Interpretation:** The sampled training data closely matches the eligible source's overall binary class proportions. The observed evaluation failure cannot be attributed to a substantial distortion of the overall binary class balance based on these counts alone.

**Limitation:** Binary counts do not establish whether individual attack families are adequately represented in training. The held-out capture's different class proportions also do not, by themselves, explain the low attack recall.

**Next action:** Investigate attack-family coverage in the eligible training captures and compare it with the held-out WebAttacks families.

**Status:** Binary class balance verified; family-level coverage investigation pending.

### Attack-Family Coverage Inspection Plan — 11 October 2026

**Objective:** Inventory the original attack labels in the eligible training captures and compare them with the held-out WebAttacks capture.

**Eligible training captures:**
- Monday Working Hours
- Tuesday Working Hours
- Wednesday Working Hours
- Thursday Afternoon Infiltration

**Held-out capture:** Thursday Morning WebAttacks.

**Method:** Read the original `Label` column from each processed capture, count records by original label, and distinguish BENIGN from individual attack families. Do not train a model or modify any dataset.

**Questions:**
1. Which attack families occur in the eligible training captures?
2. Are Web Attack Brute Force, Web Attack XSS, and Web Attack Sql Injection present in training?
3. How many records of each held-out attack family are available in the training captures?

**Limitation:** Label presence alone does not establish that the model learned a useful decision boundary for a family.

**Status:** Coverage inspection planned; label inventory pending.

### Attack-Family Coverage Results — 11 October 2026

**Method:** Count original labels in the four eligible training captures and the held-out Thursday Morning WebAttacks capture.

**Results:**

| Attack family | Eligible training records | Held-out records |
|---|---:|---:|
| Web Attack Brute Force | 0 | 1,507 |
| Web Attack XSS | 0 | 652 |
| Web Attack Sql Injection | 0 | 21 |
| **Total held-out attacks** | **0** | **2,180** |

The eligible training captures contain BENIGN traffic and the following attack families: FTP-Patator, SSH-Patator, DoS GoldenEye, DoS Hulk, DoS Slowhttptest, DoS slowloris, Heartbleed, and Infiltration.

**Interpretation:** All three attack families in the held-out capture are absent from the eligible training captures. The experiment therefore evaluates generalization to unseen attack families, rather than ordinary recognition of these known families.

The model detected 5 of 2,180 held-out attacks. The absence of these families from training is a plausible major contributor to the poor recall, but this experiment alone does not establish causation.

**Research implication:** Evaluate known-family and unseen-family detection separately when assessing the proposed intrusion prevention system.

**Status:** Attack-family coverage verified; experimental follow-up pending.

### Controlled Known-Family Follow-Up Experiment — 11 October 2026

**Objective:** Investigate whether poor performance is associated with evaluating attack families that were absent from training.

**Existing baseline:** The model was trained on eligible captures containing BENIGN traffic and eight attack families. The held-out Thursday Morning WebAttacks capture contains three attack families absent from training, with 2,180 attack records in total.

**Proposed comparison:**
1. Retain the existing unseen-family evaluation as the baseline.
2. Evaluate the saved model on a separate capture containing attack families represented in the training data.
3. Report attack-family counts, precision, recall, F1-score, false positives, and false negatives.
4. Keep the existing model, baseline report, and held-out capture unchanged.
5. Clearly distinguish differences between captures from differences caused by attack-family familiarity.

**Candidate known-family captures:** Tuesday Working Hours (FTP-Patator and SSH-Patator), Wednesday Working Hours (DoS families and Heartbleed), and Thursday Afternoon Infiltration (Infiltration).

**Important limitation:** These captures were used for training, so evaluating on them would measure performance on familiar training data rather than provide an independent generalization test. A valid known-family generalization test requires a separate split or capture with the same families excluded from model fitting.

**Next action:** Inspect the original label counts and capture boundaries to choose a defensible evaluation design before running another experiment.

**Status:** Follow-up experiment planned; evaluation design pending.

### Evaluation Design Decision — 11 October 2026

**Decision:** Do not evaluate the existing model on its own training records as evidence of generalization.

**Reason:** The current model was fitted on a sample of 300,000 records drawn from four eligible captures. Performance on those same records would be an in-sample measurement and could overstate performance on unseen traffic.

**Preferred design:** Identify a separate capture or partition containing attack families represented during training, while ensuring the evaluated records were excluded from model fitting.

**Controls:**
- Preserve the existing unseen-family baseline.
- Keep training and evaluation records disjoint.
- Verify family presence and record counts before fitting or evaluating.
- Report per-family precision, recall, F1-score, false positives, and false negatives where applicable.
- Do not interpret differences between captures as a causal effect of family familiarity without controlling for other differences.

**Status:** Evaluation-design principles recorded; dataset-split inspection pending.

### Candidate Known-Family Evaluation Split — 11 October 2026

**Inspection results:**
- The existing baseline trains on Monday, Tuesday, Wednesday, and Thursday Afternoon Infiltration captures.
- Thursday Morning WebAttacks is the current held-out capture.
- Eight processed capture files are available.
- Existing evaluation scripts include `evaluate_binary_by_capture.py` and `evaluate_capture_holdout_by_family.py`.

**Candidate:** Friday PortScan capture, which contains BENIGN and PortScan records.

**Reason for consideration:** PortScan is a different attack family from the three Web Attack families in the current held-out capture.

**Important limitation:** The existing baseline training configuration does not include Friday PortScan, so evaluating that capture with the unchanged baseline would test another unseen-family case, not known-family generalization. A separate model and carefully defined split would be needed to test PortScan as a known family without evaluating on its training records.

**Next action:** Inspect the existing capture-level evaluation script and report to determine what comparisons are already supported.

**Status:** Candidate identified; evaluation design not yet finalized.


### Existing Capture-Level Evaluation Script Review — 11 October 2026

**Source:** `ml/evaluation/evaluate_binary_by_capture.py`

**Verified findings:**
- The script loads `ml/models/binary_random_forest.joblib`.
- It evaluates Friday Morning, Friday DDoS, and Friday PortScan captures.
- It reports binary BENIGN/ATTACK metrics and original source-label counts.
- It writes results to `binary_capture_evaluation.json`.
- The script does not itself establish whether the evaluation captures overlap with the model's training data.

**Important distinction:** The current unseen-WebAttacks baseline uses `binary_random_forest_capture_holdout.joblib`. The existing capture-level script loads a different model. Its results must not be attributed to the current baseline without verifying the other model's provenance.

**Next action:** Check whether the older model and its evaluation report exist, then inspect available provenance before relying on those results.

**Status:** Script reviewed; model provenance verification pending.

### Model Artifact and Report Inventory — 11 October 2026

**Objective:** Verify the existence of the older binary model and its capture-level evaluation report before relying on their results.

**Artifacts to check:**
- `ml/models/binary_random_forest.joblib`
- `ml/models/binary_random_forest_capture_holdout.joblib`
- `data/cicids2017/processed/binary_capture_evaluation.json`
- `data/cicids2017/processed/binary_capture_holdout_report.json`

**Method:** List matching artifacts and inspect Git working-tree status. Do not load, retrain, overwrite, or delete any model.

**Status:** Artifact inventory pending.

### Model Artifact Inventory Results — 11 October 2026

**Model artifacts found:**
- `binary_random_forest.joblib`
- `binary_random_forest_capture_holdout.joblib`
- `binary_random_forest_validation.joblib`

**Evaluation reports found:**
- `binary_capture_evaluation.json`
- `binary_capture_holdout_report.json`

**Git status:** `docs/research-log.md` is modified, and four evaluation scripts are untracked.

**Interpretation:** The older model and capture-level report are available for inspection. Their existence does not establish which data were used to train the older model or whether its Friday evaluation captures were excluded from training.

**Next action:** Inspect the older model's saved report and training metadata to establish its provenance before interpreting its evaluation results.

**Status:** Artifact inventory completed; older model provenance pending.

### Older Model Capture-Level Results — 11 October 2026

**Source:** `data/cicids2017/processed/binary_capture_evaluation.json`

| Capture | Attack family | Attack records | Detected attacks | Attack recall |
|---|---|---:|---:|---:|
| Friday Morning | Bot | 1,966 | 0 | 0.00% |
| Friday Afternoon DDoS | DDoS | 128,027 | 81,248 | 63.46% |
| Friday Afternoon PortScan | PortScan | 158,930 | 157 | 0.10% |

**Interpretation:** The older model's reported attack recall varies substantially across these three captures. DDoS recall is considerably higher than Bot and PortScan recall.

**Limitation:** The report does not establish which data were used to train `binary_random_forest.joblib`. These results cannot be assumed to represent independent generalization performance, and they must not be attributed to the newer capture-holdout model.

**Next action:** Inspect Git history and available training scripts to determine whether the older model's provenance can be established.

**Status:** Older-model report interpreted; provenance verification pending.


### Older Model Provenance Investigation — 11 October 2026

**Repository inspection results:**
- Training scripts available: `train_binary_classifier.py`, `train_binary_validation.py`, and `train_binary_capture_holdout.py`.
- `train_binary_classifier.py` explicitly saves `ml/models/binary_random_forest.joblib`.
- The repository history contains no recorded commits for the older model artifact itself.
- Git history is available for the training scripts.

**Interpretation:** The older model's generating script has been identified, but the model artifact's exact training run and dataset provenance remain unverified.

**Next action:** Inspect `train_binary_classifier.py` to establish its configured input data, preprocessing, sampling, and model settings.

**Status:** Generating script identified; provenance investigation continues.


### Older Model Training Configuration Review — 11 October 2026

**Source:** `ml/training/train_binary_classifier.py`

**Training captures:**
- Monday Working Hours
- Tuesday Working Hours
- Wednesday Working Hours
- Thursday Afternoon Infiltration
- Thursday Morning WebAttacks

**Evaluation captures:**
- Friday Morning
- Friday Afternoon DDoS
- Friday Afternoon PortScan

**Training configuration:**
- Random sample: 300,000 rows
- Random seed: 42
- Binary labels: BENIGN = 0; non-BENIGN = 1
- Random Forest: 100 trees, maximum depth 20, minimum leaf size 2
- Median imputation fitted on the training sample

**Interpretation:** The source code specifies Thursday Morning WebAttacks as training data for the older model, whereas the newer capture-holdout experiment explicitly excludes that capture from training. The older model's Friday evaluation is capture-separated according to its configuration, but its exact historical training run cannot be proven from the source file alone.

**Status:** Older model's intended training and evaluation configuration documented; historical artifact provenance remains partly unverified.

### Next Research Direction — 11 October 2026

**Decision:** Prioritize a controlled evaluation design before modifying the existing model or introducing blockchain integration.

**Rationale:**
- The unseen-WebAttacks baseline has extremely low attack recall.
- The older model's Friday evaluation shows substantial variation across attack families.
- The models use different training-capture configurations, so their results cannot isolate the effect of attack-family familiarity.

**Preferred next experiment:** Design a reproducible, family-aware train/test split that excludes evaluation records from model fitting and records family-level support in both partitions. Preserve the current model and report as the baseline.

**Evaluation requirements:**
- Document which attack families appear in each partition.
- Prevent overlap between training and test records.
- Report binary and per-family precision, recall, F1-score, false positives, and false negatives.
- Keep model artifacts and reports separate from the existing baseline.
- Treat any performance improvement as an experimental result, not proof of causation unless competing explanations are controlled.

**Status:** Research direction selected; split design and implementation pending.

### Known-Family Evaluation Design — 11 October 2026

**Objective:** Establish a controlled record-level baseline for attack families represented in both training and test partitions.

**Proposed design:**
1. Use the eligible Monday, Tuesday, Wednesday, and Thursday Afternoon Infiltration captures.
2. Retain the original multiclass `Label` temporarily for partitioning and family-level reporting; derive the binary target separately (`BENIGN = 0`, non-BENIGN = 1).
3. Inspect exact duplicate rows before splitting and document the chosen duplicate-handling policy to reduce the risk of identical records appearing in both partitions.
4. Create a reproducible 80/20 train/test split, stratified by the original attack-family label where the label counts permit it.
5. Fit preprocessing and the model using training data only. Do not use the test partition for fitting, feature selection, threshold selection, or model tuning.
6. Preserve the existing baseline artifacts. Store the new model, configuration, predictions, and report under separate filenames.
7. Report binary metrics and per-family support, precision, recall, F1-score, false positives, and false negatives.

**Interpretation limits:**
- This is a record-level split, not a capture-separated or time-separated test.
- Records from the same capture may share capture-specific characteristics, so results may overestimate performance on genuinely new traffic.
- Rare families may have too few distinct records for stable estimates; report their support and limitations.
- Compare this result with the unseen-family baseline as a difference in evaluation setting, not as a controlled causal comparison.

**Status:** Experimental design proposed; duplicate inspection, split implementation, and evaluation pending.

### Duplicate-Record Inspection Plan — 11 October 2026

**Objective:** Assess the risk of duplicate records crossing the proposed record-level train/test boundary.

**Scope:**
- Monday Working Hours
- Tuesday Working Hours
- Wednesday Working Hours
- Thursday Afternoon Infiltration

**Inspection procedure:**
1. Count exact duplicate feature rows within each capture.
2. Count exact duplicate feature rows across the four captures.
3. Inspect whether duplicate rows have conflicting original attack-family labels.
4. Distinguish duplicate feature vectors from duplicate complete records, including labels.
5. Do not delete, modify, or overwrite source datasets during this inspection.

**Decision criteria:**
- If exact duplicates exist, document their frequency and label consistency before selecting a splitting strategy.
- Avoid placing identical feature records in both partitions where practical.
- Preserve rare attack families and document any limitations that prevent a clean split.

**Limitations:** Exact row equality does not establish that two network flows are the same real-world event. Conversely, records representing similar flows may differ slightly and evade exact-duplicate checks.

**Status:** Inspection planned; execution and results pending.

### Duplicate Inspection Results — 11 October 2026

**Dataset scope:** Four eligible captures; 1,957,132 total rows.

| Capture | Rows | Repeated feature rows | Repeated complete rows |
|---|---:|---:|---:|
| Monday Working Hours | 529,918 | 26,935 | 26,935 |
| Tuesday Working Hours | 445,909 | 24,065 | 24,065 |
| Wednesday Working Hours | 692,703 | 81,957 | 81,909 |
| Thursday Afternoon Infiltration | 288,602 | 35,630 | 35,630 |
| **Combined** | **1,957,132** | **186,158** | **186,049** |

Additional hash-based results:
- Distinct feature patterns reported in multiple captures: 15,384.
- Feature patterns reported with multiple labels: 72.
- Source files were not modified.

**Interpretation:** Repeated feature rows are common enough to warrant explicit handling before a record-level split. The 72 reported label conflicts require a more precise audit because the initial cross-capture aggregation can hide conflicts within an individual capture. Hash equality alone is not proof that records represent the same underlying network event.

**Next action:** Audit feature-pattern/label conflicts within and across captures, verify the conflicting groups against actual feature values, and then select a reproducible splitting policy.

**Status:** Initial duplicate screening complete; conflict audit pending.

### Label-Conflict Audit Results — 11 October 2026

The second hash-based audit processed the four eligible captures, totaling 1,957,132 rows.

Results:
- Distinct feature hashes: 1,770,974.
- Hashes associated with multiple original labels: 109.
- Conflicting hashes confined to one capture: 35.
- Conflicting hashes spanning multiple captures: 74.
- Example conflicts include `BENIGN` and `DoS Hulk`; one reported hash occurs 3,361 times.

The earlier audit reported 72 conflicts because it deduplicated feature-hash/capture pairs before checking labels, potentially hiding conflicts within captures.

**Interpretation:** Feature-pattern/label ambiguity must be investigated before choosing the split policy. These counts are preliminary because hash equality does not prove exact feature-vector equality.

**Next action:** Verify candidate conflicts by comparing the actual feature values, then quantify confirmed conflicting records and determine how they should be handled during evaluation.

**Status:** Hash-based conflict candidates identified; exact-value verification pending.

### Exact Feature-Vector Conflict Verification — 11 October 2026

The numeric feature-vector audit processed all 1,957,132 rows from the four eligible captures.

Results:
- Distinct exact numeric feature vectors: 1,772,172.
- Feature vectors associated with multiple original labels: 108.
- Conflicts confined to one capture: 35.
- Conflicts spanning multiple captures: 73.

The inspected examples primarily associate `BENIGN` and `DoS Hulk` with identical numeric feature vectors. One reported feature vector occurred 3,361 times.

**Interpretation:** These conflicts persist after comparing actual numeric feature values, rather than relying solely on hash equality. They show that some feature vectors are associated with inconsistent original labels. They do not establish that the corresponding records represent the same real-world network flow.

**Proposed split policy:** Keep the original dataset unchanged. For the controlled record-level experiment, assign identical feature vectors to a single partition so exact feature matches cannot cross the train/test boundary. Preserve original labels and report conflicting-label support separately. Do not silently relabel or discard conflicting observations.

**Limitation:** Grouping exact feature vectors prevents exact-vector overlap but does not prevent leakage from near-duplicate flows or shared capture conditions.

**Status:** Numeric feature conflicts verified; implementation of a grouped split pending.

### Grouped Train/Test Split Design — 11 October 2026

**Objective:** Design a reproducible known-family evaluation that prevents exact numeric feature-vector groups from crossing the train/test boundary.

**Proposed approach:**
1. Keep the original four source captures unchanged.
2. Preserve the original `Label` column and derive the binary target separately.
3. Assign identical numeric feature vectors to the same group.
4. Use a deterministic grouped partition with a fixed random seed and an approximate 80/20 target split.
5. Verify that no exact feature-vector group occurs in both partitions.
6. Check original attack-family coverage and class counts in each partition before fitting the model.
7. If the partition omits a family or creates an unusable class distribution, revise the partitioning approach before training.
8. Fit the imputer and classifier using training records only.
9. Keep model artifacts, predictions, and evaluation reports separate from existing baselines.

**Technical limitation:** A grouped random split does not inherently guarantee stratification by attack family. The actual partition must be validated. Rare families and conflicting-label groups may prevent a clean, balanced split.

**Leakage limitation:** This design prevents exact numeric feature-vector overlap, but does not prevent near-duplicate flows or shared capture-specific characteristics from crossing partitions.

**Status:** Grouping and validation requirements defined; implementation pending.

### Splitter Selection — 11 October 2026

Environment verified:
- scikit-learn: 1.9.1
- `GroupShuffleSplit`: available
- `StratifiedGroupKFold`: available

**Selected candidate:** `StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42)`.

**Grouping variable:** Exact numeric feature-vector identity.

**Stratification target:** Original multiclass attack-family `Label`, not the derived binary target.

**Reason:** This splitter attempts to preserve label proportions while keeping groups intact. Unlike a standard random grouped split, it explicitly considers class proportions.

**Validation required before model fitting:**
1. Confirm that no feature-vector group crosses the train/test boundary.
2. Compare family counts and proportions across all five folds.
3. Identify rare or missing families and inspect the 108 verified conflicting-label feature vectors.
4. Record the actual training/test sizes and class distributions for the selected fold.

**Limitation:** Stratification is an optimization goal, not a guarantee. Group constraints and conflicting labels may prevent a balanced split.

**Status:** Splitter candidate selected; implementation and fold validation pending.

### Grouped Split Validator — Initial Code Review — 11 October 2026

**Script:** `ml/evaluation/validate_grouped_capture_split.py`

**Validation performed:** Python syntax compilation passed.

**Issues identified before execution:**
1. The implementation constructs and retains Python tuples for all feature rows, which may consume excessive memory on the 1,957,132-row dataset under the 7 GB WSL memory limit.
2. Missing numeric values require explicit canonicalization before exact feature-vector grouping.
3. The group-level label-conflict summary is recomputed inside each fold and should be calculated once.
4. The full-dataset memory requirement has not been measured.

**Decision:** Do not execute the current implementation on the full dataset. Optimize grouping and conflict validation first, then review the revised script before execution.

**Status:** Syntax validated; memory efficiency and missing-value handling require revision. No model was trained and no source datasets were modified.

### Grouped Split Validator — Memory Optimization Plan — 11 October 2026

**Objective:** Reduce memory overhead while preserving correct exact-feature grouping.

**Planned changes:**
1. Normalize numeric features consistently, including missing values and signed zero.
2. Use compact numeric representations and integer group identifiers instead of retaining a Python tuple for every row.
3. Use hashes only to identify candidate matches; resolve collisions using exact normalized feature values.
4. Calculate conflicting-label group information once rather than repeating it for each fold.
5. Report group overlap and family coverage for every fold.
6. Review the revised implementation before running it against the complete dataset.

**Constraints:**
- Keep source CSV files and existing model artifacts unchanged.
- Do not train a model during split validation.
- Do not assume the revised implementation will fit within the 7 GB WSL memory limit without testing.
- Preserve reproducibility with five folds and random seed 42.

**Status:** Memory optimization planned; revised implementation and execution pending.

### Revised Grouped Split Validator — Syntax Check — 11 October 2026

**Script:** `ml/evaluation/validate_grouped_capture_split.py`

**Result:** `python -m py_compile` completed successfully.

**Implementation review:**
- Uses numeric feature arrays and normalizes infinities and signed zero.
- Handles missing values during exact feature comparisons.
- Calculates conflicting-label groups once.
- Uses grouped, stratified five-fold splitting with seed 42.
- Resolves hash collisions through feature-value comparisons.

**Remaining concern:** Individual row comparisons within large hash buckets may be computationally expensive. Runtime and peak memory have not been measured.

**Decision:** Do not run the full-dataset validator yet. Optimize repeated-row grouping and review the revised algorithm before execution.

**Status:** Syntax validated; performance review pending. No model trained and no source datasets modified.

### Grouping Algorithm Optimization — 11 October 2026

**Objective:** Reduce the computational cost of exact feature-vector grouping.

**Planned change:**
- Group rows by their hash values.
- Within each bucket, identify unique normalized feature rows using vectorized operations where practical.
- Assign one integer group ID to each distinct feature vector.
- Map repeated occurrences back to the same group ID.
- Preserve consistent handling of missing numeric values and signed zero.
- Continue resolving hash collisions using actual feature values rather than assuming hash equality means vector equality.

**Validation requirements:**
- Confirm repeated feature vectors receive identical group IDs.
- Confirm different vectors in the same hash bucket remain separate.
- Confirm conflicting-label groups are preserved and reported.
- Check memory and runtime before processing the complete dataset.

**Status:** Optimization approach documented; implementation and validation pending.

### Grouping Optimization Syntax Check — 11 October 2026

**Script:** `ml/evaluation/validate_grouped_capture_split.py`

**Result:** Python syntax compilation passed after replacing the row-by-row hash-bucket comparison with vectorized `numpy.unique` grouping.

**Remaining validation:**
- Verify repeated rows receive the same group ID.
- Verify different feature vectors are not merged.
- Verify missing values are grouped consistently.
- Verify hash collisions cannot merge distinct vectors.
- Measure resource use before running the full dataset.

**Decision:** Test the grouping logic on a small synthetic dataset before running full-dataset validation.

**Status:** Syntax validated; functional tests pending. No model trained and no source datasets modified.

### Synthetic Feature-Grouping Test — 11 October 2026

**Test:** Five synthetic feature rows, including duplicate rows, matching missing-value patterns, and a distinct feature vector.

**Results:**
- Input rows: 5.
- Unique groups: 3.
- Identical rows received matching group IDs.
- Rows with matching missing-value positions were grouped consistently.
- Distinct feature vectors remained separate.
- All assertions passed.

**Interpretation:** The tested `numpy.unique` grouping operation behaves as expected for these synthetic cases.

**Limitations:** This test does not validate hash-collision handling, the complete validator, cross-capture grouping, fold stratification, or full-dataset memory usage.

**Status:** Synthetic grouping test passed; full-validator validation remains pending.

### Integrated Grouped Validator Review — 11 October 2026

**Files reviewed:**
- `ml/evaluation/validate_grouped_capture_split.py`
- Current Git working-tree status

**Findings:**
- The script integrates numeric normalization, hash-bucket grouping, conflicting-label analysis, and five-fold stratified grouped splitting.
- Syntax compilation and the small synthetic grouping test passed.
- The full implementation has not been executed on the dataset.
- Large duplicate buckets may create substantial temporary memory allocations.
- Group overlap is reported but should also be enforced as a validation assertion.
- Capture membership is loaded but not yet summarized for each fold.

**Decision:** Do not run the current validator on the full dataset. Address resource usage and strengthen validation checks first.

**Repository status:** The research log is modified; the validator and four diagnostic scripts are untracked. No commit or push was performed.

**Status:** Integrated code reviewed; further revisions required before execution.

### Grouped Validator Resource and Assertion Improvements — 11 October 2026

**Objective:** Make the grouped split validator more resource-conscious and strengthen its correctness checks.

**Required changes:**
1. Reduce unnecessary copies of the full dataset and intermediate arrays.
2. Normalize missing numeric values and signed zero consistently.
3. Preserve exact feature-vector equality when assigning group IDs; hash equality alone must not determine group identity.
4. Calculate conflicting-label groups once.
5. Assert that train/test feature-group overlap is zero for every fold.
6. Report per-capture train/test membership alongside original-label distributions.
7. Review the revised implementation before full-dataset execution.

**Constraints:** Do not modify source datasets, retrain the existing model, or overwrite existing reports during validation.

**Status:** Improvements

### GitHub Research Checkpoint — 11 October 2026

**Objective:** Preserve the current research and evaluation work in the GitHub repository before pausing development.

**Planned files:**
- `docs/research-log.md`
- `ml/evaluation/compare_capture_feature_distributions.py`
- `ml/evaluation/compare_capture_holdout_prediction_groups.py`
- `ml/evaluation/inspect_capture_holdout_false_negatives.py`
- `ml/evaluation/inventory_capture_label_overlap.py`
- `ml/evaluation/validate_grouped_capture_split.py`

**Pre-push requirements:**
1. Review the working-tree changes and intended files.
2. Run syntax checks on the Python evaluation scripts.
3. Check for whitespace errors and accidental sensitive or generated files.
4. Stage only the intended code and documentation.
5. Commit and push to the configured GitHub remote.
6. Verify the commit and synchronization status.

**Restrictions:** Do not commit processed datasets, trained model artifacts, generated evaluation outputs, credentials, or unrelated files.

**Status:** GitHub checkpoint planned; review, commit, and push pending.

### README Revision and GitHub Checkpoint — 11 October 2026

**Objective:** Update the project README to provide an accurate overview of the decentralized, self-learning Intrusion Prevention System and prepare the current research work for GitHub.

**Planned README sections:**
- Project overview and objectives
- Planned architecture and technology stack
- Repository structure
- Ubuntu WSL2 and Python environment setup
- CIC-IDS2017 dataset and preprocessing
- Security and isolated-lab testing scope
- Development roadmap
- Research-log reference
- License and dataset attribution

**Documentation requirements:**
- Clearly distinguish implemented functionality from planned components.
- Do not claim that Suricata integration, automated prevention, anomaly detection, or Hyperledger Fabric auditing is operational unless verified.
- Keep datasets, trained models, generated evaluation outputs, and credentials out of Git.
- Preserve the existing research history and document experimental limitations accurately.

**GitHub checkpoint:** Review the README, research log, and intended evaluation scripts; run checks; stage only approved files; commit and push; verify repository synchronization.

**Status:** README revision and GitHub checkpoint pending.

### Pre-Push Syntax Check — 11 October 2026

**Validation performed:** Python syntax compilation for five evaluation scripts.

Scripts checked:
- `compare_capture_feature_distributions.py`
- `compare_capture_holdout_prediction_groups.py`
- `inspect_capture_holdout_false_negatives.py`
- `inventory_capture_label_overlap.py`
- `validate_grouped_capture_split.py`

**Result:** All five scripts compiled successfully.

**Limitations:** Syntax compilation does not verify runtime behavior, evaluation correctness, memory usage, or model performance. The grouped split validator has not been run on the complete dataset.

**Next action:** Verify Git working-tree status, whitespace checks, and the intended README and research-log changes before staging files.

**Status:** Syntax check passed; pre-push review continues.

### Git Pre-Push Review — 11 October 2026

**Review results:**
- Confirmed the Git remote is `origin`, pointing to the project GitHub repository.
- Confirmed the current branch is `main`.
- Confirmed `README.md` and `docs/research-log.md` contain local changes.
- Identified five new evaluation scripts intended for review before staging.
- Confirmed the generated capture-holdout report and trained model are ignored by Git.
- `git diff --check` reported an extra blank line at the end of `docs/research-log.md`.

**Next action:** Remove the trailing blank line, rerun whitespace checks, review the final staged changes, and then commit and push the intended files.

**Status:** Review in progress; no new commit or push has been performed.

### Pre-Commit Verification — 11 October 2026

**Files staged:** Seven intended files: the README, research log, and five evaluation scripts.

**Checks completed:**
- `git diff --exit-code` passed; no unstaged changes remained.
- `git diff --cached --check` passed with no whitespace errors.
- Reviewed staged filenames and change summary.
- No dataset or trained-model artifacts were included in the staged file list.

**Next action:** Commit the reviewed changes to the `main` branch, push to the configured GitHub remote, and verify the resulting repository state.

**Status:** Pre-commit checks passed; commit and push are pending.

### Research Checkpoint Commit — 11 October 2026

**Commit:** `fa95c3a`  
**Message:** `Document research progress and add evaluation diagnostics`

The commit includes seven files:
- Updated `README.md`
- Updated `docs/research-log.md`
- `compare_capture_feature_distributions.py`
- `compare_capture_holdout_prediction_groups.py`
- `inspect_capture_holdout_false_negatives.py`
- `inventory_capture_label_overlap.py`
- `validate_grouped_capture_split.py`

The staged whitespace check passed before the commit. The five evaluation scripts passed Python syntax compilation. The grouped capture-split validator remains subject to further memory and correctness validation before full-dataset execution.

**Next action:** Push the commit to the configured GitHub remote and verify synchronization.

**Status:** Local commit created; remote push pending.

