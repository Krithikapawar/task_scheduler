class Task:
    def __init__(self, task_id, priority, deadline, dependencies=None):
        self.task_id = task_id
        self.priority = priority
        self.deadline = deadline
        self.dependencies = dependencies or []

    def __lt__(self, other):
        return (self.priority, self.deadline) < (other.priority, other.deadline)

    def __repr__(self):
        return f"Task({self.task_id}, P:{self.priority}, D:{self.deadline})"
