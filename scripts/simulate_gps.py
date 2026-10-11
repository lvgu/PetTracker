
import json
import math
import time
from datetime import datetime, timezone


DEVICE_ID = "pet-001"

# 仅用于演示的起始坐标
START_LATITUDE = 34.2600
START_LONGITUDE = 108.9420

# 模拟移动幅度，不代表真实运动速度
STEP = 0.0001


def generate_location(index: int) -> dict:
    """生成一条模拟定位数据。"""

    latitude = START_LATITUDE + STEP * math.sin(index / 5)
    longitude = START_LONGITUDE + STEP * index

    return {
        "device_id": DEVICE_ID,
        "latitude": round(latitude, 6),
        "longitude": round(longitude, 6),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def main():
    print("PetTracker 模拟定位程序启动")
    print("按 Ctrl+C 停止程序。\n")

    index = 0

    try:
        while True:
            location = generate_location(index)

            # 将定位数据转换为 JSON 字符串
            message = json.dumps(
                location,
                ensure_ascii=False
            )

            print(message)

            index += 1
            time.sleep(2)

    except KeyboardInterrupt:
        print("\n模拟定位程序已停止。")


if __name__ == "__main__":
    main()
