"""Unit tests for the Suricata EVE ingestion module."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "services" / "ml-service"),
)

from eve_ingestion import iter_eve_records, normalize_alert  # noqa: E402


class EveIngestionTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.path = Path(self.temp_dir.name) / "events.jsonl"

    def write_events(self, lines):
        self.path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return list(iter_eve_records(self.path))

    def valid_alert(self):
        return {
            "event_type": "alert",
            "timestamp": "2026-10-12T10:00:00.000000+0000",
            "flow_id": 12345,
            "src_ip": "192.0.2.10",
            "src_port": 53000,
            "dest_ip": "192.0.2.53",
            "dest_port": 53,
            "proto": "UDP",
            "app_proto": "dns",
            "alert": {
                "signature_id": 9900001,
                "signature": "Synthetic test alert",
                "severity": 3,
                "category": "test",
                "action": "allowed",
            },
        }

    def test_normalizes_valid_alert_and_preserves_raw_event(self):
        event = self.valid_alert()
        normalized = normalize_alert(event)

        self.assertEqual(normalized["schema_version"], 1)
        self.assertEqual(normalized["source"], "suricata")
        self.assertEqual(normalized["signature_id"], 9900001)
        self.assertEqual(normalized["protocol"], "UDP")
        self.assertEqual(normalized["app_protocol"], "dns")
        self.assertEqual(normalized["raw_event"], event)

    def test_classifies_non_alert_event(self):
        results = self.write_events([
            json.dumps({"event_type": "dns"})
        ])
        self.assertEqual(results[0]["status"], "non_alert")
        self.assertIsNone(results[0]["normalized"])

    def test_reports_malformed_json_and_continues(self):
        event = self.valid_alert()
        results = self.write_events([
            "{broken json",
            json.dumps(event),
        ])

        self.assertEqual(results[0]["status"], "malformed")
        self.assertEqual(results[0]["line_number"], 1)
        self.assertEqual(results[1]["status"], "alert")

    def test_rejects_non_object_json(self):
        results = self.write_events(['["not", "an", "object"]'])
        self.assertEqual(results[0]["status"], "malformed")
        self.assertEqual(results[0]["error"], "JSON record must be an object")

    def test_rejects_missing_or_blank_event_type(self):
        results = self.write_events([
            json.dumps({}),
            json.dumps({"event_type": " "}),
        ])
        self.assertEqual(
            [result["status"] for result in results],
            ["malformed", "malformed"],
        )

    def test_rejects_missing_or_invalid_alert_object(self):
        events = [
            {"event_type": "alert"},
            {"event_type": "alert", "alert": []},
        ]
        results = self.write_events([json.dumps(event) for event in events])
        self.assertEqual(
            [result["status"] for result in results],
            ["malformed", "malformed"],
        )

    def test_rejects_invalid_signature_ids(self):
        invalid_ids = [None, "123", True, 0, -1, 1.5]
        lines = [
            json.dumps({
                "event_type": "alert",
                "alert": {"signature_id": signature_id},
            })
            for signature_id in invalid_ids
        ]
        results = self.write_events(lines)
        self.assertTrue(
            all(result["status"] == "malformed" for result in results)
        )

    def test_accepts_positive_integer_signature_id(self):
        event = {
            "event_type": "alert",
            "alert": {"signature_id": 123},
        }
        results = self.write_events([json.dumps(event)])
        self.assertEqual(results[0]["status"], "alert")
        self.assertEqual(results[0]["normalized"]["signature_id"], 123)

    def test_preserves_parsed_event_on_semantic_error(self):
        event = {"event_type": "alert"}
        results = self.write_events([json.dumps(event)])
        self.assertEqual(results[0]["status"], "malformed")
        self.assertEqual(results[0]["event"], event)

    def test_missing_optional_fields_are_none(self):
        event = {
            "event_type": "alert",
            "alert": {"signature_id": 123},
        }
        normalized = normalize_alert(event)

        self.assertIsNone(normalized["timestamp"])
        self.assertIsNone(normalized["src_ip"])
        self.assertIsNone(normalized["dest_port"])
        self.assertIsNone(normalized["severity"])


if __name__ == "__main__":
    unittest.main()
