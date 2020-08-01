'''from azureml import core
from azureml.core import Workspace'''
import mlflow
import mlflow.sklearn

'''ws = Workspace.from_config()
mlflow.set_tracking_uri(ws.get_mlflow_tracking_uri())
compute = {"name":"cpu-cluster", "vm_size":"STANDARD_D2_V2", "max_nodes":4}

another_project_run = mlflow.projects.run(uri="mlflow/examples/sklearn_elasticnet_wine", 
                                            entry_point = "train.py", 
                                            parameters={'alpha':0.3}, 
                                            experiment_name = "azureml-wine", 
                                            backend = "azureml", 
                                            backend_config = compute)'''
submitted_run = mlflow.projects.run(uri="mlflow/examples/sklearn_elasticnet_wine", 
                                            entry_point = "train.py", 
                                            parameters={'alpha':0.3},
                                            use_conda=False)