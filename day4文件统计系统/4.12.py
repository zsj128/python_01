import os
print(os.getcwd())
print(os.listdir(os.getcwd()))
for i in os.listdir(os.getcwd()):
    if os.path.isfile and i.endswith('.py'):
        print(i)
"""l=[f for f in os.listdir(os.getcwd()) if os.path.isfile and f.endswith('.py')]
print(l)"""