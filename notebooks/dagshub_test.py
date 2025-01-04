import mlflow
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/abay.betty.21/my-first-repo.mlflow")
dagshub.init(repo_owner='abay.betty.21', repo_name='my-first-repo', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)