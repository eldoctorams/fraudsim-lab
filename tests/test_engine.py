import unittest
from maat_forge import ForgeConfig, forge_campaign

class EngineTests(unittest.TestCase):
    def test_reproducible(self):
        config=ForgeConfig(events=100,fraud_rate=.1,seed=7)
        self.assertEqual(forge_campaign(config),forge_campaign(config))
    def test_ground_truth(self):
        result=forge_campaign(ForgeConfig(events=100,fraud_rate=.12,seed=3,scenario="mule-network"))
        self.assertEqual(result["metrics"]["fraud_events"],12)
        self.assertTrue(all("ground_truth_reason" in event for event in result["events"]))
    def test_manifest(self):
        result=forge_campaign(ForgeConfig(events=20))
        self.assertTrue(result["manifest"]["synthetic_only"])
        self.assertEqual(len(result["manifest"]["dataset_sha256"]),64)
    def test_validation(self):
        with self.assertRaises(ValueError): forge_campaign(ForgeConfig(events=2))

if __name__=="__main__": unittest.main()
