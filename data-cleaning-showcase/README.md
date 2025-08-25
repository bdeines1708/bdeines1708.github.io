# Data Cleaning Showcase

**Author:** Ben Deines  
**Start date:** 2025-08-25

Reproducible walkthrough for profiling, cleaning, and validating a messy CSV.
Deliverables: clear notebooks (profile → clean → validate), issues log, and a data dictionary.

## Structure
```
data-cleaning-showcase/
├─ notebooks/
│  ├─ 01_profile_raw.ipynb
│  ├─ 02_clean_transform.ipynb
│  ├─ 03_validate_qa.ipynb
├─ data/
│  ├─ raw/    # put original file(s) here
│  └─ clean/  # scripts/notebooks write cleaned files here
├─ src/
│  ├─ utils.py
│  └─ dq_rules.py
├─ reports/
│  ├─ data_dictionary.md
│  └─ issues_log.md
├─ requirements.txt
└─ README.md
```

## How to run
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```
Open the notebooks in order. Replace `data/raw/your_file.csv` with your dataset.
