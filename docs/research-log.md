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

