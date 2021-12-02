#day1


#part1
def main():
    increases = 0

    with open("input.txt") as file:
        contents = file.readlines()
    for i in range(0, len(contents) - 1):
        if eval(contents[i]) < eval(contents[i+1]):
            increases += 1
    print(increases)

if __name__ == "__main__":
    main()

#part2
def main():
    increases = 0

    with open("input.txt") as file:
        contents = file.readlines()
    for i in range(0, len(contents) - 3):
        if eval(contents[i]) + eval(contents[i+1]) + eval(contents[i+2]) < eval(contents[i+1]) + eval(contents[i+2]) + eval(contents[i+3]):
            increases += 1
    print(increases)

if __name__ == "__main__":
    main()