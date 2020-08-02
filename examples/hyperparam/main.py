from azureml import core
from azureml.core import Workspace

import mlflow
import mlflow.sklearn

workspace = Workspace.from_config()  
mlflow.set_tracking_uri(workspace.get_mlflow_tracking_uri())

submitted_run = mlflow.projects.run(uri="MlflowProjectNotebooks/examples/hyperparam", 
                                    experiment_name = "hyperparam",
                                    backend = "azureml",
                                    backend_config = "MlflowProjectNotebooks/examples/hyperparam/backend_config.json")