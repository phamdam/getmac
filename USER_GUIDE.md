# 📱 Hướng Dẫn Sử Dụng RegisterWiFiMAC

## Giới Thiệu

**RegisterWiFiMAC** là ứng dụng để đăng ký địa chỉ MAC của thiết bị WiFi với hệ thống mạng trường học. Ứng dụng này tự động phát hiện tất cả các card WiFi trong thiết bị của bạn và cho phép bạn đăng ký chúng.

---

## 🖥️ Windows

### Yêu Cầu Hệ Thống
- Windows 7 hoặc cao hơn
- 50 MB dung lượng trống
- Kết nối Internet

### Cài Đặt & Chạy

1. **Tải về:** Tìm tệp `RegisterWiFiMAC.exe`
2. **Chạy:** Nhấp đúp trên `RegisterWiFiMAC.exe`
3. **Cấp quyền:** Nếu được hỏi, nhấp **"Có"** hoặc **"Yes"**

> ℹ️ Không cần cài đặt gì. Ứng dụng sẽ khởi động ngay lập tức!

### Sử Dụng Ứng Dụng

1. **Nhập Mã Học Sinh:** Nhập mã học sinh của bạn vào ô `Mã học sinh`
2. **Chọn MAC:** Nhấp chọn một card WiFi từ danh sách
3. **Đăng Ký:** Nhấp nút **"Đăng ký MAC đã chọn"**
4. **Xong:** Chờ thông báo "Đăng ký thành công!"

### Làm Mới Danh Sách
- Nếu danh sách không hiển thị card WiFi của bạn
- Nhấp **"Làm mới danh sách MAC WiFi"**
- Hoặc đóng và mở lại ứng dụng

---

## 🍎 macOS

### Yêu Cầu Hệ Thống
- macOS 10.13 hoặc cao hơn
- 50 MB dung lượng trống
- Kết nối Internet

### Cài Đặt & Chạy

1. **Tải về:** Tìm thư mục `RegisterWiFiMAC.app`
2. **Chạy:** Nhấp đúp trên `RegisterWiFiMAC.app`
3. **Cho phép:** Nhấp **"Open"** nếu được hỏi

> ℹ️ Lần đầu chạy có thể mất một vài giây. Các lần sau sẽ nhanh hơn.

### Gặp Lỗi "Cannot be opened because..."?

Mở **Terminal** và chạy:
```bash
xattr -d com.apple.quarantine ~/Downloads/RegisterWiFiMAC.app
```

Sau đó nhấp đúp lại trên `RegisterWiFiMAC.app`

### Sử Dụng Ứng Dụng

Giống như trên Windows:
1. **Nhập Mã Học Sinh**
2. **Chọn MAC từ danh sách**
3. **Nhấp Đăng Ký**
4. **Chờ thông báo thành công**

---

## ❓ Câu Hỏi Thường Gặp

### Q: Làm sao để biết MAC của tôi?
**A:** Ứng dụng sẽ hiển thị danh sách tất cả MAC. Chọn cái có tên "WiFi" hoặc "Airport" trên Mac.

### Q: Tôi không thấy card WiFi của mình?
**A:** 
- Nhấp "Làm mới danh sách MAC WiFi" trên Windows
- Hoặc đóng và mở lại ứng dụng
- Kiểm tra card WiFi có bật không

### Q: Ứng dụng có an toàn không?
**A:** Có! Ứng dụng này chỉ đọc thông tin MAC của bạn và gửi tới server. Không có dữ liệu nào bị lưu cục bộ.

### Q: Mã học sinh sai ở đâu?
**A:** Kiểm tra:
- Không có khoảng trắng thừa
- Đúng mã trong hệ thống trường học
- Kiểm tra chữ hoa/thường (nếu yêu cầu)

### Q: Lỗi kết nối API?
**A:** 
- Kiểm tra kết nối Internet
- Kiểm tra server có hoạt động không
- Thử lại sau vài phút

### Q: Tôi có thể đăng ký nhiều thiết bị không?
**A:** Có! Đơn giản chỉ cần chạy ứng dụng trên từng thiết bị.

### Q: Cần quyền Admin không?
**A:** 
- **Windows:** Có (để tắt Random MAC)
- **macOS:** Có (để kiểm soát Wi-Fi)

---

## 🔧 Cấu Hình Nâng Cao

### Đổi Server API (Windows)

1. Mở **Command Prompt**
2. Chạy:
```cmd
set API_URL=http://your-api-server:8000/api/register-mac
RegisterWiFiMAC.exe
```

### Đổi Server API (macOS)

1. Mở **Terminal**
2. Chạy:
```bash
export API_URL=http://your-api-server:8000/api/register-mac
~/RegisterWiFiMAC.app/Contents/MacOS/RegisterWiFiMAC
```

---

## ⚠️ Ghi Chú Quan Trọng

1. **MAC Address là gì?**
   - MAC (Media Access Control) là địa chỉ duy nhất của card mạng
   - Định dạng: `XX:XX:XX:XX:XX:XX` (ví dụ: `A1:B2:C3:D4:E5:F6`)

2. **Địa chỉ Private MAC**
   - Một số thiết bị có tính năng "Private Address"
   - Nếu MAC thay đổi mỗi lần kết nối, hãy bật "Private Address"
   - Trên Windows: Random MAC
   - Trên macOS: Private Address trong System Settings

3. **Quyền Admin**
   - Ứng dụng có thể yêu cầu quyền quản trị để:
     - Tắt Random MAC (Windows)
     - Kiểm soát Wi-Fi (macOS)
   - Điều này là bình thường và cần thiết

---

## 📞 Hỗ Trợ

Nếu gặp vấn đề:

1. Kiểm tra lại mã học sinh
2. Kiểm tra kết nối Internet
3. Thử làm mới danh sách
4. Đóng và mở lại ứng dụng
5. Liên hệ bộ phận IT của trường

---

## 📋 Thông Tin Ứng Dụng

- **Tên:** RegisterWiFiMAC
- **Phiên bản:** 1.0.0
- **Loại:** Standalone Application (không cần cài đặt)
- **Kích thước:** ~50 MB
- **Hệ điều hành:** Windows 7+ / macOS 10.13+

---

**Cập nhật lần cuối:** 2026-08-14  
**Nguồn:** GetMac Project
