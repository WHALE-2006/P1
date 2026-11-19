import random
from datetime import datetime


def generate_lucky_summary() -> None:
    """Print a quick random demo summary."""
    numbers = random.sample(range(1, 50), 6)
    moods = ["Tập trung", "Hào hứng", "Bình tĩnh", "text"]

    print(f"=== Antigravity Demo ({datetime.now():%H:%M:%S}) ===")
    print(f"6 số ngẫu nhiên: {sorted(numbers)}")
    print(f"Trạng thái gợi ý: {random.choice(moods)}")


if __name__ == "__main__":
    generate_lucky_summary()
