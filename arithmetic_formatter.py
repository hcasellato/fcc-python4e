import re
def arithmetic_arranger(problems, answer = False):
    top   = []
    bot   = []
    line  = []
    a     = []
    final = ""
    # Test lenght
    if len(problems) > 5:
        return "Error: Too many problems."
    for i in range(len(problems)):
        # Split
        split = re.split(pattern="\s", string=problems[i])
        # Test if number
        if (split[0].isnumeric() and split[2].isnumeric()) == False:
            return "Error: Numbers must only contain digits."
        # Test if longer than 4 digits
        if len(split[0]) > 4 or len(split[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        t     = len(split[0])
        b     = len(split[2])
        # Test operands
        if split[1] == "+":
            op = str(int(split[0]) + int(split[2]))
        elif split[1] == "-":
            op = str(int(split[0]) - int(split[2]))
        else:
            return "Error: Operator must be '+' or '-'."
        if t >= b:
            top.append(" "*2 + split[0])
            bot.append(split[1] + " " + " "*abs(t - b) + split[2])
            line.append("-"*(t + 2))
            a.append(" "*abs(t + 2 - len(op)) + op)
        else:
            top.append(" "*abs(b - t + 2) + split[0])
            bot.append(split[1] + " " + split[2])
            line.append("-"*(b + 2))
            a.append(" "*abs(b - len(op) + 2) + op)
    for x in range(len(top)):
        if x < (len(top) - 1):
            final += top[x] + "    "
        else:
            final += top[x] + "\n"
    for x in range(len(bot)):
        if x < (len(bot) - 1):
            final += bot[x] + "    "
        else:
            final += bot[x] + "\n"
    for x in range(len(line)):
        if x < (len(line) - 1):
            final += line[x] + "    "
        else:
            if answer == True:
                final += line[x] + "\n"
            else:
                final += line[x]
    if answer == True:
        for x in range(len(a)):
            if x < (len(a) - 1):
                final += a[x] + "    "
            else:
                final += a[x]
    return final

# Ran 10 tests in 0.08s =)