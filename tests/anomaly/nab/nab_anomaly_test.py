import unittest2 as unittest
import json
import os


BENCHMARK_PATH = "tests/anomaly/nab/benchmark_results.json"
RESULTS_PATH = os.environ['NAB'] + "/results/final_results.json"
RUN_NAB_CMD = "python " + os.environ['NAB'] + \
  "/run.py -d numenta --detect --score --normalize --skipConfirmation"
EPS = 10e-2



class NABAnomalyTest(unittest.TestCase):
  """Regression tests for NAB on nupic."""



  def testNABScoresBenchmark(self):
    """Test that NAB on nupic produces expected scores."""

    # Run NAB nupic
    os.system(RUN_NAB_CMD)

    with open(BENCHMARK_PATH) as benchmarkFile:
      benchmarkData = json.load(benchmarkFile)

    with open(RESULTS_PATH) as resultsFile:
      resultsData = json.load(resultsFile)

    for benchmarkName in benchmarkData["numenta"]:
      benchmarkValue = benchmarkData["numenta"][benchmarkName]
      resultValue = resultsData["numenta"][benchmarkName]
      self.assertAlmostEqual(benchmarkValue, resultValue, delta=EPS)


if __name__ == "__main__":
  unittest.main()
