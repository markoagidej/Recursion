'''
id: Unique identifier for the task.
name: Name or description of the task.
subtasks: List of subtasks (nested hierarchy), if any.
priority: Priority level of the task (optional).
'''

# Task 1: Design the Task Scheduler Function

'''
Demo task list ref prioities
1       1   ->  1   ->  3
2       2   ->  3   ->  4
1       3   ->  5   ->  5
-2      4   ->  4   ->  1
-1      5   ->  2   ->  2
3       6   ->  6   ->  6
-3      7   ->  7   ->  8
-3      8   ->  8   ->  9
--2     9   ->  9   ->  10
---1    10  ->  10  ->  7
*Technically the last appearing task of a certain priority level shows first in this code
'''

def schedule_tasks(task_hierarchy):
    task_list = []
    # Fill task list with crrent level tasks
    for task in task_hierarchy:
        task_list.append(task)
    # Sort current level tasks by priority
    # sorted_tasks = mergeSortTasks(task_list)
    mergeSortTasks(task_list)
    # Iterate backwards through current level tasks
    index = len(task_list) - 1
    while index >= 0:
        # If a task has subtasks, sort that list (via recursive vall) to then be inserted into the current sorted task list, to maintain sub task priority with its parent task
        if task_list[index]["subtasks"]:
            sub_task_list = schedule_tasks(task_list[index]["subtasks"])
            beginning = task_list[:index + 1]
            end = task_list[index + 1:]
            task_list = beginning + sub_task_list + end
        index -= 1
    return task_list

def mergeSortTasks(task_list):
    if len(task_list) > 1:
        mid = len(task_list) // 2
        left = task_list[:mid]
        right = task_list[mid:]

        mergeSortTasks(left)
        mergeSortTasks(right)

        left_index = right_index = main_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index]["priority"] < right[right_index]["priority"]:
                task_list[main_index] = left[left_index]
                left_index += 1
            else:
                task_list[main_index] = right[right_index]
                right_index += 1

            main_index += 1

        while left_index < len(left):
            task_list[main_index] = left[left_index]
            left_index += 1
            main_index += 1
            
        while right_index < len(right):
            task_list[main_index] = right[right_index]
            right_index += 1
            main_index += 1

# Task 2: Implement Task Scheduling Logic

# Task 3: Test the Task Scheduler Function

task_chart = [
    {
        "id": 1,
        "name": "task1",
        "subtasks": [],
        "priority": 1
    },
    {
        "id": 2,
        "name": "task2",
        "subtasks": [],
        "priority": 2
    },
    {
        "id": 3,
        "name": "task3",
        "subtasks": [
            {
                "id": 4,
                "name": "task4",
                "subtasks": [],
                "priority": 2
            },
            {
                "id": 5,
                "name": "task5",
                "subtasks": [],
                "priority": 1
            }
        ],
        "priority": 1
    },
    {
        "id": 6,
        "name": "task6",
        "subtasks": [
            {
                "id": 7,
                "name": "task7",
                "subtasks": [],
                "priority": 3
            },
            {
                "id": 8,
                "name": "task8",
                "subtasks": [
                {
                    "id": 9,
                    "name": "task9",
                    "subtasks": [
                    {
                        "id": 10,
                        "name": "task10",
                        "subtasks": [],
                        "priority": 1
                    }
                ],
                    "priority": 2
                }
            ],
                "priority": 3
            }
        ],
        "priority": 3
    }
]

ordered_task_list = schedule_tasks(task_chart)
for task in ordered_task_list:
    print(task["id"])

# Task 4: Analyze Time and Space Complexity
'''
Time Complexity is O(n + (n log n)). Merge sort is always O(n log n). All other operations are O(n)
Space Complexity is O(4n) or O(n). A new list copying the original is made. Another set of lists eequaling the length of the original is made when it is sorted. Every time there is a subtask, which could be every time, new lists need to be made which equals the previous list length.
The list slicing is probably the worst contributer to complexity in this code. Implementing a Linked List will make the constant list insertions much more efficient
'''

