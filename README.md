# 🛡 SOC Investigation Workbench

A modular Security Operations Center (SOC) Investigation Platform built with Python and Streamlit for investigating Windows Event Logs, extracting Indicators of Compromise (IOCs), correlating security events, mapping MITRE ATT&CK techniques, performing risk assessment, and generating investigation reports.

---

# Features

- Windows Event Log (.evtx) Parsing
- Linux Log Parsing
- Firewall Log Parsing
- Email Evidence Parsing
- CSV Log Support
- IOC Extraction
- Sigma Rule Detection
- MITRE ATT&CK Mapping
- Risk Assessment Engine
- Event Correlation
- Case Management
- SQLite Database Storage
- Investigation Reports
- Interactive Streamlit Dashboard
- Relationship Graph Visualization
- Unit Testing
- Integration Testing

---

# Technology Stack

- Python 3.11
- Streamlit
- Pydantic
- Plotly
- Pandas
- NetworkX
- SQLite
- Python-EVTX
- ReportLab
- Pytest

---

# Project Structure

```
soc-investigation-workbench/
│
├── dashboard/
├── ingestion/
├── extraction/
├── detection/
├── intelligence/
├── correlation/
├── investigation/
├── services/
├── database/
├── models/
├── reports/
├── utils/
├── tests/
├── data/
├── screenshots/
├── docs/
│
├── app.py
├── config.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# Investigation Workflow

```
Evidence Files
      │
      ▼
Evidence Classifier
      │
      ▼
Parser Engine
      │
      ▼
Platform Parser
      │
      ▼
Extraction Engine
      │
      ▼
IOC Extraction
      │
      ▼
Sigma Detection
      │
      ▼
MITRE Mapping
      │
      ▼
Risk Assessment
      │
      ▼
Correlation Engine
      │
      ▼
Case Manager
      │
      ▼
SQLite Database
      │
      ▼
Dashboard & Reports
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/<username>/soc-investigation-workbench.git
```

Go into the project

```bash
cd soc-investigation-workbench
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

```bash
streamlit run app.py
```

---

# Running Tests

```bash
pytest -v
```

Current Status

```
14 Tests Passed
```

---

# Dashboard

The application provides:

- Summary Dashboard
- Analytics
- Event Explorer
- IOC Explorer
- Timeline
- MITRE ATT&CK Mapping
- Risk Assessment
- Relationship Graph
- Report Generator
- Case Management

---

# Supported Evidence

| Evidence | Status |
|----------|--------|
| Windows EVTX | ✅ |
| Linux Logs | ✅ |
| Firewall Logs | ✅ |
| CSV Logs | ✅ |
| Email (.eml) | ✅ |

---

# Future Enhancements

- VirusTotal Integration
- AbuseIPDB Integration
- MISP Integration
- YARA Live Rules
- Sigma Community Rules
- Multi-user Authentication
- REST API
- Docker Deployment
- Kubernetes Deployment

---

# Test Coverage

- Evidence Classification
- IOC Extraction
- Parser Engine
- Sigma Detection
- MITRE Mapping
- Risk Assessment
- Correlation Engine
- SOC Engine
- End-to-End Investigation Pipeline

```
14 / 14 Tests Passing
```

---

# License

MIT License

---

# Author

**Sahana**

SOC Analyst | Python | Digital Forensics | Threat Detection | Incident Response