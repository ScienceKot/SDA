n, m = tuple(input().split())
n, m = int(n), int(m)
cmd = []
for i in range(n):
    command = input()
    cmd.append(command)
memory = [0 for i in range(m)]
done = 1
for c in cmd:
    if 'alloc' in c:
        value = int(c.split()[1])
        if memory.count(0) >= value:
            while True:
                if value == 0:
                    break
                else:
                    memory[memory.index(0)] = 1
                    value -=1
            print(done)
            done+=1
        else:
            print("NULL")
    if 'erase' in c:
        value = int(c.split()[1])
        if value >=len(memory):
            print("ILLEGAL_ERASE_ARGUMENT")
        else:
            memory[value] == 0
    if c == 'defragment':
        zeros = memory.count(0)
        ones = memory.count(1)
        memory = []
        for i in range(ones):
            memory.append(1)
        for i in range(zeros):
            memory.append(0)