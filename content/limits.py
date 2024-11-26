import time


def check_rate_limit(headers):
    remaining = int(headers.get('X-RateLimit-Remaining', 0))
    if remaining == 0:
        reset_time = int(headers.get('X-RateLimit-Reset', time.time()))
        sleep_time = reset_time - time.time()
        time.sleep(sleep_time)
