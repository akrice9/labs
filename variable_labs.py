import math
carrying_weight_percentage = 1/3
coconut_weight = 1450
macaw_weight = 900
macaw_limit = macaw_weight * carrying_weight_percentage
number_macaws = coconut_weight/macaw_limit
print("you need " + str(math.ceil(number_macaws)) + " macaws to carry a coconut.")

crane_weight = 1900
crane_limit = crane_weight * carrying_weight_percentage
number_cranes = coconut_weight/crane_limit
print("you need " + str(math.ceil(number_cranes)) + " cranes to carry a coconut.")

crane_machine_weight = 12000000
number_cranes = crane_machine_weight/crane_limit
print("you need " + str(math.ceil(number_cranes)) + " cranes to carry a crane.")

ant_weight = 0.06
ant_limit = ant_weight * 20
number_ants = coconut_weight/ant_limit
print("you need " + str(math.ceil(number_ants)) + " ants to carry a coconut.")