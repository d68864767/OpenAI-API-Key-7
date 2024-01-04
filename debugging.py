```python
# Importing necessary modules
from allegro_trains import Task
from mlflow import start_run, log_param, log_metric
from tensorboard import SummaryWriter

def run():
    # Initialize Allegro Trains Debugger
    task = Task.init(project_name='AI Model Debugging', task_name='debugging')

    # Start a new run with MLflow Tracking
    with start_run():
        # Log a parameter (key-value pair)
        log_param("param1", 5)

        # Log a metric; metrics can be updated throughout the run
        log_metric("foo", 1)
        log_metric("foo", 2)
        log_metric("foo", 3)

    # Initialize TensorBoard Debugger
    writer = SummaryWriter()

    # Write a scalar to the tensorboard
    writer.add_scalar('Loss/train', 0.1, 1)

    # Make sure to close the writer
    writer.close()

    print("Debugging process has been completed.")

if __name__ == "__main__":
    run()
```
