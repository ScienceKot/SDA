history = input().upper()
R_count = history.count('R')
if R_count == history.count('L') and R_count == history.count('U') and R_count == history.count('D'):
    print('BUG')
else:
    print('OK')