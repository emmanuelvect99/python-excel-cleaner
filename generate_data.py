import csv
import random

# Initial mock data set with explicit entry errors
data = [
    ["2024-01-15", "SARL ATLAS", "contact@atlas.ma", "06 61 12 34 56", "1500", "payé"],
    ["2024-01-15", "SARL ATLAS", "contact@atlas.ma", "0661123456", "1500", "Payé"],
    ["2024/01/16", "societe B", "info@societeb.com", "06.62.99.88.77", "invalid", "non payé"],
    ["2024-01-17", "Cabinet K", "k@gmail.com", "0611223344", "3200", "PAYÉ"],
]

clients = [
    ("SARL ATLAS", "contact@atlas.ma", "0661123456"),
    ("Société B", "info@societeb.com", "0662998877"),
    ("Cabinet K", "k@gmail.com", "0611223344"),
    ("Maroc Logistics", "contact@maroclogistics.ma", "0655443322"),
    ("Atlas Tech", "support@atlastech.ma", "0522112233"),
    ("Maghreb Auto", "commercial@maghrebauto.ma", "0677889900"),
    ("BatiServices SARL", "devis@batiservices.ma", "0612345678"),
    ("Souss Export", "sales@sousse xport.ma", "0699887766"),
    ("Digital Solutions", "hello@digitalsolutions.ma", "0644332211"),
    ("Pharmacie Du Centre", "contact@pharmacentre.ma", "0537889900")
]

statuses = ["Payé", "payé", "PAYÉ", "non payé", "Non Payé", "En attente", "annulé", "PAYE"]
dates = [f"2024-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 28)]

# Generate 210 realistic records with noise
for i in range(210):
    client, email, phone = random.choice(clients)
    date = random.choice(dates)
    
    if random.random() < 0.05:
        date = date.replace("-", "/")
        
    amount = str(random.choice([500, 1200, 1500, 2300, 3200, 4500, 8000, "invalid", 0]))
    status = random.choice(statuses)
    
    if random.random() < 0.03:
        client = "   "
    if random.random() < 0.02:
        amount = "invalid"
        
    data.append([date, client, email, phone, amount, status])

filename = "donnees_facturation.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Client", "Email", "Telephone", "Montant_HT", "Statut"])
    writer.writerows(data)

print(f"[SUCCESS] Generated raw dataset '{filename}' with {len(data)} records.")