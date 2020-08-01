# Configuration

Setting up your local conda environment, Azure Machine Learning services, and Mlflow Projects.

## Table of Contents
1. Environment Setup
    A. Conda installation
    B. AzureML-MLflow integration with MLflow Projects
2. Configure your Azure ML Workspace and services
    A. Workspace parameters
    B. Access your workspace
    C. Create a new workspace
    D. Create compute resources
3. MLflow Projects Setup
4. How to use the sample notebooks
5. Going further

## Environment Setup

### 1. Conda Installation

First, you need to [install Miniconda3](https://docs.conda.io/en/latest/miniconda.html) with the relevant OS installation for Python 3.6 or greater. Let the installer add the conda installation of Python to your PATH environment variable. There is no need to set the Python PATH environment variable yourself.

Check conda is on the  `PATH` by running the following command. 
```
conda --version
```
If you already had conda installed, update conda.
```
conda update conda
```
Then, create a clean conda environment with Python 3.6 and the provided environment.yaml file. This will create a conda environment with the name of the configuration file. If you don't want to use this configuration, you can explicitly add the packages listed by following the MLflow and AzureML setup.
```
# conda environment from configuration file
conda env create -f mlflow-proj-env.yaml

# clean environment without configuration file
conda create --name mlflow-proj-env python=3.6
```

Now activate your conda environment by running,
```
conda activate mlflow-proj-env
```
Validate by checking if your environment is listed,
```
conda info --envs
```
The active environment is the one with an asterisk (*)
Verify which version of Python is in your current environment
```
python --version
```
### 2. MLflow Setup
### 3. AzureML Setup

### Before you start
You should have Anaconda or Miniconda3 installed. MLflow requires conda to be on the `PATH` for the projects feature. 