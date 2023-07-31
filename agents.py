import pandas as pd
import numpy as np
import datetime
# import pprint
# from collections import OrderedDict


# Place Agents.csv into a DataFrame. Prompt for command.
agents = pd.read_csv('Agents.csv')
agents.index += 1
print("Welcome. \nAvailable commands: add, remove, list, stats, in, out, shape, exit")
print(agents)

def add():
    name = str(input("Enter name: "))
    agent_name = str(input("Enter agent name: "))
    age = str(input("Enter age: "))
    status = False
    agents.loc[len(agents)+1] = [name, agent_name, age, status]
    print("Welcome " + name + ", a.k.a Agent " + agent_name + " (Age " + age + ")")
    update()

def remove():
    name = input("Enter name: ")
    global agents
    agents = agents[agents['Name'] != name]
    print(name + " has been removed.")
    update()

def stats():
    print("Number of agents: " + str(len(agents)))
    p = (agents['Status'] == True).sum()
    print("Agents Present: " + str(p))
    print("Agents Absent: " + str(len(agents) - p))
    print("Youngest Agent: ")
    print("Oldest Agent: ")
    print("Average Agent Age: ")


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
    agents['Status'] = False
    print("See y'all tomorrow!")
    update()

def update():
    agents.to_csv('Agents.csv', index=False)

while True:
    command = input("\nEnter command: ")
    if command == "add":
        add()
    elif command == "remove":
        remove()
    elif command == "list":
        print(agents)
    elif command == "stats":
        stats()  
    elif command == "in":
        in_agent()
    elif command == "out":
        out_agent()
    elif command == "clear":
        clear()
    elif command == "shape":
        print(agents.shape)
    elif command == "exit":
        break