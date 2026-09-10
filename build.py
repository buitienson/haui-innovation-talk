#!/usr/bin/env python3
"""Wrap src/talk.html (the raw Artifact-style fragment, no <html>/<head>/<body>)
into index.html (a full standalone page) for GitHub Pages.

Usage: python3 build.py
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src" / "talk.html"
OUT = ROOT / "index.html"

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
    '<meta name="viewport" content="width=device-width, initial-scale=1">'
    f'<meta name="description" content="Tham luận: Thực trạng và vướng mắc triển khai đổi mới sáng tạo tại Đại học — trường hợp HaUI">'
    f"<title>{title}</title>{head_extra}</head><body>{body}</body></html>"
)

OUT.write_text(html, encoding="utf-8")
print(f"Wrote {OUT} ({len(html):,} bytes)")
