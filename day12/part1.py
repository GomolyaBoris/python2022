import re

def compute_sum(string):
    return sum([int(n) for n in re.findall("-?\d+", string)])


if __name__ == "__main__":
    with open("input.txt") as input:
        inp = input.readline()

        out = open("output1.txt", "w")
        out.write(str(compute_sum(inp)))
        out.close()
