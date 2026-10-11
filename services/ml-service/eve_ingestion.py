"""Parse, validate, and normalize Suricata EVE JSON Lines records."""

import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any


SCHEMA_VERSION = 1


def normalize_alert(event: dict[str, Any]) -> dict[str, Any]:
    """Normalize a validated Suricata alert and preserve its source event."""
    alert = event["alert"]

    return {
        "schema_version": SCHEMA_VERSION,
        "source": "suricata",
        "event_type": "alert",
        "timestamp": event.get("timestamp"),
        "flow_id": event.get("flow_id"),
        "src_ip": event.get("src_ip"),
        "src_port": event.get("src_port"),
        "dest_ip": event.get("dest_ip"),
        "dest_port": event.get("dest_port"),
        "protocol": event.get("proto"),
        "app_protocol": event.get("app_proto"),
        "signature_id": alert["signature_id"],
        "signature": alert.get("signature"),
        "severity": alert.get("severity"),
        "category": alert.get("category"),
        "action": alert.get("action"),
        "raw_event": event,
    }


def iter_eve_records(path: str | Path) -> Iterator[dict[str, Any]]:
    """Yield classified records and continue after invalid input lines."""
    with Path(path).open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue

            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                yield {
                    "line_number": line_number,
                    "status": "malformed",
                    "error": str(exc),
                    "event": None,
                    "normalized": None,
                }
                continue

            if not isinstance(event, dict):
                yield {
                    "line_number": line_number,
                    "status": "malformed",
                    "error": "JSON record must be an object",
                    "event": event,
                    "normalized": None,
                }
                continue

            event_type = event.get("event_type")
            if not isinstance(event_type, str) or not event_type.strip():
                yield {
                    "line_number": line_number,
                    "status": "malformed",
                    "error": "event_type must be a non-empty string",
                    "event": event,
                    "normalized": None,
                }
                continue

            if event_type != "alert":
                yield {
                    "line_number": line_number,
                    "status": "non_alert",
                    "error": None,
                    "event": event,
                    "normalized": None,
                }
                continue

            alert = event.get("alert")
            if not isinstance(alert, dict):
                yield {
                    "line_number": line_number,
                    "status": "malformed",
                    "error": "alert event must contain an alert object",
                    "event": event,
                    "normalized": None,
                }
                continue

            signature_id = alert.get("signature_id")
            if (
                not isinstance(signature_id, int)
                or isinstance(signature_id, bool)
                or signature_id <= 0
            ):
                yield {
                    "line_number": line_number,
                    "status": "malformed",
                    "error": "alert.signature_id must be a positive integer",
                    "event": event,
                    "normalized": None,
                }
                continue

            yield {
                "line_number": line_number,
                "status": "alert",
                "error": None,
                "event": event,
                "normalized": normalize_alert(event),
            }
