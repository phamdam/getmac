# README (Chi tiết) - Project GetMac

Phiên bản mở rộng của hướng dẫn, mục tiêu giúp bạn hiểu sâu code, luồng xử lý và cách chạy/chỉnh sửa dự án.

## Tổng quan project
- Frontend/Client: `app.py` — GUI Tkinter quét MAC WiFi và gửi yêu cầu đăng ký.
- Backend/API: `main.py` — FastAPI, kết nối Mikrotik và Google Sheets.
- Test: `tests/test_app.py` — unit tests mẫu cho `app.py`.

---

## 1) Chuẩn bị môi trường (chi tiết từng lệnh)

1. Mở terminal tại thư mục project.
2. Tạo môi trường ảo và kích hoạt (Windows PowerShell):

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Cài phụ thuộc:

```powershell
pip install -r requirements.txt
```

4. (Nếu cần) đặt biến môi trường trong PowerShell:

```powershell
$env:GOOGLE_SERVICE_ACCOUNT_FILE = "C:\path\to\service-account.json"
$env:GOOGLE_SHEET_ID = "your_sheet_id_here"
$env:MIKROTIK_IP = "172.16.1.1"
$env:MIKROTIK_USER = "admin"
$env:MIKROTIK_PASS = "password"
$env:API_URL = "http://127.0.0.1:8000/api/register-mac"
```

Ghi chú: `os.getenv(...)` trong code sẽ đọc các giá trị này nếu có.

---

## 2) Luồng hoạt động (end-to-end)

1. Chạy backend:

```powershell
uvicorn main:app --host 0.0.0.0 --port 8000
```

2. Chạy client GUI:

```powershell
python app.py
```

3. Client: `app.py` thực hiện:
- Gọi `refresh_network_list()` → `scan_wifi_macs()` → chạy `netsh wlan show interfaces` và parse output.
- Chuẩn hóa MAC bằng `normalize_mac()`.
- Người dùng chọn MAC và nhập `Mã học sinh`, nhấn đăng ký → `submit_data()` gửi `POST` tới `API_URL`.

4. Server: `main.py` xử lý POST `/api/register-mac`:
- Validate input bằng Pydantic `ClientRequest`.
- Kiểm tra Mikrotik bằng `find_mac_in_mikrotik()`.
- Nếu không tồn tại: gọi `add_mac_to_mikrotik()` để thêm lease và `append_registration_to_sheet()` để lưu vào Google Sheet.

---

## 3) Giải thích các đoạn mã & lệnh quan trọng

- `os.getenv("API_URL", "http://...")`: lấy cấu hình từ biến môi trường, có giá trị mặc định.
- `subprocess.check_output(..., shell=True, text=True)`: chạy lệnh hệ thống, trả chuỗi. `shell=True` chạy qua shell (cẩn thận với injection nếu dùng input không tin cậy).
- `requests.post(API_URL, json=payload, timeout=15)`: gửi HTTP POST với body JSON.
- `Pydantic BaseModel`: validate dữ liệu đầu vào cho endpoint (tự động parse và kiểm tra kiểu).
- `routeros_api.RouterOsApiPool(...)`: kết nối và thao tác Mikrotik RouterOS API.
- `gspread.service_account(...)` hoặc `Credentials.from_service_account_info(...)`: xác thực Google Sheets bằng Service Account.

---

## 4) Cấu trúc code và best-practices hiện tại

- Entry points:
  - `app.py`: GUI start — cuối file có `refresh_network_list()` và `root.mainloop()`.
  - `main.py`: server start via `uvicorn main:app`.
- Tách trách nhiệm: GUI thu thập và gửi; server validate, tương tác Mikrotik, ghi Google Sheet.

Best-practices gợi ý:
- Tách logic mạng/Mikrotik vào module riêng (`mikrotik.py`) để dễ test.
- Thêm `argparse` cho `app.py` để override `API_URL` khi chạy.
- Viết unit test cho `main.py` bằng cách mock `routeros_api` và `gspread`.

---

## 5) Chạy test

1. Cài pytest (nếu chưa có):

```powershell
pip install pytest
```

2. Chạy test:

```powershell
pytest -q
```

Ghi chú: Test mẫu `tests/test_app.py` kiểm tra `normalize_mac` và hành vi khi `subprocess.check_output` ném exception.

---

## 6) Debugging nhanh

- Client:
  - Nếu không thấy danh sách MAC: kiểm tra quyền chạy `netsh` (chạy PowerShell với quyền Admin).
  - Kiểm tra output lỗi in ra terminal (app.py in `print(...)`) và hộp thoại messagebox.
- Server:
  - Chạy `uvicorn main:app --reload` để bật auto-reload.
  - Kiểm tra logs console; endpoint admin `/` có giao diện giúp xem logs và bảng MAC lưu trên Google Sheet.

---

## 7) Xuất PDF từ Markdown (tùy chọn)

1. Cài Pandoc: https://pandoc.org/installing.html
2. Chạy lệnh chuyển:

```powershell
pandoc README-deep.md -o README-deep.pdf
```

Hoặc dùng VS Code extension "Markdown PDF" để xuất nhanh.

---

## 8) Gợi ý phát triển tiếp

- Tách `mikrotik` logic sang `mikrotik.py` và viết wrapper có interface rõ ràng để mock trong test.
- Thêm endpoint health-check và authentication cho admin.
- Viết pipeline CI (GitHub Actions) để chạy `pytest` và static checks (`flake8`/`ruff`).

---

Nếu bạn muốn, mình sẽ tự động tạo các file hỗ trợ (ví dụ: `mikrotik.py` skeleton, tests mock, và GitHub Actions workflow). Yêu cầu tiếp theo là gì?