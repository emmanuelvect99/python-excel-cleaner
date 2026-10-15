import pandas as pd
import numpy as np

def clean_data_pipeline(input_file: str, clean_output_file: str, report_output_file: str) -> None:
    print("[INFO] Starting automated data cleaning pipeline...")
    
    # 1. Load dataset
    df = pd.read_csv(input_file)
    initial_count = len(df)
    
    # 2. Strip leading/trailing whitespaces
    string_cols = df.select_dtypes(include=['object']).columns
    for col in string_cols:
        df[col] = df[col].astype(str).str.strip()
        
    # 3. Filter invalid customer names
    df = df[df['Client'].str.len() > 0]
    df = df[df['Client'] != 'nan']
    
    # 4. Standardize date format to YYYY-MM-DD
    df['Date'] = df['Date'].str.replace('/', '-')
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    
    # 5. Sanitize numeric values
    df['Montant_HT'] = pd.to_numeric(df['Montant_HT'], errors='coerce').fillna(0.0)
    
    # 6. Normalize status labels
    status_mapping = {
        'payé': 'Paid', 'PAYÉ': 'Paid', 'PAYE': 'Paid', 'Payé': 'Paid',
        'non payé': 'Unpaid', 'Non Payé': 'Unpaid',
        'annulé': 'Cancelled', 'En attente': 'Pending'
    }
    df['Statut'] = df['Statut'].replace(status_mapping).str.capitalize()
    
    # 7. Deduplicate
    df.drop_duplicates(inplace=True)
    
    final_count = len(df)
    print(f"[SUCCESS] Reduced dataset from {initial_count} to {final_count} valid rows.")
    
    # Export cleaned dataset
    df.to_csv(clean_output_file, index=False)
    
    # 8. Generate summary report
    summary = df.groupby('Statut')['Montant_HT'].agg(
        Transaction_Count='count',
        Total_Revenue='sum',
        Average_Order_Value='mean'
    ).reset_index()
    
    summary['Total_Revenue'] = summary['Total_Revenue'].round(2)
    summary['Average_Order_Value'] = summary['Average_Order_Value'].round(2)
    
    summary.to_csv(report_output_file, index=False)
    print(f"[SUCCESS] Financial report generated: '{report_output_file}'")

if __name__ == "__main__":
    clean_data_pipeline('donnees_facturation.csv', 'donnees_propres.csv', 'rapport_financier.csv')