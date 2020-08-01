from azureml import core
from azureml.core import Workspace

import mlflow

workspace = Workspace.from_config()  
mlflow.set_tracking_uri(workspace.get_mlflow_tracking_uri())


submitted_run = mlflow.projects.run(uri="mlflow/examples/lightgbm",
                                    experiment_name="lightgbm",
                                    backend = "azureml",
                                    backend_config="mlflow/examples/lightgbm/backend.json")