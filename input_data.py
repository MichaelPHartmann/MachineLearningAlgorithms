with open("cars.csv", "r") as f:
    lines = f.readlines()

with open("cars_data.csv", "w+") as c:
    for i, line in enumerate(lines):
        split_line = line.split(";")
        split_line[-1] = split_line[-1].strip("\n")
        if i == 0:
            split_line.append("Location Code")
        elif i == 1:
            continue
        else:
            if split_line[-1] == "US":
                split_line.append("1")
            elif split_line[-1] == "Europe":
                split_line.append("2")
            elif split_line[-1] == "Japan":
                split_line.append("3")
            else:
                split_line.append("0")
        split_line.append("\n")
        line_to_write = ",".join(split_line)
        c.write(line_to_write)
