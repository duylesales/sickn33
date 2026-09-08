# 🌱 Seed Keywords — Các Mảng Chưa Được Phủ

> **Mục đích**: `keyword-planner-manifera.com-2026-06-12 (1).csv` (1.595 từ khóa) **không phủ** một số dịch vụ Manifera đang bán và một số thuật ngữ mua hàng phổ biến. Tệp này là danh sách seed để (a) chạy Keyword Planner đợt mới và (b) làm hạt giống cho các cụm nội dung tương lai.
> **Cách dùng**: nạp từng nhóm vào Keyword Planner với filter Location = Netherlands + Belgium + Germany, rồi bổ sung kết quả vào [`google_ads_keywords_manifera.md`](./google_ads_keywords_manifera.md) §3 và bảng ánh xạ ở [`seo_geo_plan_vendor_keywords.md`](./seo_geo_plan_vendor_keywords.md) §2.

---

## 1. eCommerce / Webshop — 🔴 lỗ hổng lớn nhất
> CSV chỉ có 2 dòng eCommerce (`ecommerce app developers`, `ecommerce app development companies`, mỗi từ 10 volume) trong khi đây là một trong sáu dịch vụ chính thức của Manifera.

"magento development agency"
"magento development company netherlands"
"magento 2 migration service"
"magento to shopify migration"
"woocommerce development agency"
"b2b ecommerce platform development"
"b2b webshop development"
"custom webshop development"
"headless commerce development"
"ecommerce erp integration"
"payment gateway integration service"
"webshop koppeling erp"

## 2. Staff Augmentation — 🔴 thuật ngữ hợp đồng của khách MNC
> Không xuất hiện một dòng nào trong CSV, dù đây là một trong ba mô hình hợp đồng Manifera cung cấp.

"staff augmentation"
"it staff augmentation services"
"software development staff augmentation"
"team extension services"
"extended development team"
"outstaffing software development"
"augment engineering team"

## 3. Legacy Modernization — 🔴 hợp đồng giá trị cao nhất
"legacy system modernization"
"legacy application modernization services"
"legacy software migration company"
"monolith to microservices migration"
"replatforming legacy software"
"technical debt audit service"
"code audit service"
"software due diligence service"

## 4. EU Cloud & Compliance — dịch vụ đã có trang nhưng không có dữ liệu từ khóa
"cloud migration services netherlands"
"gdpr compliant cloud hosting"
"eu data residency software"
"azure west europe migration"
"aws eu migration partner"
"data sovereignty compliance software"
"nis2 software compliance"

## 5. Ngành dọc — đã có 300 bài viết nhưng chưa có nghiên cứu từ khóa
> Nguồn bài sẵn có: `extra-4-support` (fintech, healthtech, logistics), `extra-5-support` (nhà hàng/hospitality), `extra-11-decision` (fintech/insurance/banking compliance).

"fintech software development company"
"pci dss compliant development partner"
"healthcare software development company eu"
"medical device software development"
"logistics software development company"
"warehouse management system development"
"restaurant ordering system development"
"insurance software development solvency ii"

## 6. AI — cửa sổ định vị còn mở (competition thấp)
"ai software development company netherlands"
"offshore ai development team"
"llm integration services"
"rag application development company"
"ai agent development services"
"machine learning development partner"
"ai proof of concept development"

## 7. Thương hiệu & so sánh — cần theo dõi, không nhất thiết đấu giá
"manifera reviews"
"manifera clutch"
"manifera vs"
"best offshore development companies netherlands"
"top software development companies amsterdam"
"vietnam vs poland software development"
"vietnam vs india outsourcing"
"nearshore vs offshore development"

---

## Việc cần làm sau khi có dữ liệu

| # | Việc | Đầu ra |
|---|---|---|
| 1 | Chạy Keyword Planner cho nhóm 1–4, filter NL/BE/DE | Volume + bid thật cho từng nhóm |
| 2 | Chạy lại toàn bộ CSV gốc với filter Location = Netherlands | Biết quy mô thật của thị trường nhà (CSV hiện là volume toàn cầu) |
| 3 | Quyết định nhóm 1 (webshop) có xứng đáng một pillar riêng không | Câu hỏi #4 trong [`implementation_plan.md`](./implementation_plan.md) §9 |
| 4 | Dùng nhóm 2–3 làm hạt giống cho cụm nội dung mới (nếu cần viết thêm) | Chỉ sau khi 1.382 bài tồn kho đã được đăng |
| 5 | Rà quảng cáo đối thủ qua Google Ads Transparency Center cho nhóm 7 | Danh sách từ khóa đối thủ đang trả tiền |
