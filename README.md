# 📊 Production-Ready Automated Data Cleaning & ETL Pipeline

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/pandas-2.0%2B-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Tested with Pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC.svg?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An industrial-grade, automated **ETL (Extract, Transform, Load)** pipeline built with Python and Pandas. Designed to ingest messy raw spreadsheet data, sanitize string casing, strip leading/trailing whitespace, enforce format standardization, eliminate duplicate records, and produce production-ready datasets accompanied by structured execution logs.

---

## 🌐 Architectural Overview & Business Value

In corporate environments, unstandardized Excel exports introduce costly errors in downstream BI tools (Power BI, Tableau, SQL databases). Manual data preparation is time-consuming and error-prone.

This project delivers a **reusable, fully automated solution** that guarantees data consistency and reliability across operations:

```text
               +-----------------------+
               |  Raw Input (.xlsx)    |
               +-----------+-----------+
                           |
                           v
               +-----------------------+
               |   ETL Engine (Pandas) |
               | - String Trimming     |
               | - Lowercase Casing    |
               | - Deduplication       |
               +-----------+-----------+
                           |
            +--------------+--------------+
            |                             |
            v                             v
+-----------------------+     +-----------------------+
| Clean Output (.xlsx)  |     | Audit Log (pipeline.log)|
+-----------------------+     +-----------------------+
```

### Key Highlights
- **CLI-Driven Execution**: Flexible command-line interface (`argparse`) allowing dynamic file path specification for automation and orchestration (e.g., Airflow, Cron).
- **Enterprise Logging**: Audit trail capability via standard `logging` module writing both to terminal and persistent log files (`pipeline.log`).
- **Quality Assurance**: Automated unit testing powered by `pytest` ensuring regression resistance.
- **Data Integrity Guarantee**: Standardized handling of missing values, duplicate removal, and string sanitization.

---

## 🛠️ Tech Stack & Standards

- **Core Runtime**: Python 3.10+
- **Data Manipulation**: `pandas`, `openpyxl`
- **Testing & QA**: `pytest`
- **Configuration & CLI**: `argparse`
- **Logging & Monitoring**: Python native `logging`

---

## ⚡ Quick Start & Installation

### Prerequisites
- Python 3.10 or higher
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/emmanuelvect99/python-excel-cleaner.git
cd python-excel-cleaner
```

### 2. Set Up Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate.bat

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage & Execution

### Step 1: Generate Mock Data (Optional)
Generate a synthetic dataset containing deliberate duplicates, dirty formatting, and unstandardized casing for testing:
```bash
python generate_data.py
```

### Step 2: Run the ETL Pipeline
Execute the pipeline using default inputs or specify custom file paths:

**Default Execution:**
```bash
python cleaner.py
```

**Custom File Execution (CLI Mode):**
```bash
python cleaner.py --input data_raw.xlsx --output data_clean.xlsx
```

---

## 🧪 Automated Testing & Validation

This project adheres to professional software engineering standards. Run the `pytest` suite to verify data transformation logic and safeguard against regressions:

```bash
pytest
```

**Sample Output:**
```text
================================= test session starts =================================
platform win32 -- Python 3.10.11, pytest-9.1.1, pluggy-1.6.0
collected 1 item

test_cleaner.py .                                                        [100%]

================================== 1 passed in 0.15s ==================================
```

---

## 📋 Data Transformation Showcase

| Raw Attribute / Field | Transformation Rule | Sanitized Output |
| :--- | :--- | :--- |
| `"  Alice "` | Trim leading/trailing whitespace | `"Alice"` |
| `"ALICE@EMAIL.COM "` | String trimming & Lowercase normalization | `"alice@email.com"` |
| Duplicate Rows | Exact row match deduplication | Removed & logged |
| Missing Records | Standardized null handling | Imputed / Cleaned |

---

## 📂 Project Structure

```text
python-excel-cleaner/
│
├── cleaner.py          # Main ETL pipeline implementation (CLI & Logging)
├── test_cleaner.py     # Automated unit test suite (Pytest)
├── generate_data.py   # Test dataset generator script
├── requirements.txt   # Pinpoint project dependencies
├── pipeline.log       # Automatically generated runtime audit log
└── README.md          # Project documentation
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👨‍💻 Author

**Ouattara Emmanuel**  
*Data Engineering & Python Automation Enthusiast*  
- **GitHub**: [@emmanuelvect99](https://github.com/emmanuelvect99)
