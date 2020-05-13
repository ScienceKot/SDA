target = int(input("Enter the wnated number by jack:"))
position = 0
jump_size = 1
jumps = 0
while target != position:
    if abs(target - position) < jump_size:
        position -= jump_size
    else:
        position += jump_size
    jump_size +=1
    jumps +=1
print(jumps)