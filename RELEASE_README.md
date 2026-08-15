# RegisterWiFiMAC - Version 1.0.0

**Ứng dụng Đăng ký MAC WiFi cho Hệ Thống Mạng Trường Học**

![Status](https://img.shields.io/badge/Status-Production%20Ready-green)
![Windows](https://img.shields.io/badge/Windows-7%2B-blue)
![macOS](https://img.shields.io/badge/macOS-10.13%2B-black)
![Python](https://img.shields.io/badge/Built%20with-Python%203.11-blue)

---

## 🎯 Mục Đích

Ứng dụng này giúp học sinh đăng ký địa chỉ MAC của thiết bị WiFi để có thể kết nối với mạng trường học một cách nhanh chóng và dễ dàng.

## ✨ Tính Năng

- ✅ **Phát hiện tự động** tất cả card WiFi trong thiết bị
- ✅ **Giao diện đơn giản** dễ sử dụng
- ✅ **Hỗ trợ Windows và macOS**
- ✅ **Không cần cài đặt** - chỉ cần tải và chạy
- ✅ **Đóng gói hoàn chỉnh** - tất cả thư viện được bao gồm
- ✅ **Bảo mật** - dữ liệu được gửi đến server an toàn

---

## 📦 Tải Về

### Phiên Bản Windows
- **Tệp:** `RegisterWiFiMAC.exe`
- **Kích thước:** ~19.4 MB
- **Yêu cầu:** Windows 7 hoặc cao hơn

**Cách dùng:** Tải về, nhấp đúp và chạy!

### Phiên Bản macOS
- **Tệp:** `RegisterWiFiMAC.app`
- **Kích thước:** ~19.4 MB  
- **Yêu cầu:** macOS 10.13 hoặc cao hơn

**Cách dùng:** Tải về, nhấp đúp và chạy!

---

## 🚀 Cách Sử Dụng

### Windows

```
1. Tải RegisterWiFiMAC.exe
2. Nhấp đúp trên tệp
3. Nhập mã học sinh
4. Chọn card WiFi
5. Nhấp "Đăng ký MAC đã chọn"
6. Chờ thông báo thành công!
```

### macOS

```
1. Tải RegisterWiFiMAC.app
2. Nhấp đúp trên thư mục app
3. Nhập mã học sinh
4. Chọn card WiFi
5. Nhấp "Đăng ký MAC đã chọn"
6. Chờ thông báo thành công!
```

---

## ❓ FAQ

**Q: Cần cài đặt gì không?**  
A: Không! Chỉ cần tải tệp và chạy.

**Q: Có an toàn không?**  
A: Có! Ứng dụng chỉ đọc MAC address và gửi tới server.

**Q: Tại sao cần quyền Admin?**  
A: Để kiểm soát cài đặt WiFi trên thiết bị của bạn.

**Q: Làm sao nếu không thấy card WiFi?**  
A: Nhấp "Làm mới danh sách MAC WiFi" hoặc khởi động lại ứng dụng.

---

## 📋 Yêu Cầu Hệ Thống

| Yêu Cầu | Windows | macOS |
|---------|---------|-------|
| Hệ điều hành | Windows 7+ | macOS 10.13+ |
| Dung lượng | 50 MB | 50 MB |
| Bộ nhớ | 256 MB | 256 MB |
| Internet | Có | Có |

---

## 🐛 Khắc Phục Sự Cố

### Windows

| Lỗi | Giải pháp |
|-----|----------|
| "File không tìm thấy" | Kiểm tra đường dẫn tệp |
| "Access Denied" | Chạy với quyền Admin |
| Ứng dụng chậm khởi động | Điều này là bình thường lần đầu |

### macOS

| Lỗi | Giải pháp |
|-----|----------|
| "Cannot be opened" | Chạy: `xattr -d com.apple.quarantine RegisterWiFiMAC.app` |
| "Permission denied" | Cấp quyền cho ứng dụng |
| WiFi không phát hiện | Kiểm tra WiFi đã bật chưa |

---

## 📖 Tài Liệu

- 📘 [Hướng Dẫn Sử Dụng Chi Tiết](USER_GUIDE.md)
- 📗 [Hướng Dẫn Xây Dựng](BUILD_GUIDE.md)
- 📕 [Hướng Dẫn Phân Phối](DISTRIBUTION_GUIDE.md)

---

## 🔧 Chi Tiết Kỹ Thuật

### Build Info
- **Công cụ:** PyInstaller 6.20.0
- **Phiên bản Python:** 3.11.6
- **Loại:** One-file executable (không cần cài đặt)

### Thư Viện
- requests (HTTP client)
- urllib3 (Advanced HTTP)
- certifi (SSL certificates)
- tkinter (GUI framework)
- Và nhiều dependencies khác

### API Endpoint
```
Default: http://172.16.1.220:8000/api/register-mac

Để đổi server, thiết lập biến môi trường:
Windows: set API_URL=http://your-server:8000/api/register-mac
macOS:   export API_URL=http://your-server:8000/api/register-mac
```

---

## 📊 Tính Năng Chi Tiết

### Windows (app.py)
- Sử dụng `netsh wlan` để quét card WiFi
- Hỗ trợ vô hiệu hóa Random MAC
- Giao diện Tkinter đầy đủ

### macOS (app_macos.py)
- Sử dụng `networksetup` để quét card WiFi
- Phát hiện địa chỉ Private MAC
- Hỗ trợ tắt/bật WiFi để làm mới
- Giao diện Tkinter đầy đủ

---

## 🎓 Hướng Dẫn Cho Nhà Trường

### Để Phân Phối Cho Học Sinh

1. **Tải các tệp:**
   - `RegisterWiFiMAC.exe` (cho Windows)
   - `RegisterWiFiMAC.app` (cho macOS)

2. **Tạo hướng dẫn:** Sử dụng [USER_GUIDE.md](USER_GUIDE.md)

3. **Phân phối:** Qua:
   - Email
   - Trang web trường
   - USB
   - Cloud storage

4. **Hỗ trợ học sinh:** 
   - Cấu hình API URL chính xác
   - Hướng dẫn cài đặt
   - Khắc phục sự cố

### Cấu Hình Cho Trường

```bash
# Windows
set API_URL=http://192.168.1.100:8000/api/register-mac
RegisterWiFiMAC.exe

# macOS
export API_URL=http://192.168.1.100:8000/api/register-mac
./RegisterWiFiMAC.app/Contents/MacOS/RegisterWiFiMAC
```

---

## 📝 License

Dự án này được sử dụng nội bộ cho trường học.

---

## 👨‍💻 Thông Tin Dự Án

- **Dự án:** GetMac
- **Loại:** Student Network Registration App
- **Platform:** Python (Cross-platform)
- **Bao gồm:** Standalone Windows & macOS apps

---

## 📞 Support

Nếu gặp vấn đề:
1. Đọc [USER_GUIDE.md](USER_GUIDE.md)
2. Kiểm tra [BUILD_GUIDE.md](BUILD_GUIDE.md)
3. Xem mục Khắc Phục Sự Cố ở trên
4. Liên hệ bộ phận IT

---

**Phiên bản:** 1.0.0  
**Cập nhật:** 2026-08-14  
**Trạng thái:** ✅ Production Ready
