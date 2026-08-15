# 🚀 Hướng Dẫn Nhanh - Build macOS qua GitHub

## ⚡ 3 Bước Đơn Giản

### Step 1️⃣: Push Code lên GitHub
```bash
cd d:\VibeCode\GetMac
git add .
git commit -m "Build v1.0.0"
git push origin main
```

### Step 2️⃣: Chờ Build Hoàn Thành
- Vào GitHub Repository
- Chọn tab **"Actions"**
- Xem build đang chạy (5-10 phút)

### Step 3️⃣: Tải RegisterWiFiMAC.app
- Trong tab Actions, chọn workflow chạy mới nhất
- Cuộn xuống **"Artifacts"**
- Tải **"RegisterWiFiMAC-macOS"** (chứa .app)

---

## 🎯 Để Tạo Release Chính Thức

```bash
# 1. Cập nhật code
git add .
git commit -m "Release v1.0.0"
git push origin main

# 2. Tạo tag
git tag v1.0.0
git push origin v1.0.0

# 3. GitHub tự động:
#    - Build Windows + macOS
#    - Tạo Release page
#    - Upload cả 2 tệp
```

**Sau 10-15 phút, vào GitHub > "Releases" để tải!**

---

## 📂 File Sẽ Nhận Được

- `RegisterWiFiMAC.exe` (19.4 MB) - Windows
- `RegisterWiFiMAC.app` (~19.4 MB) - macOS

---

## ✅ Xong!

Bây giờ bạn có macOS app mà **không cần máy Mac** 🎉

---

**Xem chi tiết:** [GITHUB_ACTIONS_GUIDE.md](GITHUB_ACTIONS_GUIDE.md)
