# Start DB

```bash
# Start postgres, pgadmin
$ docker-compose up -d
```

# Set up pgadmin

- access to `localhost:8000` via browser
- Set up DB connection with below value
  - General
    - Name : postgresqls
  - Connection
    - Host name/address : postgresqls
    - Password : password

# Set up Python environment

```bash
# Create virtual environment
$ python -m venv {environment_name}

# Activate virtual environment
$ source {environment_name}/bin/activate

# Install dependency
$ pip install -r requirements.txt
```

# Execute seed

```bash
# Execute seed
python src/seed.py
```

# Other

```bash
# Make requirement file
$ pip freeze > requirements.txt

# Exit virtual environment
$ deactivate
```
