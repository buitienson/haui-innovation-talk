# Tham luận — ĐMST tại Đại học (HaUI)

Trang trình chiếu dạng landing page (20 slide, điều hướng bằng phím mũi tên / click / vuốt)
cho bài tham luận tại Hội nghị Viên chức Ban Khoa học, Công nghệ và Đổi mới sáng tạo,
Đại học Công nghiệp Hà Nội — năm học 2025–2026 (9h30, Thứ Bảy 12/9/2026, Phòng 603 Nhà A1).

Chủ đề: *"Thực trạng và các vướng mắc khi triển khai hoạt động đổi mới sáng tạo tại Đại học;
đề xuất, kiến nghị"* — Bùi Tiến Sơn, Phòng Đổi mới sáng tạo.

**Live:** https://buitienson.github.io/haui-innovation-talk/

## Điều khiển khi trình chiếu

- `→` / `Space` / click nửa phải màn hình: slide tiếp
- `←` / click nửa trái: slide trước
- `F`: bật/tắt toàn màn hình
- Chấm bên phải: nhảy nhanh tới slide bất kỳ (hover để xem tên)
- Vuốt trái/phải: dùng được trên điện thoại/tablet

## Cấu trúc

- `src/talk.html` — nội dung gốc (fragment kiểu Artifact, không có `<html>/<head>/<body>`)
- `build.py` — bọc `src/talk.html` thành `index.html` hoàn chỉnh để GitHub Pages phục vụ
- Sửa nội dung: sửa `src/talk.html` rồi chạy `python3 build.py`

Nội dung đối chiếu với outline đầy đủ (kèm speaker note + nguồn trích dẫn từng slide) ở
`InnovationAdvisory/2026 Hoi nghi DMST Dai hoc - Tham luan HaUI/`.
