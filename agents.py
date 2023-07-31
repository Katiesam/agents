import pandas as pd
import numpy as np
import pprint
from collections import OrderedDict

# class Agent:
#     def __init__(self, name, agent_name, age, status):
#         self.name = name
#         self.agent_name = agent_name
#         self.age = age
#         self.status = status

# agents = {}

# Place Agents.csv into a DataFrame. Prompt for command.
agents = pd.read_csv('Agents.csv', index_col='Name')
print("Welcome. \nAvailable commands: add, remove, list, stats, in, out, update, shape, exit")
print(agents.to_string())

def add():
    name = str(input("Enter name: "))
    agent_name = str(input("Enter agent name: "))
    age = str(input("Enter age: "))
    status = False
    row_df = pd.DataFrame([[name, agent_name, age, status]], columns=['Name', 'AgentName', 'Age', 'Status'])
    agents.append(row_df, inplace=True)
    update()
    print("Welcome " + name + ", a.k.a Agent " + agent_name + " (Age " + age + ")")

def remove():
    name = input("Enter name: ")
    agents.drop(agents[name], inplace=True)
    print(name + " has been removed.")
    update()

def stats():
    print("Stats: ")
    print("Number of agents: " + str(len(agents)))
    p = 0
    print("Agents Present: " + str(p))
    print("Agents Absent: " + str(len(agents) - p))

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
    elif command == "update":
        update()
    elif command == "shape":
        print(agents.shape)
    elif command == "exit":
        break