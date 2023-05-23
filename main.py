import math

class Task:
    def __init__(self, a, m, b):
        self.a = a
        self.m = m
        self.b = b
        self.e = (a + 4*m + b) / 6
        self.sd = (b - a) / 6

def main():
    tasks = []
    while True:
        a = input("Enter the optimistic estimate for a task (or 'done' to finish): ")
        if a == 'done':
            break
        m = float(input("Enter the most likely estimate for the task: "))
        b = float(input("Enter the pessimistic estimate for the task: "))
        tasks.append(Task(float(a), m, b))

    total_e = sum(task.e for task in tasks)
    total_sd = math.sqrt(sum(task.sd**2 for task in tasks))

    project_e = total_e
    project_sd = total_sd

    ci_min = project_e - 2*project_sd
    ci_max = project_e + 2*project_sd

    print(f"Project's 95% confidence interval: {ci_min:.2f} ... {ci_max:.2f} points")

if __name__ == '__main__':
    main()