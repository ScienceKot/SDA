init_path = input("Enter the path:")
for i in range(10, 1, -1):
    init_path = init_path.replace(i*"/", '/')
print("the normalised path is {}".format(init_path))