def getInputLines(filename):
    with open(filename) as input_file:
        lines = []
        for line in input_file.readlines():
            lines.append(line.strip())
    return lines