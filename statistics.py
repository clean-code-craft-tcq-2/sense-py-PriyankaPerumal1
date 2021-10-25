class EmailAlert:
  emailSent = False
 
class LEDAlert:
  ledGlows = False

class StatsAlerter:
  def __init__(self,maxThreshold, alerts):
    self.maxThreshold = maxThreshold
    self.emailAlert = alerts[0]
    self.ledAlert = alerts[1]
    
  def checkAndAlert(self,numbers):
    computedStats = statistics.calculateStats(numbers)
    if(computedStats["max"] > self.maxThreshold):
      self.emailAlert.emailSent = True
      self.ledAlert.ledGlows = True
      
def calculateStats(numbers):
  computeStats = {}
  if(len(numbers)!=0):
    computeStats["min"] = min(numbers)
    computeStats["max"] = max(numbers)
    computeStats["avg"] = sum(numbers)/len(numbers)
  else: 
    computeStats["min"] = math.nan
    computeStats["max"] = math.nan
    computeStats["avg"] = math.nan
  return computeStats
