from maat_forge import ForgeConfig, forge_campaign


def test_campaign_is_reproducible():
    config = ForgeConfig(events=100, fraud_rate=.1, seed=7)
    assert forge_campaign(config) == forge_campaign(config)


def test_ground_truth_matches_requested_rate():
    result = forge_campaign(ForgeConfig(events=100, fraud_rate=.12, seed=3, scenario="mule-network"))
    assert result["metrics"]["fraud_events"] == 12
    assert all("ground_truth_reason" in event for event in result["events"])


def test_manifest_proves_synthetic_origin():
    result = forge_campaign(ForgeConfig(events=20))
    assert result["manifest"]["synthetic_only"] is True
    assert len(result["manifest"]["dataset_sha256"]) == 64
