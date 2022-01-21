import random
class Hat:
    def __init__(self, **contents):
        self.contents = []
        for x, q in contents.items():
            for i in range(0,q):
                self.contents.append(x)
    def draw(self, draw):
        if draw > len(self.contents):
            self.contents = self.contents
        else:
            e = random.sample(self.contents, k=draw)
            for l in range(draw):
                self.contents.remove(e[l])
        return e

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    all = hat.contents
    if num_balls_drawn > len(all): # Dirtiest if statement that I ever wrote :(
        num_balls_drawn = len(all)
    exp = []
    good = 0
    for x, q in expected_balls.items():
            for i in range(0,q):
                exp.append(x)
    exp.sort()
    for e in range(num_experiments):
        fu = random.sample(all, k=num_balls_drawn)
        fu.sort()
        t = 0
        set_exp = list(set(exp))
        set_exp.sort()
        set_fu = list(set(fu))
        set_fu.sort()
        if len(set_exp) <= len(set_fu):
            for l in set_exp:
                c_exp = exp.count(l)
                c_fu  = fu.count(l)
                if c_exp <= c_fu:
                    t += 1
            if t == len(list(set(exp))):
                good += 1
    return good/num_experiments

# Ran 3 tests in 0.020s XD