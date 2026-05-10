<div align="center">

# 🖥 Smart Glass — Construction Site (Backend)
### 건설 현장 안전관리 스마트글래스 — Django REST Backend

<p>
  <img src="https://img.shields.io/badge/Project-2022_한이음_ICT-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Award-전국_600팀_중_장려상-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Role-Team_Lead-red?style=flat-square" />
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/DRF-A30000?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" />
</p>

</div>

---

## 🏗 About

건설 현장 작업자의 스마트글래스가 캡처한 안전 이벤트(이미지 + 음성)를 수신하고 관리하는 **Django REST 백엔드**입니다.

작업자 글래스 → AWS S3 → 본 백엔드 → 관제용 Android 앱 / 웹 대시보드 흐름의 중심에 있습니다.

> 결과: 현장 점검 흐름 약 **40% 개선** / 한이음 전국 600팀 중 **장려상** / 정보처리학회 **우수논문상**.

---

## 📦 Project Structure

```
detectUS/
├── detectUS/        # Project root (settings, urls)
├── accounts/        # 작업자/관리자 계정 인증
├── home/            # 메인 대시보드 / 이벤트 피드
├── listapp/         # 안전 이벤트 리스트 / 필터링
└── settingsapp/     # 현장 / 알림 설정
```

| Django App | 역할 |
|---|---|
| `accounts` | 작업자 / 관리자 회원가입 / 로그인 / 권한 |
| `home` | 메인 대시보드 — 실시간 이벤트 피드 |
| `listapp` | 캡처된 안전 이벤트 목록 + 검색 / 필터 |
| `settingsapp` | 현장 / 알림 / 임계값 등 설정 관리 |

---

## 🔄 Request Flow

```
[Smart Glass Device]              [Django Backend]                  [Client]
PiCamera + Mic                    detectUS                          Android / Web
       │                                │                                │
       │ ── upload event ──► AWS S3 ◄── │ ── fetch metadata ───►         │
       │                                │ ── REST API ─────────►         │
```

1. 글래스 디바이스가 사진/음성을 AWS S3에 직접 업로드 (boto3)
2. 본 백엔드에 이벤트 메타데이터 등록 (REST API)
3. Django REST Framework가 인증 + 직렬화 + 페이징 처리
4. Android와 Web 클라이언트에 실시간 이벤트 노출

---

## 🛠 Tech Stack

- **Framework**: Django + Django REST Framework
- **Database**: SQLite (개발) → AWS RDS 확장 가능
- **Storage**: AWS S3 (이미지 / 음성)
- **Auth**: Django built-in + DRF Token
- **Deployment**: AWS EC2

---

## 🔗 Related Repositories

| | |
|---|---|
| 🖥 **Backend** *(this repo)* | [backend](https://github.com/SmartGlassAtConstructionSite/backend) |
| 🦺 Device firmware | [smartglass](https://github.com/SmartGlassAtConstructionSite/smartglass) |

---

## 🏆 Awards

- 🥉 **2022 한이음 ICT 멘토링 장려상** — 과학기술정보통신부 / KCC정보통신 (전국 600팀)
- 🏅 **2022 한국정보처리학회 ACK 우수논문상**

---

## 👥 Team

강현구,김성민,이민영,최혜린,최태훈

---

<div align="center">

*From device to dashboard — keeping the site safer in real time.*

</div>
