"""
FINRA Python Financial Engine
- Modul 1: Analisis Arus Kas & Kapasitas Investasi dari Dataset Transaksi CSV
- Modul 2: Fama-French Five-Factor Model Calculation & Archetype Mapping
- Modul 3: Estimasi Expected Return Portofolio & Proyeksi Akumulasi Aset
"""

import os
import json
import pandas as pd

# 1. Load dataset transaksi
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
csv_path = os.path.join(project_root, 'storage', 'app', 'dataset_transactions.csv')
if not os.path.exists(csv_path):
    print(f"Error: {csv_path} tidak ditemukan.")
    exit(1)

df = pd.read_csv(csv_path)
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['YearMonth'] = df['Date'].dt.to_period('M')

# Pisahkan Income dan Expense
incomes = df[df['Type'].str.lower() == 'income']
expenses = df[df['Type'].str.lower() == 'expense']

total_income = float(incomes['Amount'].sum())
total_expense = float(expenses['Amount'].sum())
net_savings = total_income - total_expense
savings_rate = (net_savings / total_income * 100) if total_income > 0 else 0.0


# -------------------------------------------------------------
# MODUL 1: LAPORAN KINERJA KEUANGAN PER TAHUN (ANNUAL REPORT)
# -------------------------------------------------------------
years_list = sorted(df['Year'].unique())

annual_summary = df.groupby(['Year', 'Type'])['Amount'].sum().unstack(fill_value=0.0)
if 'Income' not in annual_summary.columns:
    annual_summary['Income'] = 0.0
if 'Expense' not in annual_summary.columns:
    annual_summary['Expense'] = 0.0

annual_summary['NetSavings'] = annual_summary['Income'] - annual_summary['Expense']
annual_summary['SavingsRate%'] = (annual_summary['NetSavings'] / annual_summary['Income'] * 100).fillna(0.0)

print("=" * 80)
print("LAPORAN KEUANGAN TAHUNAN FINRA (ANNUAL REPORT)")
print("=" * 80)
print(f"{'Tahun':<6} | {'Pemasukan':<16} | {'Pengeluaran':<16} | {'Net Arus Kas':<16} | {'Savings Rate':<12}")
print("-" * 80)

annual_reports = []
for year in years_list:
    row = annual_summary.loc[year]
    inc = float(row['Income'])
    exp = float(row['Expense'])
    net = float(row['NetSavings'])
    sr = float(row['SavingsRate%'])

    # Top 3 kategori pengeluaran tahun ini
    year_expenses = expenses[expenses['Year'] == year]
    top_cats = year_expenses.groupby('Category')['Amount'].sum().sort_values(ascending=False).head(3).to_dict()

    annual_reports.append({
        'year': int(year),
        'income': inc,
        'expense': exp,
        'net_savings': net,
        'savings_rate_pct': sr,
        'top_expenses': top_cats
    })
    print(f"{year:<6} | Rp {inc:>13,.2f} | Rp {exp:>13,.2f} | Rp {net:>13,.2f} | {sr:>10.2f}%")

print("-" * 80)

# Rincian Top Kategori Pengeluaran Tiap Tahun
print("\n[Rincian 3 Pengeluaran Terbesar Tiap Tahun]:")
for rep in annual_reports:
    cat_items = ", ".join([f"{c}: Rp {a:,.0f}" for c, a in rep['top_expenses'].items()])
    print(f" * Tahun {rep['year']}: {cat_items}")

# -------------------------------------------------------------
# MODUL 2: FAMA-FRENCH FIVE-FACTOR MODEL INVESTING ENGINE
# -------------------------------------------------------------
print("\n" + "=" * 80)
print("FAMA-FRENCH FIVE-FACTOR MODEL INVESTING ENGINE (ANNUAL CAGR)")
print("=" * 80)
print("Model Formulasi Fama-French (2015):")
print("E(R_i) - R_f = b_i*(R_m - R_f) + s_i*SMB + h_i*HML + r_i*RMW + c_i*CMA\n")

# Parameter Benchmark Pasar Finansial Tahunan Indonesia (IDX & SBN Risk-Free)
rf = 0.0625          # Risk-Free Rate tahunan (BI-Rate / SBN 10-Yr ~ 6.25%)
mkt_premium = 0.065   # Premi Risiko Pasar IHSG (Rm - Rf ~ 6.5%)
smb_premium = 0.025   # Size Factor: Small-Cap minus Big-Cap (~ 2.5%)
hml_premium = 0.038   # Value Factor: High PBV minus Low PBV (~ 3.8%)
rmw_premium = 0.032   # Profitability Factor: Robust minus Weak Operating Profit (~ 3.2%)
cma_premium = 0.021   # Investment Factor: Conservative minus Aggressive Capex (~ 2.1%)

archetypes = {
    'defensive_quality': {
        'name': 'Defensive Quality Compounder',
        'target_factors': {'MKT': 0.65, 'SMB': 0.15, 'HML': 0.40, 'RMW': 0.90, 'CMA': 0.85},
        'desc': 'Proteksi modal maksimal dengan bobot laba prima (RMW) dan utang minim (CMA).'
    },
    'balanced_compounder': {
        'name': 'Smart Beta Factor Balanced',
        'target_factors': {'MKT': 0.95, 'SMB': 0.35, 'HML': 0.70, 'RMW': 0.75, 'CMA': 0.60},
        'desc': 'Keseimbangan prima antara Value, Quality, dan Market Return.'
    },
    'deep_value_cashflow': {
        'name': 'Fama Value & High Yield Hunter',
        'target_factors': {'MKT': 0.90, 'SMB': 0.45, 'HML': 0.95, 'RMW': 0.60, 'CMA': 0.70},
        'desc': 'Eksploitasi maksimal saham murah berdividen tinggi (HML Factor).'
    },
    'aggressive_growth_alpha': {
        'name': 'Small-Cap & Growth Alpha',
        'target_factors': {'MKT': 1.25, 'SMB': 0.85, 'HML': 0.20, 'RMW': 0.80, 'CMA': 0.30},
        'desc': 'Agresif mengejar pertumbuhan Small-Mid Cap bertumbuh cepat (SMB Factor).'
    }
}

factor_results = []
for key, arch in archetypes.items():
    f = arch['target_factors']
    # Formula Fama-French
    expected_excess_return = (
        f['MKT'] * mkt_premium +
        f['SMB'] * smb_premium +
        f['HML'] * hml_premium +
        f['RMW'] * rmw_premium +
        f['CMA'] * cma_premium
    )
    expected_cagr = (rf + expected_excess_return) * 100

    factor_results.append({
        'key': key,
        'name': arch['name'],
        'expected_cagr_pct': round(expected_cagr, 2),
        'factors': f,
        'desc': arch['desc']
    })

    print(f"[{arch['name']}]")
    print(f"  - Profil Faktor : MKT={f['MKT']}, SMB={f['SMB']}, HML={f['HML']}, RMW={f['RMW']}, CMA={f['CMA']}")
    print(f"  - Expected CAGR : {expected_cagr:.2f}% per tahun\n")

# Ekspor hasil analisa ke JSON untuk Laravel
output_json_path = os.path.join(project_root, 'storage', 'app', 'python_analysis_output.json')
with open(output_json_path, 'w', encoding='utf-8') as f:
    json.dump({
        'annual_reports': annual_reports,
        'fama_french_results': factor_results
    }, f, indent=4)

print("=" * 80)
print(f"Laporan tahunan berhasil disimpan ke: {output_json_path}")
print("=" * 80)
