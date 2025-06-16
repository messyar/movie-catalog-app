import logging
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent
STORE_PATH = BASE_PATH / "store.json"


LOG_LEVEL = logging.INFO
LOG_FORMAT: str = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)


# Never store tokens
API_TOKENS = frozenset(
    {
        "zlHCGvRtlNqjmdp08xNQhQ",
        "psEUzh3ASZ_zULxUG9k8_w",
    }
)
