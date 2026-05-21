import os
dirs=os.walk(os.getcwd())
print(list(dirs))
"""for r,d,f, in dirs:
    for ds in d:
        print(os.path.join(r,ds))
    for fs in f:
        print(os.path.join(r,fs))"""