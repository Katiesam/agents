import pandas as pd
import numpy as np
import datetime
import time

# import pprint
# from collections import OrderedDict

# To add:
# Sort by first/last name, age: display df but don't modify original ie. don't update

# Place Agents.csv into a DataFrame. Prompt for command.
# f = 'Agents.csv'
f = 'Week8.csv'
agents = pd.read_csv(f)
agents.index += 1
print(agents)

column_names = list(agents.columns)
name_col = column_names[0]
agent_name_col = column_names[1]
in_col = column_names[2]
out_col = column_names[3]
age_col = column_names[4]
parent_col = column_names[5]
email_col = column_names[6]
phone_col = column_names[7]
print(column_names)
print("\nWelcome. \nAvailable commands: add, remove, list, stats, in, out, shape, exit")

def add():
    name = input("Enter name: ")
    agent_name = input("Enter agent name: ")
    age = input("Enter age: ")
    parent = input("Enter parent name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    agents.loc[len(agents)+1] = [name, agent_name, 0, 0, age, parent, email, phone]
    print("Welcome " + name + ", a.k.a Agent " + agent_name + " (Age " + age + ")")
    update()

def remove():
    name = input("Enter name: ")
    global agents
    agents = agents[agents[name_col] != name]
    print(name + " has been removed.")
    update()

def edit():
    number = input("Enter number: ")
    attribute = input("Which column would you like to edit? ")
    value = input("Enter value: ")
    print("Agent has been edited. ")

def stats():
    print("Number of agents: " + str(len(agents)))
    p = agents[in_col].notnull().sum()
    print("Agents Present: " + str(p))
    print("Agents Absent: " + str(len(agents) - p))
    y = min(agents[age_col])
    o = max(agents[age_col])
    a = np.average(agents[age_col])
    print("Youngest Agent Age: " + str(y))
    print("Oldest Agent Age: " + str(o))
    print("Average Agent Age: " + str(a))

def in_agent():
    name = str(input("Enter name: "))
    agents['Status'] = np.where(agents.Name == name, True, agents.Status)
    print("Agent " + name + " has arrived.")
    update()

def out_agent():
    name = str(input("Enter name: "))
    agents['Status'] = np.where(agents.Name == name, False, agents.Status)
    print("Agent " + name + " has departed.")
    update()

def clear():
    agents.loc['SIGNED IN?', 'SIGN OUT TIME'] = 0
    print("Sign in/out cleared. ")
    update()

def update():
    agents.to_csv(f, index=False)

# def getName(kind):
#     # kind can be name, agent name, parent, email
#     name = input("Enter " + kind + ": ")
#     valid = type(name) == str
#     while not valid:
#         num = input("Invalid input. Re-enter " + str(kind) + ": ")
#         valid = type(name) == str
#     # return name
#     print(name)
#     print(valid)

def getNum(kind):
    # kind can be row#, age, phone#
    num = input("Enter " + str(kind) + ": ")
    valid = num.isnumeric()
    while not valid:
        num = input("Invalid input. Re-enter " + str(kind) + ": ")
        valid = num.isnumeric()
    return num
    # print(num)
    # print(valid)

def checkRow(num):
    print(range(1, len(agents) + 1))
    if int(num) in range(1, len(agents) + 1):
        return True
    else: 
        return False
    
def getTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    # print(current_time)
    return (current_time)

while True:
    command = input("\nEnter command: ")
    if command == "add":
        # add()
        name = input("Enter name: ")
        agent_name = input("Enter agent name: ")
        age = input("Enter age: ")
        parent = input("Enter parent name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        agents.loc[len(agents)+1] = [name, agent_name, 0, 0, age, parent, email, phone]
        print("Welcome " + name + ", a.k.a Agent " + agent_name + " (Age " + age + ")")
        update()
    elif command == "remove":
        # remove()
        entered = input("Enter row number: ")
        name = agents.loc[int(entered), name_col]
        agent_name = agents.loc[int(entered), agent_name_col]
        # confirm = input("Please confirm removal of " + name + ", a.k.a Agent " + agent_name + ". (y/n) ")
        confirm = input("Please confirm removal of row #" + str(entered) + ". (y/n) ")
        if confirm == 'y':
            agents = agents[agents.index != int(entered)]
            print("Row #" + entered + " has been removed.")
            update()
        elif confirm == 'n':
            print("Removal cancelled. ")
    elif command == "edit":
        # edit()
        number = input("Enter row number: ")
        attribute = input("Which column would you like to edit? ")
        value = input("Enter value: ")
        agents.loc[int(number), str(attribute)] = value
        print("Row #" + number + " has been edited.")
        update()
    elif command == "list":
        print(agents)
    elif command == "sort":
        sort()
    elif command == "stats":
        stats()  
    elif command == "in":
        # in_agent()
        entered = input("Enter row number: ")
        t = getTime()
        agents.loc[int(entered), 'SIGNED IN?'] = t
        print(agents.loc[int(entered), name_col] + " has arrived at " + t + ". ")
        update()
    elif command == "out":
        # out_agent()
        entered = input("Enter row number: ")
        t = getTime()
        agents.loc[int(entered), 'SIGN OUT TIME'] = t
        print("Agent " + agents.loc[int(entered), name_col] + " has departed at " + t + ". ")
        update()
    elif command == "clear":
        clear()
    elif command == "shape":
        print(agents.shape)
    elif command == "exit":
        break
    elif command == "get1":
        num = int(getNum("phone"))
        print(num)
        print(checkRow(num))
    elif command == "time":
        getTime()