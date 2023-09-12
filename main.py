
def count_batteries_by_health(present_capacities):
  return {
    "healthy": list(range(83, 101)),
    "exchange": list(range(63, 83)),
    "failed": list(range(63))
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 72]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
