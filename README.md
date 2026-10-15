# 📊 Automated Sales Data Cleaner & Executive Financial Reporter

An end-to-end Python data pipeline built with Pandas to clean, normalize, and summarize messy CSV/Excel invoice datasets automatically.

## 🎯 Business Value
Small and medium businesses lose hours manually fixing messy spreadsheet data (inconsistent dates, duplicate rows, bad numeric entries, and inconsistent status labels). This pipeline automates the entire ETL (Extract, Transform, Load) process in seconds.

## 🛠️ Key Features
- **Data Sanitization:** Strips leading/trailing spaces, standardizes phone numbers, and removes empty customer fields.
- **Date Normalization:** Unifies inconsistent date formats (e.g., `YYYY/MM/DD` or `YYYY-MM-DD`) into ISO standard (`YYYY-MM-DD`).
- **Currency & Type Sanitization:** Converts non-numeric or corrupted values into clean float amounts (`0.0`).
- **Status Mapping:** Harmonizes mixed-case payment statuses (`payé`, `PAYÉ`, `paid` -> `Paid`).
- **Deduplication:** Filters out strict duplicate transactions.
- **Executive Financial KPI Summary:** Automatically generates a separate summary CSV calculating total revenue, transaction counts, and average order value (AOV) grouped by payment status.

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/emmanuelvect99/python-excel-cleaner.git](https://github.com/emmanuelvect99/python-excel-cleaner.git)
   cd python-excel-cleaner