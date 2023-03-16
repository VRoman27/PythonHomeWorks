def find(path, text):
    print('\n'*100)
    data = open(path, 'r')
    for line in data:
        if line.split(' ')[1] == text:
            print(line)
            data.close()
            return
    print("Не найден!")
    data.close()
    print('\n')
