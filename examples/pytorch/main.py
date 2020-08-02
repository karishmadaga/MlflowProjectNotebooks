from azureml import core
from azureml.core import Workspace

import mlflow

workspace = Workspace.from_config()  
mlflow.set_tracking_uri(workspace.get_mlflow_tracking_uri())

config = {"COMPUTE": "cpu-cluster", "USE_CONDA": "True"}

submitted_run = mlflow.projects.run(uri=".",
                                    experiment_name="pytorch",
                                    backend = "azureml",
                                    backend_config = config)