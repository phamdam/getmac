# 🚀 Build macOS qua GitHub Actions

Bạn không cần máy Mac để build ứng dụng macOS! Sử dụng **GitHub Actions** để build tự động trên máy chủ Mac của GitHub.

---

## 📋 Yêu Cầu

1. **GitHub Repository** (công khai hoặc riêng tư)
2. **GitHub Account**
3. Các tệp workflow đã được tạo trong thư mục `.github/workflows/`

---

## 🔧 Có 3 Workflow Khác Nhau

### 1. **build-windows.yml** ⚙️
- Build Windows executable tự động
- Chạy khi push code vào nhánh `main`, `master`, `develop`
- Lưu kết quả dưới dạng artifact

### 2. **build-macos.yml** 🍎
- Build macOS app tự động
- Chạy khi push code vào nhánh `main`, `master`, `develop`
- Tạo DMG installer (tuỳ chọn)
- Lưu kết quả dưới dạng artifact

### 3. **build-and-release.yml** 🎯
- Build cả Windows và macOS **cùng lúc**
- Tự động tạo GitHub Release
- Chỉ chạy khi bạn tạo một tag (ví dụ: `v1.0.0`)
- **ĐÂY LÀ WORKFLOW ĐƯỢC KHUYẾN KHÍCH DÙNG**

---

## 🚀 Cách Sử Dụng

### Phương Pháp 1: Push Code Để Build

```bash
git push origin main
```

**Kết quả:** 
- GitHub Actions tự động build Windows + macOS
- Artifacts lưu trong tab "Actions"
- Bạn có thể tải xuống ngay

### Phương Pháp 2: Tạo Release (Khuyến Khích)

```bash
# Tạo tag mới
git tag v1.0.0
git push origin v1.0.0
```

**Kết quả:**
- Build Windows và macOS tự động
- Tạo GitHub Release tự động
- Tất cả tệp executable được tải lên Release
- Người dùng có thể tải từ trang Release

### Phương Pháp 3: Manual Trigger

Vào **GitHub > Actions > chọn workflow > "Run workflow"**

---

## 📥 Tải Artifacts

### Cách 1: Từ Tab Actions

1. Vào **GitHub Repository**
2. Chọn tab **Actions**
3. Chọn workflow chạy mới nhất
4. Cuộn xuống phần **Artifacts**
5. Tải `RegisterWiFiMAC-macOS` (hoặc Windows)

### Cách 2: Từ GitHub Release

1. Vào **Releases**
2. Chọn version
3. Tải `RegisterWiFiMAC.exe` hoặc `RegisterWiFiMAC.app`

---

## 📝 Cấu Trúc Thư Mục

```
GetMac/
├── .github/
│   └── workflows/
│       ├── build-windows.yml         ⚙️ Build Windows
│       ├── build-macos.yml           🍎 Build macOS
│       └── build-and-release.yml     🎯 Build + Release (khuyến khích)
│
├── app.py                            (Windows)
├── app_macos.py                      (macOS)
├── RegisterWiFiMAC-windows.spec
├── RegisterWiFiMAC-macos.spec
├── requirements.txt
└── ... (tệp khác)
```

---

## ✅ Quy Trình Build

```
┌─────────────────────────────────────┐
│  Push Code hoặc Tạo Tag             │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  GitHub Actions Trigger             │
└──────────────┬──────────────────────┘
               │
        ┌──────┴──────┐
        ▼             ▼
   ┌─────────┐   ┌─────────┐
   │ Windows │   │ macOS   │
   │ Build   │   │ Build   │
   └────┬────┘   └────┬────┘
        │             │
        └──────┬──────┘
               ▼
      ┌──────────────────┐
      │ Create Release   │
      │ (nếu có tag)     │
      └──────────────────┘
```

---

## 🎯 Ví Dụ: Tạo Release v1.0.0

### Bước 1: Commit Code
```bash
git add .
git commit -m "Release version 1.0.0"
git push origin main
```

### Bước 2: Tạo Tag
```bash
git tag v1.0.0
git push origin v1.0.0
```

### Bước 3: GitHub Actions Tự Động Build
- Chờ 5-10 phút
- Vào **GitHub > Releases**
- Tìm `v1.0.0`
- Tải `RegisterWiFiMAC.exe` và `RegisterWiFiMAC.app`

---

## 🔍 Monitoring Build

### Xem Log Chi Tiết

1. Vào **GitHub > Actions**
2. Chọn workflow đang chạy
3. Chọn job (Windows hoặc macOS)
4. Xem chi tiết log

### Troubleshooting

Nếu build thất bại:
1. Kiểm tra log trong tab **Actions**
2. Thường là do:
   - `requirements.txt` không chính xác
   - `.spec` file có lỗi
   - Python version không tương thích

---

## 📊 Thời Gian Build

| Platform | Thời Gian |
|----------|-----------|
| Windows | ~5-10 phút |
| macOS | ~5-10 phút |
| Cả hai | ~15-20 phút |

---

## 🛡️ Bảo Mật

- ✅ Workflows chỉ chạy khi bạn push
- ✅ Không có thông tin nhạy cảm trong file
- ✅ GitHub token tự động được cấp
- ✅ Artifacts chỉ lưu 30 ngày (có thể thay đổi)

---

## 💡 Tips

1. **Tự động build mỗi khi push:**
   - Sử dụng `build-windows.yml` hoặc `build-macos.yml`

2. **Build release cuối cùng:**
   - Sử dụng `build-and-release.yml`
   - Tạo tag: `git tag v1.0.0`

3. **Thay đổi nhánh trigger:**
   - Sửa `branches` trong YAML file

4. **Thêm icon:**
   - Thêm `icon.ico` cho Windows
   - Thêm `icon.icns` cho macOS trong `.spec` file

---

## 📌 Workflow Được Khuyến Khích

**Sử dụng `build-and-release.yml`:**

```bash
# 1. Phát triển
git add .
git commit -m "Add new feature"
git push origin main

# 2. Sẵn sàng release
git tag v1.0.0
git push origin v1.0.0

# 3. GitHub Actions tự động:
#    - Build Windows
#    - Build macOS
#    - Tạo Release
#    - Upload executables

# 4. Người dùng tải từ GitHub Releases
```

---

## 🚀 Lợi Ích

✅ **Tự động hóa:** Không cần build thủ công  
✅ **Cross-platform:** Windows + macOS cùng lúc  
✅ **Không cần máy Mac:** Build trên GitHub  
✅ **Dễ phân phối:** Tự động tạo Release  
✅ **An toàn:** Code lưu trên GitHub  
✅ **Miễn phí:** GitHub Actions miễn phí  

---

## 📞 Hỗ Trợ

Nếu gặp lỗi:
1. Kiểm tra tab **Actions** trong GitHub
2. Xem log chi tiết
3. Kiểm tra `requirements.txt`
4. Kiểm tra `.spec` file

---

**Cập nhật:** 2026-08-14  
**Loại:** GitHub Actions Guide
