
def calculateStats(numbers):
  computeStats = {}
  if(len(numbers)!=0):
    computeStats["min"] = min(numbers)
    computeStats["max"] = max(numbers)
    computeStats["avg"] = sum(numbers)/len(numbers)
  else: 
    computeStats["min"] = 0
    computeStats["max"] = 0
    computeStats["avg"] = 0
  return computeStats
