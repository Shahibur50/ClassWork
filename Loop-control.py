"""
Loop control version 1.1.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

# Pass
# Continue
# break

# A runner is practicing in a stadium and the coach is giving orders.

t = 180

for i in range(t, 1, -1):
	t = t - 5
	
	if t > 150:
		print("Time:", t, "| Do another lap.")
		continue
	if t > 120:
		print("Time:", t, "| You are improving your laptime!")
		pass
	if t < 105:
		print("Time:", t, "| Excellent, you have beaten the best runner's record!")
		break
print("")