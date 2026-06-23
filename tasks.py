# adding states to the taks , it wouldbe Done:False, impplementing using a dictionary , so the list would be a list of dictionaries

#also removing and adding funstions realted to tasks here only i/o in the index

def add_task(tasks,text):
    tasks.append({'task':text,'status':False})

def remove_task(tasks,index):
    if 1<=index<=len(tasks):
        return tasks.pop(index-1)
    return None

#togle done/not
def togle_task(task,index):
    if 1<=index<=len(task):
        task[index-1]['status']= not task[index-1]['status']
        return True
    return False