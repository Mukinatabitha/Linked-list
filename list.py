from Node import *;
class TaskQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_task(self, task_name):
        """
        Adds a new task to the end of the queue.
        """
        new_node = TaskNode(task_name)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def run_task(self):
        """
        Removes and runs the task at the front of the queue.
        """
        if self.head is None:
            print("No tasks to run.")
            return
        print(f"Running task: {self.head.name}")
        self.head = self.head.next
        if self.head is None:
            self.tail = None  # Reset tail if queue becomes empty

    def show_tasks(self):
        """
        Displays all tasks currently in the queue.
        """
        if self.head is None:
            print("No tasks in the queue.")
            return
        print("Current Task Queue:")
        current = self.head
        while current:
            print(f" - {current.name}")
            current = current.next
if __name__ == "__main__":
    queue = TaskQueue()
    queue.add_task("Clean the house")
    queue.add_task("Pay bills")
    queue.add_task("Water the plants")

    queue.show_tasks()
    queue.run_task()
    queue.show_tasks()
