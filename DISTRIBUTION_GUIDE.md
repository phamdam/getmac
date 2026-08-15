# Hướng dẫn Phân phối RegisterWiFiMAC

## 📦 Các Phiên bản Đã Đóng gói

### Windows - RegisterWiFiMAC.exe
- **Kích thước:** ~19.4 MB
- **Vị trí:** `dist/RegisterWiFiMAC.exe`
- **Trạng thái:** ✅ Đã xây dựng thành công
- **Yêu cầu:** Windows 7 hoặc cao hơn (x64/x86)

### macOS - RegisterWiFiMAC.app  
- **Vị trí:** `dist/RegisterWiFiMAC.app`
- **Yêu cầu:** macOS 10.13 hoặc cao hơn
- **Ghi chú:** Chưa được xây dựng trên Windows (cần chạy trên macOS)

---

## 🚀 Cách Sử dụng Cho Người Dùng

### Windows

1. **Tải về** tệp `RegisterWiFiMAC.exe`
2. **Nhấp đúp** để chạy ứng dụng
3. Không cần cài đặt gì thêm!

**Cấu hình API URL (tuỳ chọn):**
```batch
set API_URL=http://your-server:8000/api/register-mac
RegisterWiFiMAC.exe
```

### macOS

1. **Tải về** thư mục `RegisterWiFiMAC.app`
2. **Sao chép** vào thư mục `Applications` (tuỳ chọn)
3. **Nhấp đúp** hoặc chạy từ Terminal:
```bash
./RegisterWiFiMAC.app/Contents/MacOS/RegisterWiFiMAC
```

**Nếu gặp lỗi "damaged app":**
```bash
xattr -d com.apple.quarantine RegisterWiFiMAC.app
```

**Cấu hình API URL (tuỳ chọn):**
```bash
export API_URL=http://your-server:8000/api/register-mac
./RegisterWiFiMAC.app/Contents/MacOS/RegisterWiFiMAC
```

---

## 🔧 Xây Dựng Lại

### Windows
```batch
cd C:\path\to\GetMac
.\build-windows.bat
```

### macOS (chỉ chạy trên Mac)
```bash
cd /path/to/GetMac
chmod +x build-macos.sh
./build-macos.sh
```

---

## 📋 Cấu trúc Thư mục Xây Dựng

```
GetMac/
├── dist/
│   ├── RegisterWiFiMAC.exe          # ✅ Windows executable (19.4 MB)
│   └── RegisterWiFiMAC.app          # macOS app bundle (xây dựng trên Mac)
├── build/                           # Thư mục tạm thời
├── RegisterWiFiMAC-windows.spec     # Cấu hình xây dựng Windows
├── RegisterWiFiMAC-macos.spec       # Cấu hình xây dựng macOS
├── build-windows.bat                # Script xây dựng Windows
├── build-macos.sh                   # Script xây dựng macOS
├── app.py                           # Ứng dụng Windows
└── app_macos.py                     # Ứng dụng macOS
```

---

## ✅ Checklist Phân phối

- [x] Windows executable được tạo
- [ ] macOS app được tạo (cần xây dựng trên Mac)
- [ ] Kiểm tra chức năng trên cả hai nền tảng
- [ ] Đóng gói để phân phối
- [ ] Tạo hướng dẫn cho người dùng

---

## 🐛 Khắc phục Sự cố

### Windows
| Vấn đề | Giải pháp |
|-------|----------|
| "Cannot find module" | Chạy build lại từ thư mục chính xác |
| Ứng dụng chậm khởi động | Điều này là bình thường lần đầu |
| UAC warning | Có thể bỏ qua, ứng dụng vẫn hoạt động |

### macOS
| Vấn đề | Giải pháp |
|-------|----------|
| "Cannot be opened" | Chạy: `xattr -d com.apple.quarantine RegisterWiFiMAC.app` |
| Permission denied | Cấp quyền: `chmod +x RegisterWiFiMAC.app/Contents/MacOS/RegisterWiFiMAC` |
| Networksetup error | Chạy app với quyền admin hoặc từ trong folder Applications |

---

## 📊 Thông Tin Kỹ Thuật

**Công Cụ Đóng Gói:** PyInstaller 6.20.0  
**Phiên Bản Python:** 3.11.6  
**Kiểu Xây Dựng:** One-file executable  
**Ngày Xây Dựng:** 2026-08-14

### Các Thư Viện Được Bao Gồm
- requests (HTTP client)
- urllib3 (Advanced HTTP)
- certifi (SSL certificates)
- tkinter (GUI)
- subprocess (Command execution)
- Tất cả dependencies khác

---

## 📖 Hướng Dẫn Phân phối

### Tạo ZIP Distribution

**Windows:**
```batch
cd dist
tar -czf RegisterWiFiMAC-Windows.zip RegisterWiFiMAC.exe
```

**macOS:**
```bash
cd dist
zip -r RegisterWiFiMAC-macOS.zip RegisterWiFiMAC.app
```

### Đóng gói cho Release
1. Tạo thư mục release
2. Sao chép `dist/RegisterWiFiMAC.exe` cho Windows
3. Sao chép `dist/RegisterWiFiMAC.app` cho macOS (xây dựng trên Mac)
4. Thêm tệp `README.md` với hướng dẫn
5. Đóng gói thành ZIP và phân phối

---

## 🎯 Các Bước Tiếp Theo

1. **Xây dựng macOS:**
   - Chuyển dự án sang Mac
   - Chạy `./build-macos.sh`
   - Sao chép `dist/RegisterWiFiMAC.app` về Windows

2. **Kiểm tra chất lượng:**
   - Kiểm tra trên Windows và macOS
   - Kiểm tra kết nối API
   - Kiểm tra scanning WiFi

3. **Phân phối:**
   - Tạo bộ cài đặt (tuỳ chọn)
   - Tạo hướng dẫn người dùng
   - Xuất bản trên trang web

---

**Ghi chú:** Tài liệu này được cập nhật ngày 2026-08-14
