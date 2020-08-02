from azureml import core
from azureml.core import Workspace

import mlflow

workspace = Workspace.from_config()  
mlflow.set_tracking_uri(workspace.get_mlflow_tracking_uri())
mlflow.set_experiment("mlflow-example")

# backend config: either use JSON object or dictionary
# :param "COMPUTE": if present in object, it will default to a remote run with the specified compute target
# :param USE_CONDA: tells azureml-mlflow whether to use the local conda env or to create 
# a new one from the project's MLproject

"""User managed environement"""
backend_config = {"USE_CONDA": False}
local_env_run = mlflow.projects.run(uri=".", 
                                    parameters={'alpha':0.3},
                                    backend = "azureml",
                                    backend_config = backend_config)

"""System managed environment"""
backend_config = {"USE_CONDA": True}
local_mlproject_run = mlflow.projects.run(uri=".", 
                                    parameters={'alpha':0.3},
                                    backend = "azureml",
                                    backend_config = backend_config)
