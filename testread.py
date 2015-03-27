def read_depots(file):
   depots = []
   depots_f = open(file)
   for line in depots_f:
    depots.append(line.rstrip())
   return depots
print (read_depots("depots.txt"))
