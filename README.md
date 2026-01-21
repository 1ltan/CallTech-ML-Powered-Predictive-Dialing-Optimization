# CallTech-ML-Powered-Predictive-Dialing-Optimization
CallTech: ML-Powered Predictive Dialing Optimization

## Installation and Launch

### Install dependencies

```bash
# Create virtual environment
py -3.11 -m venv venv

# Activate
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Database configuration

Create a `.env` file:

```env
DB_HOST= your_HOST
DB_PORT= your_PORT
DB_NAME= your_DB_NAME
DB_USER= your_DB_USER
DB_PASSWORD= your_PASSWORD

```

### Prepare the database

Ensure that PostgreSQL contains database `DB_NAME` and table filled with training data.

---

## Running the Server

```bash
uvicorn app.main:app --reload
```

Server will be available at: `http://localhost:8000`

---

## API Documentation
`http://localhost:8000/docs`

---

## API Usage

### 1. Train Model

**POST `/train-model`**

```json
{
  "test_split": 0.2,
}
```

### 2. Predict

**POST `/predict`**

```json
{
  "education": "Graduation",
  "marital_status": "Single",
  "income": 64155,
  "kidhome": 1,
  "teenhome": 1,
  "recency": 15,
  "mntwines": 161,
  "mntfruits": 121,
  "mntmeatproducts": 80,
  "mntfishproducts": 52,
  "mntsweetproducts": 64,
  "mntgoldprods": 62,
  "numdealspurchases": 12,
  "numwebpurchases": 15,
  "numcatalogpurchases": 20,
  "complain": 10,
  "age": 43,
  "total_children": 2,
  "customer_for_years": 12
}
```
### 3. Report

**GET `/generate-report`**

Generates reports based on the available data.  
All generated reports will be saved in the following directory: app/reports
