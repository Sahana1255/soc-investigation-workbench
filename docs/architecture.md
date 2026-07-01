# SOC Investigation Workbench Architecture

## High-Level Architecture

```
                    Evidence Files
                           │
      ┌────────────────────┼────────────────────┐
      │                    │                    │
 Windows EVTX         Linux Logs         Firewall Logs
      │                    │                    │
      └────────────────────┼────────────────────┘
                           │
                           ▼
                 Evidence Classifier
                           │
                           ▼
                    Parser Engine
                           │
      ┌────────────────────┼────────────────────┐
      │                    │                    │
 WindowsParser      LinuxParser        FirewallParser
      │                    │                    │
      └────────────────────┼────────────────────┘
                           │
                           ▼
                      Event Objects
                           │
                           ▼
                  Investigation Engine
                           │
      ┌──────────────┬───────────────┬───────────────┐
      │              │               │               │
 IOC Extractor   Sigma Engine   MITRE Mapper   Risk Engine
      │              │               │               │
      └──────────────┴───────────────┴───────────────┘
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
                 Streamlit Dashboard
                           │
                           ▼
               PDF Investigation Report
```

---

## Core Components

### Evidence Layer

- Windows EVTX
- Linux Logs
- Firewall Logs
- Email Evidence
- CSV Evidence

---

### Processing Layer

- Evidence Classification
- Parsing
- IOC Extraction
- Investigation

---

### Intelligence Layer

- Sigma Detection
- MITRE ATT&CK Mapping
- Risk Assessment

---

### Correlation Layer

- Relationship Mapping
- Timeline Generation
- Event Correlation

---

### Presentation Layer

- Streamlit Dashboard
- PDF Reports
- Case Management