# Configuration

Setting up your local conda environment, Azure Machine Learning services, and Mlflow Projects.

## Table of Contents
1. Environment Setup
    - Conda installation
    - AzureML-MLflow integration with MLflow Projects
2. Configure your Azure ML Workspace and services
    - Workspace parameters
    - Access your workspace
    - Create a new workspace
    - Create compute resources
3. MLflow Projects Setup
4. How to use the sample notebooks
5. Going further

## Environment Setup

### Before you start
You should have Anaconda or Miniconda3 installed. MLflow requires conda to be on the `PATH` for the projects feature.

### 1. Conda Installation

[Install Miniconda3](https://docs.conda.io/en/latest/miniconda.html) with the relevant OS installation for **Python 3.6** or greater. Let the installer add the conda installation of Python to your PATH environment variable. If you don't, you'll need to set the Python PATH environment variable yourself!

Check conda is on the  `PATH` by running the following command. 
```
conda --version
```
If you already had conda installed, update conda if you can.
```
conda update conda
```
Clone this repository to use its notebooks and environment configuration file.
```
git clone https://github.com/KarishmaDaga/MlflowProjectNotebooks.git
```
Then, create a clean conda environment with Python 3.6 and the provided environment.yaml file (i.e. [bug-bash.yaml](bug-bash.yaml)). This will create a conda environment with the name of the configuration file. If you don't want to use this file, you can explicitly add the packages in the configuration file. 
```
# conda environment from configuration file
conda env create -f bug-bash.yaml python=3.6

# clean environment without configuration file
conda create --name {env-name} python=3.6
```

Now activate your conda environment by running,
```
conda activate bug-bash
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
### AzureML Setup
Install the patch containing the MLflow Projects integration from here into your conda environment,
```
``` 
Check the correct version is installed by running,
```
pip show azureml-mlfow
pip show azureml-core
```
Check the correct version of Mlflow is installed by running,
```
pip show mlflow
```

## Configure your Azure ML Workspace and services
I've created a workspace and a few compute resources to use for the bug bash.


