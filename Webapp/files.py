
# 'r' = opens file for reading, also 'r' is default value so u allowed not to pass it
# 'r' doesnt create file with given name if not exists, other modes create if file with given name dont exist
# 'w' open file for writing, if file have data then data is deleted
# 'a' opens file to append data, does not delete existing data.
# 'x' open new file for writing, Error in case file with given name already exists
# by default interpretator awaits text data(for example asci or utf-8)
# in case file have images, videos or something not text we have to say open file as a binary
# by appending 'b' to any mode. ('ab', 'wb' etc)
# by adding something like 'x+b' or 'a+b', 'r+a' in file mode u say that u want to read and write into file
# or write into binary file
todos = open('todos.txt', 'a')
print('feed the cat', file=todos)

print('kappa', file = todos)

todos.close()

tasks = open('todos.txt')

for chore in tasks:
    #print(chore)
    print(chore, end='')

tasks.close()

with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')



