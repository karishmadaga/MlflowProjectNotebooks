from azureml import core
from azureml.core import Workspace

import mlflow

workspace = Workspace.from_config()  
mlflow.set_tracking_uri(workspace.get_mlflow_tracking_uri())

experiment_name = "mlflow-example"
mlflow.set_experiment(experiment_name)

submitted_run = mlflow.projects.run(uri=".", 
                                    parameters={'alpha':0.3},
                                    backend = "azureml",
                                    backend_config = "./backend_config.json")
