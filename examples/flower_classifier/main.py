from azureml import core
from azureml.core import Workspace

import mlflow
import mlflow.sklearn

workspace = Workspace.from_config()  
mlflow.set_tracking_uri(workspace.get_mlflow_tracking_uri())

submitted_run = mlflow.projects.run(uri=".", 
                                    experiment_name = "flower_classifier",
                                    backend = "azureml",
                                    backend_config = "./backend_config.json")
