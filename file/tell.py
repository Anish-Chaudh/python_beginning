with open('file.txt', 'r') as file:
    # Move the file pointer to the 10th byte
    file.seek(10)
    print(file.tell())
    
    # Read the next 5 bytes from the current position
    data = file.read(5)
    
    print(data)