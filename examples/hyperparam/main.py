from azureml import core
from azureml.core import Workspace

import mlflow
import mlflow.sklearn

workspace = Workspace.from_config()  
mlflow.set_tracking_uri(workspace.get_mlflow_tracking_uri())

mlflow.set_experiment("hyperparam")

config = {"COMPUTE": "cpu-cluster", "USE_CONDA": True}
uri = "MlflowProjectNotebooks/examples/hyperparam/"
submitted_run = mlflow.projects.run(uri=uri, 
                                    backend = "azureml",
                                    backend_config = config)

# train Keras DL model
submitted_run = mlflow.projects.run(uri=uri,
                                    entry_point = "train",
                                    backend = "azureml",
                                    backend_config = config)
# Use hyperopt
submitted_run = mlflow.projects.run(uri=uri,
                                    entry_point = "hyperopt",
                                    backend = "azureml",
                                    backend_config = config)

# Use GPyOpt
submitted_run = mlflow.projects.run(uri=uri,
                                    entry_point = "gpyopt",
                                    backend = "azureml",
                                    backend_config = config)
# Use random search
submitted_run = mlflow.projects.run(uri=uri,
                                    entry_point = "random",
                                    backend = "azureml",
                                    backend_config = config)