import time
import re
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Cấu hình trình duyệt Edge
edge_options = Options()
edge_options.add_argument("--start-maximized")
service = Service(executable_path="C:/Users/vu090/Downloads/edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_options)

# Mở TikTok và chờ trang tải xong
driver.get("https://www.tiktok.com/")
time.sleep(1)  # Điều chỉnh thời gian chờ nếu cần

# Hàm lấy thời gian còn lại của video
def get_remaining_time():
    try:
        # Tìm phần tử chứa thời gian video
        time_element = driver.find_element(By.XPATH, '//div[contains(@class, "tiktok-1g3unbt-DivSeekBarTimeContainer")]')
        time_text = time_element.text.strip()
        # Sử dụng biểu thức chính quy để tách thời gian còn lại
        match = re.match(r'(\d{2}):(\d{2})/(\d{2}):(\d{2})', time_text)
        if match:
            minutes_left = int(match.group(1))
            seconds_left = int(match.group(2))
            total_seconds_left = minutes_left * 60 + seconds_left
            return total_seconds_left
        else:
            return 5  # Trả về 5 giây nếu không lấy được thời gian
    except Exception as e:
        print(f"Lỗi khi lấy thời gian: {e}")
        return 5  # Trả về 5 giây nếu gặp lỗi

# Vòng lặp tự động lướt video
while True:
    try:
        remaining_time = get_remaining_time()
        print(f"Đang xem video trong {remaining_time} giây...")
        time.sleep(remaining_time + 2)  # Thêm 2 giây để chuyển sang video tiếp theo
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ARROW_RIGHT)  # Gửi phím mũi tên phải để chuyển video
        print(">> Chuyển video")
    except KeyboardInterrupt:
        print("Dừng lại")
        break
    except Exception as e:
        print(f"Lỗi: {e}")
        break

driver.quit()
