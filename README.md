# GitHub Data Analytics

This project fetches commit and issue data from the `psf/requests` GitHub repository, stores it in a SQLite database, and creates dbt models to aggregate the data by month.

This guide provides step-by-step instructions to set up and run the GitHub API project on macOS.

It is recommended to read the overview.pdf before going through the steps of running the project!

## Prerequisites
Before starting, ensure you have the following installed on your macOS machine:

- Python 3.x
- SQLite3
- pip (Python package installer)

## Installation Steps

### 1. Clone the Repository

Clone the GitHub API project repository to your local machine:

```bash
git clone https://github.com/zeto95/audibene_challenge.git
cd github-api-project 
```

### 2. Set up Python Enviroment 

# Install virtualenv if you haven't already
```bash
pip install virtualenv
```

# Create a virtual environment
```bash
virtualenv venv
```

# Activate the virtual environment
```bash
source venv/bin/activate
```

### 3. Install Python Dependencies:
```bash
pip install -r requirements.txt
```
### 4. Set Environment Variables
```bash
export GITHUB_TOKEN="your_github_token_here"
```
### 5. Fetch Data from GitHub API and Store in SQLite
```bash
python api_data.py
```

### 6. Set Up dbt Project
```bash
cd dbt_project
```
# Create the dbt profile
```bash
mkdir -p ~/.dbt
cp profiles.yml ~/.dbt/profiles.yml
```

# Install dbt and required dependencies
```bash
pip install dbt-core==1.1.0 dbt-sqlite==1.1.0
```
# Initialize dbt project
```bash
dbt init
```
# Verify dbt installation
```bash
dbt --version
```
### 7. Create Output Directory (data_schemas)
```bash
mkdir -p dbt_project/data_schemas
```

### 8. Run dbt Models
```bash
dbt run
```
### 9. View Results
```bash
sqlite3 github_data.db

sqlite> SELECT * FROM commits;
sqlite> .exit
```