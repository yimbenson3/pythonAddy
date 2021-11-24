from datetime import datetime, timezone

def getCurrentTimestamp():
    return str(datetime.now(timezone.utc))
