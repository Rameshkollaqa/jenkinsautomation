
import csv
import math
import sys

JTL_FILE = sys.argv[1] if len(sys.argv) > 1 else "results.jtl"

MAX_P95_MS = 3000
MAX_ERROR_RATE_PERCENT = 1.0

response_times = []
total_requests = 0
failed_requests = 0

with open(JTL_FILE, newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    if not reader.fieldnames or not {
        "elapsed", "success"
    }.issubset(reader.fieldnames):
        raise ValueError(
            "JTL must be CSV with elapsed and success columns."
        )

    for row in reader:
        total_requests += 1
        response_times.append(int(row["elapsed"]))

        if row["success"].strip().lower() != "true":
            failed_requests += 1

if total_requests == 0:
    print("FAIL: No requests found in the JTL file.")
    sys.exit(1)

response_times.sort()
p95_index = math.ceil(0.95 * total_requests) - 1
p95_ms = response_times[p95_index]

error_rate = failed_requests / total_requests * 100

print(f"Total requests: {total_requests}")
print(f"Failed requests: {failed_requests}")
print(f"Error rate: {error_rate:.2f}%")
print(f"P95 response time: {p95_ms} ms")

passed = (
    p95_ms < MAX_P95_MS
    and error_rate < MAX_ERROR_RATE_PERCENT
)

if passed:
    print("SLA RESULT: PASS")
    sys.exit(0)
else:
    print("SLA RESULT: FAIL")
    sys.exit(1)