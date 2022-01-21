class Category:
    def __init__(self, name):
        self.name = name.title()
        self.ledger = list()
        self.wallet = 0
    
    def __str__(self):
        title = ("*"*((30 - len(self.name)) // 2) + self.name + "*"*((30 - len(self.name)) // 2)) + "\n"
        for i in range(len(self.ledger)):
            title += "{:<23}".format(self.ledger[i]["description"][:23])
            title += "{:>7}".format(format(round(self.ledger[i]["amount"], 2),".2f")) + "\n"
        title += "Total: " + format(self.get_balance(), ".2f")
        return title

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.wallet += amount
    
    def get_balance(self):
        return round(self.wallet, 2)
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def withdraw(self, withdraw, description = ""):
        withdraw = -abs(withdraw)
        if self.check_funds(abs(withdraw)):
            self.wallet += withdraw
            self.ledger.append({"amount": withdraw, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + destination.name)
            destination.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

def create_spend_chart(categories):
    names = []
    soma = 0
    for i in categories:
        names.append(i.name)
        soma += round(i.ledger[0]["amount"] - i.wallet, 2)
    for i in range(len(names)):
        names[i] = names[i] + " "*(len(max(names,key=len)) - len(names[i]))
    title = "Percentage spent by category\n"
    for x in list(range(100,-1,-10)):
        title += "{:>3}".format(str(x)) + "| "
        for i in categories:
            perc = (int(round((i.ledger[0]["amount"] - i.wallet) / soma, 2) * 100))
            if i.name != names[len(names)-1].replace(" ", ""):
                if perc < x:
                    title += "   "
                else:
                    title += "o  "
            else:
                if perc < x:
                    title += "   \n"
                else:
                    title += "o  \n"
    title += "    -" + "-"*(3*len(names)) + "\n"
    for i in range(len(names[0])):
        for x in range(len(names)):
            if x == 0:
                title += "     " + names[x][i] + "  "
            elif x < (len(names) - 1):
                title += names[x][i] + "  "
            else:
                if i < (len(names[0]) - 1):
                    title += names[x][i] + "  \n"
                else:
                    title += names[x][i] + "  "
    return title

# Ran 11 tests in 0.001s =)