import os

print('Hello github')
x = range(0, 100)

for i in x:
    if i % 3:
        print(i)
        
print()
print(f'CPU count: {os.cpu_count()}')