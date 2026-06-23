# so I am trying to create a simple cli based to do list in python
# intial version will be very basic and will just allow the user to add tasks and view them

# start by a main fuction to handle the user input and call the appropriate functions
from tasks import add_task,remove_task,togle_task

def main():
    tasks = []
    print("Welcome to To-DO-List CLI!!!")
    while True:
        functions=("Add a task","View tasks", "Remove tasks","Toggle Task","Exit")
        print("\n Please choose an option:")
        for i in range(len(functions)):
            print(i+1,functions[i])
        try: #try to make sure that even if some one enter five or three intead of 5 or 3 then instead of a error 
            choice=int(input("Enter the item of your choice:\t"))
        except ValueError:
            print("I can only understand numbers here. Please enter an integer.")
            continue
        if choice==1:
            task=empty_check_input("Enter your task:\t")
            add_task(tasks,task)
        elif choice==2:
            view(tasks)
        elif choice==3:
            remove_from(tasks)
        elif choice==4:
            try: #try to make sure that even if some one enter five or three intead of 5 or 3 then instead of a error 
                choice=int(input("Enter the item of your choice:\t"))
                togle_task(tasks,choice)
            except ValueError:
             print("I can only understand numbers here. Please enter an integer.")
             continue
        elif choice==5:
            break
        else:
            print("Invalid Choice enter a number of your option")
            continue
        

#v2 upgrade checking for empty entry in input of tasks
def empty_check_input(prompt):
    while True:
        task=input(prompt).strip()
        if task:
            return task
        print("Enter a valid task")

# #here I am using a fuction to add to the list ,I am using it to be fancy but you could just use append in the if itself, yeah but this is better as now I could add other functionalitieslike i could check for empty entry
# def add (chosen_list,tasktobe):
#     chosen_list.append(tasktobe)
#     print("Yohoo!! I just added your stuff to the list")


#now I am creating another function to view the list another fancy trick 

def view(chosen_list):
    if len(chosen_list)==0:
        print("No tasks found. Either you're all caught up or haven't added anything yet.")
    else:
        for i in range(len(chosen_list)):
         print(f"{i+1}|{chosen_list[i]['task']:<15}|{chosen_list[i]['status']}")

def remove_from(chosen_list):
    try:
        chosen_task=int(input("Enter the number of Task to be removed:\t"))
    except ValueError:
        print("I can only understand numbers here. Please enter an integer.")
        return
    
    if 1 <= chosen_task <= len(chosen_list):
        choice=input(f"Are you sure you Want to remove {chosen_list[chosen_task-1]['task']}:\t")
        if choice.strip().lower()=="yes":
            remove_task(chosen_list,chosen_task)
            print("Task Removed Sucessfully")
        elif choice.strip().lower()=="no":
            return
        else:
            print(" Yes/No Question !!")
            return
    else:
        print("Task not found.")



main()