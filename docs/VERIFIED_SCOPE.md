# ขอบเขตที่ตรวจสอบจากระบบจริง

Repository: `intasan/yolo11-object-detection`
ฐาน source ที่ตรวจ: `0f8e0ecba9708cbad4a2e2043102dcd1c7779030`

**สถานะ: ยังฝึกหรือประเมินไม่ได้**

รัน train.py แล้วขาด ultralytics; ไม่มีภาพและ labels ของ dataset และไม่มี weights/ผลประเมินที่ตรวจสอบได้

## แหล่งหลักฐาน

- [evidence/source-audit.json](../evidence/source-audit.json)
- [evidence/attempt-train-py.txt](../evidence/attempt-train-py.txt)

## Traceability จาก source

| ไฟล์ที่ตรวจ | ขอบเขตที่ยืนยันได้ |
|---|---|
| [train.py](../train.py) | พบ source ใน commit ข้างต้น; การมีไฟล์ไม่ใช่การทดสอบผ่าน |

## เกณฑ์ตรวจรับ BA / SA

| เกณฑ์ | หลักฐาน / สถานะ |
|---|---|
| ขอบเขตปัจจุบันตรงกับ source | ยังฝึกหรือประเมินไม่ได้ |
| End-to-end ด้วยข้อมูลจริง | รัน train.py แล้วขาด ultralytics; ไม่มีภาพและ labels ของ dataset และไม่มี weights/ผลประเมินที่ตรวจสอบได้ |
| ผลการทดสอบที่ทำซ้ำได้ | อ่าน command, stdout, exit code ใน evidence; syntax check ไม่ใช่ runtime test |
| ข้อมูลจริงและ provenance | เฉพาะราคาทองใน live-verification.txt ที่มี URL/เวลา publication; ไม่ใช้ fixture เป็นข้อมูลจริง |
| UAT โดยเจ้าของงานหรือผู้ใช้งาน | ยังไม่ได้ดำเนินการในรอบนี้ |

## ข้อจำกัดการแสดงผลงาน

ผล unit tests เป็นการตรวจ logic โดยมี fixture ตาม suite เดิม ไม่ใช่หลักฐานธุรกรรมจริง การฝึกโมเดลจริง การทำงานของอุปกรณ์จริง หรือการรับรองจากผู้ใช้ ไม่สร้างข้อมูลธุรกิจทดแทนข้อมูลที่ขาด และไม่อนุมานว่าไม่มีข้อมูลเท่ากับปลอดภัย
