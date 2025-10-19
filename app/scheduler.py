from collections import defaultdict, deque
from .task import Task

def topological_sort(tasks):
    """Returns a list of task_ids in topological order."""
    graph = defaultdict(list)
    indegree = defaultdict(int)

    # Build graph and compute indegrees
    for task in tasks:
        for dep in task.dependencies:
            graph[dep].append(task.task_id)
            indegree[task.task_id] += 1

    # Queue of tasks with no dependencies
    queue = deque([task.task_id for task in tasks if indegree[task.task_id] == 0])
    topo_order = []

    while queue:
        current = queue.popleft()
        topo_order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != len(tasks):
        raise ValueError("Cycle detected in task dependencies!")
    return topo_order

def schedule_tasks(tasks):
    """
    Returns a list of Task objects in scheduled order:
    - Dependencies are respected
    - Tasks with higher priority come first
    - Tasks with earlier deadlines are prioritized
    """
    task_map = {task.task_id: task for task in tasks}
    topo_order = topological_sort(tasks)

    # Respect dependency order first
    schedule = [task_map[tid] for tid in topo_order]

    # Secondary sort: priority -> deadline
    schedule.sort(key=lambda t: (t.priority, t.deadline))

    return schedule
