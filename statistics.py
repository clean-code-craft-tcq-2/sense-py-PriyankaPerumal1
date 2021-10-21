
def calculateStats(numbers):
  computeStats = {}
  if(len(numbers)!=0):
    computeStats["min"] = min(numbers)
    computeStats["max"] = max(numbers)
    computeStats["avg"] = sum(numbers)/len(numbers)
  return computeStats
