#!/usr/bin/env python3
"""Wrap src/talk.html (the raw Artifact-style fragment, no <html>/<head>/<body>)
into index.html (a full standalone page) for GitHub Pages.

Usage: python3 build.py
"""
import re
import pathlib
import datetime

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src" / "talk.html"
OUT = ROOT / "index.html"

built_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# Không nhúng mã commit: build.py chạy TRƯỚC khi chính commit chứa bản build này
# được tạo ra, nên mã hash nhúng vào luôn luôn lệch 1 bước so với commit thật -
# gây hiểu lầm "chưa deploy". Chỉ hiện giờ dựng, đủ để biết bản có mới hay không.
version_tag = (
    '<div id="build-version" style="position:fixed;left:1rem;bottom:.6rem;z-index:10;'
    'font:11px -apple-system,Arial,sans-serif;pointer-events:none;">'
    f'Bản dựng {built_at}</div>'
)

body = SRC.read_text(encoding="utf-8")

m = re.search(r"<title>(.*?)</title>", body)
title = m.group(1) if m else "ĐMST tại Đại học — HaUI"
if m:
    body = body[: m.start()] + body[m.end():]

head_extra = ""
m2 = re.search(r"<style>.*?</style>", body, re.S)
if m2:
    head_extra = m2.group(0)
    body = body[: m2.start()] + body[m2.end():]

html = (
    '<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
    f'<meta name="description" content="Tham luận: Thực trạng và vướng mắc triển khai đổi mới sáng tạo tại Đại học — trường hợp HaUI">'
    '<meta name="apple-mobile-web-app-capable" content="yes">'
    '<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">'
    f"<title>{title}</title>{head_extra}</head><body>{version_tag}{body}</body></html>"
)

OUT.write_text(html, encoding="utf-8")
print(f"Wrote {OUT} ({len(html):,} bytes)")
