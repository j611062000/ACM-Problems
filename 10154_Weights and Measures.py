"""
1. min weight
2. net_strength >= dp[-1]
"""

import re


class turtle():

    def __init__(self, weight, net_strength, strength):
        self.weight = weight
        self.net_strength = net_strength
        self.strength = strength


# weight / strength
with open("10154_Weights and Measures_data.txt", "r") as file:
    data = file.readlines()
    p = re.compile(r'\d+')
    turtles = []

    for element in data:
        temp = list(map(int, p.findall(element)))
        # construct a list containing element of (weight, strength)
        turtles.append(turtle(temp[0], temp[1] - temp[0], temp[1]))


turtles.sort(key=lambda x: (x.strength, x.weight))
print("turtles (weight/strength)= {}".format(
    [(x.weight, x.strength) for x in turtles]))
# dp[i]: the minimal weight of piling i turtles

dp = [0]
for i in range(len(turtles)):
    dp.append(float("inf"))
print("dp = {}\n".format(dp))

chosen_turtles = []
max_turtles = 0

for turtle in turtles:
    print("\n")
    print("turtle = {!s:<9} with net_strength {}:".format((turtle.weight, turtle.strength), turtle.net_strength))
    for i in range(len(dp), 1, -1):
        if turtle.net_strength >= dp[i - 2] and turtle.weight < dp[i - 1] - dp[i - 2]:
            dp[i - 1] = dp[i - 2] + turtle.weight
            print("dp[{}] is revised,dp = {}".format(i - 1, dp))
        if dp[i - 1] != float("inf"):
            max_turtles = max(max_turtles, i - 1)


print(max_turtles)
"""
[Pseudocode]
Input: n pairs of integer
  
class turtle:
  int weight, strength, net_weight

/* If 2 turtles have the same strenght, then we sort them by their weight. */
turtle turtles[n] := stores the turtles which have been sorted by their strength in ascending order

dp[0] := 0
dp[1] ~ dp[n] := infinite

for <turtle in turtles> do:
    for <i from n to 1> do:

        if <turtle.net_strength >= dp[i - 1] and turtle.weight < dp[i] - dp[i - 1]> do
            dp[i] = dp[i - 1] + turtle.weight
        Endif
        
    Endfor
Endfor

for <i frome 1 to n> do:
    if dp[i] == inf:
        ans = i
        break for
    Endif
Endfor

Output: ans
"""
