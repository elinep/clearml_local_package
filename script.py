import my_local_package
from clearml import Task
task = Task.init(project_name='elinep', task_name='local_package_enqueue')
task.execute_remotely(exit_process=True)

print(my_local_package.__version__)

