# end-to-end-ML-Project-with-mlFlow

## Workflow

1. Update config.yaml
2. Update Schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src folder
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Update the app.py

# How to run?

### STEPS:

Clone the repository

```bash
    https://github.com/saGit1990/end-to-end-ML-Project-with-mlFlow
```

### Step 1: create a virtual environment

```bash
    python -m venv /path/to/new/virtual/environment
```
### Step 2: activate the virtual environment
```bash
    venv/script/activate
```

### Step 3: Install the dependencies on requirements.txt file



#### MLFLOW SETUP

### Dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI = https://dagshub.com/{user name}/{repo-name}

MLFLOW_TRACKING_USERNAME = personal access token

python script.py

Run this to export as env variable:

```bash
export MLFLOW_TRACKING_URI = https://dagshub.com/<user-name>/<repo-name>
export MLFLOW_TRACKING_USERNAME = <token>
```