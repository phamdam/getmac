# Hệ thống đăng ký thiết bị mạng

## Yêu cầu
- Python 3.11
- Windows

## Cài đặt
1. Mở terminal tại thư mục project.
2. Chạy:
   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

## Cấu hình Google Sheets
1. Tạo Google Service Account và tải file JSON key về.
2. Chia sẻ Google Sheet với email của Service Account.
3. Lấy `GOOGLE_SHEET_ID` từ URL của bảng tính.

## Biến môi trường cần thiết
Trên Windows PowerShell:
```powershell
$env:GOOGLE_SERVICE_ACCOUNT_FILE = "C:\path\to\service-account.json"
$env:GOOGLE_SHEET_ID = "your_sheet_id_here"
$env:MIKROTIK_IP = "172.16.1.1"
$env:MIKROTIK_USER = ""
$env:MIKROTIK_PASS = ""
$env:API_URL = "http://127.0.0.1:8000/api/register-mac"
```
Nếu bạn muốn dùng nội dung JSON thay vì file:
```powershell
$env:GOOGLE_SERVICE_ACCOUNT_JSON = Get-Content "C:\path\to\service-account.json" -Raw
```

## Chạy backend server
```powershell
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Chạy client app
```powershell
python app.py
```

## Ghi chú
- Frontend sẽ tìm và hiển thị các địa chỉ MAC WiFi (BSSID) từ lệnh `netsh`.
- Người dùng chọn MAC và nhấn đăng ký.
- Backend kiểm tra qua Mikrotik API xem MAC đã tồn tại trong bảng DHCP lease chưa.
- Nếu chưa tồn tại, backend sẽ thêm MAC vào DHCP lease và lưu dữ liệu vào Google Sheet.
- Nếu MAC đã tồn tại, backend thông báo lại cho người dùng.
