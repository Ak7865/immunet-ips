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

### Suricata Integration Decision — 11 October 2026

**Decision:** Begin the network-monitoring integration in detection-only mode while continuing to investigate the current ML baseline's poor attack-family generalization.

**Planned sequence:**
1. Configure Suricata inside the isolated project laboratory.
2. Verify traffic capture and inspect generated events.
3. Establish a benign-traffic baseline.
4. Generate one controlled test attack against the lab application.
5. Verify whether Suricata generates a corresponding alert.
6. Evaluate Suricata alerts and ML predictions independently.
7. Consider controlled prevention only after the detection pipeline and event mapping are validated.

**Safety constraints:** Attack traffic must remain within the isolated laboratory. No automatic blocking is enabled during the initial experiments.

**Limitation:** The current CIC-IDS2017 Random Forest baseline detected only 5 of 2,180 attacks in the held-out WebAttacks evaluation. It is not ready to be trusted as an automatic prevention mechanism.

**Status:** Decision recorded; Suricata configuration and live detection testing have not yet been completed.

### Suricata Environment Preflight — 11 October 2026

**Objective:** Inspect the existing WSL environment before beginning Suricata integration.

**Checks planned:**
- Confirm the operating system and kernel environment.
- Check whether Docker is installed and responding.
- Check whether Docker Compose is available.
- Check whether Suricata is installed and identify its version.
- Check whether the project already contains a Suricata configuration or Compose service.

**Safety constraint:** This step is inspection only. It will not install packages, start containers, capture traffic, generate attacks, or modify firewall rules.

**Next action:** Run the environment checks and choose the smallest required setup step based on their results.

**Status:** Preflight planned; environment results pending.

### Suricata Environment Preflight Results — 11 October 2026

**Environment:** Ubuntu 24.04.5 LTS under WSL2, kernel `6.6.87.2-microsoft-standard-WSL2`.

**Findings:**
- The `docker` command is unavailable inside the Ubuntu distribution.
- Docker's diagnostic recommends enabling Docker Desktop WSL integration.
- Docker Compose is unavailable because Docker CLI access is missing.
- Suricata is not installed on the Ubuntu host.
- No matching Suricata or Compose configuration files were found within the project's searched directory depth.

**Decision:** Restore Docker CLI access through Docker Desktop's WSL integration before selecting and configuring the Suricata container.

**Safety:** No packages were installed, containers started, traffic captured, or firewall rules changed.

**Status:** Preflight complete; Docker integration setup pending.

### Docker Desktop WSL Integration Check — 11 October 2026

**Objective:** Restore Docker CLI access from Ubuntu 24.04 under WSL2.

**Planned checks:**
- Confirm Docker Desktop is installed and running on Windows.
- Inspect Docker Desktop's WSL integration settings.
- Confirm integration is enabled for the Ubuntu distribution.
- Recheck Docker CLI access from Ubuntu after applying any required setting changes.

**Safety:** This step changes no project files, installs no packages, starts no attack simulations, and modifies no firewall rules.

**Next action:** Inspect Docker Desktop and enable the existing WSL integration if necessary.

**Status:** Windows-side Docker Desktop check pending.

### Docker Desktop WSL Integration Verified — 11 October 2026

**Environment:** Ubuntu 24.04.5 LTS under WSL2.

**Verification results:**
- Docker CLI is accessible inside Ubuntu.
- Docker version: `29.0.1`, build `eedd969`.
- Docker Compose version: `v2.40.3-desktop.1`.
- Docker server responds successfully with version `29.0.1`.

**Decision:** Use the existing Docker Desktop WSL integration for the planned containerized Suricata environment. Do not install a separate Docker Engine in Ubuntu.

**Next action:** Check Docker container and network availability, then choose an isolated lab topology for Suricata testing.

**Status:** Docker access verified; Suricata not yet installed or configured.

### Docker Lab Preflight — 11 October 2026

**Objective:** Inspect the existing Docker environment before creating the Suricata lab.

**Checks planned:**
- List running containers.
- List all containers, including stopped containers.
- List existing Docker networks.
- Verify that Docker can run a basic container without changing project services.

**Safety:** No existing containers or networks will be removed or modified. No attack traffic will be generated.

**Next action:** Review the Docker inventory and select an isolated network topology for the Suricata experiment.

**Status:** Preflight note recorded; inspection pending.

### Docker Inventory Results — 11 October 2026

**Environment:** Docker Desktop accessed from Ubuntu 24.04 under WSL2.

**Observed state:**
- Running containers: 0.
- Existing containers: 26.
- Docker networks: `bridge`, `fabric_test`, `grocery_default`, `host`, and `none`.
- Docker images: 14, occupying approximately 3.172 GB.
- Existing project resources include Hyperledger Fabric containers and a grocery application PostgreSQL container.

**Decision:** Preserve existing containers, images, networks, and volumes. Create a dedicated network for the IPS lab instead of reusing existing project networks.

**Design consideration:** Suricata must be connected to a suitable traffic-capture path. Docker network membership alone does not guarantee visibility into all lab traffic.

**Next action:** Check available memory and disk capacity, then choose the smallest practical isolated lab topology.

**Status:** Docker inventory complete; no existing resources modified.

### IPS Lab Resource Preflight — 11 October 2026

**Objective:** Check available memory, filesystem capacity, and Docker storage before downloading or starting Suricata.

**Checks planned:**
- Inspect WSL memory and swap availability.
- Check free disk space for the project filesystem.
- Check Docker image, container, and volume storage usage.

**Safety:** Inspection only. No images will be pulled, containers started, or resources deleted.

**Next action:** Review resource availability and select an appropriate Suricata container configuration.

**Status:** Resource preflight pending.

### IPS Lab Resource Preflight Results — 11 October 2026

**Environment:** Ubuntu 24.04 under WSL2 with Docker Desktop integration.

**Observed resources:**
- Total memory: approximately 6.8 GiB.
- Available memory at inspection: approximately 5.1 GiB.
- Total swap: 2 GiB; approximately 1.3 GiB free.
- Project filesystem: approximately 948 GiB available.
- Docker images: 3.172 GB.
- Docker volumes: approximately 257.6 MB.

**Decision:** Proceed with a lightweight Suricata container experiment, monitoring memory consumption during startup and traffic capture. Avoid concurrent ML training during initial live testing.

**Limitations:** The reported available memory is a snapshot and may change. Actual Suricata resource requirements depend on configuration and traffic volume.

**Next action:** Identify a suitable Suricata image and confirm the configuration needed for a safe detection-only lab.

**Status:** Resource preflight passed; image selection and configuration pending.

### Suricata Image Selection — 11 October 2026

**Candidate image:** `openeuler/suricata:8.0.4-oe2403sp4`

**Source:** Docker Hub documentation for the openEuler CloudNative SIG Suricata image.

**Rationale:**
- The image documentation lists Suricata 8.0.4 and supports the `amd64` architecture.
- Containerized execution avoids installing Suricata directly into the Ubuntu host.
- The initial experiment will use detection-only operation.
- The lab will eventually verify traffic visibility and generated JSON events before integrating the ML service.

**Limitations:** Image availability, architecture compatibility, runtime configuration, and required Linux capabilities must be verified before starting the container. This candidate has not yet been pulled or tested.

**Next action:** Inspect the candidate image's published metadata and verify the host architecture.

**Status:** Candidate selected; image inspection pending.

### Suricata Image Compatibility Check — 11 October 2026

**Objective:** Verify the local architecture and inspect the candidate container image metadata before downloading it.

**Checks planned:**
- Identify the WSL architecture.
- Check whether the candidate image tag is already present locally.
- Inspect the local image metadata if available.
- Determine whether a remote image pull is needed.

**Safety:** Inspection only; no container starts, traffic capture, firewall changes, or image downloads.

**Next action:** Review the command output before deciding whether to pull the image.

**Status:** Compatibility check pending.

### Suricata Image Compatibility Results — 11 October 2026

**Findings:**
- WSL architecture: `x86_64`.
- Docker server architecture: `x86_64`.
- Candidate image `openeuler/suricata:8.0.4-oe2403sp4` is not present locally.
- No existing local Docker image matching `suricata` was found.

**Decision:** Verify the candidate image tag and its published architecture before downloading it.

**Safety:** No image was pulled, no container was started, and no network or firewall configuration was changed.

**Next action:** Verify image availability and provenance, then decide whether to pull it.

**Status:** Local architecture verified; remote image verification pending.

### Suricata Remote Image Verification — 11 October 2026

**Image candidate:** `openeuler/suricata:8.0.4-oe2403sp4`

**Source checked:** Docker Hub documentation for `openeuler/suricata`.

**Findings:**
- The repository identifies the image as maintained by the openEuler CloudNative SIG.
- The published tag list identifies `8.0.4-oe2403sp4` as Suricata 8.0.4 on openEuler 24.03-LTS-SP4.
- The published architecture list includes `amd64` and `arm64`.
- The local WSL and Docker server architecture is `x86_64`, compatible with `amd64`.

**Limitations:** This was a documentation check. The image has not been pulled, its local digest has not been recorded, and runtime behavior has not been tested.

**Next action:** Pull the selected image and inspect its local metadata before starting any container.

**Status:** Published tag and architecture verified; image pull pending.

### Suricata Image Download — 11 October 2026

**Image:** `openeuler/suricata:8.0.4-oe2403sp4`

**Result:** Docker successfully pulled the image.

**Recorded digest:** `sha256:c765ec1015f929c9b8ca2fcde8138f00e805124e02c2398af085aef28a0ff96a`

**Storage:** Docker reports approximately 1.07 GB of disk usage for the image.

**Inspection issue:** The metadata inspection command failed when accessing `.Config.Cmd`, because that field is absent from the image configuration. This does not indicate a failed image download.

**Safety:** No Suricata container has been started; no traffic capture or firewall changes have occurred.

**Next action:** Inspect the image metadata using fields that are available, identify the documented entrypoint and startup behavior, and check the supported Suricata command-line options before creating a container.

**Status:** Image downloaded; startup configuration inspection pending.

### Suricata Image Metadata Verified — 11 October 2026

**Image:** `openeuler/suricata:8.0.4-oe2403sp4`

**Verified metadata:**
- Image ID: `sha256:c765ec1015f929c9b8ca2fcde8138f00e805124e02c2398af085aef28a0ff96a`
- OS: `linux`
- Architecture: `amd64`
- Image creation timestamp: `2026-07-10T09:38:13.95551403Z`
- Entrypoint: `/entrypoint.sh`
- Default command: absent (`null`)
- Working directory: `/`
- Configured user: empty
- Image labels: absent (`null`)

**Decision:** Inspect the image entrypoint and available Suricata command-line options before starting a container. Do not assume the image runs as a non-root user or has a safe default command.

**Status:** Image metadata verified; startup behavior remains unverified.

### Suricata Entrypoint Inspection — 11 October 2026

**Objective:** Determine how the downloaded container image starts Suricata and which command-line options are available.

**Checks planned:**
- Read `/entrypoint.sh` from the image without executing it as a service.
- Inspect the Suricata executable's version and help output.
- Identify the expected configuration file and startup arguments, if documented by the image.
- Avoid unnecessary Linux capabilities and privileged container settings.

**Safety:** No persistent container, live capture, attack traffic, or firewall modification.

**Next action:** Inspect the entrypoint and executable help, then design a minimal detection-only container configuration.

**Status:** Inspection planned; startup behavior not yet verified.

### Suricata Entrypoint Inspection Results — 11 October 2026

**Verified:**
- Suricata reports version `8.0.4 RELEASE`.
- The executable supports offline PCAP processing (`-r`), live interface capture (`-i`), configuration testing (`-T`), and JSON-compatible logging through its configuration.
- The image entrypoint copies files from `/etc/suricata.dist/` into `/etc/suricata/` when destination files do not exist.
- The entrypoint checks `sys_nice` and `net_admin` capabilities.
- When those capability checks fail, the entrypoint warns that it will run as root. If both pass, it attempts to run Suricata as the `suricata` user.

**Safety decision:** Do not use privileged mode or add Linux capabilities until the selected capture method requires them. Prefer offline PCAP testing or another minimal-permission method where practical.

**Next action:** Inspect the default configuration files and logging settings before running Suricata against any traffic.

**Status:** Version and help verified; default configuration and capture behavior not yet tested.

### Suricata Default Configuration Inspection — 11 October 2026

**Image inspected:** `openeuler/suricata:8.0.4-oe2403sp4`

**Findings:**
- `/etc/suricata.dist/` contains `update.yaml`.
- The expected `/etc/suricata.dist/suricata.yaml` file was not found.
- The configuration summary returned no matching settings because the expected file was absent.
- Suricata's executable and help output were available in earlier checks.

**Interpretation:** The configuration path and startup requirements remain unresolved. The missing file at this specific path does not establish that no configuration exists elsewhere in the image.

**Next action:** Inspect the image filesystem for `suricata.yaml`, rule files, and relevant configuration directories. Do not start live capture or grant additional privileges until the configuration requirements are understood.

**Status:** Default configuration not found at the expected path; filesystem inspection pending.

### Suricata Filesystem Inspection Results — 11 October 2026

**Image:** `openeuler/suricata:8.0.4-oe2403sp4`

**Findings:**
- The executable exists at `/usr/bin/suricata`.
- `/etc/suricata/` and `/etc/suricata.dist/` contain `update.yaml`, but no `suricata.yaml` was found.
- `/usr/share/suricata/rules/` contains built-in protocol event rule files.
- `/usr/share/suricata/classification.config` and `/usr/share/suricata/reference.config` are present.
- `/var/lib/suricata/` exists but contains no files at inspection time.

**Interpretation:** The image's configuration requirements are not yet satisfied for a normal detection run. The presence of protocol event rules does not establish that a complete attack-signature ruleset is installed.

**Next action:** Check the image documentation for its intended configuration source and startup procedure. If necessary, prepare a project-owned minimal configuration and validate it with Suricata's configuration-test mode before any traffic capture.

**Safety:** No live capture, attack traffic, firewall changes, or persistent containers were used.

**Status:** Executable and built-in event rules verified; complete detection configuration remains pending.

### Suricata Image Startup Documentation Review — 11 October 2026

**Source reviewed:** Published documentation for `openeuler/suricata`.

**Findings:**
- The image documentation describes mounting `/etc/suricata` for configuration files.
- Its example for live interface capture uses host networking and `net_admin`, `net_raw`, and `sys_nice` capabilities.
- The local image does not contain `suricata.yaml` in the inspected configuration directories.
- The documented live-capture example is not appropriate as the default for this project's first isolated test.

**Decision:** Do not start live capture with host networking or add Linux capabilities at this stage. Prepare and validate a project-owned Suricata configuration, then begin with a controlled detection test.

**Next action:** Determine the safest source for a version-compatible configuration and establish how to validate it before use.

**Status:** Startup documentation reviewed; configuration preparation pending.

### Suricata Configuration Source Decision — 11 October 2026

**Decision:** Use the official OISF Suricata 8.0.4 configuration template as the reference for the project-owned configuration.

**Rationale:**
- The downloaded container reports Suricata `8.0.4 RELEASE`.
- The container image does not contain `suricata.yaml` in the inspected configuration directories.
- The official OISF repository provides the Suricata configuration template.
- Version-matched configuration reduces the risk of using unsupported or changed options.
- Project-owned configuration files can be reviewed, version-controlled, and tested independently of the container image.

**Constraints:**
- Keep configuration under the project directory.
- Do not modify host system configuration.
- Do not enable live capture, inline IPS mode, host networking, or extra Linux capabilities at this stage.
- Validate the configuration with Suricata's `-T` option before processing any traffic.

**Next action:** Retrieve the version-matched template into a project-local location, inspect its variables and placeholders, and prepare a valid configuration for offline testing.

**Status:** Configuration source selected; retrieval and validation pending.

### Suricata 8.0.4 Configuration Template Retrieved — 11 October 2026

**Source:** Official OISF Suricata repository, tag `suricata-8.0.4`.

**File:** `config/suricata/suricata.yaml.in`

**Download result:** Successful.

**File size:** 93,543 bytes; 2,355 lines.

**Inspection findings:**
- The file is a build-time template rather than a directly usable runtime configuration.
- Placeholders include `@PACKAGE_VERSION@`, `@MAJOR_MINOR@`, `@e_logdir@`, `@prefix@`, `@e_enable_evelog@`, `@e_sysconfdir@`, and `@e_defaultruledir@`.
- Logging, plugin, run-directory, and rule-path settings depend on build-time values.

**Decision:** Preserve the original template. Do not rename it directly to `suricata.yaml` or replace placeholders indiscriminately.

**Next action:** Inspect the relevant configuration sections and determine a safe, version-compatible way to generate a runtime configuration with valid paths and EVE JSON logging.

**Status:** Template downloaded and inspected; runtime configuration not yet generated or validated.

### Suricata Runtime Configuration Preparation — 11 October 2026

**Objective:** Determine how to convert the official Suricata 8.0.4 template into a valid runtime configuration for the container image.

**Checks planned:**
- Inventory all remaining template placeholders.
- Inspect EVE JSON output configuration.
- Inspect default rule and configuration paths.
- Identify network settings that need to remain suitable for offline testing.
- Preserve the original template unchanged.

**Safety constraints:** Do not substitute placeholders blindly, generate attack traffic, start live capture, enable IPS mode, or grant additional container capabilities.

**Next action:** Review the relevant configuration sections and determine the minimum changes needed for a valid runtime configuration.

**Status:** Template downloaded; runtime configuration preparation in progress.

### Suricata Configuration Path and Ruleset Audit — 11 October 2026

**Findings:**
- The official Suricata 8.0.4 template contains unresolved build-time placeholders.
- EVE JSON output is configured as `eve.json`, but its enabled setting is a placeholder.
- The template expects `suricata.rules` and references classification and reference configuration files.
- The template includes AF_PACKET and PCAP interface examples; these do not mean live capture is currently enabled.
- The container inspection previously found classification and reference files, but no complete `suricata.yaml` or full `suricata.rules` file in the inspected locations.

**Decision:** Verify the container's actual configuration, rules, and log directories before generating the runtime configuration. Do not assume distribution paths from the template.

**Safety:** No live capture, inline IPS, or additional Linux capabilities will be enabled during this audit.

**Status:** Template inspected; container path and ruleset audit pending.

### Suricata Ruleset Availability and Build Paths — 11 October 2026

**Findings:**
- The container runs Suricata 8.0.4 RELEASE with detection support.
- The image includes protocol-event rule files under `/usr/share/suricata/rules/`.
- No complete `suricata.rules` file was found in the inspected rule directories.
- Classification and reference configuration files exist under `/usr/share/suricata/`.
- Build information reports `/usr/etc/suricata/` as the configuration directory and `/usr/var/log/suricata/` as the log directory.

**Decision:** Do not assume the image contains a complete attack-signature ruleset. Inspect the installed `suricata-update` utility and its configured sources before selecting a ruleset.

**Safety constraints:** Do not download or enable rules yet, start packet capture, or change existing Docker resources.

**Next action:** Inspect updater version, help, and source configuration.

**Status:** Image paths and available rule files audited; updater inspection pending.

### Suricata Ruleset Updater Inspection — 11 October 2026

**Findings:**
- Installed utility: `suricata-update` 1.3.7.
- Supported operations include listing sources, listing enabled sources, enabling/disabling sources, adding sources, and updating rules.
- The inspected update configuration contains a reload command but no explicit source configuration.
- The updater's help output confirms that a custom configuration file and output directory can be specified.

**Decision:** Inspect the available and enabled ruleset sources before selecting a source or downloading rules.

**Safety constraints:** Do not run `update`, `update-sources`, or `enable-source` yet. Do not modify the container image or existing Docker resources.

**Next action:** Query the updater's source index and current enabled-source list.

**Status:** Updater capabilities verified; source selection pending.

### Suricata Ruleset Source Inventory — 11 October 2026

**Tool:** `suricata-update` 1.3.7
**Suricata:** 8.0.4 RELEASE

**Available source findings:**
- `et/open`: Emerging Threats Open Ruleset, vendor Proofpoint, MIT license.
- `oisf/trafficid`: Suricata Traffic ID ruleset, vendor OISF, MIT license.
- The updater lists additional community and commercial sources, but they have not been selected.

**Currently enabled sources:**
- `et/open`
- `oisf/trafficid`

**Important distinction:** An enabled source is not proof that its rules have already been downloaded, installed, or loaded by a running Suricata process.

**Decision:** Retain the two currently enabled sources for initial detection-only evaluation. Before downloading, verify the updater's source metadata and determine how to direct its output to a project-local directory.

**Safety constraints:** Do not enable additional sources, run a rules update, start packet capture, or enable inline IPS.

**Status:** Source inventory complete; project-local rules retrieval pending.

### Suricata Updater Output and Source Definitions — 11 October 2026

**Findings:**
- `suricata-update` 1.3.7 supports a custom rules output directory through `-o` and a custom data directory through `-D`.
- The container stores source definitions under `/usr/var/lib/suricata/update/sources/`.
- Source-definition files exist for `et/open` and `oisf/trafficid`.
- The project-local `rules/suricata/` directory does not yet exist.

**Decision:** Inspect the enabled-source definitions before retrieving rules. Future rule output should be directed to a project-local directory, and the original container image and existing Docker resources must remain unchanged.

**Safety constraints:** No rule downloads, source changes, live capture, or IPS-mode changes during this inspection.

**Status:** Updater output options confirmed; source definitions identified for inspection.

### Suricata Enabled-Source Definitions Verified — 11 October 2026

**Source definitions inspected:**
- `/usr/var/lib/suricata/update/sources/et-open.yaml`
  - Source: `et/open`
  - Checksum verification: enabled
- `/usr/var/lib/suricata/update/sources/oisf-trafficid.yaml`
  - Source: `oisf/trafficid`

**Interpretation:** The updater has definitions for the two enabled sources. This does not establish that their rules are downloaded, validated, or loaded into a running Suricata process.

**Decision:** Keep the container image unchanged and use a project-local workspace for subsequent ruleset retrieval and validation. Preserve the original template and keep live capture and inline prevention disabled.

**Next action:** Inspect existing project ignore rules and directory conventions before creating a persistent rules workspace.

**Status:** Source definitions verified; project-local rules workspace preparation pending.

### Suricata Rules Workspace and Git Hygiene — 11 October 2026

**Objective:** Check the repository's existing ignore rules and directory conventions before preparing a persistent, project-local Suricata rules workspace.

**Checks planned:**
- Inspect the root `.gitignore`, if present.
- Check existing ignore rules relevant to Suricata configuration, downloaded rules, logs, and runtime data.
- Inspect the current project directory structure and Git status.
- Identify whether the proposed rules directory conflicts with existing project files.

**Safety constraints:**
- Do not modify files during this inspection.
- Do not delete, prune, or alter existing Docker resources.
- Do not download rules or start packet capture.
- Preserve the original Suricata template.

**Next action:** Use the inspection results to determine the appropriate project-local rules directory and Git ignore policy.

**Status:** Source definitions verified; repository hygiene inspection pending.

### Suricata Rules Directory and Git Ignore Decision — 11 October 2026

**Repository findings:**
- The project has an existing `docker/suricata/` directory containing `.gitkeep`.
- The official template is located at `config/suricata/suricata.yaml.in`.
- Root `.gitignore` already excludes `data/` and `logs/`.
- No tracked Suricata rules files were found.
- Current Git status includes an uncommitted research-log change and untracked `config/suricata/`.

**Decision:** Keep configuration under `config/suricata/`. Use a separate project-local `rules/suricata/` directory for downloaded rules, rather than mixing them with Docker files or configuration templates.

**Git policy:** Review and add a narrow ignore rule for downloaded/generated rules if appropriate. Do not ignore the configuration template or research documentation. Do not stage or commit files as part of this step.

**Safety constraints:** Preserve existing files and Docker resources; do not download or activate rules yet.

**Status:** Repository structure reviewed; rules directory and ignore policy selected for implementation.

### Project-Local Suricata Rules Workspace Created — 11 October 2026

**Planned changes:**
- Add a narrow `.gitignore` rule for downloaded/generated Suricata rules.
- Create `rules/suricata/` as the project-local destination for the ruleset.
- Preserve `config/suricata/suricata.yaml.in` and all research documentation in Git.
- Leave existing Docker-related files unchanged.

**Rationale:** Third-party rules can change independently of the project and may be large. Keeping generated rules out of routine commits avoids accidental vendor-rule redistribution while allowing the project to document its ruleset source and retrieval procedure.

**Safety constraints:** No rules are downloaded or enabled in this step. No Docker resources are changed. No files are staged or committed.

**Status:** Implementation planned; repository changes pending verification.

### Suricata Rules Workspace Setup Verified — 11 October 2026

**Changes made:**
- Added `/rules/suricata/*` to the root `.gitignore`.
- Added an exception for `/rules/suricata/.gitkeep`.
- Created `rules/suricata/.gitkeep`.

**Verification:**
- `git check-ignore` identifies `rules/suricata/example.rules` as ignored.
- `.gitkeep` is explicitly exempted from the ignore rule.
- Git reports the expected pending changes in `.gitignore`, the research log, and the untracked configuration and rules directories.

**Status:** Project-local rules workspace created. No rules have been downloaded or activated.

**Next action:** Retrieve the enabled rules into the project-local workspace using an isolated, temporary container and validate the resulting files before configuring Suricata to load them.

### Suricata Ruleset Retrieval Plan — 11 October 2026

**Objective:** Retrieve the enabled `et/open` and `oisf/trafficid` rules into `rules/suricata/` without modifying the container image or host-level Suricata paths.

**Planned approach:**
- Run the existing Suricata 8.0.4 container as a temporary, one-off updater.
- Mount the project-local rules directory as the output destination.
- Use an isolated, project-local updater data directory for caches and source metadata.
- Preserve the original template and existing project files.
- Inspect the resulting rules and updater output before configuring Suricata to load them.

**Safety constraints:**
- Do not use `--privileged`, host networking, or additional Linux capabilities.
- Do not start live capture or inline IPS.
- Do not remove, prune, or alter existing Docker resources.
- Do not commit downloaded third-party rules.

**Validation requirements:** Confirm retrieval status, resulting files, and rule counts before proceeding to runtime configuration.

**Status:** Retrieval approach planned; updater execution not yet performed.

### Suricata Rules Retrieval Execution — 11 October 2026

**Preconditions:**
- Project-local rules directory exists at `rules/suricata/`.
- Git ignores downloaded/generated rules while preserving `.gitkeep`.
- Enabled sources are `et/open` and `oisf/trafficid`.
- Suricata 8.0.4 and `suricata-update` 1.3.7 are available in the container image.

**Execution plan:**
- Use a temporary updater container with explicit mounts for rules output and updater state.
- Keep all persistent output under the project directory.
- Review the updater result and generated rule files before using them.

**Safety constraints:**
- No live packet capture or inline IPS.
- No privileged container, host networking, or additional capabilities.
- No changes to existing Docker resources.
- No Git staging or commit of downloaded rules.

**Status:** Ready for the retrieval command; ruleset download has not yet been attempted.
### Suricata Ruleset Retrieval Completed — 11 October 2026

**Execution:** Ran `suricata-update` 1.3.7 in a temporary container using the Suricata 8.0.4 image, with the output directory mounted to the project-local `rules/suricata/` path.

**Sources retrieved:**
- `et/open` — Emerging Threats Open Ruleset.
- `oisf/trafficid` — Suricata Traffic ID ruleset.

**Updater-reported results:**
- Total rules loaded: 69,105.
- Rules disabled: 15.
- Rules enabled: 53,149.
- Flowbit dependency rules enabled: 136.
- Combined output: `/rules/suricata.rules`.
- Classification output: `/rules/classification.config`.
- Updater completed successfully.

**Limitations:**
- The source index was reported as older than two weeks.
- Rule testing was skipped using `--no-test`.
- Successful retrieval does not prove the rules are compatible with the final project configuration or loaded by Suricata.

**Safety:** No live capture or inline IPS was started. No additional Linux capabilities or host networking were requested.

**Next action:** Inspect the generated files, their sizes, rule counts, and Git ignore behavior before configuring Suricata to load them.

**Status:** Retrieval completed; file inspection and runtime validation pending.

### Downloaded Suricata Ruleset Inspected — 11 October 2026

**Files verified:**
- `rules/suricata/suricata.rules`: 69,105 lines; 45,892,735 bytes.
- `rules/suricata/classification.config`: 43 lines; 3,228 bytes.
- `rules/suricata/.gitkeep`: present.

**Rule-file checks:**
- Updater-reported total rules: 69,105.
- Local rule-file line count: 69,105.
- Rules with active `alert`, `drop`, `reject`, or `pass` actions: 53,149.
- Unique signature IDs: 69,105.
- Git ignore verification succeeded for both downloaded files.

**Limitations:** Line counts and unique signature IDs are structural checks, not proof of rule correctness or runtime compatibility. The updater was run with `--no-test`, so Suricata has not yet validated this ruleset against the project configuration.

**Status:** Downloaded files and Git ignore behavior verified; runtime validation pending.

**Next action:** Prepare a runtime configuration from the version-matched template, using the confirmed project-local rule and classification paths, then validate it with Suricata's configuration-test mode before processing traffic.

### Runtime Configuration Preparation — Template Section Review — 11 October 2026

**Objective:** Identify the minimum template sections needed to prepare a valid Suricata 8.0.4 runtime configuration.

**Known project files:**
- Template: `config/suricata/suricata.yaml.in`
- Rules: `rules/suricata/suricata.rules`
- Classification file: `rules/suricata/classification.config`

**Review targets:**
- Build-time placeholders affecting YAML syntax and filesystem paths.
- EVE JSON logging configuration.
- Default rule path and rule-file list.
- Classification and reference configuration paths.
- Network variables and packet-capture interface examples.

**Constraints:** Preserve the original template. Do not start live capture, enable inline IPS, or grant additional capabilities. Do not assume that a template becomes runtime-valid merely by replacing placeholder strings.

**Next action:** Inspect the exact relevant sections and use the results to determine a minimal configuration-generation strategy.

**Status:** Downloaded rules inspected; runtime configuration preparation pending.


### Suricata Runtime Configuration Strategy — 11 October 2026

**Inspection findings:**
- The template declares `suricata-version: "@MAJOR_MINOR@"`.
- The default log directory and EVE JSON enabled setting contain build-time placeholders.
- Plugin entries also contain build-time placeholders.
- The rules section expects `suricata.rules`.
- Classification and reference paths contain build-time placeholders.
- The container provides `/usr/share/suricata/classification.config` and `/usr/share/suricata/reference.config`.

**Decision:** Prepare a project-owned runtime configuration using explicit, valid paths for logs, rules, classification, and reference files. Enable EVE JSON logging for future event analysis. Preserve the original template unchanged and avoid indiscriminate placeholder substitution.

**Validation plan:** Use the Suricata 8.0.4 binary's configuration-test mode (`-T`) before processing any traffic. Keep live capture, inline IPS, host networking, and additional capabilities disabled.

**Status:** Required configuration sections inspected; runtime configuration generation and validation pending.

### Project-Owned Suricata Runtime Configuration Created — 11 October 2026

**Objective:** Generate a runtime configuration separate from the original OISF template.

**Planned configuration:**
- Preserve `config/suricata/suricata.yaml.in` unchanged.
- Create `config/suricata/suricata.yaml`.
- Configure explicit log, rules, classification, and reference paths.
- Enable EVE JSON output for later event inspection.
- Keep live capture and inline IPS disabled during initial validation.

**Validation:** Inspect the generated configuration and its changes before running Suricata's configuration-test mode.

**Safety:** Do not enable additional capabilities, host networking, or prevention actions. Do not modify existing Docker resources.

**Status:** Runtime configuration generation planned; validation pending.
### Candidate Suricata Runtime Configuration Generated — 11 October 2026

**File created:** `config/suricata/suricata.yaml`

**Generation result:**
- File size: 93,427 bytes.
- Unresolved placeholder scan: none found.
- Original template retained separately at `config/suricata/suricata.yaml.in`.
- The generated configuration has not yet passed Suricata's configuration-test mode.

**Important validation targets:**
- Effective rule directory and `suricata.rules` entry.
- Classification and reference configuration paths.
- EVE JSON enabled setting and output filename.
- Plugin entries after placeholder substitution.
- Any settings that may attempt live capture during startup.

**Decision:** Inspect these settings before running the configuration test. Do not treat placeholder removal as proof of YAML validity or runtime compatibility.

**Status:** Candidate generated; configuration inspection and validation pending.

### Candidate Runtime Configuration Inspection — 11 October 2026

**Verified settings:**
- Runtime configuration: `config/suricata/suricata.yaml`.
- `suricata-version`: `8.0`.
- Default log directory: `/var/log/suricata`.
- EVE JSON output: enabled, filename `eve.json`.
- Default rule path: `/rules`.
- Rule file: `suricata.rules`.
- Classification file: `/rules/classification.config`.
- Reference file: `/usr/share/suricata/reference.config`.
- Required project-local rules and classification files exist.

**Plugin review:** The PF_RING, Napatech, and nDPI plugin entries are commented out after substitution.

**Remaining concern:** The configuration includes multiple capture-engine sections. Their presence is not proof that live capture will start, but startup and test mode must be handled explicitly.

**Decision:** Before configuration validation, inspect the relevant capture-engine settings and determine a safe test invocation. Do not start a live sensor or enable inline prevention.

**Status:** Core paths and EVE settings verified; configuration-test invocation not yet run.

### Suricata Capture-Engine Configuration Inspection — 11 October 2026

**Configuration reviewed:** `config/suricata/suricata.yaml`

**Findings:**
- AF_PACKET defines `eth0` and a default interface.
- PCAP defines `eth0` and a default interface.
- The DPDK section contains example PCI hardware address `0000:3b:00.0`.
- PF_RING defines `eth0`.
- Napatech contains example stream settings.
- The configuration also includes PCAP-file processing settings.
- The project rules file contains 69,105 lines and occupies 45,892,735 bytes.

**Interpretation:** Capture-engine interface definitions in a configuration file do not, by themselves, establish which run mode will be used. The DPDK hardware address and other environment-dependent settings require compatibility validation.

**Safety constraint:** The next validation must use Suricata's configuration-test mode (`-T`) inside the selected container, without host networking, elevated privileges, or intentional live packet capture.

**Status:** Inspection complete; configuration validation pending.

### Suricata Configuration Test Passed — 11 October 2026

**Test environment:**
- Container image: `openeuler/suricata:8.0.4-oe2403sp4`
- Suricata version: `8.0.4 RELEASE`
- Configuration: `config/suricata/suricata.yaml`
- Rules directory: `rules/suricata/`
- Test mode: `-T`
- Command configuration path: `/etc/suricata/suricata.yaml`

**Result:** Suricata successfully loaded the candidate configuration and exited normally.

**Safety:** The test used an isolated container without host networking or additional capabilities. Configuration and rules were mounted read-only.

**Limitations:** This result establishes configuration-load success only. It does not establish live-capture readiness, attack-detection accuracy, or prevention effectiveness.

**Decision:** Preserve the validated configuration as the current candidate. Next, inspect the generated runtime logs and confirm the rule-loading details before conducting controlled detection experiments.

**Status:** Configuration test passed; detection testing not yet performed.

### Suricata Rule Paths and Runtime Log Inspection — 11 October 2026

**Configuration findings:**
- Default rule path: `/rules`.
- Configured rule file: `suricata.rules`.
- Classification file: `/rules/classification.config`.
- Reference file: `/usr/share/suricata/reference.config`.
- EVE JSON logging is enabled with filename `eve.json`.

**Ruleset inventory:**
- Total rule-file lines: 69,105.
- Lines beginning with an active `alert`, `drop`, `reject`, or `pass` action: 53,149.

**Runtime files observed:**
- `logs/suricata/eve.json`: 0 bytes.
- `logs/suricata/suricata.log`: 1,381 bytes.
- `logs/suricata/stats.log`: 0 bytes.
- `logs/suricata/fast.log`: 0 bytes.

**Interpretation:** An empty EVE file is consistent with a configuration-only test that processed no traffic. Rule-file counts are inventory figures, not proof of successful rule loading.

**Decision:** Inspect `suricata.log` to establish the rule-loading result and identify any warnings before conducting detection experiments.

**Status:** Paths and log files inspected; actual rule-loading details pending.

### Suricata Rule-Loading Validation Passed — 11 October 2026

**Environment:** Suricata 8.0.4 RELEASE in Docker, running configuration-test mode.

**Verified results from `logs/suricata/suricata.log`:**
- Rule files processed: 1.
- Rules successfully loaded: 53,149.
- Rules failed: 0.
- Rules skipped: 0.
- Signatures processed: 53,154.
- IP-only rules: 1,216.
- Signatures inspecting packet payload: 4,543.
- Signatures inspecting the application layer: 47,159.
- Decoder-event-only signatures: 110.
- Threshold configuration parsed successfully, with 0 rules found.
- Suricata reported that the configuration loaded successfully and exited normally.
- Engine mode was reported as IDS mode by default.

**Interpretation:** The candidate configuration and configured ruleset passed Suricata's configuration test. The five-signature difference between successfully loaded rules and processed signatures is reported by Suricata itself; it should not be interpreted as five failed rules.

**Limitations:** No traffic was processed, so detection effectiveness, EVE alert generation, and live-capture readiness remain unverified. The zero-rule threshold configuration is an observation, not evidence of a failure.

**Decision:** Proceed to a controlled, offline PCAP detection experiment before considering live traffic capture. Keep inline prevention disabled.

**Status:** Configuration and ruleset validation passed; detection experiment pending.

### Suricata Offline Detection Test Plan — 11 October 2026

**Prerequisites verified:**
- Suricata 8.0.4 is available in Docker.
- Candidate configuration passes `-T` validation.
- All 53,149 configured rules load successfully; zero failed and zero skipped.
- EVE JSON output is enabled.
- The project-local runtime log directory is `logs/suricata/`.

**Experiment objective:** Verify that Suricata can process a controlled PCAP offline, apply its configured detection rules, and write the resulting events to EVE JSON.

**Test boundaries:**
- Use a small, locally generated or otherwise authorized PCAP.
- Process the file in offline mode; do not capture live interfaces.
- Do not use host networking, elevated container privileges, or inline prevention.
- Preserve the original runtime configuration and ruleset.
- Record the PCAP provenance, Suricata command, exit status, event counts, and relevant log messages.

**Success criteria:**
1. Suricata completes offline packet processing.
2. The EVE JSON output is valid JSON, if events are written.
3. Any generated alerts are attributable to the test traffic and loaded rules.
4. A lack of alerts is reported accurately and is not treated as proof that detection is broken.

**Limitations:** Configuration validation alone does not establish detection effectiveness. This experiment is a functional smoke test, not a comprehensive accuracy or performance evaluation.

**Status:** Offline detection experiment planned; PCAP generation and execution pending.

### Synthetic Benign PCAP Preparation — 11 October 2026

**Objective:** Create a minimal, locally generated packet capture for the first offline Suricata processing test.

**Planned traffic:** Synthetic Ethernet, IPv4, UDP, and DNS packets representing a benign DNS query and response.

**Isolation:** Packet bytes will be generated locally and written to a PCAP file. No packets will be transmitted, and no live network interface will be opened.

**Test constraints:**
- Use a dedicated test directory under `data/`.
- Do not modify the candidate Suricata configuration or rules.
- Do not use live capture, host networking, elevated container privileges, or inline prevention.
- Verify the PCAP file and its packet count before processing it with Suricata.

**Success criteria:** A valid, readable PCAP containing the intended synthetic packets is available for offline testing.

**Limitations:** This benign capture tests packet processing and logging infrastructure. It does not demonstrate attack detection or prevention effectiveness.

**Status:** PCAP generation planned; file creation and validation pending.

### Synthetic DNS PCAP Created — 11 October 2026

**Artifact:** `data/suricata-test/benign-dns.pcap`

**Verification results:**
- File type: classic PCAP, version 2.4.
- Link type: Ethernet.
- Packet count reported by the generator: 2.
- File size: 214 bytes.
- SHA-256: `3cd346f634f3da468a97db566d2220bdcaadf32b586c6befd6a9c7cdb1d97c17`.

**Traffic description:** The generated capture contains a synthetic DNS query and response involving documentation-only IPv4 addresses in `192.0.2.0/24`.

**Safety:** Packets were written directly to a file. No network transmission or live capture was performed.

**Limitations:** File identification and checksum do not independently verify every protocol field. Suricata's offline processing will provide the next functional check.

**Status:** PCAP file created and identified; offline processing pending.

### Suricata Offline PCAP Smoke Test Passed — 11 October 2026

**Environment:** Suricata 8.0.4 in Docker, processing a local PCAP in offline mode.

**Input:** `data/suricata-test/benign-dns.pcap`

**Observed results:**
- PCAP files read: 1.
- Packets processed: 2.
- Packet bytes reported by Suricata: 158.
- EVE JSON output size: 9,888 bytes.
- DNS events: 2.
- Flow events: 1.
- Statistics events: 1.
- Invalid JSON lines: 0.
- Total valid EVE events: 4.

**Interpretation:** Suricata successfully processed the synthetic capture, decoded both DNS packets, and emitted valid EVE JSON. This verifies basic offline packet processing and event logging.

**Limitations:** This was a benign smoke test, not an attack-detection test. No alert was observed in the event-type summary, but this summary alone does not establish whether every rule was eligible to match the synthetic traffic. The test does not establish live-capture readiness or prevention effectiveness.

**Decision:** Preserve this test as a functional baseline. The next experiment should use a controlled, locally generated detection test to verify alert generation before integrating Suricata events with the machine-learning component.

**Status:** Offline processing and EVE JSON validation passed; controlled alert test pending.

### Controlled Suricata Alert-Test Plan — 11 October 2026

**Objective:** Verify that Suricata can match a deliberately selected test signature and emit an alert in EVE JSON.

**Existing baseline:**
- Configuration-test mode passed.
- 53,149 rules loaded; zero failed and zero skipped.
- The synthetic benign DNS PCAP processed successfully.
- Four valid EVE events were emitted: two DNS, one flow, and one statistics event.
- No alert was established by the previous event-type summary.

**Planned method:**
1. Inspect the current rule syntax and EVE alert-output configuration.
2. Create a separate temporary test rule with a unique signature ID.
3. Generate a small, locally constructed packet matching that rule.
4. Run Suricata offline against the packet using the temporary rule in an isolated test configuration.
5. Confirm the expected signature ID and alert event in valid EVE JSON.

**Safety constraints:**
- Do not edit or replace the production candidate ruleset.
- Do not transmit packets or capture live interfaces.
- Keep IDS mode and inline prevention disabled.
- Keep the test isolated from existing Docker services.

**Success criteria:** The expected test signature appears in an EVE `alert` event, and the event JSON parses successfully.

**Limitations:** A successful synthetic signature test validates the alert pipeline, not the detection accuracy of the full ruleset against real attacks.

**Status:** Alert-generation test planned; execution pending.

### Suricata Alert-Output Configuration Inspection — 11 October 2026

**Configuration reviewed:** `config/suricata/suricata.yaml`

**Findings:**
- EVE JSON logging is enabled.
- The EVE `types` list includes an `alert` event configuration.
- DNS, HTTP, and other protocol-specific event logging sections are present.
- The project rules directory currently contains `.gitkeep`, `classification.config`, and `suricata.rules`.
- Existing rules use Suricata signature syntax with fields such as `msg`, `sid`, and `rev`.

**Interpretation:** The configuration contains an EVE alert-output section, but the previous benign PCAP test did not establish that a signature match produces an alert event.

**Decision:** Use a dedicated temporary configuration and test rule for the next experiment. Do not edit the main ruleset or enable prevention.

**Status:** Alert-output configuration inspected; controlled alert test pending.

### Isolated Suricata Alert-Test Workspace Plan — 11 October 2026

**Objective:** Prepare a disposable workspace for verifying Suricata alert generation with a dedicated synthetic signature.

**Workspace:** `data/suricata-test/`

**Planned test artifacts:**
- A copy of the validated runtime configuration.
- A dedicated test-rule file containing one unique signature.
- The existing benign PCAP as a reference input.
- Separate output logs for the alert test.

**Isolation requirements:**
- Do not modify `config/suricata/suricata.yaml`.
- Do not modify `rules/suricata/suricata.rules`.
- Keep the test rule separate from the downloaded ruleset.
- Use offline PCAP processing only.
- Keep inline prevention disabled.
- Preserve the existing test artifacts.

**Validation sequence:** Prepare the isolated configuration, confirm the intended rule and EVE output paths, then test the signature against a purpose-built local PCAP.

**Limitations:** Creating the workspace alone does not demonstrate alert generation. That requires a subsequent execution and inspection of EVE JSON.

**Status:** Workspace plan documented; isolated configuration preparation pending.

### Isolated Suricata Alert-Test Workspace Created — 11 October 2026

**Workspace:** `data/suricata-test/`

**Verified artifacts:**
- `alert-test.yaml` created at 93,427 bytes.
- `benign-dns.pcap` retained at 214 bytes.
- `alert-rules/` directory created for the dedicated test signature.
- `alert-logs/` directory created for separate test output.

**Integrity checks:**
- SHA-256 of `config/suricata/suricata.yaml` and `data/suricata-test/alert-test.yaml` matches: `2295828355619be27e7a70746e1a33bfa3c9e3ad859439abf100a4b65bb24779`.
- Main ruleset SHA-256: `ba7d40a9b1492f6580c0bfca1566b367de7754f78a81b2f210e24851a12c8ea5`.

**Current test configuration paths:** The copied configuration still points to `/rules/suricata.rules` and `/var/log/suricata`. These paths must be adjusted in the isolated copy before the alert test.

**Decision:** Configure the isolated copy to load only the dedicated test rule and write logs to its dedicated output directory. Preserve the main configuration and ruleset.

**Status:** Workspace integrity verified; isolated path changes pending.

### Isolated Alert-Test Configuration Path Plan — 11 October 2026

**Target file:** `data/suricata-test/alert-test.yaml`

**Planned changes to the isolated copy only:**
1. Set `default-log-dir` to `/var/log/suricata-test`.
2. Set `default-rule-path` to `/test-rules`.
3. Replace the configured `suricata.rules` entry with a dedicated test-rule filename, `alert-test.rules`.
4. Point `classification-file` to the existing classification configuration available in the container, unless validation shows a different path is required.

**Container mounts planned for the experiment:**
- `data/suricata-test/alert-test.yaml` mounted read-only as the test configuration.
- `data/suricata-test/alert-rules/` mounted read-only as `/test-rules`.
- `data/suricata-test/alert-logs/` mounted as `/var/log/suricata-test`.
- The synthetic PCAP mounted read-only.

**Safety constraints:** No modifications to the main configuration or main ruleset; no live capture, host networking, additional capabilities, or inline prevention.

**Validation:** Inspect the exact resulting paths before running a configuration test.

**Status:** Planned; isolated configuration has not yet been edited.

### Isolated Alert-Test Configuration Updated — 11 October 2026

**Target:** `data/suricata-test/alert-test.yaml`

**Verified changes:**
- Log directory: `/var/log/suricata-test`.
- Default rule directory: `/test-rules`.
- Rule filename: `alert-test.rules`.
- Classification file: `/usr/share/suricata/classification.config`.

**Integrity verification:**
- Main configuration SHA-256 remains `2295828355619be27e7a70746e1a33bfa3c9e3ad859439abf100a4b65bb24779`.
- Isolated configuration SHA-256 is `ea4857de495036eba3eb7cb53155e597c5a8ea1d57c3273cc3757072d55f964e`.

**Interpretation:** The isolated configuration has the intended rule and logging paths. The main configuration remains unchanged.

**Caveat:** The isolated configuration has not yet been tested with its dedicated rule file. The classification-file path must also be confirmed against the container image before validation.

**Status:** Isolated path changes verified; dedicated rule creation and configuration validation pending.

### Dedicated Suricata Test Signature Plan — 11 October 2026

**Objective:** Prepare a single synthetic signature to verify the alert-generation pipeline.

**Test configuration:** `data/suricata-test/alert-test.yaml`

**Dedicated rule location:** `data/suricata-test/alert-rules/alert-test.rules`

**Planned signature properties:**
- A unique local-test signature ID.
- Alert action only; no `drop` or `reject` action.
- A narrowly scoped match against synthetic test traffic.
- A descriptive message identifying the experiment.

**Supporting configuration:** Confirm that the container provides the configured classification file before validation.

**Safety constraints:**
- Do not edit `rules/suricata/suricata.rules`.
- Do not enable inline prevention or live capture.
- Use offline processing and a separate EVE log directory.
- Do not interpret a successful synthetic signature match as proof of general attack-detection accuracy.

**Status:** Test signature design documented; supporting-file verification and rule creation pending.

### Dedicated Suricata Test Rule Created — 11 October 2026

**Supporting files verified inside the container:**
- `/usr/share/suricata/classification.config` exists.
- `/usr/share/suricata/reference.config` exists.

**Test rule:** `data/suricata-test/alert-rules/alert-test.rules`

**Signature details:**
- Action: `alert`.
- Protocol: UDP.
- Source: `192.0.2.10:53000`.
- Destination: `192.0.2.53:53`.
- Match: first four UDP payload bytes are `12 34 01 00`.
- Signature ID: `9900001`.
- Revision: `1`.

**Integrity check:** Main ruleset SHA-256 remains `ba7d40a9b1492f6580c0bfca1566b367de7754f78a81b2f210e24851a12c8ea5`.

**Interpretation:** The dedicated rule targets the synthetic DNS query and uses an alert-only action. Its successful creation does not yet establish that Suricata accepts or matches it.

**Status:** Supporting files verified and test rule created; isolated configuration validation pending.

### Isolated Suricata Configuration Test Passed — 11 October 2026

**Test configuration:** `data/suricata-test/alert-test.yaml`

**Test rule:** `data/suricata-test/alert-rules/alert-test.rules`

**Observed result:**
- Suricata version: 8.0.4 RELEASE.
- Configuration-test mode reported: `Configuration provided was successfully loaded. Exiting.`
- Test signature ID: `9900001`.
- Isolated configuration SHA-256: `ea4857de495036eba3eb7cb53155e597c5a8ea1d57c3273cc3757072d55f964e`.

**Limitation:** The captured terminal output does not show the detailed signature-loading count. Successful configuration loading alone does not confirm that the intended signature matched any packet.

**Decision:** Inspect the isolated test log for the rule-loading count and any errors before running the offline alert experiment.

**Status:** Configuration test passed; explicit signature-load verification pending.

### Isolated Signature-Load Verification — 11 October 2026

**Observed results:**
- Suricata configuration-test exit status: `0`.
- Suricata reported that the configuration loaded successfully.
- The captured output did not include a rule-loading summary.
- Successful configuration loading alone does not prove that signature `9900001` was loaded.

**Decision:** Inspect the test configuration's rule filename and the exact contents of the mounted rule file before proceeding. Do not interpret missing

### Isolated Rule Path Verification — 11 October 2026

**Verified:**
- Rule directory: `/test-rules`.
- Configured rule filename: `alert-test.rules`.
- Local test rule exists and is 148 bytes.
- Signature ID: `9900001`.
- Classification file is readable inside the Suricata container.
- Reference configuration path: `/usr/share/suricata/reference.config`.

**Unresolved:** The previous configuration-test output reported successful configuration loading but did not expose the detailed rule-loading count.

**Decision:** Capture the next test's complete stdout and stderr, including the process exit status, so we can distinguish successful configuration parsing from successful signature loading.

**Status:** Rule paths verified; explicit signature-load count pending.

### Suricata Test Signature Loading — Diagnostic Still Required — 11 October 2026

**Observed:**
- Configuration-test exit status: `0`.
- Suricata reports that the configuration loaded successfully.
- Captured output does not include the expected rule-loading count.
- The isolated rule file exists, uses signature ID `9900001`, and is referenced by the isolated configuration.
- The classification file is readable in the container.

**Interpretation:** Configuration-test success is established, but explicit evidence of the test signature being loaded is still missing. The output alone does not establish whether the rule matched or whether an alert was generated.

**Decision:** Avoid repeating the same command without improving observability. Inspect the isolated test logs and use a dedicated offline alert run to verify the expected signature ID in EVE JSON.

**Status:** Configuration accepted; signature loading and alert generation remain to be verified.


### Isolated Test Signature Load Confirmed — 11 October 2026

**Evidence source:** `data/suricata-test/alert-logs/suricata.log`

**Verified results:**
- Rule files processed: 1.
- Rules successfully loaded: 1.
- Rules failed: 0.
- Rules skipped: 0.
- Signatures processed: 1.
- Configuration test completed successfully.

**Test signature:** SID `9900001`, message `LOCAL TEST Synthetic DNS Query`.

**Interpretation:** Suricata successfully loaded the dedicated test signature. The empty EVE JSON file is consistent with configuration-test mode, which does not process the PCAP.

**Limitations:** Signature loading does not prove that the rule matches traffic or produces an alert.

**Decision:** Run the isolated configuration against the synthetic DNS PCAP in offline mode, then verify the EVE alert's signature ID.

**Status:** Signature loading verified; offline alert-generation test pending.

### Suricata Synthetic Alert Generation Passed — 11 October 2026

**Environment:** Suricata 8.0.4 in Docker, processing a local PCAP offline.

**Input:** `data/suricata-test/benign-dns.pcap`

**Rule:** `data/suricata-test/alert-rules/alert-test.rules`

**Observed results:**
- PCAP files processed: 1.
- Packets processed: 2.
- Packet bytes reported by Suricata: 158.
- Dedicated test rules loaded: 1.
- Rules failed: 0.
- Rules skipped: 0.
- EVE alert events: at least 1.
- Expected signature ID `9900001`: matched.
- Signature message: `LOCAL TEST Synthetic DNS Query`.
- Source IP: `192.0.2.10`.
- Destination IP: `192.0.2.53`.
- Invalid EVE JSON lines: 0.

**Interpretation:** The test verifies that Suricata can process the synthetic capture, match a dedicated alert-only rule, and emit an alert in valid EVE JSON. The alert pipeline works in this controlled offline scenario.

**Limitations:** This synthetic test does not measure detection accuracy against real attacks, validate live network capture, or demonstrate prevention effectiveness. The temporary signature is a test fixture, not an attack-detection rule.

**Decision:** Preserve this result as the Suricata alert-pipeline baseline. Next, inspect the resulting EVE event fields and plan a controlled test using an existing, relevant Suricata signature before considering live traffic.

**Status:** Synthetic offline alert test passed; broader detection validation pending.

### Suricata EVE Alert Schema Inspection — 11 October 2026

**Evidence source:** `data/suricata-test/alert-logs/eve.json`

**Observed alert fields:**

| Field | Observed value |
|---|---|
| `event_type` | `alert` |
| `timestamp` | `2026-10-11T17:50:00.000000+0000` |
| `src_ip` | `192.0.2.10` |
| `src_port` | `53000` |
| `dest_ip` | `192.0.2.53` |
| `dest_port` | `53` |
| `proto` | `UDP` |
| `app_proto` | `dns` |
| `alert.signature_id` | `9900001` |
| `alert.signature` | `LOCAL TEST Synthetic DNS Query` |
| `alert.action` | `allowed` |
| `flow_id` | `1461331347` |
| `pcap_cnt` | `1` |
| `pkt_src` | `wire/pcap` |

**Flow metadata:** The event also contains packet and byte counters for the client-to-server and server-to-client directions.

**Interpretation:** EVE provides useful event metadata for alert correlation, logging, and downstream analysis. The observed `allowed` action is consistent with alert-only IDS behavior.

**ML integration constraint:** These event fields are not equivalent to the existing model's 77 CIC-IDS2017 features. Any adapter must define explicit feature mappings and handle unavailable features without inventing values.

**Limitations:** This event was generated by a synthetic test signature against a synthetic PCAP. It does not establish attack-detection accuracy or live-capture behavior.

**Status:** EVE alert schema inspected; integration design pending.

### Built-In Suricata Signature Selection Plan — 11 October 2026

**Objective:** Select a suitable existing Suricata signature for a controlled offline detection experiment.

**Current baseline:**
- Suricata 8.0.4 configuration test passed.
- The main ruleset loaded 53,149 rules successfully.
- A dedicated synthetic signature generated an EVE alert with SID `9900001`.
- EVE JSON parsing succeeded with no invalid lines.
- The observed test alert had action `allowed`, consistent with alert-only IDS behavior.

**Planned selection criteria:**
1. The signature must exist in the downloaded ruleset and be enabled.
2. Its matching conditions must be understood before creating test traffic.
3. The test should use locally generated or otherwise authorized offline PCAP data.
4. The test must not depend on live capture, external targets, or inline prevention.
5. The result must identify the actual signature ID and alert event, if any.

**Limitations:** A synthetic rule match validates the alert pipeline, not the detection accuracy of the downloaded ruleset. A built-in rule should not be selected merely because its name sounds relevant; its full matching conditions must be inspected.

**Status:** Selection criteria documented; candidate signature inspection pending.

### Built-In Suricata Rule Inventory — 11 October 2026

**Objective:** Identify and inspect an enabled signature from the downloaded Suricata ruleset before designing an offline detection test.

**Ruleset location:** `rules/suricata/suricata.rules`

**Inspection procedure:**
1. Search the ruleset for candidate alert signatures.
2. Read each candidate's complete rule definition, including protocol, source and destination constraints, content matches, SID, and revision.
3. Confirm the candidate is enabled and determine what traffic would satisfy its matching conditions.
4. Select a candidate only after its conditions are understood.

**Safety constraints:** This stage is read-only. Do not modify the production ruleset, generate traffic, enable live capture, or activate packet blocking.

**Evidence limitation:** Finding a signature in the ruleset does not demonstrate that it detects an attack. Detection must be evaluated separately using a controlled, matching test input.

**Status:** Inspection plan recorded; candidate selection pending.

### Built-In DNS Signature Candidate Identified — 11 October 2026

**Candidate:** ET Open DNS signature, SID `2034819`.

**Signature message:** `ET ATTACK_RESPONSE DNS Query for Observed CVE-2021-44228 Security Scanner Domain (log4j .binaryedge .io)`

**Observed matching conditions:**
- DNS application protocol.
- Source address must match `$HOME_NET`.
- DNS query inspection using `dns.query`.
- A dot-prefixed, case-insensitive domain suffix match for `.log4j.binaryedge.io`.
- The rule uses the `alert` action.

**Why it is a candidate:** A synthetic DNS query can be generated for an isolated offline PCAP test without contacting the named domain or attempting exploitation.

**Checks still required:**
1. Inspect the complete rule and confirm its SID and revision.
2. Account for the configured `$HOME_NET` when constructing the test packet.
3. Determine whether the offline test produces the expected EVE alert.

**Safety and evidence limitations:** No external DNS request or exploit attempt is planned. A successful signature match would validate this specific detection condition, not Log4Shell exploitation detection in general.

**Status:** Candidate identified; detailed inspection pending.

### Built-In DNS Signature Conditions Verified — 11 October 2026

**Verified candidate:** SID `2034819`, revision `1`.

**Rule conditions confirmed:** The signature inspects DNS queries from `$HOME_NET` and matches the case-insensitive suffix `.log4j.binaryedge.io`, with `dotprefix` and `endswith` modifiers. Its action is `alert`.

**Test-design consequence:** The existing synthetic PCAP uses source address `192.0.2.10`, outside the configured `$HOME_NET`. It is therefore unsuitable for directly testing this rule.

**Next test design:** Create a separate, locally generated DNS PCAP using a synthetic query such as `probe.log4j.binaryedge.io` and a source address within the configured HOME_NET. Process the PCAP offline and inspect EVE JSON for SID `2034819`.

**Safety constraints:** Do not contact the named domain, send DNS queries onto a network, modify the main ruleset, or enable live capture.

**Status:** Candidate rule verified; dedicated synthetic test preparation pending.

### Synthetic DNS Packet Generation Readiness — 11 October 2026

**Objective:** Prepare an isolated PCAP to test built-in Suricata DNS signature SID `2034819`.

**Preflight result:** Python standard-library imports `socket` and `struct` succeeded in the project's virtual environment.

**Planned test input:**
- DNS query name: `probe.log4j.binaryedge.io`.
- Synthetic source address: within the configured `192.168.0.0/16` HOME_NET.
- Destination: a synthetic DNS server address; no DNS request will be transmitted.
- Output: a separate PCAP under `data/suricata-test/`.
- Validation: inspect the PCAP and process it offline with the isolated Suricata test configuration.

**Preservation constraints:** Keep the existing `benign-dns.pcap`, main runtime configuration, downloaded ruleset, and previous alert-test artifacts unchanged.

**Status:** Packet-generation prerequisites verified; PCAP creation pending.

### Dedicated DNS Signature-Test PCAP Created — 11 October 2026

**Output file:** `data/suricata-test/log4j-signature-test.pcap`

**Reported creation result:**
- File size: 238 bytes.
- Packet count: 2.
- Query name: `probe.log4j.binaryedge.io`.
- Synthetic client: `192.168.56.10:53001`.
- Synthetic DNS server: `192.168.56.53:53`.

**Intended purpose:** Offline testing of Suricata SID `2034819`, which matches a specific DNS query suffix.

**Verification still required:** Confirm the PCAP header, packet records, DNS query contents, and packet lengths before processing it with Suricata. The pasted terminal output was partially interleaved, so successful file creation alone is not sufficient validation.

**Safety:** The file is intended for offline processing only; no DNS traffic was transmitted.

**Status:** File creation reported successful; integrity verification pending.

### Synthetic DNS PCAP Integrity Check Failed — 11 October 2026

**Test file:** `data/suricata-test/log4j-signature-test.pcap`

**Observed result:** The integrity checker stopped with `AssertionError: Not Ethernet IPv4`.

**Likely cause:** Review of the packet-generation code shows that the Ethernet header was constructed from the destination and source MAC addresses without appending the IPv4 EtherType field (`08 00`). This makes the frame layout inconsistent with the checker’s expected Ethernet/IPv4 structure.

**Impact:** The PCAP has not passed integrity validation. No Suricata detection result should be inferred from it.

**Corrective plan:** Repair the packet-generation code, regenerate the dedicated PCAP, and rerun the integrity checks. Preserve the existing benign PCAP, main configuration, and downloaded ruleset.

**Status:** Integrity validation failed; packet-builder correction pending.

### Corrected PCAP Generator — Header Validation Still Failing — 11 October 2026

**Test file:** `data/suricata-test/log4j-signature-test.pcap`

**Observed result:** The regenerated PCAP failed the magic-number assertion before packet validation completed.

**Expected header:** A little-endian PCAP file should begin with bytes `d4 c3 b2 a1`.

**Possible causes:** The file may not contain the expected header, or the pasted command may have been altered or interleaved during execution. The actual file bytes must be inspected before selecting a correction.

**Next diagnostic:** Read the file's first 32 bytes and report its size without modifying it.

**Preservation:** Do not delete or modify the existing PCAPs, ruleset, or Suricata configurations during diagnosis.

**Status:** PCAP integrity remains unverified; header inspection pending.

### PCAP Header Bytes Inspected — 11 October 2026

**File:** `data/suricata-test/log4j-signature-test.pcap`

**Observed evidence:**
- File size: 242 bytes.
- First four bytes: `d4 c3 b2 a1`, consistent with a little-endian PCAP header.
- The file's header begins with the expected magic bytes.

**Interpretation:** The earlier magic-number assertion failure cannot be reproduced from the currently observed header bytes. The full PCAP is not yet validated; Ethernet framing, packet lengths, and DNS contents still need independent verification.

**Next step:** Run a minimal read-only check of the PCAP header and the Ethernet EtherType of the first packet.

**Status:** Header magic confirmed; full integrity verification pending.

### PCAP Header and Ethernet Framing Check Passed — 11 October 2026

**File:** `data/suricata-test/log4j-signature-test.pcap`

**Verified values:**
- PCAP magic: `d4 c3 b2 a1`.
- PCAP version: `2.4`.
- Link type: `1` (Ethernet).
- First packet EtherType: `08 00` (IPv4).
- First packet IP version: `4` (IPv4).

**Interpretation:** The file header and first packet's Ethernet/IPv4 framing match the expected format.

**Remaining validation:** Verify both packet records, UDP lengths, DNS message structure, and the exact query name `probe.log4j.binaryedge.io`.

**Status:** Header and first-frame checks passed; full packet validation pending.

### Dedicated DNS Signature-Test PCAP Validated — 11 October 2026

**File:** `data/suricata-test/log4j-signature-test.pcap`

**Validation results:**
- PCAP header and Ethernet link type validated.
- Exactly two complete packet records found.
- Both packets have valid Ethernet/IPv4/UDP framing and consistent length fields.
- Packet 1: `192.168.56.10` → `192.168.56.53`.
- Packet 2: `192.168.56.53` → `192.168.56.10`.
- DNS query name: `probe.log4j.binaryedge.io`.
- File size: 242 bytes.

**Interpretation:** The synthetic PCAP passed the implemented structural checks. The query is designed to satisfy the domain-suffix condition of Suricata SID `2034819`, and its source address is within the configured `$HOME_NET`.

**Next step:** Process the PCAP offline using the isolated Suricata test configuration, then inspect EVE JSON for an alert with SID `2034819`.

**Limitations:** PCAP validation does not prove that Suricata will generate an alert. No live traffic or exploitation is involved.

**Status:** PCAP integrity checks passed; offline signature test pending.

### Built-In DNS Signature Test — Rule-Loading Failure — 11 October 2026

**Test input:** `data/suricata-test/log4j-signature-test.pcap`

**Observed result:** Suricata read one PCAP file containing two packets, but reported that `/test-rules/alert-test.rules` did not match any file and that no rules were loaded.

**Diagnosis:** The Docker command mounted `rules/suricata` at `/test-rules`, while the isolated test signature is stored under `data/suricata-test/alert-rules/alert-test.rules`. The mounted directory therefore does not contain the requested test-rule file.

**Impact:** This run provides no evidence for or against detection by SID `2034819`. The signature was not loaded.

**Corrective plan:** Mount the isolated `alert-rules` directory at `/test-rules`, use the existing isolated test log directory `data/suricata-test/alert-logs`, and rerun the offline PCAP test. Do not modify the main ruleset or runtime configuration.

**Status:** Rule-loading failure diagnosed; corrected offline run pending.

### Isolated Suricata Test Paths Verified — 11 October 2026

**Verification results:**
- Test rule exists at `data/suricata-test/alert-rules/alert-test.rules`.
- Isolated configuration sets `default-log-dir` to `/var/log/suricata-test`.
- Isolated configuration sets `default-rule-path` to `/test-rules`.
- The configured rule filename is `alert-test.rules`.
- The isolated log directory `data/suricata-test/alert-logs` exists.

**Root cause confirmed:** The previous Docker command mounted the main downloaded rules directory at `/test-rules`, instead of mounting the directory containing the isolated test rule.

**Corrective action:** Mount `data/suricata-test/alert-rules` at `/test-rules` and `data/suricata-test/alert-logs` at `/var/log/suricata-test`. Keep the isolated configuration and main ruleset unchanged.

**Status:** Correct local paths verified; corrected offline run pending.

### Built-In DNS Signature Test — Run Result Requires Log Verification — 11 October 2026

**Test input:** `data/suricata-test/log4j-signature-test.pcap`

**Observed output:** Suricata 8.0.4 started, stopped, and reported reading one PCAP file with two packets.

**Uncertainty:** The pasted command appears truncated or interleaved around the configuration and log-directory arguments. The terminal output does not establish that the intended isolated configuration was loaded or that SID `2034819` was active.

**Next diagnostic:** Inspect the isolated EVE JSON and Suricata log files to determine whether the candidate rule was loaded and whether an alert with SID `2034819` was generated.

**Interpretation constraint:** A completed PCAP read alone is not evidence of a signature match.

**Status:** Offline processing reported; rule activation and alert result unconfirmed.

### Built-In DNS Test — Candidate Signature Not Yet Loaded — 11 October 2026

**Log inspection results:**
- The isolated Suricata log records one rule file processed.
- One rule loaded successfully; zero rules failed or were skipped.
- No EVE alert with candidate SID `2034819` was found in the inspected output.
- The isolated test rule file was previously created with synthetic SID `9900001`.

**Interpretation:** The current isolated configuration loads the synthetic test rule, not the built-in candidate signature. Therefore, the absence of SID `2034819` is not evidence that the built-in signature failed to detect the query.

**Next step:** Inspect the isolated rule file and the candidate rule's location in the downloaded ruleset. Then prepare a dedicated test rules file containing only the selected built-in signature, without modifying the main ruleset.

**Safety:** Continue using offline PCAP processing only. Do not contact the named domain or enable live capture.

**Status:** Rule-loading behavior understood; built-in candidate integration pending.

### Built-In DNS Candidate Rule Verified — 11 October 2026

**Isolated test rule:** SID `9900001`, a local synthetic DNS-query signature.

**Built-in candidate:** SID `2034819`, revision `1`, in `rules/suricata/suricata.rules`.

**Candidate message:** `ET ATTACK_RESPONSE DNS Query for Observed CVE-2021-44228 Security Scanner Domain (log4j .binaryedge .io)`.

**Verified facts:**
- The built-in candidate exists as an active `alert dns` rule in the downloaded ruleset.
- The isolated test-rule file contains only SID `9900001`.
- Therefore, the earlier isolated run could not evaluate SID `2034819`.

**Next step:** Create a separate candidate-only rule file containing the exact verified built-in signature. Configure a dedicated offline test to load that file, while preserving both the main ruleset and the existing synthetic test rule.

**Safety:** Use only the synthetic PCAP and offline processing. Do not resolve or contact the named domain.

**Status:** Candidate verified; dedicated rule-file preparation pending.

### Dedicated Built-In Candidate Rule File Created — 11 October 2026

**New file:** `data/suricata-test/alert-rules/builtin-candidate.rules`

**Candidate SID:** `2034819`, revision `1`.

**Reported creation result:**
- One matching rule extracted from the downloaded ruleset.
- The candidate was written to a separate test-only file.
- The main ruleset was not modified.
- The existing synthetic rule was not modified.

**Verification still required:** Independently confirm that the new file contains exactly one complete rule with SID `2034819` and the expected DNS suffix conditions.

**Next step:** After verification, configure an isolated offline test to load the candidate-only rule file and process the validated synthetic PCAP.

**Status:** Candidate file created; independent verification pending.

### Built-In Candidate Rule File Verified — 11 October 2026

**File:** `data/suricata-test/alert-rules/builtin-candidate.rules`

**Verification results:**
- Exactly one rule is present.
- The rule uses the `alert dns` action and protocol.
- SID `2034819` and revision `1` are correct.
- DNS query inspection is enabled through `dns.query`.
- The expected `.log4j.binaryedge.io` suffix is present.
- `nocase` and `endswith` modifiers are present.

**Interpretation:** The dedicated candidate file contains the intended signature and is ready for isolated configuration testing.

**Next step:** Create a separate candidate-test configuration that points to `/test-rules/builtin-candidate.rules`. Preserve the existing isolated configuration, synthetic test rule, main runtime configuration, and downloaded ruleset.

**Safety:** Continue with offline PCAP processing only. Do not contact the named domain or enable live capture.

**Status:** Candidate rule verified; dedicated configuration preparation pending.

### Dedicated Built-In Candidate-Test Configuration Plan — 11 October 2026

**Objective:** Prepare an isolated Suricata configuration that loads only the verified built-in DNS signature, SID `2034819`.

**Planned configuration:**
- Source template: `data/suricata-test/alert-test.yaml`.
- New configuration: `data/suricata-test/builtin-candidate-test.yaml`.
- Rule path inside the container: `/test-rules`.
- Rule filename: `builtin-candidate.rules`.
- Log directory inside the container: `/var/log/suricata-candidate-test`.

**Preservation requirements:**
- Do not modify the main runtime configuration.
- Do not modify the existing isolated test configuration.
- Do not modify either rule file or the downloaded ruleset.
- Keep the test restricted to offline PCAP processing.

**Next validation:** Confirm the new configuration references the candidate-only rule file and its dedicated log directory, then run Suricata's configuration test before processing the PCAP.

**Status:** Configuration plan recorded; isolated configuration creation pending.

### Dedicated Candidate-Test Configuration Created — 11 October 2026

**New file:** `data/suricata-test/builtin-candidate-test.yaml`

**Reported settings:**
- Rule filename: `builtin-candidate.rules`.
- Container log directory: `/var/log/suricata-candidate-test`.
- Source configuration: `data/suricata-test/alert-test.yaml`.

**Reported result:** The new configuration was created, and the source configuration was preserved.

**Verification still required:** Inspect the saved configuration to confirm the rule path, rule filename, and log directory are correct before running Suricata's configuration test.

**Preservation:** The main runtime configuration, downloaded ruleset, existing isolated configuration, and original synthetic rule must remain unchanged.

**Status:** New configuration created; independent inspection pending.

### Candidate-Test Configuration Paths Verified — 11 October 2026

**Configuration:** `data/suricata-test/builtin-candidate-test.yaml`

**Verified settings:**
- `default-log-dir`: `/var/log/suricata-candidate-test`
- `default-rule-path`: `/test-rules`
- Rule filename: `builtin-candidate.rules`
- Classification file: `/usr/share/suricata/classification.config`
- Reference file: `/usr/share/suricata/reference.config`

**Interpretation:** The saved configuration references the intended candidate-only rule file and dedicated log directory. The original isolated test configuration remains separate.

**Next step:** Run Suricata's configuration test using this configuration and mount `data/suricata-test/alert-rules` at `/test-rules`. Confirm that SID `2034819` loads successfully before processing the PCAP.

**Status:** Configuration paths verified; Suricata configuration test pending.

### Candidate-Test Configuration Test Passed — 11 October 2026

**Configuration tested:** `data/suricata-test/builtin-candidate-test.yaml`

**Runtime:** Suricata 8.0.4 in a Docker container.

**Observed result:** Suricata reported `Configuration provided was successfully loaded. Exiting.`

**Interpretation:** The candidate-test configuration is syntactically acceptable to Suricata.

**Remaining verification:** Inspect the dedicated Suricata log to confirm that `builtin-candidate.rules` was processed and SID `2034819` loaded successfully.

**Safety:** This was a configuration-only test using `-T`; no PCAP was processed and no live capture was started.

**Status:** Configuration test passed; candidate rule-loading confirmation pending.

### Candidate Signature Loading — Shared Log Is Ambiguous — 11 October 2026

**Observed evidence:** The shared `data/suricata-test/alert-logs/suricata.log` contains a rule-loading entry at 18:28:50 reporting one rule loaded and zero failed or skipped.

**Limitation:** The directory contains logs from earlier synthetic-rule tests. The shared log alone does not establish that the latest entry belongs to the candidate-only configuration.

**Next step:** Use a fresh, dedicated log directory for the candidate-only configuration test, then verify the new log reports one rule successfully loaded. This will separate candidate-rule evidence from earlier test runs.

**Safety:** Do not delete or overwrite the existing test logs, rules, PCAPs, or configurations. Continue using configuration tests and offline PCAP processing only.

**Status:** Shared log reviewed; candidate-specific rule-loading confirmation pending.

### Dedicated Candidate-Test Log Directory Created — 11 October 2026

**Directory:** `data/suricata-test/candidate-logs/`

**Observed result:** The directory was created successfully and is available for the candidate-only configuration test.

**Purpose:** Separate new candidate-test logs from earlier synthetic-rule tests so rule-loading evidence can be attributed to the correct run.

**Preservation:** Existing logs, rules, PCAPs, and configurations were not intentionally modified by this directory-creation step.

**Next step:** Rerun the candidate-only configuration test with this fresh directory mounted at `/var/log/suricata-candidate-test`, then inspect the new `suricata.log` for the rule-loading count.

**Status:** Dedicated log directory ready; fresh configuration test pending.

### Built-In Candidate Rule Loading Confirmed — 11 October 2026

**Configuration:** `data/suricata-test/builtin-candidate-test.yaml`

**Dedicated logs:** `data/suricata-test/candidate-logs/`

**Observed result from the fresh Suricata log:**
- Rule files processed: 1.
- Rules successfully loaded: 1.
- Rules failed: 0.
- Rules skipped: 0.
- Configuration test completed successfully.

**Interpretation:** Suricata loaded one rule from the candidate-test rule directory without reporting load failures. The rule file was independently verified to contain only candidate SID `2034819`, revision `1`.

**Next step:** Run the validated synthetic DNS PCAP through this configuration offline and inspect EVE JSON for SID `2034819`.

**Limitations:** Rule loading alone does not prove that the signature will match the test packet. No live capture or prevention has been tested.

**Status:** Candidate rule loading confirmed; offline detection test pending.

### Built-In DNS Signature Offline Run — 12 October 2026

**Test input:** `data/suricata-test/log4j-signature-test.pcap`

**Candidate signature:** SID `2034819`, revision `1`.

**Observed output:**
- Suricata 8.0.4 started and stopped.
- One PCAP file was read.
- Two packets were processed.

**Verification still required:**
- Inspect the fresh EVE JSON for an alert with SID `2034819`.
- Confirm which configuration was loaded for this run. The pasted command does not visibly include the explicit `-c /etc/suricata/suricata.yaml` argument used in the earlier configuration test.

**Interpretation constraint:** Reading the PCAP successfully does not establish that the candidate signature matched. A missing alert must not be interpreted as a detection failure until rule loading and configuration use are confirmed.

**Safety:** Offline PCAP processing only; no live capture or external DNS request.

**Status:** Offline run completed; detection result pending EVE inspection.

### Built-In Suricata DNS Signature Matched — 12 October 2026

**Test objective:** Evaluate the built-in ET Open DNS signature SID `2034819` using a controlled, synthetic offline PCAP.

**Test environment:**
- Suricata 8.0.4 in Docker.
- Dedicated candidate-only configuration: `data/suricata-test/builtin-candidate-test.yaml`.
- Candidate rule file: `data/suricata-test/alert-rules/builtin-candidate.rules`.
- PCAP: `data/suricata-test/log4j-signature-test.pcap`.
- EVE output: `data/suricata-test/candidate-logs/eve.json`.

**Observed detection:**
- SID: `2034819`.
- Revision: `1`.
- DNS query: `probe.log4j.binaryedge.io`.
- Source: `192.168.56.10:53001`.
- Destination: `192.168.56.53:53`.
- PCAP packet number: `1`.
- EVE alert action: `allowed`.
- EVE event counts: 1 alert, 2 DNS events, 1 flow event, and 1 stats event.
- Invalid EVE JSON lines: 0.

**Result:** The built-in signature matched the synthetic DNS query and generated an EVE alert. This validates the rule's matching condition and the offline alert-output pipeline.

**Limitations:** This experiment does not demonstrate Log4Shell exploitation, real-world attack detection accuracy, or inline packet prevention. No external DNS request, exploit, or live capture was involved. The EVE action `allowed` is consistent with alert-only IDS behavior.

**Next step:** Summarize the completed Suricata detection-only validation and decide how to integrate Suricata alerts into the project's event pipeline without treating EVE fields as equivalent to the 77 CIC-IDS2017 model features.

**Status:** Built-in signature match confirmed in offline testing.

### Suricata Detection Validation and Integration Plan — 12 October 2026

**Completed validation:**
- Suricata 8.0.4 runs in Docker.
- The main configuration test passed.
- The downloaded ruleset loaded successfully in the main configuration.
- A synthetic alert rule validated the EVE alert-output pipeline.
- Built-in ET Open DNS signature SID `2034819` matched the synthetic query `probe.log4j.binaryedge.io` in an offline PCAP.
- EVE JSON parsing completed with zero invalid lines.

**Current architecture decision:**
1. Keep Suricata in detection-only mode.
2. Treat Suricata alerts and ML predictions as separate evidence sources.
3. Preserve raw EVE events for auditing and reproducibility.
4. Define an explicit event schema before integrating Suricata output with the ML service.
5. Do not map EVE fields directly onto the 77 CIC-IDS2017 model features without a validated feature-mapping process.
6. Do not enable inline prevention until detection quality, false positives, failure handling, and enforcement behavior have been evaluated.

**Next implementation phase:** Inspect the existing project architecture and identify the appropriate location for a Suricata EVE ingestion and normalization component.

**Evidence limitation:** The successful built-in signature test used synthetic offline traffic. It does not establish real-world attack-detection accuracy or prevention effectiveness.

**Status:** Offline signature validation complete; integration design pending.

### Existing Project Structure Inspected — 12 October 2026

**Repository:** `/home/ah076/decentralized-ips`

**Top-level components observed:**
- `ml/`: model training, preprocessing, and evaluation scripts.
- `services/`: existing service components requiring further inspection.
- `blockchain/`: blockchain-related components requiring further inspection.
- `config/suricata/`: Suricata runtime configuration.
- `rules/suricata/`: downloaded Suricata rules workspace.
- `data/suricata-test/`: isolated synthetic PCAPs, candidate rules, and test configurations.
- `logs/suricata/`: Suricata runtime output.
- `tests/`: existing test area.

**Architecture decision:** Treat Suricata EVE ingestion as a separate detection-event component. Preserve raw EVE events and normalize them into an explicit event schema. Keep Suricata alerts separate from ML predictions until a validated integration contract exists.

**Next inspection:** Examine the contents of `services/`, `blockchain/`, and `tests/` to identify existing entry points, event-processing conventions, and integration boundaries before selecting an implementation location.

**Preservation constraints:** Do not modify application code, ML models, Suricata configuration, or blockchain components during this inspection.

**Status:** Top-level structure inspected; service integration point not yet identified.

### Service and Integration Boundary Inspection — 12 October 2026

**Inspection method:** Read-only file inventory of `services/`, `blockchain/`, `tests/`, `scripts/`, and `docker/`.

**Findings:**
- `services/decision-service/` contains only `.gitkeep`.
- `services/ml-service/` contains only `.gitkeep`.
- `services/rule-engine/` contains only `.gitkeep`.
- `services/sync-agent/` contains only `.gitkeep`.
- `blockchain/chaincode/`, `blockchain/client/`, and `blockchain/network/` contain only `.gitkeep`.
- `tests/`, `scripts/`, and the inspected Docker subdirectories contain only `.gitkeep`.

**Conclusion:** No existing application service, event-ingestion implementation, API entry point, or test suite was identified in these directories.

**Design implication:** A dedicated Suricata EVE ingestion component may be appropriate, but its interface and location must be chosen after reviewing the README and documented architecture. Avoid adding dependencies or introducing a service framework before establishing the minimum requirements.

**Status:** Service boundaries inspected; implementation design not yet finalized.

### Architecture Documentation Review Plan — 12 October 2026

**Objective:** Determine the intended service responsibilities and integration boundaries before implementing Suricata EVE ingestion.

**Current evidence:**
- The ML training and evaluation scripts exist under `ml/`.
- The service directories inspected so far contain only `.gitkeep` placeholders.
- The blockchain directories inspected so far contain only `.gitkeep` placeholders.
- Suricata has successfully generated an alert from a synthetic offline PCAP.

**Review scope:**
1. Read the README for the project's stated architecture, technology choices, and implementation phases.
2. Identify relevant headings in `docs/research-log.md` concerning service design, event processing, ML inference, and blockchain auditing.
3. Compare documented intentions with the existing repository structure.

**Decision criteria:** Choose the smallest component that can ingest EVE JSON, preserve raw events, validate and normalize alert records, and be tested independently. Do not assume that blockchain auditing or ML inference must be part of the first implementation.

**Safety constraints:** Documentation inspection only. No source-code changes, dependency installation, live traffic capture, or prevention-mode changes.

**Status:** Architecture review planned; implementation location remains undecided.

### Documented Target Architecture Reviewed — 12 October 2026

**Source reviewed:** `README.md`, sections 1–6 and 10.

**Documented component responsibilities:**
- **Suricata:** Monitor network traffic and generate security events.
- **ML service:** Classify supported traffic records and return predictions.
- **Decision service:** Evaluate predictions and apply decision policies.
- **Rule engine:** Validate proposed prevention actions.
- **Blockchain audit layer:** Planned Hyperledger Fabric integration for security-event auditing.

**Current implementation status:** The README identifies this as the planned target architecture, not a fully operational system. The inspected service and blockchain directories contain only placeholders.

**Integration implication:** Suricata EVE events need a defined interface before they can be consumed by another component. EVE alert records must not be treated as equivalent to the existing CIC-IDS2017 model's 77 input features.

**Next step:** Inspect the README's architecture diagram and technology-stack sections to determine the intended data flow and whether the initial EVE adapter should be a standalone module or part of the planned ML service.

**Constraints:** Documentation review only; no code changes, new dependencies, live capture, or prevention-mode changes.

**Status:** Target responsibilities confirmed; exact EVE ingestion boundary still pending.

### Suricata EVE Ingestion Boundary Selected — 12 October 2026

**Basis:** README sections 3, 4, 6, and 10, plus the inspected repository structure.

**Documented target flow:** Suricata → ML service → decision service → validated rule engine → prevention/enforcement. Hyperledger Fabric is planned for auditing selected security events and decisions.

**Initial implementation boundary:** Begin with a small, independently testable Python EVE ingestion and normalization module. Keep it separate from model inference, decision policy, enforcement, and blockchain integration.

**Initial responsibilities:**
1. Read EVE JSON records from a file.
2. Parse each JSON record independently.
3. Identify event type and validate the minimum structure required for normalization.
4. Preserve the original record for traceability.
5. Normalize alert fields into an explicit, versioned event schema.
6. Report malformed records without silently treating them as valid alerts.

**Out of scope:** Live packet capture, inline prevention, rule modification, direct conversion to the 77 CIC-IDS2017 features, automatic ML classification, and blockchain writes.

**Proposed location:** `services/ml-service/` is a candidate because the roadmap explicitly calls for Suricata-to-ML integration. Confirm the module interface and existing dependencies before implementation.

**Validation plan:** Use the already generated offline EVE data, including the synthetic alert and built-in signature test. Verify valid-event parsing, malformed-line handling, preservation of raw fields, and deterministic normalization.

**Status:** Initial component boundary selected for design; implementation has not started.

### Python Dependency and Environment Inspection Plan — 12 October 2026

**Objective:** Identify the existing Python environment and dependency conventions before implementing the Suricata EVE ingestion module.

**Inspection scope:**
1. Verify the active Python interpreter and version.
2. Check whether the standard library can support JSON Lines parsing and validation for the initial module.
3. Inspect existing dependency manifests and relevant ML-service files.
4. Identify available testing tools without installing anything.

**Initial design preference:** Use Python standard-library facilities for file reading, JSON parsing, schema checks, and error reporting unless repository requirements demonstrate a need for an additional dependency.

**Constraints:** Read-only inspection. Do not install packages, modify dependency manifests, create source files, or alter the ML model.

**Status:** Dependency inspection planned; implementation remains pending.

### Suricata EVE Parser Contract — 12 October 2026

**Runtime:** Python 3.12.3 in the project virtual environment.

**Dependency decision:** Use Python standard-library modules for the initial implementation. No new package installation is required for JSON Lines parsing.

**Proposed module location:** `services/ml-service/eve_ingestion.py`.

**Input contract:**
- Accept a path to an EVE JSON Lines file.
- Read one JSON object per non-empty line.
- Preserve the parsed original event.
- Handle malformed JSON lines explicitly without silently discarding them.

**Normalized alert contract, schema version 1:**
- `schema_version`
- `source` (Suricata)
- `event_type`
- `timestamp`
- `flow_id`
- `src_ip`, `src_port`
- `dest_ip`, `dest_port`
- `protocol`, `app_protocol`
- `signature_id`, `signature`, `severity`, `category`, `action`
- `raw_event` (original parsed JSON object)

**Validation rules:**
1. Normalize only records whose `event_type` is `alert`.
2. Treat absent optional fields as `null`; do not fabricate values.
3. Preserve the original event so additional Suricata fields remain available for auditing.
4. Report malformed JSON with its line number.
5. Distinguish valid non-alert events from malformed records.
6. Do not infer that an alert proves an attack succeeded or that traffic was blocked.

**Testing plan:** Cover a valid alert, a valid non-alert event, a malformed JSON line, missing optional fields, and preservation of the raw event.

**Integration boundary:** This module will not invoke the ML model, create prevention rules, or write to Hyperledger Fabric.

**Status:** Parser contract proposed; implementation not yet started.

### Suricata EVE Sample Inspection Plan — 12 October 2026

**Objective:** Verify the proposed normalized-alert schema against the actual EVE JSON output produced during offline testing.

**Input:** Existing file `logs/suricata/eve.json`, generated by the Suricata offline PCAP smoke test.

**Inspection scope:**
1. Count the event types present in the file.
2. Inspect the top-level keys of a representative alert, if one exists.
3. Check the types and presence of timestamp, flow, source/destination, protocol, and alert fields.
4. Confirm whether the current file contains alerts or only DNS, flow, and statistics events.

**Method:** Read-only Python inspection. Print a compact summary rather than dumping the complete EVE log.

**Constraints:** Do not modify the EVE file, Suricata configuration, rules, or application code. Do not assume that this benign-PCAP output contains an alert; the synthetic alert test used a separate output directory.

**Status:** Sample inspection planned; parser contract will be adjusted only if the observed EVE structure requires it.

### Benign EVE Sample Inspection Results — 12 October 2026

**Input:** `logs/suricata/eve.json`

**Observed event counts:**
- DNS: 2
- Flow: 1
- Statistics: 1
- Alert: 0

**Parsing result:** Zero invalid JSON records were found in the inspected file.

**Interpretation:** The file represents the benign offline-PCAP smoke test. Its lack of alerts is consistent with that test's purpose and does not contradict the successful alert-generation tests, which used separate output directories.

**Schema limitation:** This file does not provide a representative alert record, so alert-specific field validation must use the dedicated synthetic-alert or built-in-signature EVE output.

**Next step:** Inspect one dedicated alert record and verify its field names and data types before implementing the parser.

**Status:** Benign EVE structure validated; alert schema verification remains pending.

### Dedicated Suricata Alert Schema Inspection Plan — 12 October 2026

**Objective:** Verify the normalized-alert contract against a real Suricata EVE alert generated during the offline signature test.

**Expected input:** `data/suricata-test/candidate-logs/eve.json`, subject to confirming that this is the actual output path used by the successful built-in-signature test.

**Fields to inspect:**
- `event_type` and `timestamp`
- `flow_id`
- Source and destination IP addresses and ports
- `proto` and `app_proto`
- Nested `alert` fields: `signature_id`, `signature`, `severity`, `category`, and `action`
- Presence and types of optional fields

**Method:** Read-only Python inspection of one alert record, with JSON validity checks and a compact field summary.

**Constraints:** Do not modify the EVE log, configuration, rules, or source code. Do not infer attack success or prevention effectiveness from an alert.

**Status:** Dedicated alert schema inspection planned; the exact output path must be confirmed before parsing.

### Dedicated Suricata Alert Schema Verified — 12 October 2026

**Inspection method:** Read-only Python inspection of EVE JSON files under `data/suricata-test/`.

**Files found:**
- `data/suricata-test/alert-logs/eve.json`
- `data/suricata-test/candidate-logs/eve.json`

**Alert records found:** 2 across the inspected files.

**Verified event structure:**
- Top-level fields include `timestamp`, `flow_id`, `src_ip`, `src_port`, `dest_ip`, `dest_port`, `proto`, `app_proto`, `event_type`, and nested `alert`.
- Nested alert fields include `action`, `gid`, `signature_id`, `rev`, `signature`, `category`, and `severity`.
- The inspected synthetic alert used signature ID `9900001`, protocol `UDP`, and application protocol `dns`.
- Its `alert.action` was `allowed`, consistent with alert-only IDS operation.

**Schema implication:** The parser must read signature metadata from the nested `alert` object. `proto` and `app_proto` must remain distinct fields.

**Evidence limitation:** This verifies the event structure and alert-generation path, not real-world detection accuracy or prevention effectiveness.

**Status:** Representative alert schema verified; parser implementation pending.

### Dedicated Suricata Alert Schema Verified — 12 October 2026

**Inspection method:** Read-only Python inspection of EVE JSON files under `data/suricata-test/`.

**Files found:**
- `data/suricata-test/alert-logs/eve.json`
- `data/suricata-test/candidate-logs/eve.json`

**Alert records found:** 2 across the inspected files.

**Verified event structure:**
- Top-level fields include `timestamp`, `flow_id`, `src_ip`, `src_port`, `dest_ip`, `dest_port`, `proto`, `app_proto`, `event_type`, and nested `alert`.
- Nested alert fields include `action`, `gid`, `signature_id`, `rev`, `signature`, `category`, and `severity`.
- The inspected synthetic alert used signature ID `9900001`, protocol `UDP`, and application protocol `dns`.
- Its `alert.action` was `allowed`, consistent with alert-only IDS operation.

**Schema implication:** The parser must read signature metadata from the nested `alert` object. `proto` and `app_proto` must remain distinct fields.

**Evidence limitation:** This verifies the event structure and alert-generation path, not real-world detection accuracy or prevention effectiveness.

**Status:** Representative alert schema verified; parser implementation pending.

### EVE Parser File Creation Interrupted — 12 October 2026

**Target file:** `services/ml-service/eve_ingestion.py`

**Observation:** The terminal output from the heredoc creation command shows only the initial imports and fragments of the intended Python code. Successful file creation has not been verified.

**Assessment:** The file may be incomplete or malformed. No syntax check or functional test has been performed.

**Recovery plan:**
1. Inspect the current file contents and size.
2. Confirm the actual state before attempting recovery.
3. Recreate or repair the module using a paste-safe method.
4. Run a Python syntax check before functional tests.

**Preservation constraints:** Do not modify the ML model, Suricata configuration or rules, blockchain components, or dependency manifests.

**Status:** Initial file creation unverified; recovery inspection required.

### EVE Parser Syntax Check Passed — 12 October 2026

**File:** `services/ml-service/eve_ingestion.py`

**Command:** `python -m py_compile services/ml-service/eve_ingestion.py`

**Result:** Passed. Python returned to the shell prompt without reporting a syntax error.

**Verified so far:** The file exists, contains the intended parser functions, and compiles under Python 3.12.3.

**Not yet verified:** Functional behavior, malformed-line recovery, event classification, optional-field handling, and raw-event preservation.

**Next step:** Run read-only functional checks against the existing offline EVE data and synthetic in-memory cases. Do not modify the model, Suricata configuration, rules, or dependency manifests.

**Status:** Syntax valid; functional validation pending.

### EVE Parser Functional Tests Passed — 12 October 2026

**Module:** `services/ml-service/eve_ingestion.py`

**Test results:**
- `data/suricata-test/alert-logs/eve.json`: 1 alert normalized successfully.
- `data/suricata-test/candidate-logs/eve.json`: 1 alert normalized successfully.
- Synthetic non-alert event: correctly classified as `non_alert`.
- Malformed JSON line: correctly classified as `malformed`, with its line number.
- Subsequent valid alert: processed successfully after malformed input.
- JSON array instead of an object: correctly classified as `malformed`.
- Missing optional source fields: represented as `None`.
- Raw-event preservation: normalized event's `raw_event` matched the original parsed event.

**Result:** All executed parser assertions passed. No dependencies were installed, and existing EVE logs were not modified.

**Scope limitation:** These checks validate parsing and normalization behavior. They do not establish ML detection quality, real-world attack detection, or prevention effectiveness.

**Next step:** Review the module's input validation and error-reporting behavior before deciding whether to add a persistent automated test suite.

**Status:** Initial EVE parser implemented and functionally validated.

### EVE Parser Input Validation Review Plan — 12 October 2026

**Current implementation:** `services/ml-service/eve_ingestion.py`

**Verified behavior:** Syntax compilation and initial functional checks passed for existing Suricata alert records, non-alert records, malformed JSON, non-object JSON values, optional fields, and raw-event preservation.

**Edge cases to review:**
1. An alert event whose `alert` field is missing or is not a JSON object.
2. An alert event whose signature ID or timestamp has an unexpected type.
3. An event with a missing or unknown `event_type`.
4. An empty EVE file or a file containing only blank lines.
5. A missing or unreadable input file.
6. Whether the parser should distinguish syntactically valid JSON from semantically valid Suricata alert records.

**Review objective:** Decide which conditions should remain acceptable with optional `None` values and which should be reported as validation errors. Avoid inventing missing fields or silently claiming that an incomplete event is fully valid.

**Constraints:** Review only; do not modify source code or install dependencies yet. Preserve the existing parser's current behavior until the review is documented.

**Status:** Initial functional validation passed; edge-case policy review pending.

### EVE Parser Validation Policy — 12 October 2026

**Reviewed file:** `services/ml-service/eve_ingestion.py`

**Existing behavior:**
- Invalid JSON syntax is reported as `malformed`.
- JSON values that are not objects are reported as `malformed`.
- Valid non-alert objects are reported as `non_alert`.
- Any object with `event_type: "alert"` is currently normalized, even when its nested alert metadata is missing or invalid.

**Proposed validation policy:**
1. Require `event_type` to be a non-empty string.
2. Classify valid, recognized non-alert events as `non_alert`.
3. Report missing or invalid event types as `malformed`.
4. Require alert events to contain an `alert` object.
5. Require alert events to contain a positive integer `signature_id`; reject booleans and strings as substitutes for integers.
6. Keep optional fields nullable; do not invent timestamps, IP addresses, ports, protocol names, severity values, or categories.
7. Preserve raw parsed events for both valid alerts and malformed semantic records whenever JSON parsing succeeded.
8. Continue processing later lines after an invalid record.
9. Do not claim full semantic validation of every Suricata EVE field; validate only the minimum contract required by this component.

**Compatibility:** Existing known-good synthetic and built-in signature alerts must continue to normalize successfully.

**Next step:** Implement these focused validation checks and add tests for missing alert metadata, invalid signature IDs, missing event types, and continued processing.

**Status:** Review complete; validation changes pending.

### EVE Parser Semantic Validation Added — 12 October 2026

**File:** `services/ml-service/eve_ingestion.py`

**Syntax check:** `python -m py_compile services/ml-service/eve_ingestion.py` completed successfully after the update.

**Validation changes implemented:**
- `event_type` must be a non-empty string.
- Alert events must contain an `alert` object.
- `alert.signature_id` must be a positive integer; booleans and strings are rejected.
- Missing optional normalized fields remain `None`.
- Parsed source events are retained in malformed results when JSON parsing succeeds.
- Processing continues after invalid records.

**Not yet verified:** Functional regression tests against existing EVE alert files and new semantic-validation cases.

**Next step:** Run the regression and edge-case test suite before treating the updated parser as validated.

**Status:** Updated source compiles; functional regression testing pending.

### EVE Parser Edge-Case Test Needs Diagnosis — 12 October 2026

**Module:** `services/ml-service/eve_ingestion.py`

**Regression results:**
- Existing synthetic-alert EVE file: 1 alert normalized successfully.
- Existing built-in-signature EVE file: 1 alert normalized successfully.

**Edge-case test result:** The temporary test script raised `TypeError: 'NoneType' object is not subscriptable`. The full edge-case suite did not complete.

**Assessment:** The failure has not yet been attributed to the parser or test script. No source-code changes should be made until the failing test expression and actual parser output are inspected.

**Next step:** Rerun the synthetic fixture with diagnostic output showing each record's line number, status, error, and whether a normalized record exists.

**Status:** Existing-alert regression checks passed; edge-case suite inconclusive.

### EVE Parser Edge-Case Failure Diagnosed — 12 October 2026

**Root cause:** The synthetic test script used the wrong zero-based list index when retrieving the valid alert record. It accessed `results[5]`, which represents the record with signature ID `0`, instead of `results[6]`, which represents the valid alert with signature ID `123`.

**Diagnostic results:** All nine records received the expected status:
- DNS event: `non_alert`
- Invalid JSON: `malformed`
- Missing alert object: `malformed`
- String signature ID: `malformed`
- Boolean signature ID: `malformed`
- Zero signature ID: `malformed`
- Positive integer signature ID: `alert`
- Missing event type: `malformed`
- Blank event type: `malformed`

**Conclusion:** The observed failure was caused by the test script's incorrect index, not by a demonstrated parser defect. No source-code change was required.

**Next step:** Rerun the complete assertion-based regression and edge-case suite with the corrected index.

**Status:** Root cause identified; final assertion-based verification pending.

### EVE Parser Regression and Edge-Case Tests Passed — 12 October 2026

**Module:** `services/ml-service/eve_ingestion.py`

**Regression checks:**
- `data/suricata-test/alert-logs/eve.json`: 1 alert normalized successfully.
- `data/suricata-test/candidate-logs/eve.json`: 1 alert normalized successfully.
- Schema version, positive signature ID, and raw-event preservation assertions passed for existing alerts.

**Edge-case checks:** All nine classifications matched expectations:
- Valid non-alert event.
- Malformed JSON.
- Missing alert object.
- String signature ID.
- Boolean signature ID.
- Zero signature ID.
- Valid positive integer signature ID.
- Missing event type.
- Blank event type.

**Additional assertions passed:**
- Malformed records retained their source line numbers.
- Parsing continued after malformed input.
- Missing optional source fields were represented as `None`.
- Parsed source events were preserved in normalized output and semantic-error results.

**Test correction:** The previous test failure was caused by an incorrect zero-based index in the test script. The corrected assertion suite completed successfully without requiring a source-code change.

**Scope limitation:** These results validate parsing and normalization behavior only. They do not demonstrate ML detection quality, real-world attack detection, or prevention effectiveness.

**Next step:** Add a persistent standard-library `unittest` suite under `tests/` so parser regressions can be checked reproducibly.

**Status:** Initial parser implementation, syntax check, existing-alert regression tests, and edge-case tests passed.

### Permanent EVE Parser Test Suite Plan — 12 October 2026

**Target file:** `tests/test_eve_ingestion.py`

**Test framework:** Python standard-library `unittest`; no additional dependencies.

**Planned test coverage:**
1. Normalize a valid alert and verify its schema version and signature fields.
2. Preserve the original event in `raw_event`.
3. Classify valid non-alert events correctly.
4. Report malformed JSON with the correct line number.
5. Reject non-object JSON values.
6. Reject missing or blank event types.
7. Reject alert records with a missing or invalid `alert` object.
8. Reject missing, non-integer, boolean, and non-positive signature IDs.
9. Continue processing valid records after malformed input.
10. Preserve nullable optional fields as `None`.

**Test design:** Use temporary fixture files for deterministic unit tests. Keep unit tests independent of existing Suricata log files so they remain reproducible even if those logs are rotated or regenerated.

**Constraints:** Add only the test file in this step. Do not change the parser, model, Suricata configuration, rules, dependencies, or blockchain components.

**Status:** Test plan documented; permanent test suite not yet created.

### Permanent EVE Parser Unit Tests Passed — 12 October 2026

**Test file:** `tests/test_eve_ingestion.py`

**Test command:** `python -m unittest discover -s tests -p 'test_*.py' -v`

**Result:** 10 tests passed; 0 failures; 0 errors. Runtime was approximately 0.008 seconds.

**Verified behaviors:**
- Valid alert normalization and schema version.
- Original event preservation.
- Non-alert classification.
- Malformed JSON reporting and continued processing.
- Rejection of non-object JSON values.
- Rejection of missing or blank event types.
- Rejection of missing or invalid alert objects.
- Rejection of invalid signature IDs, including strings, booleans, zero, negative integers, and floats.
- Acceptance of positive integer signature IDs.
- Nullable optional fields and source-event preservation on semantic errors.

**Dependencies:** No new packages installed; tests use Python's standard-library `unittest`.

**Scope limitation:** These tests establish parser behavior only. They do not demonstrate ML detection accuracy, live traffic integration, or prevention effectiveness.

**Next step:** Review the working-tree changes and repository ignore rules before deciding what should be committed. Do not commit generated logs, PCAPs, downloaded rules, or other test artifacts.

**Status:** EVE parser and permanent unit test suite validated.

### Git Working-Tree Review — 12 October 2026

**Files reported by Git:**
- Modified: `.gitignore`
- Modified: `docs/research-log.md`
- Untracked: `config/suricata/`
- Untracked: `rules/`
- Untracked: `services/ml-service/eve_ingestion.py`
- Untracked: `tests/test_eve_ingestion.py`

**Change summary:** The research log has 2,280 added lines in the current diff. This requires inspection before staging to ensure the content is intentional.

**Ignore verification:** Generated EVE logs and the downloaded Suricata ruleset are ignored by Git. They should not be added to a commit.

**New implementation files:** The EVE ingestion module and its standard-library unit tests are present in the working tree. The permanent test suite previously passed all 10 tests.

**Next step:** Inspect the full untracked-file inventory and review `.gitignore` changes. Verify the research-log diff before staging any files.

**Constraints:** Do not stage, commit, or push files until the change inventory is reviewed. Preserve runtime configuration and research evidence; exclude downloaded rules, generated logs, and PCAPs.

**Status:** Initial working-tree review complete; staging decision pending.

### Suricata File Inventory and Research-Log Review — 12 October 2026

**Configuration files found:**
- `config/suricata/suricata.yaml` — 93,427 bytes; generated runtime configuration.
- `config/suricata/suricata.yaml.in` — 93,543 bytes; upstream template.

**Rules files found:**
- `rules/suricata/.gitkeep` — empty directory placeholder.
- `rules/suricata/classification.config` — 3,228 bytes.
- `rules/suricata/suricata.rules` — 45,892,735 bytes.

**Ignore-rule finding:** `.gitignore` excludes files under `/rules/suricata/` while explicitly allowing `.gitkeep`. Generated logs and test artifacts are also ignored.

**Research-log finding:** The current diff reports 2,302 added lines. The initial preview contains some apparent missing spaces in sentences. The complete change must be checked before staging or committing.

**Proposed tracking policy:** Track the project-owned parser, permanent tests, intended runtime configuration and template, documentation, and the rules-directory placeholder where appropriate. Do not track generated logs, PCAPs, or the downloaded/generated full ruleset.

**Status:** File inventory collected; content and formatting review pending. No files staged, committed, or pushed.

### Suricata Configuration and Whitespace Review — 12 October 2026

**Runtime configuration:** `config/suricata/suricata.yaml` contains substitutions for the Suricata 8.0.4 template, including the version, log directory, EVE enablement, plugin comments, and selected filesystem paths. The upstream template intentionally retains build-time placeholders.

**Placeholder check:** The runtime configuration has no matches for the checked placeholder patterns. The template retains expected placeholders such as `@PACKAGE_VERSION@` and `@MAJOR_MINOR@`.

**Research-log formatting:** `git diff --check` reports trailing whitespace on line 3733, in a `suricata-update` tool entry. This needs a targeted review before staging.

**Next action:** Inspect the affected research-log section and verify runtime configuration paths used for rules, classification, reference data, and logging. Make no broad automated replacements.

**Status:** Initial configuration comparison complete; final pre-staging review pending.

### Suricata Path Verification and Git Ignore Review — 12 October 2026

**Verified runtime settings:**
- Default log directory: `/var/log/suricata`
- EVE JSON output is enabled and uses `eve.json`.

**Git ignore verification:**
- Downloaded/generated Suricata rules and classification data are ignored.
- Generated Suricata logs are ignored.
- Synthetic PCAP test files are ignored.

**Formatting issue:** `git diff --check` identifies trailing whitespace on the `suricata-update` version line at line 3733. A targeted correction is required.

**Outstanding verification:** The previous output did not establish the active default rule path, rule filename, classification configuration path, or reference configuration path. These settings must be checked explicitly before deciding whether to track the runtime configuration.

**Status:** Ignore behavior verified; one whitespace issue and runtime path verification remain.

### GitHub Push Preparation — 12 October 2026

**Objective:** Safely publish the reviewed decentralized IPS project changes to the existing `origin` remote on branch `main`.

**Intended files for review:** `.gitignore`, `docs/research-log.md`, the Suricata runtime configuration and upstream template, `services/ml-service/eve_ingestion.py`, and `tests/test_eve_ingestion.py`. Track `rules/suricata/.gitkeep` only as a directory placeholder if appropriate.

**Excluded artifacts:** Downloaded/generated Suricata rules, generated classification data, EVE logs, PCAPs, and temporary test artifacts.

**Required checks:** Verify runtime configuration paths, correct the identified research-log whitespace, run the permanent unit tests, inspect the staged diff, and confirm that no unintended files are staged.

**Publishing policy:** Commit and push only after these checks pass. Do not force-push or delete existing project resources.

**Status:** Final pre-push review pending.

### Final Pre-Commit Validation — 12 October 2026

**Unit tests:** All 10 permanent EVE ingestion tests passed using Python's standard-library `unittest` runner.

**Suricata runtime paths verified:**
- Default rule directory: `/rules`
- Rules file: `suricata.rules`
- Classification configuration: `/rules/classification.config`
- Reference configuration: `/usr/share/suricata/reference.config`

**Outstanding issue:** `git diff --check` reports trailing whitespace on the `suricata-update` tool version line at line 3733 in `docs/research-log.md`.

**Next action:** Remove only the trailing whitespace on the affected line, rerun validation, and inspect the staged file list and diff before committing.

**Status:** Tests passed; whitespace correction and final Git review pending.

### Git Staging Decision — 12 October 2026

**Validation results:**
- All 10 permanent EVE ingestion unit tests passed.
- `git diff --check` completed without errors after correcting the identified trailing whitespace.
- Suricata rule, classification, and reference paths were verified.

**Files selected for staging review:**
- `.gitignore`
- `docs/research-log.md`
- `config/suricata/suricata.yaml`
- `config/suricata/suricata.yaml.in`
- `rules/suricata/.gitkeep`
- `services/ml-service/eve_ingestion.py`
- `tests/test_eve_ingestion.py`

**Excluded from staging:** Downloaded/generated rules, generated classification data, logs, PCAPs, and temporary test artifacts.

**Publishing gate:** Inspect the staged file list, staged diff, and staged whitespace validation before committing. Push only after the review passes.

**Status:** Validation passed; staging review pending.

### Staged Configuration Whitespace Review — 12 October 2026

**Staged files:** Seven intended project paths are staged for review.

**Validation finding:** `git diff --cached --check` identified trailing whitespace on three comment lines in each Suricata configuration file:
- `config/suricata/suricata.yaml`
- `config/suricata/suricata.yaml.in`

**Assessment:** The reported issues are whitespace in comments, not evidence of a runtime configuration failure.

**Next action:** Remove trailing whitespace from the two configuration files, restage them, and rerun staged whitespace validation and the parser unit tests.

**Safety:** Do not include downloaded rules, generated logs, PCAPs, or temporary test artifacts. Do not commit until staged validation passes.

**Status:** Staging review found formatting issues; correction pending.

### Staged Validation Passed — 12 October 2026

**Permanent unit tests:** All 10 EVE ingestion tests passed.

**Whitespace validation:** `git diff --cached --check` completed without errors after trailing whitespace was removed from both Suricata configuration files.

**Staged inventory:** Seven approved paths are staged:
- `.gitignore`
- `config/suricata/suricata.yaml`
- `config/suricata/suricata.yaml.in`
- `docs/research-log.md`
- `rules/suricata/.gitkeep`
- `services/ml-service/eve_ingestion.py`
- `tests/test_eve_ingestion.py`

**Excluded artifacts:** Downloaded/generated rules, generated classification data, logs, PCAPs, and temporary test artifacts.

**Next action:** Perform a final staged-diff review, create a commit, push to `origin main`, and verify the resulting commit and remote synchronization.

**Status:** Staged validation passed; commit and push pending.

### Final Git Review — 12 October 2026

**Branch and remote:** The current branch is `main`, with `origin` pointing to `https://github.com/Ak7865/immunet-ips.git`.

**Staged review:** Seven intended paths are staged. The staged whitespace check passed, and the staged inventory contains no downloaded rules, generated logs, or PCAP files.

**Remaining change:** `docs/research-log.md` has additional unstaged edits after the initial staging. These must be included and checked before the commit.

**Next action:** Stage the updated research log, rerun staged whitespace validation and unit tests, commit the reviewed changes, push to `origin main`, and verify the resulting commit and working-tree state.

**Status:** Final review passed with research-log restaging required; publishing pending.

