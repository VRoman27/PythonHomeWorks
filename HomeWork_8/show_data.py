def printAll(path):
    print('\n'*100)
    data = open(path, 'r')
    for line in data:
        print(line)
    data.close()
    print('\n')