X# EnfermeriaENESMorelia
Our final project in Project Management is to improve one of the attention services at ENES Morelia. We chose to enhance the user experience at the university's nursing clinic by developing software that streamlines the registration process when requesting medical attention. Currently, this process is done manually in a notebook, which can be inefficient and even tedious, especially considering that people visit the nursing clinic in situations of physical discomfort or even emergencies.
cat > README.md << 'EOF'
# ENES Morelia Infirmary System

Visit registration system for the ENES Morelia, UNAM infirmary.

## Requirements
- Python 3.12
- MariaDB or MySQL

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/bialycal/EnfermeriaENESMorelia.git
cd EnfermeriaENESMorelia
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the database
Enter MariaDB/MySQL and run:
```sql
CREATE DATABASE IF NOT EXISTS bd_enfermeria;
GRANT ALL PRIVILEGES ON bd_enfermeria.* TO 'root'@'localhost' IDENTIFIED BY 'enesmorelia';
FLUSH PRIVILEGES;
EXIT;
```

Then import the schema:
```bash
mysql -u root -p bd_enfermeria < bd_enfermeria.sql
```

### 5. Run the server
```bash
uvicorn main:app --reload
```

Open http://127.0.0.1:8000

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/students/{no_cuenta} | Get student by ID |
| POST | /api/students/ | Register new student |
| GET | /api/staff/ | Get all staff |
| GET | /api/staff/{id} | Get staff member by ID |
| POST | /api/staff/ | Register new staff member |
| POST | /api/visits/ | Register a visit |
| GET | /api/visits/today | Get today's visits |
EOF
