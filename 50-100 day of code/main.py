with open('myfile.txt', 'r') as f:
    i = 0
    for line in f:
        line = line.strip()
        if not line:          # skip blank lines
            continue

        i += 1
        parts = line.split(",")

        if len(parts) >= 3:
            m1 = parts[0].strip()
            m2 = parts[1].strip()
            m3 = parts[2].strip()

            print(f"Marks of student {i} in math is : {m1}")
            print(f"Marks of student {i} in science is : {m2}")
            print(f"Marks of student {i} in english is : {m3}")
            print()
        else:
            print("Invalid line:", line)