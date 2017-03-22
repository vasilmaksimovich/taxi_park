t = 255000
CONS = 8

cost_fuel = 0
# r = t / 1000
base_repair = 5000
cost_base_repair = 500
cons = CONS
for i in xrange(t / 1000):
    cons = cons + (CONS * 0.01)
    cost_fuel = cost_fuel + (10 * cons)

# return (cons)
# return (cost_fuel)

print cons
print cost_fuel

cost_car = 10000

for i in xrange(t / 1000):

    if i == base_repair / 1000:
        cost_car = (cost_car - 9.5) + cost_base_repair
    else:
        cost_car = cost_car - 9.5
print cost_car





