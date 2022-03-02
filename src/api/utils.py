from datetime import datetime
from json import JSONEncoder
from typing import Any


class DatetimeEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):
            return str(o)
        return JSONEncoder.default(self, o)
