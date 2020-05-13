# This will be uset t ostore the chat users a moment of time
chat_users = set([])
traffic = 0
# Reading the file
f = open('5A.txt', 'r')
for line in f:
    if '+' in line:
        # Adding a person to the chat
        chat_users.add(line.replace('+', '')[:-1])
    elif '-' in line:
        # Removing a person from the chat
        chat_users.remove(line.replace('-', '')[:-1])
    elif ':' in line:
        # Adding traffic
        traffic += len(line[line.index(':')+1:-1]) * len(chat_users)
print(traffic)