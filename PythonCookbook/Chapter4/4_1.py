with open('file.txt') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except:
        pass
