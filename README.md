# Linked-list
1. TaskNode Class 
--------------------------------------
Each task in the scheduler is represented by a TaskNode. It contains:
- `name`: The task's name 
- `next`: A reference to the next node in the queue (initially None)

This is similar to a person in a line who knows who comes next.

Example:
    node = TaskNode("Water plants")

2. TaskQueue Class
--------------------------------
This is the actual linked list structure that:
- Tracks the `head` (start of the list) and `tail` (end)
- Lets you add tasks (enqueue), run tasks (dequeue), and show tasks.

Main Methods:
-------------
- `add_task(task_name)`:
    Adds a new TaskNode to the end.
    If the list is empty, it sets both head and tail to the new node.

- `run_task()`:
    Removes and prints the task at the front of the list.
    Then it updates `head` to point to the next task.

- `show_tasks()`:
    Traverses the list and prints each task in order.


