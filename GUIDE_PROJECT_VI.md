**Hướng dẫn chi tiết - Project GetMac (Dành cho tự học Python)**

Mục tiêu: giải thích từng bước cài đặt, chạy và các luồng xử lý trong project này bằng tiếng Việt dễ hiểu, kèm chú giải cho các câu lệnh quan trọng trong mã.

**Tổng quan**:
- **Frontend/Client**: [app.py](app.py) — ứng dụng GUI đơn giản dùng `tkinter` để quét danh sách card WiFi và gửi yêu cầu đăng ký MAC tới backend.
- **Backend/API**: [main.py](main.py) — server FastAPI tiếp nhận yêu cầu, kiểm tra/đăng ký MAC vào Mikrotik DHCP và lưu log vào Google Sheets.
- **Test**: [tests/test_app.py](tests/test_app.py) — ví dụ unit test cho một vài hàm trong `app.py`.

**1) Chuẩn bị môi trường (chi tiết từng lệnh)**
- Mở terminal tại thư mục project.
- Tạo môi trường ảo và kích hoạt (Windows PowerShell):

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
``` 

- Lý do: môi trường ảo giữ các gói riêng cho project (tránh xung đột toàn hệ thống).
- Cài phụ thuộc:

```powershell
pip install -r requirements.txt
```

- Nếu cần đặt biến môi trường (ví dụ sử dụng Google Sheets và Mikrotik), chạy ví dụ sau trong PowerShell:

```powershell
$env:GOOGLE_SERVICE_ACCOUNT_FILE = "C:\path\to\service-account.json"
$env:GOOGLE_SHEET_ID = "your_sheet_id_here"
$env:MIKROTIK_IP = "172.16.1.1"
$env:MIKROTIK_USER = "admin"
$env:MIKROTIK_PASS = "password"
$env:API_URL = "http://127.0.0.1:8000/api/register-mac"
```

Giải thích: các biến này được `main.py` và `app.py` đọc bằng `os.getenv(...)` để cấu hình runtime.

**2) Luồng hoạt động (end-to-end)**
- Bước 1 (Client): chạy `python app.py` → ứng dụng GUI hiện lên. (Xem [README.md](README.md#L1-L50) hướng dẫn ngắn.)
- Bước 2 (Client): ứng dụng gọi `refresh_network_list()` — gọi `scan_wifi_macs()` để chạy lệnh hệ thống `netsh wlan show interfaces` (Windows) và parse kết quả.
  - Hàm `scan_wifi_macs()` sử dụng `subprocess.check_output(...)` để lấy output, duyệt từng dòng, tìm `Physical Address` và `Name` → chuẩn hóa MAC bằng `normalize_mac()`.
  - `normalize_mac(mac)`: xóa ký tự không cần thiết, chuyển thành định dạng `AA:BB:CC:DD:EE:FF` và chữ hoa.
- Bước 3 (Client): người dùng chọn MAC từ `Listbox` và nhập `Mã học sinh` → nhấn `Đăng ký MAC đã chọn` → hàm `submit_data()` tạo payload JSON `{"user_id": ..., "mac_address": ...}` và gửi `POST` tới `API_URL` (mặc định trong file: http://172.16.1.220:8000/api/register-mac).
- Bước 4 (Server): Endpoint `/api/register-mac` trong `main.py` nhận `ClientRequest` (Pydantic model), kiểm tra MAC:
  - Gọi `find_mac_in_mikrotik(mac)` để truy vấn Mikrotik DHCP lease (dùng `routeros_api`). Nếu đã tồn tại trả về message.
  - Nếu chưa, gọi `add_mac_to_mikrotik(mac, comment)` để thêm lease (gọi API Mikrotik).
  - Sau khi thêm, `append_registration_to_sheet(...)` lưu hàng mới vào Google Sheet (dùng `gspread` và Google service account credentials).
  - Hàm trả về JSON message cho client.

**3) Giải thích các câu lệnh, đoạn mã quan trọng (chi tiết)**

- `API_URL = os.getenv("API_URL", "http://172.16.1.220:8000/api/register-mac")`
  - `os.getenv` lấy biến môi trường; nếu không có thì dùng giá trị mặc định.

- `subprocess.check_output(cmd, shell=True, text=True)`
  - Chạy lệnh hệ thống và trả về chuỗi output. `shell=True` cho phép sử dụng chuỗi lệnh như trong shell; `text=True` trả về `str` thay vì `bytes`.
  - Cần xử lý ngoại lệ: `CalledProcessError` khi lệnh trả code khác 0.

- `requests.post(API_URL, json=payload, timeout=15)`
  - Gửi POST request với body JSON; `timeout` tránh treo lâu.

- Pydantic `BaseModel` (trong `main.py`):
  - `ClientRequest` tự động validate input JSON từ client, giúp đảm bảo trường `user_id` và `mac_address` tồn tại.

- `routeros_api.RouterOsApiPool(...)` và `api.get_resource('/ip/dhcp-server/lease')`
  - Kết nối tới Mikrotik và thao tác DHCP leases (thêm, list). Thao tác có thể ném exception nếu không kết nối được.

- `gspread.service_account(filename=...)` hoặc `Credentials.from_service_account_info(...)`
  - Xác thực với Google Sheets bằng Service Account. Nếu `GOOGLE_SERVICE_ACCOUNT_JSON` đặt trực tiếp dưới dạng string JSON thì `main.py` dùng `from_service_account_info`.

- `uvicorn main:app --host 0.0.0.0 --port 8000`
  - Lệnh chạy server FastAPI; `main:app` nghĩa là import `app` từ module `main`.

**4) Cấu trúc code và vị trí các luồng xử lý**
- Entry points:
  - Client GUI start: khi chạy `app.py`, cuối file có `refresh_network_list()` và `root.mainloop()` để khởi tạo giao diện.
  - Backend start: `uvicorn main:app ...` → exposes API endpoints sử dụng các hàm `find_mac_in_mikrotik`, `add_mac_to_mikrotik`, `append_registration_to_sheet`.

- Tách trách nhiệm (single responsibility):
  - `app.py` chịu giao diện và thu thập dữ liệu.
  - `main.py` chịu xác thực, truy vấn Mikrotik, lưu Google Sheet và trả kết quả cho client.

**5) Chạy test hiện có**
- Test hiện tại nằm ở `tests/test_app.py` và kiểm tra `normalize_mac` và `disable_random_mac_windows()`.
- Chạy test bằng `pytest` hoặc `python -m unittest`:

```powershell
pip install pytest
pytest -q
```

**6) Hướng dẫn debug nhanh**
- Client: chạy `python app.py` trong PowerShell, nếu lỗi về `requests` hoặc `netsh`, kiểm tra quyền (uac) và xem output trong terminal.
- Backend: chạy `uvicorn main:app --reload` để có hot-reload; kiểm tra logs console khi gọi API từ client.
- Nếu Google Sheets lỗi: kiểm tra `GOOGLE_SERVICE_ACCOUNT_FILE` và quyền chia sẻ sheet cho service account email.

**7) Gợi ý cải tiến/hãy thử**
- Thêm `argparse` cho `app.py` để override `API_URL` từ dòng lệnh.
- Tách logic Mikrotik vào module riêng `mikrotik.py` để dễ test/mock.
- Thêm unit tests cho `main.py` (mock `routeros_api` và `gspread`).

---
Nếu bạn muốn, mình sẽ:
- tạo PR skeleton cải tiến (ví dụ: `mikrotik.py`, `utils.py`) và test mock,
- hoặc chuyển hướng dẫn này thành `README-deep.md` hoặc PDF.
