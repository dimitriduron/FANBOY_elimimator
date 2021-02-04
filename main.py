# Start of File
# imported files/modules
# I'm going to put "import re" here later after we go over re in lecture, if not then this is my pre-re code

# Start of main function
if __name__ == '__main__':
    # replace file "input.txt" with whatever file you want to read from
    file = open("input.txt", "r")   # opens file to read
    line = file.read()
    file.close()                    # closes the file
    revised_lines = []

    while True:
        i = 0
        while line[i] != ",":                       # finds the comma that will separate the different lines
            i += 1
            if line[i] == ".":
                break
        revised_lines.append(line[0:i])
        line = line[i:]
        if line[0] == '.':
            break
        space_count = 0
        i = 0
        while space_count < 2:
            if line[i] == " ":
                space_count += 1
            i += 1
        line = line[i:]
    revised_lines[-1] = revised_lines[-1] + "."     # will fix the last line not having a period

    # outputs the end result of the file, as suggested by assignment
    count = 1
    for x in revised_lines:
        print(str(count) + ": " + x)
        count += 1
# End of File
