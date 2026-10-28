# FINRA — Financial Intelligent Assistant for Daily Analytics

> **Proposal Rancangan Agen Cerdas & Prototipe Sistem Asisten Finansial Harian Berbasis LLM, Rule-Based Guardrails, dan Model Multi-Faktor Fama-French**

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Colab PoC](https://img.shields.io/badge/Google%20Colab-PoC%20Active-orange.svg)](https://colab.research.google.com/drive/1UkFa2gaso8EK0PSTxS3tQhFhC4OTpD9f?usp=sharing)
[![Proposal PDF](https://img.shields.io/badge/Proposal%20Document-PDF-red.svg)](./Proposal-Agen%20Cerdas%20FINRA.pdf)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Ringkasan Proyek

**FINRA** (*Financial Intelligent Assistant for Daily Analytics*) adalah sistem agen cerdas hibrida (*Utility-Based Agent*) yang dirancang untuk mengatasi friksi pencatatan keuangan harian bagi mahasiswa dan profesional muda. FINRA mengombinasikan keunggulan antarmuka bahasa alami (*Natural Language Processing*) berbasis Large Language Models (LLM) dengan kepastian deterministik dari sistem berbasis aturan (*Rule-Based Guardrails*) dan model portofolio multi-faktor Fama-French.

Sistem ini diajukan untuk memenuhi tugas Evaluasi Tengah Semester (ETS) mata kuliah **INFO-3530 Kecerdasan Buatan** — Program Studi Informatika, Universitas Bhayangkara Jakarta Raya.

### 👥 Tim Pengembang (Kelompok FINRA - F5A1)
1. **Jidan Asyura Hartana** (NIM: `202410715146`) — Lead AI & Backend Architecture (50%)
2. **Yusuf Sanjaya** (NIM: `202410715162`) — System Requirements & Evaluation (50%)

---

## 🚀 Fitur dan Kemampuan Agen Cerdas

1. **Natural Language Expense Parsing (NLP Adapter)**  
   Mengekstrak transaksi harian dari input teks percakapan bebas (contoh: *"tadi sore ngopi kenangan 25rb pake gopay"*) menjadi entitas terstruktur format JSON (nominal, pos belanja, tanggal, metode pembayaran).
2. **Deterministic Rule Engine & Guardrails (RB-01 s/d RB-06)**  
   Validasi ketat terhadap nominal tidak wajar (negatif/nol), penegakan kuota pos belanja mengacu pada formula 50/30/20 Elizabeth Warren (*50% Needs, 30% Wants, 20% Savings*), serta pencegahan halusinasi kalkulasi finansial.
3. **Anomaly & Outlier Detection (Z-Score)**  
   Mendeteksi lonjakan transaksi di luar kebiasaan historis pengguna untuk memicu peringatan dini dan mekanisme *Human-in-the-Loop*.
4. **Multi-Factor Portfolio Recommendation Engine (Fama-French 2015)**  
   Mengalokasikan sisa kas surplus bulanan pengguna ke dalam 4 arketipe portofolio terukur secara kuantitatif (*Defensive Quality Compounder, Smart Beta Balanced, Fama Value Hunter, dan Small-Cap Alpha*).

---

## 📂 Berkas Dokumen & Artefak Proyek

- 📄 **[Proposal-Agen Cerdas FINRA.pdf](./Proposal-Agen%20Cerdas%20FINRA.pdf)**: Dokumen naskah lengkap proposal ETS (Format Times New Roman 12, margin 3 cm, spasi 1,5, dilengkapi diagram arsitektur, diagram kelas, diagram urutan, evaluasi PoC Python, dan Lampiran A–E).
- 📝 **[Proposal-Agen Cerdas FINRA.docx](./docs/Proposal-Agen%20Cerdas%20FINRA.docx)**: Dokumen Word master.
- 🐍 **[finra_factor_analysis.py](./finra_factor_analysis.py)**: Kode sumber modul analitik Python PoC.
- 📊 **[dataset_transactions.csv](./dataset_transactions.csv)**: Dataset benchmark transaksi Kaggle (10.000 baris transaksi).
- 🖼️ **[docs/figures/](./docs/figures/)**: Seluruh diagram sistem beresolusi tinggi:
  - `gambar_4_1_arsitektur_finra.png` — Diagram Arsitektur Sistem FINRA
  - `gambar_5_1_class_diagram.png` — Diagram Kelas Konseptual
  - `gambar_5_2_sequence_diagram.png` — Diagram Urutan Pencatatan Transaksi
  - `gambar_5_3_poc_cashflow_503020.png` — Visualisasi Arus Kas & Pos 50/30/20
  - `gambar_5_4_poc_fama_french.png` — Grafik Simulasi Return Portofolio Multi-Faktor

### 🔗 Tautan Eksternal
- **Notebook Google Colab (Proof of Concept Python)**:  
  [https://colab.research.google.com/drive/1UkFa2gaso8EK0PSTxS3tQhFhC4OTpD9f?usp=sharing](https://colab.research.google.com/drive/1UkFa2gaso8EK0PSTxS3tQhFhC4OTpD9f?usp=sharing)
- **Repositori GitHub**:  
  [https://github.com/JidanAsyura/FINRA](https://github.com/JidanAsyura/FINRA)

---

## 💻 Cara Menjalankan Modul Analitik Python (PoC)

```bash
# 1. Clone repositori
git clone https://github.com/JidanAsyura/FINRA.git
cd FINRA

# 2. Setup Virtual Environment (opsional)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# atau
.venv\Scripts\activate    # Windows

# 3. Install Dependensi
pip install pandas numpy matplotlib

# 4. Jalankan Analisis Finansial PoC
python finra_factor_analysis.py
```

---

## 📜 Lisensi
Proyek ini dilisensikan di bawah lisensi [MIT](LICENSE).
