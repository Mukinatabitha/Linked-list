class TaskNode:
    """
    Represents a single task node in the linked list.
    """
    def __init__(self, task_name):
        self.name = task_name
        self.next = None
