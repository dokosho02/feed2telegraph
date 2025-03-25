import concurrent.futures
import time

def do_task(task_number):
    print(f"Task {task_number} started")
    time.sleep(1)  # Simulate some work
    print(f"Task {task_number} completed")
    return task_number

def main():
    tasks = [1, 2, 3, 4, 5]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(do_task, tasks))
    
    print(f"Results: {results}")

if __name__ == "__main__":
    main()
