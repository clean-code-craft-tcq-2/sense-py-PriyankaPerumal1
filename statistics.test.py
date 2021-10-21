import unittest
import statistics
import math

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
  
class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Design the assert here.
    self.assertFalse(math.isnan(computedStats["avg"]))
    self.assertFalse(math.isnan(computedStats["max"]))
    self.assertFalse(math.isnan(computedStats["min"]))
    # Use nan and isnan in https://docs.python.org/3/library/math.html

  def test_raise_alerts_when_max_above_threshold(self):
    emailAlert = EmailAlert()
    ledAlert = LEDAlert()
    maxThreshold = 10.5
    statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
    statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
    self.assertTrue(emailAlert.emailSent)
    self.assertTrue(ledAlert.ledGlows)

if __name__ == "__main__":
  unittest.main()
