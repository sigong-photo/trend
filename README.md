# TrendPulse | 블로그 트렌드 레이더 ⚡

실시간 검색 급상승 키워드, 야놀자 놀 티켓(NOL TICKET) 오픈예정 공연, 마감 임박 콘서트 및 전시 행사를 실시간 큐레이션하여 블로그 글감과 상세 아웃라인을 제공하는 대시보드 웹 애플리케이션입니다.

---

## ✨ 주요 기능

1. **실시간 트렌드 및 문화 행사 큐레이션**
   - **놀 티켓 오픈예정**: 야놀자 놀 티켓 콘서트 오픈예정(등록순) 실시간 수집 및 티켓팅 D-Day 카운트다운
   - **종료 임박 콘서트**: 둘러보기 종료 임박순 정렬 (기무라 타쿠야, 고상지 트리오 등)
   - **종료 임박 전시**: 전시 둘러보기 종료 임박순 정렬 (ENHYPEN, 고야전, 경복궁 야간관람 등)
   - **다양한 카테고리 필터**: 축제, 팝업, 전시, 여행, 맛집, 건강, 생활정보 등

2. **블로그 포스팅 지원 (상세 모달)**
   - 카드 클릭 시 배경 정보, 타깃 독자층, 추천 검색 키워드 제공
   - SEO 최적화된 4단계 블로그 목차(Outline) 자동 생성
   - 공식 예매 링크 원클릭 연결

3. **작업 상태 관리 & 반응형 다크 UI**
   - 상태 변경: 미발행 / ✔️ 발행 완료
   - 다크 글래스모피즘(Dark Glassmorphism) 디자인 & 실시간 키워드 검색

---

## 🚀 빠른 시작 (Local)

### 1. 가상환경 및 패키지 설치
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. 데이터 수집 실행
```bash
python collector.py
```

### 3. 웹 서버 실행
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```
브라우저에서 `http://localhost:8000` 접속

---

## 🌐 외부(공용 웹) 접속 방법

### 1) 클라우드 배포 (무료 호스팅)
- **Render / Railway / Fly.io** 연동 시 `Procfile` 또는 시작 명령:
  ```bash
  uvicorn app:app --host 0.0.0.0 --port $PORT
  ```

### 2) 터널링 도구 (즉시 외부 공개)
- **Cloudflare Tunnel (추천, 무료/도메인 지원)**:
  ```bash
  cloudflared tunnel --url http://localhost:8000
  ```
- **ngrok**:
  ```bash
  ngrok http 8000
  ```

---

## ⏰ 스케줄러 실행 (매일 오전 6시 자동 수집)
```bash
python scheduler.py
```
