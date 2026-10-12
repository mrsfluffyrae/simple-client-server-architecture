# APPLICATION LAYER - the rules of the app
import data

def get_tasks():
    return data.load_tasks()

def add_task(title):
    title = title.strip()
    if title == "":
        return None          # empty tasks are not allowed
    tasks = data.load_tasks()
    tasks.append(title)
    data.save_tasks(tasks)
    return title
