from collections import defaultdict
from time import time

request_log = defaultdict(list)

RATE_LIMIT = 10
WINDOW = 60

def is_rate_limited(ip: str):
    current_time = time()

    request_log[ip] = [
        t for t in request_log[ip]
        if current_time - t < WINDOW
    ]

    if len(request_log[ip]) >= RATE_LIMIT:
        return True

    request_log[ip].append(current_time)
    return False
