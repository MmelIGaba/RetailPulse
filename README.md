# RetailPulse : SQL & ETL Data Pipeline Builder

RetailPulse is a full-stack data engineering project that demonstrates SQL proficiency, ETL pipeline development, and cloud integration. It extracts retail sales data from Kaggle, transforms it using Python, loads it into PostgreSQL, and visualizes results through a Streamlit dashboard. The project is modular, automated, and built for real-world data workflows.

## Project Overview

RetailPulse simulates an enterprise-grade data workflow:

1. **Extract** — Ingest open retail data from Kaggle.
2. **Transform** — Clean, validate, and enrich using Python.
3. **Load** — Store processed data in PostgreSQL and upload to AWS S3.
4. **Visualize** — Serve analytics via API and Streamlit dashboard.

## Architecture

[Kaggle Dataset]
↓
[Python ETL Pipeline]
↓
[AWS S3 + PostgreSQL (RDS)]
↓
[Flask/FastAPI API Layer]
↓
[Streamlit Dashboard ]

---

## Technologies Used


| Layer           | Tools & Libraries                                       |
| --------------- | ------------------------------------------------------- |
| ETL Pipeline    | Python 3.8+, pandas, kaggle, boto3, sqlalchemy, logging |
| Database        | PostgreSQL (local or AWS RDS)                           |
| Cloud Storage   | AWS S3                                                  |
| API Layer       | Flask or FastAPI                                        |
| Hosting         | Streamlit Cloud                                         |
| Automation      | GitHub Actions, Cron jobs                               |
| Version Control | Git + GitHub                                            |

## Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:MmelIGaba/RetailPulse.git
cd RetailPulse
```

## Configure Environment

Create a .env file in the /Back-End directory based on .env.example:

```
DB_HOST=your-db-host
DB_USER=your-username
DB_PASSWORD=your-password
DB_NAME=retailpulse
AWS_ACCESS_KEY=your-access-key
AWS_SECRET_KEY=your-secret-key
```

## 3. Install Dependencies

```
pip install -r Back-End/requirements.txt
pip install -r dashboard/requirements.txt

```

## 4. Run the ETL Pipeline

```
cd Back-End/etl
python extract.py
python transform.py
python load.py

```

## 5 launch the Streamlit Dashboard

```
cd dashboard
streamlit run app.py
```

## 6. Launch the Dashboard

```
cd Front-End
npm run dev
```

## Repository Structure

```
RetailPulse/
├── Back-End/
│   ├── etl/
│   ├── sql/
│   ├── requirements.txt
│   └── .env.example
├── dashboard/
│   ├── app.py
│   ├── components/
│   └── requirements.txt
├── .github/
│   └── workflows/
├── presentation/
│   └── RetailPulse_Slides.pdf
├── .gitignore
└── README.md

```

## Security & Configuration

All credentials are managed via environment variables. Do not commit real credentials or API keys. Use .env files locally and GitHub Secrets for automation.

## Learning Outcomes

By completing this project, you will:

Write and optimize SQL queries for analysis.

Design modular ETL pipelines in Python.

Integrate AWS storage and PostgreSQL.

Automate data workflows using GitHub Actions.

Visualize metrics with modern frontend tools.

## License

This project is open-source under the MIT License. You may use, modify, and distribute it with attribution.

## Author

1. Mmela Gabriel Dyantyi: Fullstack Developer and Aspiring Cloud Engineer
2. Boipelo M Ngakane: Frontend Developer | Low Code | AI | Cloud Engineer
3. [ammend as needed]
