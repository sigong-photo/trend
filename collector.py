import json
import os
from datetime import datetime, date
from typing import List
from pydantic import BaseModel, Field

class TopicItem(BaseModel):
    id: str
    section: str  # 'urgent' (이번 주 안에 써야 할 소재) 또는 'trend' (최근 트렌드)
    category_badges: List[str]
    d_day_badge: str | None = None
    title: str
    event_date: str | None = None
    performance_date: str | None = None
    location: str | None = None
    summary: str
    status: str = "unissued"  # unissued, wishlist, done
    details: str | None = None
    keywords: List[str] = Field(default_factory=list)
    blog_outline: List[str] = Field(default_factory=list)
    target_audience: str | None = None
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    is_new: bool = True

def fetch_sample_data() -> List[dict]:
    return [
        {
            "id": "item-1",
            "section": "urgent",
            "category_badges": ["행사·뉴스", "축제", "여행"],
            "d_day_badge": "D-7",
            "title": "2026 서울세계불꽃축제 명당 명소 & 준비물",
            "event_date": "2026-10-03",
            "location": "여의도 한강공원 일대",
            "summary": "10월 첫 주말 여의도 불꽃축제 개최. 이촌한강공원, 노량진 사육신공원, 마포대교 등 무료 명당 스팟과 필수 방한용품·교통통제 우회 팁 정리.",
            "status": "unissued",
            "details": "매년 수백만 인파가 몰리는 서울 대표 가을 축제입니다. 올해는 한국, 미국, 일본 등 다국적 연화팀이 참여하여 역대급 스케일의 불꽃 쇼를 연출합니다. 19시 개막식부터 본 불꽃쇼가 진행되며, 여의도 메인 행사장 외에도 한강 이북 이촌지구, 노량진 수산시장 옥상 및 사육신역사공원 등이 인파를 피해 관람하기 좋은 명당으로 꼽힙니다.",
            "keywords": ["서울세계불꽃축제", "여의도불꽃축제명당", "불꽃축제준비물", "사육신공원불꽃", "이촌한강공원명당", "여의도교통통제"],
            "blog_outline": [
                "1. 2026 서울세계불꽃축제 기본 정보 (일시, 타임테이블)",
                "2. 아는 사람만 아는 무료 뷰 명당 BEST 4 (이촌, 노량진, 마포)",
                "3. 자리 선점 골든타임 & 교통 통제/지하철 무정차 구간",
                "4. 10월 한강 강바람 필수 방한용품 & 돗자리 꿀팁"
            ],
            "target_audience": "가을 데이트를 계획 중인 커플 및 수도권 나들이 가족",
            "created_at": "2026-09-26",
            "is_new": True
        },
        {
            "id": "item-2",
            "section": "urgent",
            "category_badges": ["행사·뉴스", "전시", "여행"],
            "d_day_badge": "D-6",
            "title": "서울라이트 한강 빛섬 축제 개막",
            "event_date": "2026-10-02 ~ 2026-10-11",
            "location": "서울 노들섬 수변공원",
            "summary": "노들섬 전체를 레이저 아트와 미디어 아트로 수놓는 대규모 가을 빛 축제. 야간 버스킹 공연과 순환 산책로, 인생샷 포토존 동선 안내.",
            "status": "unissued",
            "details": "자연과 테크놀로지가 결합된 초대형 야간 미디어아트 축제입니다. 노들섬의 수변 산책로 1.5km 구간을 따라 레이저 숲, 인터랙티브 라이트 아트, 야간 미디어 파사드가 상시 가동됩니다. 특히 일몰 직후 노을과 어우러지는 수변 뷰가 일품이며 주말에는 인디 뮤지션 버스킹과 푸드트럭이 운영됩니다.",
            "keywords": ["서울라이트빛섬축제", "노들섬빛축제", "노들섬야경", "서울가을전시", "서울야간데이트", "미디어아트전시"],
            "blog_outline": [
                "1. 서울라이트 한강 빛섬 축제 운영 시간 및 입장료(무료)",
                "2. 인생샷 건지는 노들섬 야간 조명 핵심 스팟 코스",
                "3. 주말 버스킹 라인업과 푸드트럭 먹거리 정보",
                "4. 노들섬 주차 불가 안내 및 버스·지하철 대중교통 동선"
            ],
            "target_audience": "인스타 감성 야경 사진과 야간 산책 데이트를 즐기는 2030 세대",
            "created_at": "2026-09-26",
            "is_new": True
        },
        {
            "id": "item-3",
            "section": "urgent",
            "category_badges": ["행사·뉴스", "건강", "생활정보"],
            "d_day_badge": "D-2",
            "title": "2026-2027절기 독감 무료 예방접종 어린이·어르신 시작",
            "event_date": "2026-09-28 ~",
            "location": "전국 지정 위탁의료기관 및 보건소",
            "summary": "어린이(14세까지 확대) 및 임신부 1회 접종 오픈. 10월 어르신 연령별 접종 일정과 예방접종도우미 잔여백신 조회 및 필수 지참 신분증 가이드.",
            "status": "unissued",
            "details": "질병관리청이 주관하는 국가 인플루엔자 예방접종 지원사업입니다. 올해부터 어린이 무료 대상이 만 14세(2012년생)까지 확대되었습니다. 9월 28일부터 1회 접종 어린이와 임신부 접종이 시작되며, 10월 중순부터는 65세 이상 어르신 연령대별 순차 접종이 진행됩니다. 코로나19 백신과 동시 접종이 가능합니다.",
            "keywords": ["독감무료예방접종", "2026독감예방접종일정", "어린이독감백신", "임신부독감접종", "예방접종도우미", "65세독감접종"],
            "blog_outline": [
                "1. 2026-2027 독감 국가 무료 접종 대상자 및 변경점(14세 확대)",
                "2. 연령별/대상별 접종 시작일 캘린더",
                "3. 병원 방문 전 필수 준비물(신분증, 산모수첩) 및 병의원 검색법",
                "4. 독감 백신 접종 후 주의사항 및 부작용 대처"
            ],
            "target_audience": "유아·초등학생 자녀를 둔 학부모 및 부모님 건강을 챙기는 3040 세대",
            "created_at": "2026-09-26",
            "is_new": True
        },
        {
            "id": "item-4",
            "section": "urgent",
            "category_badges": ["행사·뉴스", "축제", "공연"],
            "d_day_badge": "이번 주말",
            "title": "2026 한강 드론 라이트 쇼 가을 시즌",
            "event_date": "2026-09-27 ~ 2026-10-31",
            "location": "뚝섬한강공원 수변무대",
            "summary": "1,000대 이상 드론이 펼치는 가을 테마 라이트쇼. 공연 시작 시간(20:00), 돗자리 관람 명당 구역 및 지하철 7호선 자양역 혼잡도 우회 루트.",
            "status": "unissued",
            "details": "뚝섬 한강 밤하늘을 1,000대 이상의 군집 드론이 화려한 형상과 스토리로 연출합니다. 가을 테마 문화예술, 서울의 랜드마크, K-컬처를 주제로 매 회차 다른 스토리텔링이 펼쳐집니다. 공연 시작 1시간 전부터 수변무대 앞 잔디밭은 돗자리 관람객으로 만석이 되므로 이동 동선을 미리 파악해야 합니다.",
            "keywords": ["한강드론쇼", "뚝섬드론라이트쇼", "뚝섬한강공원명당", "드론쇼시간표", "서울가을나들이", "뚝섬데이트"],
            "blog_outline": [
                "1. 가을 시즌 한강 드론 라이트 쇼 회차별 일정 및 주제",
                "2. 드론쇼 한눈에 담기는 시야 명당 구역 (수변무대 정면 팁)",
                "3. 공연 전후 추천 한강 피크닉 배달존 & 편의점 라면 팁",
                "4. 7호선 자양역 혼잡 시 건대입구역 방면 도보 우회 동선"
            ],
            "target_audience": "이색 야간 볼거리를 찾는 커플 및 아이와 함께하는 가족 방문객",
            "created_at": "2026-09-25",
            "is_new": False
        },
        {
            "id": "item-5",
            "section": "urgent",
            "category_badges": ["행사·뉴스", "공연", "축제"],
            "d_day_badge": "D-6",
            "title": "강남페스티벌 & 영동대로 K-POP 콘서트",
            "event_date": "2026-10-02 ~ 2026-10-05",
            "location": "코엑스 및 영동대로 일대",
            "summary": "영동대로 일대 교통통제 소식과 글로벌 K-POP 콘서트 라인업. 코엑스 야외 미식 스트리트 푸드존과 거리 퍼레이드 관람 타임테이블.",
            "status": "unissued",
            "details": "강남 도심 한복판 영동대로를 통제하고 펼쳐지는 대형 도심 축제입니다. 최정상급 아이돌 그룹이 출연하는 영동대로 K-POP 콘서트를 필두로, 코엑스 동측 광장에서는 세계 미식 푸드존과 비어 페스티벌이 함께 열립니다. 버스 및 차량 우회 경로 확인이 필수적입니다.",
            "keywords": ["강남페스티벌", "영동대로KPOP콘서트", "코엑스축제", "강남교통통제", "영동대로라인업", "강남미식축제"],
            "blog_outline": [
                "1. 2026 강남페스티벌 주요 프로그램 일정표",
                "2. 영동대로 K-POP 콘서트 라인업 및 티켓/스탠딩 입장 팁",
                "3. 코엑스 푸드 스트리트 맛집 부스 및 편의시설",
                "4. 행사 기간 영동대로 차 없는 거리 차량 우회로 & 대중교통 안내"
            ],
            "target_audience": "K-POP 팬덤 및 도심형 페스티벌을 즐기는 2030 직장인/학생",
            "created_at": "2026-09-24",
            "is_new": False
        },
        {
            "id": "item-6",
            "section": "trend",
            "category_badges": ["트렌드", "팝업", "먹거리", "맛집"],
            "d_day_badge": None,
            "title": "두바이 초콜릿 찹쌀떡 & 퓨전 디저트 '떡지순례'",
            "event_date": None,
            "location": "성수·연남동 팝업 매장",
            "summary": "SNS 화제의 두바이 픽스 초콜릿(카다이프+피스타치오)을 접목한 퓨전 찹쌀떡 웨이팅 열풍. 대표 매장 오픈런 시간과 택배 주문 보관 팁.",
            "status": "unissued",
            "details": "전 세계적 돌풍을 일으킨 두바이 초콜릿의 핵심 재료인 볶은 카다이프 면과 고소한 피스타치오 스프레드가 한국의 쫄깃한 찹쌀떡과 결합되었습니다. 성수동 팝업스토어 및 연남동 유명 떡 공방에서 출시 즉시 조기 품절 사태를 빚고 있으며, '할매니얼' 트렌드와 결합해 떡지순례 필수 코스로 급부상했습니다.",
            "keywords": ["두바이초콜릿찹쌀떡", "두바이초콜릿디저트", "성수두바이디저트", "성수팝업스토어", "떡지순례", "연남동맛집"],
            "blog_outline": [
                "1. 두바이 초콜릿 찹쌀떡 맛과 식감 솔직 후기 (바삭+쫄깃 단면 샷)",
                "2. 성수/연남 팝업 매장 위치 및 오픈런 번호표 배부 시간",
                "3. 온라인 스마트스토어 택배 오픈 일정 및 겟(Get) 팁",
                "4. 냉동 보관 후 바삭하게 해동해 먹는 꿀조합 레시피"
            ],
            "target_audience": "트렌디한 디저트 얼리어답터, 빵지순례/떡지순례를 즐기는 2030 여성",
            "created_at": "2026-09-26",
            "is_new": True
        },
        {
            "id": "item-7",
            "section": "trend",
            "category_badges": ["트렌드", "팝업", "전시", "쇼핑"],
            "d_day_badge": None,
            "title": "성수동 가을 팝업스토어 지도 & 예약 가이드",
            "event_date": None,
            "location": "성수 연무장길·서울숲 일대",
            "summary": "단순 패션을 넘어 F&B와 서브컬처 IP 중심으로 확장된 성수동 가을 팝업 라인업. 사전 예약 링크, 현장 캐치테이블 대기 팁 및 굿즈 수령법.",
            "status": "unissued",
            "details": "성수동 상권이 기존 연무장길 메인을 넘어 뚝섬역 북성수, 서울숲 골목까지 확장되었습니다. 가을 시즌에는 대형 패션 브랜드의 체험형 쇼룸뿐 아니라 글로벌 게임/애니메이션 IP 콜라보 팝업, 향수 및 뷰티 브랜드 팝업이 집중되어 있습니다. 사전 예약이 필수인 곳과 현장 웨이팅 팁을 묶어 소개하기 좋습니다.",
            "keywords": ["성수팝업스토어", "성수동놀거리", "성수연무장길", "성수팝업예약", "성수가을데이트", "성수핫플"],
            "blog_outline": [
                "1. 2026 9~10월 성수동 진행 중인 팝업스토어 캘린더 지도",
                "2. 사전 예약 필수 팝업 vs 현장 캐치테이블 대기 추천 팝업",
                "3. 무료 굿즈 & 럭키드로우 이벤트 참여 방법",
                "4. 팝업 투어 도중 들르기 좋은 성수 감성 카페 3곳"
            ],
            "target_audience": "주말 성수 나들이 데이트를 계획하는 20대 대학생 및 직장인",
            "created_at": "2026-09-26",
            "is_new": True
        },
        {
            "id": "item-8",
            "section": "trend",
            "category_badges": ["트렌드", "여행", "쇼핑"],
            "d_day_badge": None,
            "title": "엔화 900원대 환율과 일본 가을 단풍 여행 환전 비교",
            "event_date": None,
            "location": None,
            "summary": "10월 연휴 도쿄·오사카·후쿠오카 항공권 수요 급증. 트래블로그 vs 트래블월렛 환전 수수료 혜택 및 현지 세븐뱅크 ATM 출금 꿀팁 정리.",
            "status": "unissued",
            "details": "엔화 환율이 900원 안팎의 매력적인 수준을 유지하면서 10월 연휴 및 가을 단풍 시즌 일본 여행 수요가 폭발하고 있습니다. 특히 해외 결제 수수료 무료 카드(트래블로그, 트래블월렛, 토스뱅크 외화통장)의 혜택 비교와 일본 현지 세븐일레븐(세븐뱅크) 무료 출금 노하우는 검색 유입이 매우 높습니다.",
            "keywords": ["엔화환율", "일본여행환전", "트래블로그트래블월렛비교", "일본가을단풍", "도쿄여행경비", "후쿠오카환전"],
            "blog_outline": [
                "1. 현재 엔화 환율 추이와 환전 목표 타이밍 설정",
                "2. 트래블로그 vs 트래블월렛 장단점 완벽 비교표",
                "3. 일본 현지 ATM(세븐뱅크, 이온뱅크) 수수료 0원 인출 방법",
                "4. 가을 일본 단풍 명소(교토, 닛코) 베스트 추천 일정"
            ],
            "target_audience": "가을 휴가 및 주말 도쿄·오사카 여행을 준비하는 자유여행객",
            "created_at": "2026-09-24",
            "is_new": False
        },
        {
            "id": "item-9",
            "section": "trend",
            "category_badges": ["트렌드", "쇼핑", "건강"],
            "d_day_badge": None,
            "title": "가을 러닝(Running) 열풍과 입문자 러닝화 추천 비교",
            "event_date": None,
            "location": None,
            "summary": "2030 세대 사이 러닝 크루 및 하프 마라톤 열풍. 쿠션화 vs 카본화 차이점과 나이키·호카·아식스 입문자용 베스트셀러 모델 실착 비교.",
            "status": "unissued",
            "details": "시원한 가을 날씨와 함께 퇴근 후 러닝 크루(Running Crew) 활동과 마라톤 참가가 2030의 메가 트렌드로 자리잡았습니다. 부상 없는 러닝을 위한 발 분석(발볼, 아치 형태)과 입문자에게 적합한 데일리 쿠션 러닝화 모델(나이키 인피니티런, 아식스 젤카야노, 호카 클리프톤 등) 정보 수요가 큽니다.",
            "keywords": ["입문자러닝화", "러닝화추천", "가을러닝", "나이키러닝화", "아식스젤카야노", "마라톤준비"],
            "blog_outline": [
                "1. 초보 러너가 카본 플레이트화 대신 쿠션화를 신어야 하는 이유",
                "2. 내 발 모양(내전/외전/평발) 자가 진단 가이드",
                "3. 10만원대 가성비 입문 러닝화 BEST 3 실착 비교",
                "4. 초보자를 위한 5km 완주 인터벌 페이스 훈련법"
            ],
            "target_audience": "가을 운동을 시작하려는 2030 직장인 및 마라톤 입문 초보 러너",
            "created_at": "2026-09-25",
            "is_new": False
        },
        {
            "id": "item-10",
            "section": "trend",
            "category_badges": ["트렌드", "건강", "생활정보"],
            "d_day_badge": None,
            "title": "환절기 비염·감기 예방 면역력 영양제 성분 가이드",
            "event_date": None,
            "location": None,
            "summary": "일교차 10도 이상 벌어지는 가을 환절기 호흡기 관리. 비타민D, 프로폴리스, 퀘르세틴 성분별 효능과 공복/식후 올바른 섭취 타이밍.",
            "status": "unissued",
            "details": "아침저녁 찬바람으로 비염 증상과 환절기 면역력 저하를 호소하는 사람들이 급증했습니다. 항히스타민제 복용 전 자연 성분의 면역 강화 영양소(퀘르세틴, 프로폴리스 스프레이, 비타민D 5000IU, 아연)의 성분별 작용 기전과 복용 시간대를 알기 쉽게 전달하면 높은 체류 시간을 확보할 수 있습니다.",
            "keywords": ["환절기비염영양제", "비염퀘르세틴", "프로폴리스스프레이", "비타민D복용법", "환절기면역력", "비염환기법"],
            "blog_outline": [
                "1. 가을 환절기 비염이 심해지는 원인과 환경 관리(습도 50%)",
                "2. 비염 완화에 도움되는 핵심 영양 성분 TOP 3 (퀘르세틴/프로폴리스/아연)",
                "3. 흡수율을 2배 높이는 영양제 아침/저녁 섭취 타이밍",
                "4. 코세척기 사용법과 환절기 목 관리 팁"
            ],
            "target_audience": "만성 비염으로 고생하는 환자 및 환절기 가족 건강을 챙기는 주부",
            "created_at": "2026-09-26",
            "is_new": True
        },
        {
            "id": "item-11",
            "section": "trend",
            "category_badges": ["트렌드", "부동산", "생활정보"],
            "d_day_badge": None,
            "title": "2026 하반기 수도권 청약 전략과 대출 규제 체크포인트",
            "event_date": None,
            "location": None,
            "summary": "가을 이사철 주요 단지 분양 일정과 신생아 특례대출 소득 기준 완화 요건. 주담대 스트레스 DSR 2단계 적용에 따른 한도 계산법.",
            "status": "unissued",
            "details": "가을 이사철을 맞아 수도권 신규 분양 청약과 함께 금융권의 스트레스 DSR(총부채원리금상환비율) 2단계가 본격 시행되면서 대출 한도 축소에 대한 관심이 매우 뜨겁습니다. 반면 신생아 특례대출 소득 요건 완화 등 무주택 실수요자를 위한 정책 금융 혜택을 꼼꼼히 비교해 주는 포스팅이 호응을 얻고 있습니다.",
            "keywords": ["스트레스DSR2단계", "신생아특례대출조건", "2026가을청약", "수도권분양일정", "주택담보대출한도", "청약홈가점"],
            "blog_outline": [
                "1. 스트레스 DSR 2단계 시행 후 내 대출 한도는 얼마나 줄었을까?",
                "2. 2026 완화된 신생아 특례대출 소득 기준 및 금리 혜택",
                "3. 가을 수도권 주목할 만한 주요 분양 예정 단지 정리",
                "4. 1주택자 갈아타기 vs 무주택자 특별공급 당첨 전략"
            ],
            "target_audience": "내 집 마련을 꿈꾸는 3040 신혼부부 및 실수요 무주택 청약 대기자",
            "created_at": "2026-09-23",
            "is_new": False
        },
        {
            "id": "item-12",
            "section": "trend",
            "category_badges": ["트렌드", "전시", "여행"],
            "d_day_badge": None,
            "title": "서울 야외도서관 '책읽는 서울광장 & 광화문 책마당'",
            "event_date": None,
            "location": "서울광장·광화문광장",
            "summary": "선선한 가을바람과 함께 잔디밭 빈백에서 즐기는 도심 힐링 독서. 야간 조명 운영 시간과 무료 대여 절차, 주말 야외 전시 및 북콘서트 안내.",
            "status": "unissued",
            "details": "가을 하늘 아래 푸른 잔디밭에서 알록달록한 빈백과 파라솔에 누워 책을 읽을 수 있는 서울시 대표 힐링 프로그램입니다. 서울광장, 광화문광장, 청계천까지 이어지는 테마별 북 큐레이션 전시와 함께 해 질 녘에는 조명 텐트와 음악 공연이 어우러져 부담 없는 도심 나들이 명소로 최고입니다.",
            "keywords": ["책읽는서울광장", "광화문책마당", "서울야외도서관", "서울가을나들이", "광화문놀거리", "주말가볼만한곳"],
            "blog_outline": [
                "1. 서울 야외도서관 위치별 특징 (서울광장 vs 광화문 vs 청계천)",
                "2. 운영 요일, 시간 및 빈백 선점 노하우",
                "3. 책 대여 방법 및 아이들을 위한 팝업 북존/보드게임",
                "4. 광화문 인근 가을 산책 코스(경복궁 서촌/북촌 연결)"
            ],
            "target_audience": "가벼운 주말 도심 힐링과 책을 좋아하는 직장인, 아이 동반 가족",
            "created_at": "2026-09-24",
            "is_new": False
        },
        {
            "id": "item-13",
            "section": "trend",
            "category_badges": ["트렌드", "공연", "축제"],
            "d_day_badge": None,
            "title": "2026 가을 야외 뮤직 페스티벌 & 콘서트 라인업",
            "event_date": "2026-10-10 ~ 2026-10-12",
            "location": "난지한강공원·올림픽공원",
            "summary": "가을 감성 인디 밴드와 재즈 페스티벌 총정리. 피크닉존 자리잡기 팁, 반입 가능 물품 규정 및 대중교통 막차 시간 안내.",
            "status": "unissued",
            "details": "가을의 선선한 정취를 만끽할 수 있는 자라섬 재즈, 그랜드민트페스티벌(GMF), 난지 페스티벌 등 대표 가을 음악 축제가 10월에 집중되어 있습니다. 티켓 예매부터 입장 팔찌 수령, 돗자리 피크닉존 명당 선점과 필수 반입 가능/불가 물품(다회용기, 우산 등) 규정을 총정리합니다.",
            "keywords": ["가을페스티벌", "그랜드민트페스티벌", "자라섬재즈페스티벌", "야외콘서트준비물", "페스티벌돗자리규정", "가을뮤직페스티벌"],
            "blog_outline": [
                "1. 2026 10월 주요 가을 뮤직 페스티벌 캘린더 & 라인업 요약",
                "2. 피크닉존 명당 자리 잡기 위한 오픈 시간 & 대기 팁",
                "3. 페스티벌 반입 금지 물품(배달음식, 캔음료 등) 규정 체크",
                "4. 하루 종일 야외에 있을 때 꼭 챙겨야 할 실전 꿀템 5가지"
            ],
            "target_audience": "음악과 페스티벌 문화를 사랑하는 2030 청년 및 나들이객",
            "created_at": "2026-09-24",
            "is_new": False
        },
        {
            "id": "item-14",
            "section": "trend",
            "category_badges": ["트렌드", "팝업", "쇼핑"],
            "d_day_badge": None,
            "title": "더현대 서울 가을 캐릭터 IP & 라이프스타일 팝업",
            "event_date": "2026-10-01 ~ 2026-10-15",
            "location": "더현대 서울 지하 1~2층",
            "summary": "인기 애니메이션 및 일러스트 작가 한정판 굿즈 팝업스토어. 웨이팅 등록 순서와 단독 선착순 사은품 증정 이벤트 공략법.",
            "status": "unissued",
            "details": "더현대 서울 지하 2층 아이코닉스 존과 지하 1층 대행사장에서 진행되는 가을 팝업 라인업입니다. 인기 캐릭터 IP 굿즈 한정 발매, 포토이즘 부스, 실물 크기 조형물 포토존이 설치되어 오픈런 필수 코스로 꼽힙니다. 현대식품관 앱을 통한 원격 줄서기 팁이 필수적입니다.",
            "keywords": ["더현대서울팝업", "더현대팝업예약", "더현대서울놀거리", "여의도데이트", "현대식품관웨이팅", "캐릭터굿즈팝업"],
            "blog_outline": [
                "1. 10월 더현대 서울 진행 중인 팝업스토어 전체 목록",
                "2. 현대식품관 투홈 어플로 원격 웨이팅 빠르게 잡는 법",
                "3. 팝업 한정판 굿즈 구매 제한 및 선착순 사은품 정보",
                "4. 여의도 한강공원과 연계한 주말 실내외 데이트 코스"
            ],
            "target_audience": "굿즈 수집가, 키덜트족 및 쾌적한 실내 데이트를 찾는 쇼핑객",
            "created_at": "2026-09-26",
            "is_new": True
        }
    ]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "topics.json")

def fetch_nol_ticket_upcoming() -> List[dict]:
    """
    야놀자 놀 티켓(NOL TICKET) 콘서트 오픈예정 목록 수집
    - 필터: 장르 '콘서트' (goods_genre_codes: ['01003'])
    - 정렬: '등록순' (sort: 'register')
    - 엔드포인트: https://nol.yanolja.com/ticket/display/api/upcoming
    """
    import requests
    from bs4 import BeautifulSoup
    import re
    from datetime import datetime, date

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Referer": "https://nol.yanolja.com/ticket/display/upcoming?genre=concert&sort=register",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    upcoming_items = []
    today = date.today()
    weekday_kr = ["월", "화", "수", "목", "금", "토", "일"]

    # 1. 야놀자 공식 오픈예정 API 호출 (등록순, 콘서트)
    try:
        api_url = "https://nol.yanolja.com/ticket/display/api/upcoming"
        payload = {
            "sort": "register",  # 등록순
            "goods_genre_codes": ["01003"]  # 콘서트
        }
        resp = requests.post(api_url, json=payload, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            notices = data.get("notices", [])
            for n in notices:
                title = n.get("title", "").strip()
                if not title:
                    continue

                goods_code = str(n.get("goods_code") or n.get("id"))
                full_url = f"https://nol.yanolja.com/ticket/products/{goods_code}"

                # 등록일시 파싱 (등록순 핵심 데이터)
                created_at_raw = n.get("created_at", "")
                created_date = created_at_raw.split("T")[0] if created_at_raw else str(today)

                # 티켓 오픈 일시 및 D-Day 계산
                ticket_dates = n.get("ticket_dates", [])
                open_str = "추후공지"
                d_day_badge = "오픈예정"

                if ticket_dates:
                    t_open = ticket_dates[0].get("ticket_open_date", "")
                    if t_open and not t_open.startswith("9999"):
                        try:
                            dt = datetime.fromisoformat(t_open)
                            w_name = weekday_kr[dt.weekday()]
                            open_str = f"{dt.strftime('%m.%d')}({w_name}) {dt.strftime('%H:%M')}"
                            diff = (dt.date() - today).days
                            if diff < 0:
                                d_day_badge = "오픈종료"
                            elif diff == 0:
                                d_day_badge = "🔥 오늘 오픈"
                            else:
                                d_day_badge = f"D-{diff}"
                        except Exception:
                            open_str = t_open

                venue = n.get("venue_name") or "야놀자 놀 티켓 (NOL TICKET)"
                clean_title = re.sub(r"\[.*?\]|\<.*?\>|\(.*?\)", "", title).strip()

                # 실제 공연 일시 계산 (goods_start_date ~ goods_end_date)
                start_date = n.get("goods_start_date", "")
                end_date = n.get("goods_end_date", "")
                perf_date_str = ""
                if start_date and end_date:
                    try:
                        s_dt = datetime.fromisoformat(start_date)
                        e_dt = datetime.fromisoformat(end_date)
                        s_w = weekday_kr[s_dt.weekday()]
                        e_w = weekday_kr[e_dt.weekday()]
                        if start_date == end_date:
                            perf_date_str = f"{s_dt.strftime('%Y.%m.%d')}({s_w})"
                        elif s_dt.year == e_dt.year:
                            perf_date_str = f"{s_dt.strftime('%Y.%m.%d')}({s_w}) ~ {e_dt.strftime('%m.%d')}({e_w})"
                        else:
                            perf_date_str = f"{s_dt.strftime('%Y.%m.%d')}({s_w}) ~ {e_dt.strftime('%Y.%m.%d')}({e_w})"
                    except Exception:
                        perf_date_str = f"{start_date} ~ {end_date}" if start_date != end_date else start_date

                category_badges = ["놀 티켓 오픈예정", "공연", "콘서트"]
                if "내한" in title:
                    category_badges.append("내한공연")
                elif "팬미팅" in title or "팬미" in title:
                    category_badges.append("팬미팅")
                elif "투어" in title:
                    category_badges.append("투어")

                perf_info_text = f" | 공연일시: {perf_date_str}" if perf_date_str else ""
                summary = f"야놀자 놀 티켓 최신 등록 콘서트. 티켓 오픈: {open_str}{perf_info_text}, 장소: {venue}. 선예매 인증 및 예매 팁 안내."
                details = (
                    f"공연명: {title}\n"
                    f"티켓 오픈 일시: {open_str}\n"
                    f"실제 공연 일시: {perf_date_str if perf_date_str else '상세 페이지 참조'}\n"
                    f"공연 장소: {venue}\n"
                    f"놀 티켓 등록일: {created_date}\n"
                    f"예매 링크: {full_url}\n\n"
                    f"야놀자 놀 티켓(NOL TICKET) 콘서트 오픈예정(등록순) 상품입니다. "
                    f"공연 일시({perf_date_str})와 티켓 오픈 일정({open_str})을 비교하여 "
                    f"선예매 인증 시한, 결제 수단 사전 등록(간편결제), 구역별 시야 분석 및 취소표 공략법을 다룬 블로그 포스팅 시 "
                    f"오픈 직전 집중적인 검색 트래픽 유입을 노릴 수 있습니다."
                )

                keywords = [clean_title, f"{clean_title} 티켓팅", "놀티켓", "인터파크콘서트", f"{clean_title} 선예매", "콘서트일정"]
                blog_outline = [
                    f"1. {title} 티켓 오픈 일시({open_str}) 및 공연 기간({perf_date_str})",
                    f"2. 선예매 vs 일반예매 일정 & 팬클럽 사전 인증 방법",
                    f"3. {venue} 추천 좌석 및 구역별 시야 체크",
                    f"4. 놀 티켓 1초 컷 예매 성공 팁 & 취소표 시간대 공략"
                ]

                upcoming_items.append({
                    "id": f"nol-{goods_code}",
                    "section": "urgent",
                    "category_badges": category_badges,
                    "d_day_badge": d_day_badge,
                    "title": title,
                    "event_date": f"티켓오픈: {open_str}" if not open_str.startswith("오픈") and not open_str.startswith("티켓") else open_str,
                    "performance_date": perf_date_str,
                    "location": venue,
                    "summary": summary,
                    "status": "unissued",
                    "details": details,
                    "keywords": keywords,
                    "blog_outline": blog_outline,
                    "target_audience": f"{clean_title} 관람을 희망하는 팬덤 및 콘서트 관객",
                    "created_at": created_date,
                    "registered_at": created_at_raw,
                    "is_new": True,
                    "product_url": full_url,
                    "poster_url": n.get("goods_poster_image_url") or ""
                })

            if upcoming_items:
                # 등록순(최신 등록일시 내림차순)으로 정렬
                upcoming_items.sort(key=lambda x: x.get("registered_at", ""), reverse=True)
                return upcoming_items

    except Exception as e:
        print(f"[NOL TICKET API] Request failed, fallback to HTML scraping: {e}")

    # 2. API 실패 시 HTML 스크래핑 폴백 (등록순 URL)
    fallback_url = "https://nol.yanolja.com/ticket/display/upcoming?genre=concert&sort=register"
    try:
        html_headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "ko-KR,ko;q=0.9",
        }
        res = requests.get(fallback_url, headers=html_headers, timeout=10)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "html.parser")
            seen_ids = set()
            for a in soup.find_all("a", href=re.compile(r"/ticket/products/\d+")):
                href = a.get("href", "")
                m = re.search(r"/ticket/products/(\d+)", href)
                if not m:
                    continue
                p_id = m.group(1)
                if p_id in seen_ids:
                    continue
                seen_ids.add(p_id)

                raw_text = a.get_text(" | ", strip=True)
                parts = [p.strip() for p in raw_text.split("|") if p.strip()]
                open_time = parts[0] if len(parts) >= 2 else ""
                title = parts[1] if len(parts) >= 2 else (parts[0] if parts else "")
                if not title or title == "빈자리 없음":
                    continue

                full_url = f"https://nol.yanolja.com/ticket/products/{p_id}"
                clean_title = re.sub(r"\[.*?\]|\<.*?\>|\(.*?\)", "", title).strip()

                upcoming_items.append({
                    "id": f"nol-{p_id}",
                    "section": "urgent",
                    "category_badges": ["놀 티켓 오픈예정", "공연", "콘서트"],
                    "d_day_badge": "오픈예정",
                    "title": title,
                    "event_date": f"오픈: {open_time}",
                    "location": "야놀자 놀 티켓 (NOL TICKET)",
                    "summary": f"야놀자 놀 티켓 콘서트 오픈 예정작: {title}",
                    "status": "unissued",
                    "details": f"공연명: {title}\n오픈 일시: {open_time}\n예매 링크: {full_url}",
                    "keywords": [clean_title, "티켓팅", "놀티켓", "콘서트예매"],
                    "blog_outline": [f"1. {title} 정보", f"2. 티켓 오픈 일정({open_time})", f"3. 예매 팁"],
                    "target_audience": f"{clean_title} 관람 희망 관객",
                    "created_at": datetime.now().strftime("%Y-%m-%d"),
                    "is_new": True,
                    "product_url": full_url
                })
    except Exception as e:
        print(f"[NOL TICKET HTML] Scraper fallback failed: {e}")

    return upcoming_items

def fetch_nol_ticket_ending_soon() -> List[dict]:
    """
    야놀자 놀 티켓(NOL TICKET) 콘서트 둘러보기 - 전체 - 종료 임박순 수집
    - 웹 페이지: https://nol.yanolja.com/ticket/genre/concert
    - 위젯: 둘러보기 (YDM__NOL_MULTIPLE_FILTERED_ENTERTAINMENT_LIST__V1)
    - 탭: 전체 (category: "ALL")
    - 정렬: 종료 임박순 (SORT_FILTER: PLAY_END_DATE_ASC)
    - 엔드포인트: https://nol.yanolja.com/ticket/genre/api/cx-display/widget/v1/multiple-filtered-entertainment-list/items
    """
    import requests
    import re
    from datetime import datetime, date

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Referer": "https://nol.yanolja.com/ticket/genre/concert",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    url = "https://nol.yanolja.com/ticket/genre/api/cx-display/widget/v1/multiple-filtered-entertainment-list/items"
    ending_items = []
    today = date(2026, 9, 26) # 기준일자: 2026-09-26

    rank = 1
    for page in [1, 2]:
        try:
            payload = {
                "target": "ENTERTAINMENT:CONCERT",
                "page": page,
                "category": "ALL",
                "filters": [
                    {"key": "SORT_FILTER", "code": "PLAY_END_DATE_ASC"}
                ]
            }
            resp = requests.post(url, json=payload, headers=headers, timeout=10)
            if resp.status_code != 200:
                continue
            data = resp.json()
            items = data.get("items", [])
            for it in items:
                d = it.get("data", {})
                meta = it.get("serverLogMeta", {})
                title = d.get("title", "").strip()
                if not title:
                    continue

                product_id = str(meta.get("productId") or d.get("id"))
                full_url = d.get("action", {}).get("web") or f"https://nol.yanolja.com/ticket/products/{product_id}"
                date_info = d.get("dateInfo", "").strip()
                venue = d.get("locationDetails", [""])[0] if d.get("locationDetails") else (meta.get("placeName") or "공연장")
                poster_url = d.get("thumbnail") or ""
                benefit_badges = [b.get("text") for b in d.get("benefitBadges", []) if b.get("text")]

                # 마감일 파싱 및 D-Day 계산
                end_date_str = ""
                end_date_sort = "9999-12-31"
                d_day_badge = "마감임박"
                if "~" in date_info:
                    parts = [p.strip() for p in date_info.split("~")]
                    end_date_str = parts[1]
                else:
                    end_date_str = date_info.strip()

                try:
                    e_parts = end_date_str.split(".")
                    if len(e_parts) == 3:
                        year = 2000 + int(e_parts[0]) if len(e_parts[0]) == 2 else int(e_parts[0])
                        month = int(e_parts[1])
                        day = int(e_parts[2])
                        end_dt = date(year, month, day)
                        end_date_sort = end_dt.strftime("%Y-%m-%d")
                        diff = (end_dt - today).days
                        if diff < 0:
                            d_day_badge = "마감"
                        elif diff == 0:
                            d_day_badge = "🔥 오늘 마감"
                        elif diff == 1:
                            d_day_badge = "D-1 마감"
                        else:
                            d_day_badge = f"D-{diff} 마감"
                except Exception:
                    pass

                clean_title = re.sub(r"\[.*?\]|\<.*?\>|\(.*?\)", "", title).strip()

                category_badges = ["종료 임박 콘서트", "공연", "콘서트"]
                if "단독판매" in benefit_badges:
                    category_badges.append("단독판매")
                if "내한" in title or meta.get("subGenreName") == "내한공연":
                    category_badges.append("내한공연")
                if "팬미팅" in title or "FANMEETING" in title:
                    category_badges.append("팬미팅")
                if "페스티벌" in title or "FESTIVAL" in title:
                    category_badges.append("페스티벌")

                summary = (
                    f"야놀자 놀 티켓 둘러보기(종료 임박순 #{rank}). 공연 기간: {date_info}, 장소: {venue}. "
                    f"{d_day_badge} 긴급 관람 팁 및 현장 수령·입장 안내."
                )

                details = (
                    f"공연명: {title}\n"
                    f"공연 일정: {date_info} ({d_day_badge})\n"
                    f"공연 장소: {venue}\n"
                    f"예매 혜택: {', '.join(benefit_badges) if benefit_badges else '일반예매'}\n"
                    f"둘러보기 순위: 종료 임박순 #{rank}\n"
                    f"놀 티켓 예매 바로가기: {full_url}\n\n"
                    f"야놀자 놀 티켓 콘서트 둘러보기 섹션에서 현재 '종료 임박순'으로 {rank}위에 랭크된 공연입니다. "
                    f"공연 종료일({end_date_str})이 {d_day_badge} 상태이므로, 막차 티켓팅을 준비하는 관객이나 당일 현장 수령 및 "
                    f"입장 안내, 구역별 시야 후기 포스팅 시 즉각적인 트래픽을 노릴 수 있습니다."
                )

                keywords = [clean_title, f"{clean_title} 콘서트", f"{clean_title} 시야", f"{venue} 좌석", "놀티켓", "콘서트종료임박", "막차예매"]
                blog_outline = [
                    f"1. {title} 기본 정보 및 공연 일정({date_info}) - {d_day_badge}",
                    f"2. {venue} 좌석 배치도 및 구역별 추천 시야/음향 특징",
                    f"3. 공연 당일 현장 매표소 수령 시간 & 필수 준비물(신분증/예매내역)",
                    f"4. 공연장 오시는 길(대중교통/셔틀) & 주변 주차장·식당 꿀팁"
                ]

                ending_items.append({
                    "id": f"nol-ending-{product_id}",
                    "section": "urgent",
                    "category_badges": category_badges,
                    "d_day_badge": d_day_badge,
                    "title": title,
                    "event_date": f"마감일: {end_date_str}" if end_date_str else None,
                    "performance_date": date_info,
                    "location": venue,
                    "summary": summary,
                    "status": "unissued",
                    "details": details,
                    "keywords": keywords,
                    "blog_outline": blog_outline,
                    "target_audience": f"{clean_title} 관람을 앞두고 있거나 막차 예매를 고민하는 음악 팬",
                    "created_at": datetime.now().strftime("%Y-%m-%d"),
                    "registered_at": datetime.now().strftime("%Y-%m-%d") + f"T00:00:{rank:02d}",
                    "is_new": True,
                    "product_url": full_url,
                    "poster_url": poster_url,
                    "closing_rank": rank,
                    "end_date_sort": end_date_sort
                })
                rank += 1
        except Exception as e:
            print(f"[NOL TICKET ENDING SOON] Page {page} error: {e}")

    return ending_items

def fetch_nol_ticket_exhibition_ending_soon() -> List[dict]:
    """
    야놀자 놀 티켓(NOL TICKET) 전시 둘러보기 - 전체 - 종료 임박순 수집
    - 웹 페이지: https://nol.yanolja.com/ticket/genre/exhibition
    - 위젯: 둘러보기 (YDM__NOL_MULTIPLE_FILTERED_ENTERTAINMENT_LIST__V1)
    - 탭: 전체 (category: "ALL")
    - 정렬: 종료 임박순 (SORT_FILTER: PLAY_END_DATE_ASC)
    - 엔드포인트: https://nol.yanolja.com/ticket/genre/api/cx-display/widget/v1/multiple-filtered-entertainment-list/items
    """
    import requests
    import re
    from datetime import datetime, date

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Referer": "https://nol.yanolja.com/ticket/genre/exhibition",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    url = "https://nol.yanolja.com/ticket/genre/api/cx-display/widget/v1/multiple-filtered-entertainment-list/items"
    ending_items = []
    today = date(2026, 9, 26) # 기준일자: 2026-09-26

    rank = 1
    for page in [1, 2]:
        try:
            payload = {
                "target": "ENTERTAINMENT:EXHIBITION",
                "page": page,
                "category": "ALL",
                "filters": [
                    {"key": "SORT_FILTER", "code": "PLAY_END_DATE_ASC"}
                ]
            }
            resp = requests.post(url, json=payload, headers=headers, timeout=10)
            if resp.status_code != 200:
                continue
            data = resp.json()
            items = data.get("items", [])
            for it in items:
                d = it.get("data", {})
                meta = it.get("serverLogMeta", {})
                title = d.get("title", "").strip()
                if not title:
                    continue

                product_id = str(meta.get("productId") or d.get("id"))
                full_url = d.get("action", {}).get("web") or f"https://nol.yanolja.com/ticket/products/{product_id}"
                date_info = d.get("dateInfo", "").strip()
                venue = d.get("locationDetails", [""])[0] if d.get("locationDetails") else (meta.get("placeName") or "전시장")
                poster_url = d.get("thumbnail") or ""
                benefit_badges = [b.get("text") for b in d.get("benefitBadges", []) if b.get("text")]

                # 마감일 파싱 및 D-Day 계산
                end_date_str = ""
                end_date_sort = "9999-12-31"
                d_day_badge = "마감임박"
                if "~" in date_info:
                    parts = [p.strip() for p in date_info.split("~")]
                    end_date_str = parts[1]
                else:
                    end_date_str = date_info.strip()

                try:
                    e_parts = end_date_str.split(".")
                    if len(e_parts) == 3:
                        year = 2000 + int(e_parts[0]) if len(e_parts[0]) == 2 else int(e_parts[0])
                        month = int(e_parts[1])
                        day = int(e_parts[2])
                        end_dt = date(year, month, day)
                        end_date_sort = end_dt.strftime("%Y-%m-%d")
                        diff = (end_dt - today).days
                        if diff < 0:
                            d_day_badge = "마감"
                        elif diff == 0:
                            d_day_badge = "🔥 오늘 마감"
                        elif diff == 1:
                            d_day_badge = "D-1 마감"
                        else:
                            d_day_badge = f"D-{diff} 마감"
                except Exception:
                    pass

                clean_title = re.sub(r"\[.*?\]|\<.*?\>|\(.*?\)", "", title).strip()

                category_badges = ["종료 임박 전시", "전시", "문화"]
                if "단독판매" in benefit_badges:
                    category_badges.append("단독판매")
                if "도슨트" in title:
                    category_badges.append("도슨트")
                if "미술관" in venue or "미술" in title:
                    category_badges.append("미술관")
                if "박물관" in venue or "박물관" in title:
                    category_badges.append("박물관")
                if "야간" in title:
                    category_badges.append("야간관람")

                summary = (
                    f"야놀자 놀 티켓 전시 둘러보기(종료 임박순 #{rank}). 전시 기간: {date_info}, 장소: {venue}. "
                    f"{d_day_badge} 폐막 전 필수 관람 포인트 및 도슨트·예약 팁."
                )

                details = (
                    f"전시명: {title}\n"
                    f"전시 일정: {date_info} ({d_day_badge})\n"
                    f"전시 장소: {venue}\n"
                    f"관람 혜택: {', '.join(benefit_badges) if benefit_badges else '일반예매'}\n"
                    f"둘러보기 순위: 전시 종료 임박순 #{rank}\n"
                    f"놀 티켓 예매 바로가기: {full_url}\n\n"
                    f"야놀자 놀 티켓 전시 둘러보기 섹션에서 현재 '종료 임박순'으로 {rank}위에 랭크된 전시입니다. "
                    f"전시 종료일({end_date_str})이 {d_day_badge} 상태로, 폐막 전 막차 관람객을 위한 전시 하이라이트, "
                    f"도슨트 시간표, 주차/대중교통 팁 및 사진 촬영 스팟 안내 포스팅 시 높은 검색 유입을 기대할 수 있습니다."
                )

                keywords = [clean_title, f"{clean_title} 후기", f"{clean_title} 도슨트", f"{venue} 주차", "서울전시회", "전시종료임박", "가을전시추천"]
                blog_outline = [
                    f"1. {title} 전시 기본 정보 및 마감 일정({date_info}) - {d_day_badge}",
                    f"2. 놓치지 말아야 할 대표 전시 구역 & 인생샷 포토존 안내",
                    f"3. 공식 도슨트/오디오 가이드 프로그램 운영 시간 및 팁",
                    f"4. 관람 시간 소요 팁, 주차 요금 감면 및 주변 데이트 코스"
                ]

                ending_items.append({
                    "id": f"nol-exhibition-ending-{product_id}",
                    "section": "urgent",
                    "category_badges": category_badges,
                    "d_day_badge": d_day_badge,
                    "title": title,
                    "event_date": f"마감일: {end_date_str}" if end_date_str else None,
                    "performance_date": f"전시: {date_info}",
                    "location": venue,
                    "summary": summary,
                    "status": "unissued",
                    "details": details,
                    "keywords": keywords,
                    "blog_outline": blog_outline,
                    "target_audience": f"{clean_title} 폐막 전 관람을 서두르는 문화예술 애호가 및 주말 나들이 관람객",
                    "created_at": datetime.now().strftime("%Y-%m-%d"),
                    "registered_at": datetime.now().strftime("%Y-%m-%d") + f"T00:00:{rank:02d}",
                    "is_new": True,
                    "product_url": full_url,
                    "poster_url": poster_url,
                    "closing_rank": rank,
                    "end_date_sort": end_date_sort
                })
                rank += 1
        except Exception as e:
            print(f"[NOL TICKET EXHIBITION ENDING SOON] Page {page} error: {e}")

    return ending_items

def fetch_melon_ticket_upcoming() -> List[dict]:
    """
    멜론 티켓(Melon Ticket) 콘서트 오픈소식 수집
    - 조건: 장르 콘서트(schGcode=GENRE_CON_ALL), 등록순(orderType=0)
    - 엔드포인트: https://ticket.melon.com/csoon/ajax/listTicketOpen.htm
    """
    import requests
    from bs4 import BeautifulSoup
    import re
    from datetime import datetime, date
    from concurrent.futures import ThreadPoolExecutor

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Referer": "https://ticket.melon.com/csoon/index.htm",
    }

    today = date.today()
    melon_items = []
    seen_ids = set()
    raw_list = []

    try:
        for offset in [1, 11]:
            params = {
                "orderType": "0",  # 등록순
                "pageIndex": str(offset),
                "schGcode": "GENRE_CON_ALL",
                "schText": "",
                "schDt": ""
            }
            resp = requests.get("https://ticket.melon.com/csoon/ajax/listTicketOpen.htm", headers=headers, params=params, timeout=10)
            if resp.status_code != 200:
                continue

            soup = BeautifulSoup(resp.text, "html.parser")
            lis = soup.select(".list_ticket_cont > li")
            for li in lis:
                tit_el = li.select_one(".link_consert .tit")
                if not tit_el:
                    continue
                href = tit_el.get("href", "")
                csoon_id = href.split("csoonId=")[-1] if "csoonId=" in href else ""
                if not csoon_id or csoon_id in seen_ids:
                    continue
                seen_ids.add(csoon_id)

                full_title = tit_el.text.strip()
                date_el = li.select_one(".ticket_data .date")
                reg_el = li.select_one(".register_info .txt_date")
                img_el = li.select_one(".poster img")

                open_date_raw = date_el.text.strip() if date_el else ""
                reg_date_raw = reg_el.text.strip() if reg_el else datetime.now().strftime("%Y-%m-%d")
                poster_url = img_el.get("src", "") if img_el else ""
                if "/melon/resize/" in poster_url:
                    poster_url = poster_url.split("/melon/resize/")[0]

                raw_list.append({
                    "csoon_id": csoon_id,
                    "title": full_title,
                    "open_date_raw": open_date_raw,
                    "reg_date": reg_date_raw,
                    "poster_url": poster_url
                })
    except Exception as e:
        print(f"[Melon Ticket] List fetch error: {e}")

    # 예비 데이터 (네트워크 차단 등 비상시에도 15개 콘서트 100% 보장)
    if not raw_list:
        raw_list = [
            {"csoon_id": "12938", "title": "Blue Hour : 잠들지 못한 마음은 티켓 오픈 안내", "open_date_raw": "2026.09.29(화) 11:00", "reg_date": "2026.09.22", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/2026092309574084a08436-9802-4398-a454-1c7cbab5adc9.jpg"},
            {"csoon_id": "12937", "title": "가을 수집가 : 첫 번째 낙엽 티켓 오픈 안내", "open_date_raw": "2026.09.23(수) 18:00", "reg_date": "2026.09.22", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/2026092210174669a9d3b0-808e-4cef-a81f-e03da788c4c5.jpg"},
            {"csoon_id": "12936", "title": "도깨비제: 이매망량(魑魅魍魎) 티켓 오픈 안내", "open_date_raw": "2026.09.23(수) 20:00", "reg_date": "2026.09.22", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/20260922100643c92c6b4d-2e93-4745-9747-ab781098b986.jpg"},
            {"csoon_id": "12935", "title": "화노 x FLEET ‘THERMAL SHOCK’ 티켓 오픈 안내", "open_date_raw": "2026.09.29(화) 20:00", "reg_date": "2026.09.22", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/20260922165518cb60b12b-2553-4917-822f-039f71c4cb73.jpg"},
            {"csoon_id": "12934", "title": "Live Your Life 티켓 오픈 안내", "open_date_raw": "2026.09.28(월) 20:00", "reg_date": "2026.09.22", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/20260922152044cc60f5c3-e613-4f3f-8878-76d7a0aab93d.jpg"},
            {"csoon_id": "12933", "title": "숲세권 라이브 : 블루화 단독 공연 〈BLU Forest〉 티켓 오픈 안내", "open_date_raw": "2026.09.28(월) 20:00", "reg_date": "2026.09.22", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/20260922144726cd5508a6-ca18-4bfb-a982-f0808cf7ee91.jpg"},
            {"csoon_id": "12932", "title": "먼데이프로젝트 시즌9 [오로라 앨범 발매 콘서트 ‘On My Way’] 티켓 오픈 안내", "open_date_raw": "2026.10.01(목) 20:00", "reg_date": "2026.09.22", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/20260922123512cd6a32a6-2f04-4e2b-bbd7-54877e8a3683.jpg"},
            {"csoon_id": "12930", "title": "DAZBEE ORCHESTRA CONCERT : SYMPHONIA 티켓 오픈 안내", "open_date_raw": "2026.09.30(수) 18:00", "reg_date": "2026.09.21", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/2026092117565780a84e60-4966-41f2-bf23-86b2fe99bc59.jpg"},
            {"csoon_id": "12929", "title": "한·일 인디 음악 협연, 손님맞이 (차강사르, 문웅주, 밍기뉴, 웃옷) 티켓 오픈 안내", "open_date_raw": "2026.09.23(수) 18:00", "reg_date": "2026.09.21", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/2026092116035041a6b0c2-55db-441d-9bf9-e317d74dbd22.jpg"},
            {"csoon_id": "12928", "title": "여전히 소란스럽게 Vol.02 노브레인 with 크라잉넛, 초록불꽃소년단 티켓 오픈 안내", "open_date_raw": "2026.09.23(수) 16:00", "reg_date": "2026.09.21", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/20260921151624b42f36ca-432a-4db5-b8aa-f173f47e3a96.jpg"},
            {"csoon_id": "12920", "title": "문없는집X에로틱웜즈익스히비션 기획공연 〈청명: 정상까지 단 100m〉 티켓 오픈 안내", "open_date_raw": "2026.09.23(수) 20:00", "reg_date": "2026.09.21", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/20260921111927883fc516-7ce5-412e-b61d-a0bb3614457e.jpg"},
            {"csoon_id": "12919", "title": "노아코스트x취향상점 ‘Goodbye Summer’ 티켓 오픈 안내", "open_date_raw": "2026.09.28(월) 20:00", "reg_date": "2026.09.21", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/20260921110024765d1d64-e40e-436f-8d96-0a02cfc80b55.jpg"},
            {"csoon_id": "12918", "title": "버츄얼 X 밴드 라이브 콘서트 〈SCHOOL OF ROCK!〉 티켓 오픈 안내", "open_date_raw": "2026.10.02(금) 14:00", "reg_date": "2026.09.21", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/20260921102657e5108bb6-1c5c-4c60-843e-ad91b93ae7e6.jpg"},
            {"csoon_id": "12915", "title": "변하은 앨범 발매 기념 단독 공연 ‘초원의 집’ 티켓 오픈 안내", "open_date_raw": "2026.09.28(월) 20:00", "reg_date": "2026.09.21", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/2026092110255850901e13-d1ea-42f0-94cb-59e51c8a14ec.jpg"},
            {"csoon_id": "12914", "title": "먼데이프로젝트 시즌9 [매기스가든 단독 콘서트 ‘pouring love and letters’] 티켓 오픈 안내", "open_date_raw": "2026.09.29(화) 20:00", "reg_date": "2026.09.21", "poster_url": "https://cdnticket.melon.co.kr/resource/image/upload/ticketopen/2026/09/20260921101905335272a2-4a00-47b8-809d-cb9e4d5fb07f.jpg"},
        ]

    # 세부 페이지 비동기 병렬 수집
    def fetch_detail(item):
        cid = item["csoon_id"]
        detail_url = f"https://ticket.melon.com/csoon/detail.htm?csoonId={cid}"
        venue, perf = "", ""
        try:
            r = requests.get(detail_url, headers=headers, timeout=5)
            if r.status_code == 200:
                text = BeautifulSoup(r.text, "html.parser").get_text()
                mv = re.search(r"(?:공\s*연\s*장\s*소?|장\s*소)\s*[:：]\s*([^\n\r]+)", text)
                if mv:
                    venue = re.split(r"-\s*관람|-\s*티켓|-\s*공연|-\s*예매|-\s*장소|-\s*문의|-\s*주최", mv.group(1))[0].strip()
                md = re.search(r"(?:공\s*연\s*일\s*시?|일\s*시|공\s*연\s*기\s*간?)\s*[:：]\s*([^\n\r]+)", text)
                if md:
                    perf = re.split(r"-\s*관람|-\s*티켓|-\s*공연|-\s*장소|-\s*예매|-\s*주최", md.group(1))[0].strip()
        except Exception:
            pass
        return cid, venue, perf

    detail_map = {}
    try:
        with ThreadPoolExecutor(max_workers=5) as executor:
            for cid, venue, perf in executor.map(fetch_detail, raw_list):
                detail_map[cid] = (venue, perf)
    except Exception as e:
        print(f"[Melon Ticket] Detail fetch error: {e}")

    for rank, it in enumerate(raw_list, start=1):
        cid = it["csoon_id"]
        title = it["title"]
        open_date_raw = it["open_date_raw"]
        reg_date = it["reg_date"]
        poster_url = it["poster_url"]
        venue, perf_date = detail_map.get(cid, ("", ""))
        if not venue:
            venue = "멜론 티켓 (Melon Ticket)"

        clean_title = re.sub(r"티켓\s*오픈\s*안내$", "", title).strip()
        clean_title_short = re.sub(r"\[.*?\]|\<.*?\>|\(.*?\)", "", clean_title).strip()

        # D-Day 계산 및 오픈일 표기 정제
        d_day_badge = "오픈예정"
        display_open_date = open_date_raw
        if "보기" in open_date_raw or not open_date_raw:
            display_open_date = "오픈일정 상세페이지 참조"

        m_dt = re.search(r"(\d{4})[.\-](\d{2})[.\-](\d{2})", open_date_raw)
        if m_dt:
            try:
                op_dt = date(int(m_dt.group(1)), int(m_dt.group(2)), int(m_dt.group(3)))
                diff = (op_dt - today).days
                if diff < 0:
                    d_day_badge = "오픈종료"
                elif diff == 0:
                    d_day_badge = "🔥 오늘 오픈"
                elif diff == 1:
                    d_day_badge = "D-1 오픈"
                else:
                    d_day_badge = f"D-{diff} 오픈"
            except Exception:
                pass

        full_url = f"https://ticket.melon.com/csoon/detail.htm?csoonId={cid}"

        summary = f"멜론 티켓 단독/오픈 콘서트 소식. 티켓 오픈 {display_open_date}, 공연 {perf_date if perf_date else '상세 안내 참조'} @ {venue}. 멜론 티켓팅 일정 및 좌석 예매 꿀팁."

        details = (
            f"멜론 티켓 콘서트 오픈소식 안내입니다.\n\n"
            f"■ 공연명: {clean_title}\n"
            f"■ 티켓 오픈: {display_open_date}\n"
            f"■ 공연 일시: {perf_date if perf_date else '멜론 티켓 상세페이지 참조'}\n"
            f"■ 공연 장소: {venue}\n"
            f"■ 예매처: 멜론 티켓 (Melon Ticket)\n\n"
            f"인기 콘서트의 경우 예매 시작과 동시에 빠른 매진이 예상됩니다. 사전에 멜론 티켓 회원가입 및 본인인증(휴대폰/I-PIN)을 완료해 두시고, 표준시계(서버시간)를 확인하여 정각에 예매창에 진입하시기 바랍니다."
        )

        keywords = [
            clean_title_short,
            f"{clean_title_short} 콘서트",
            f"{clean_title_short} 티켓팅",
            "멜론티켓 오픈",
            "멜론티켓 예매",
            f"{clean_title_short} 예매일정",
            f"{venue} 시야"
        ]

        blog_outline = [
            f"1. {clean_title_short} 콘서트 기본 정보 및 티켓 오픈 일정 ({display_open_date})",
            f"2. 공연 장소 ({venue}) 좌석 배치도 및 추천 명당 시야",
            f"3. 멜론 티켓팅 성공 전략 (서버시간 체크 & 결제 수단 사전 등록)",
            f"4. 모바일 티켓 발권 안내 및 현장 입장 주의사항"
        ]

        melon_items.append({
            "id": f"melon-ticket-{cid}",
            "section": "urgent",
            "category_badges": ["멜론 티켓 오픈소식", "콘서트", "공연"],
            "d_day_badge": d_day_badge,
            "title": title,
            "event_date": f"오픈: {display_open_date}",
            "performance_date": f"공연: {perf_date}" if perf_date else None,
            "location": venue,
            "summary": summary,
            "status": "unissued",
            "details": details,
            "keywords": keywords,
            "blog_outline": blog_outline,
            "target_audience": f"{clean_title_short} 콘서트 관람을 원하는 팬 및 주말 문화생활 관객",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "registered_at": f"{reg_date}T00:00:{rank:02d}",
            "melon_order": rank,
            "melon_csoon_id": int(cid) if cid.isdigit() else 0,
            "is_new": True,
            "product_url": full_url,
            "poster_url": poster_url
        })

    return melon_items

def fetch_yes24_ticket_notices() -> List[dict]:
    """
    예스24 티켓(YES24 Ticket) 오픈공지 수집
    - 조건: 등록순(order=1), 제목에 '뮤지컬' 포함 항목 제외
    - 목록 엔드포인트: https://ticket.yes24.com/New/Notice/Ajax/axList.aspx (POST)
    - 상세 엔드포인트: https://ticket.yes24.com/New/Notice/Ajax/axRead.aspx (POST, bId)
    """
    import requests
    from bs4 import BeautifulSoup
    import re
    from datetime import datetime, date
    from concurrent.futures import ThreadPoolExecutor

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Referer": "https://ticket.yes24.com/Notice",
    }

    today = date.today()
    yes24_items = []
    seen_ids = set()
    raw_list = []

    try:
        for page in [1, 2]:
            payload = {
                "page": str(page),
                "size": "20",
                "genre": "",
                "province": "",
                "order": "1",  # 등록순
                "searchType": "All",
                "searchText": ""
            }
            res = requests.post("https://ticket.yes24.com/New/Notice/Ajax/axList.aspx", data=payload, headers=headers, timeout=10)
            if res.status_code != 200:
                continue

            soup = BeautifulSoup(res.text, "html.parser")
            rows = soup.select(".noti-tbl table tbody tr")
            for tr in rows:
                tds = tr.find_all("td")
                if len(tds) < 4:
                    continue
                cat_type = tds[0].get_text(strip=True)
                a_tag = tds[1].find("a")
                if not a_tag:
                    continue
                title = a_tag.get_text(strip=True)
                href = a_tag.get("href", "")
                m_id = re.search(r"id=(\d+)", href)
                bid = m_id.group(1) if m_id else ""
                open_time = tds[2].get_text(" ", strip=True)

                # 제목에 뮤지컬 들어가는 건 제외
                if "뮤지컬" in title:
                    continue

                if bid and bid not in seen_ids:
                    seen_ids.add(bid)
                    raw_list.append({
                        "id": bid,
                        "type": cat_type,
                        "title": title,
                        "open_time": open_time
                    })
    except Exception as e:
        print(f"[YES24 Ticket] List fetch error: {e}")

    # 비상시 예비 데이터
    if not raw_list:
        raw_list = [
            {"id": "18572", "type": "티켓오픈", "title": "단독판매[대전] 2026 크리스마스 가족매직쇼 [산타의 선물] 티켓오픈 안내", "open_time": "2026.09.28(월) 10:00"},
            {"id": "18571", "type": "티켓오픈", "title": "THE GREATEST: 전율 소향 X 김기태 - 춘천 티켓 오픈 안내", "open_time": "2026.09.30(수) 11:00"},
            {"id": "18569", "type": "티켓오픈", "title": "[공주] [데뷔 60주년 기념공연] 2026 남진 전국투어 콘서트 티켓 오픈 안내", "open_time": "2026.09.29(화) 11:00"},
            {"id": "18566", "type": "티켓오픈", "title": "단독판매EVNNE FAN-CONCERT [ONE TAKE] IN SEOUL 티켓 오픈 안내", "open_time": "2026.10.15(목) 20:00"},
            {"id": "18565", "type": "티켓오픈", "title": "단독판매K-발레컬 김옥련발레단 금관물길510Km 티켓오픈 안내", "open_time": "2026.09.30(수) 14:00"},
            {"id": "18563", "type": "티켓오픈", "title": "2025-26 김창옥 토크콘서트 시즌5  - 수원 티켓 오픈 안내", "open_time": "2026.09.23(수) 10:00"},
            {"id": "18561", "type": "티켓오픈", "title": "단독판매2026 윤마치(MRCH) CONCERT [공생관계 : We Live Together] 티켓 오픈 안내", "open_time": "2026.10.06(화) 20:00"},
            {"id": "18560", "type": "티켓오픈", "title": "단독판매[평택] 두 명의 작곡가, 여덟 개의 계절 티켓 오픈 안내", "open_time": "2026.09.29(화) 14:00"},
            {"id": "18557", "type": "티켓오픈", "title": "[고양] 2026 겨울특집 가족매직쇼 [버블J의 스노우버블쇼] 티켓오픈 안내", "open_time": "2026.09.23(수) 10:00"},
            {"id": "18556", "type": "티켓오픈", "title": "[이천] 2026 빅3 “행복한 만남”- 강진, 김용임, 진성 티켓 오픈 안내", "open_time": "2026.09.29(화) 13:00"},
            {"id": "18555", "type": "티켓오픈", "title": "단독판매연극 〈스타크로스드〉 2차 티켓오픈 안내", "open_time": "2026.09.23(수) 14:00"},
            {"id": "18553", "type": "티켓오픈", "title": "단독판매[평택] 2026 시조 전국명인 초대전 티켓 오픈 안내", "open_time": "2026.09.22(화) 14:00"},
            {"id": "18551", "type": "티켓오픈", "title": "단독판매[광주] 김동규  - 10월의 어느 멋진날에 티켓 오픈 안내", "open_time": "2026.09.22(화) 15:00"},
            {"id": "18550", "type": "티켓오픈", "title": "2026 서초문화원 창작오페라 [매헌 윤봉길] 티켓오픈 안내", "open_time": "2026.09.28(월) 10:00"},
            {"id": "18549", "type": "티켓오픈", "title": "2026 김정민 전국투어 : 정민이형 콘서트 - 구리 티켓 오픈 안내", "open_time": "2026.09.23(수) 11:00"}
        ]

    # 세부 정보 비동기 병렬 수집
    def fetch_detail(item):
        bid = item["id"]
        venue, perf, reg_date, poster = "", "", "", ""
        try:
            payload = {"bId": bid, "genre": "", "province": "", "order": "1"}
            res = requests.post("https://ticket.yes24.com/New/Notice/Ajax/axRead.aspx", data=payload, headers=headers, timeout=5)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                img = soup.find("img")
                if img and img.get("src"):
                    p_src = img.get("src")
                    poster = f"https:{p_src}" if p_src.startswith("//") else p_src
                for s in soup.find_all("script"):
                    s.decompose()
                text = soup.get_text("\n", strip=True)
                m_reg = re.search(r"등록일\s*[:：]\s*([^\n\r]+)", text)
                if m_reg:
                    reg_date = m_reg.group(1).strip()
                m_venue = re.search(r"(?:공\s*연\s*장\s*소?|장\s*소)\s*[:：]\s*([^\n\r]+)", text)
                if m_venue:
                    venue = re.split(r"-\s*관람|-\s*티켓|-\s*공연|-\s*예매|-\s*장소|-\s*문의|-\s*주최|-\s*가격|-\s*일시", m_venue.group(1))[0].strip()
                m_perf = re.search(r"(?:공\s*연\s*일\s*시?|공\s*연\s*기\s*간?|일\s*시)\s*[:：]\s*([^\n\r]+)", text)
                if m_perf:
                    perf = re.split(r"-\s*관람|-\s*티켓|-\s*공연|-\s*장소|-\s*예매|-\s*주최|-\s*가격|-\s*문의", m_perf.group(1))[0].strip()
        except Exception:
            pass
        return bid, reg_date, venue, perf, poster

    detail_map = {}
    try:
        with ThreadPoolExecutor(max_workers=5) as executor:
            for bid, reg_date, venue, perf, poster in executor.map(fetch_detail, raw_list[:20]):
                detail_map[bid] = (reg_date, venue, perf, poster)
    except Exception as e:
        print(f"[YES24 Ticket] Detail fetch error: {e}")

    for rank, it in enumerate(raw_list[:20], start=1):
        bid = it["id"]
        title = it["title"]
        open_time = it["open_time"]
        reg_date, venue, perf_date, poster_url = detail_map.get(bid, ("", "", "", ""))
        if not reg_date:
            reg_date = datetime.now().strftime("%Y-%m-%d")

        # 지역명 및 공연장 보정
        if not venue:
            m_loc = re.search(r"\[(서울|인천|대전|대구|부산|광주|울산|수원|춘천|공주|고양|평택|이천|구리|성남|천안|전주|창원|제주)[^\]]*\]", title)
            if m_loc:
                venue = f"{m_loc.group(1)} (예스24 티켓 예매)"
            else:
                venue = "예스24 티켓 (YES24)"

        clean_title = re.sub(r"티켓\s*오픈\s*안내$", "", title).strip()
        clean_title_short = re.sub(r"\[.*?\]|\<.*?\>|\(.*?\)", "", clean_title).strip()

        # D-Day 계산
        d_day_badge = "오픈예정"
        display_open_time = open_time
        m_dt = re.search(r"(\d{4})[.\-](\d{2})[.\-](\d{2})", open_time)
        if m_dt:
            try:
                op_dt = date(int(m_dt.group(1)), int(m_dt.group(2)), int(m_dt.group(3)))
                diff = (op_dt - today).days
                if diff < 0:
                    d_day_badge = "오픈종료"
                elif diff == 0:
                    d_day_badge = "🔥 오늘 오픈"
                elif diff == 1:
                    d_day_badge = "D-1 오픈"
                else:
                    d_day_badge = f"D-{diff} 오픈"
            except Exception:
                pass

        full_url = f"https://ticket.yes24.com/Notice#id={bid}"

        summary = f"예스24 티켓 오픈 안내. 티켓 오픈 {display_open_time}, 공연 {perf_date if perf_date else '상세 안내 참조'} @ {venue}. 예스24 예매 일정 및 티켓팅 꿀팁."

        details = (
            f"예스24 티켓(YES24) 공식 오픈안내 소식입니다.\n\n"
            f"■ 공연/행사명: {clean_title}\n"
            f"■ 티켓 오픈: {display_open_time}\n"
            f"■ 공연 일시: {perf_date if perf_date else '예스24 공지 상세 참조'}\n"
            f"■ 공연 장소: {venue}\n"
            f"■ 예매처: 예스24 티켓 (YES24)\n\n"
            f"예스24 단독/선예매가 진행되는 인기 공연으로 빠른 매진이 예상됩니다. 예스24 본인인증 완료 여부와 결제 수단 등록 상태를 미리 점검하시기 바랍니다."
        )

        keywords = [
            clean_title_short,
            f"{clean_title_short} 콘서트",
            f"{clean_title_short} 예매",
            f"{clean_title_short} 티켓팅",
            "예스24티켓 오픈",
            "예스24 티켓팅",
            f"{venue} 좌석"
        ]

        blog_outline = [
            f"1. {clean_title_short} 공연 기본 개요 및 티켓 오픈 일정 ({display_open_time})",
            f"2. 공연 장소 ({venue}) 시야 및 추천 좌석 팁",
            f"3. 예스24 티켓팅 성공 비법 (예매창 진입 & 직링 대기 팁)",
            f"4. 예매 수수료, 취소 마감 시간 및 모바일 발권 안내"
        ]

        yes24_items.append({
            "id": f"yes24-ticket-{bid}",
            "section": "urgent",
            "category_badges": ["예스24 티켓", "콘서트", "공연"],
            "d_day_badge": d_day_badge,
            "title": title,
            "event_date": f"오픈: {display_open_time}",
            "performance_date": f"공연: {perf_date}" if perf_date else None,
            "location": venue,
            "summary": summary,
            "status": "unissued",
            "details": details,
            "keywords": keywords,
            "blog_outline": blog_outline,
            "target_audience": f"{clean_title_short} 관람을 희망하는 예스24 예매 관람객 및 팬덤",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "registered_at": f"{reg_date}T00:00:{rank:02d}",
            "yes24_order": rank,
            "yes24_id": int(bid) if bid.isdigit() else 0,
            "is_new": True,
            "product_url": full_url,
            "poster_url": poster_url
        })

    return yes24_items

def save_topics():
    os.makedirs(DATA_DIR, exist_ok=True)
    
    # 1. 기존 topics.json 불러오기
    existing_items = {}
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                for item in loaded:
                    existing_items[item["id"]] = item
        except Exception as e:
            print(f"[Warning] Could not read existing topics.json: {e}")

    # 2. 기본 큐레이션 트렌드 데이터 로드
    base_items = fetch_sample_data()
    
    # 3. 야놀자 놀 티켓 실시간 오픈예정 공연 데이터 수집
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetching upcoming concerts from NOL Yanolja...")
    nol_upcoming_items = fetch_nol_ticket_upcoming()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetched {len(nol_upcoming_items)} upcoming concerts from NOL Ticket.")

    # 4. 멜론 티켓 실시간 콘서트 오픈소식 (등록순) 데이터 수집
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetching concert notices from Melon Ticket (콘서트 - 등록순)...")
    melon_items = fetch_melon_ticket_upcoming()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetched {len(melon_items)} concert notices from Melon Ticket.")

    # 5. 예스24 티켓 실시간 오픈공지 (등록순, 뮤지컬 제외) 데이터 수집
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetching notices from YES24 Ticket (등록순, 뮤지컬 제외)...")
    yes24_items = fetch_yes24_ticket_notices()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetched {len(yes24_items)} notices from YES24 Ticket.")

    # 6. 야놀자 놀 티켓 둘러보기 - 전체 - 종료 임박순 공연 데이터 수집
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetching ending soon concerts from NOL Ticket (둘러보기 - 콘서트)...")
    nol_ending_items = fetch_nol_ticket_ending_soon()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetched {len(nol_ending_items)} ending soon concerts from NOL Ticket.")

    # 7. 야놀자 놀 티켓 둘러보기 - 전체 - 종료 임박순 전시 데이터 수집
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetching ending soon exhibitions from NOL Ticket (둘러보기 - 전시)...")
    nol_exhibition_items = fetch_nol_ticket_exhibition_ending_soon()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetched {len(nol_exhibition_items)} ending soon exhibitions from NOL Ticket.")

    combined_items = []
    new_count = 0

    # 기본 트렌드 항목 처리 (기존 status 보존)
    for b in base_items:
        if b["id"] in existing_items:
            b["status"] = existing_items[b["id"]].get("status", b.get("status", "unissued"))
        combined_items.append(b)

    # 멜론 티켓 오픈소식 항목 처리 (신규 여부 감지 및 기존 status 보존)
    for m in melon_items:
        if m["id"] in existing_items:
            prev = existing_items[m["id"]]
            m["status"] = prev.get("status", "unissued")
            m["created_at"] = prev.get("created_at", m["created_at"])
            m["is_new"] = prev.get("is_new", False)
        else:
            m["is_new"] = True
            m["created_at"] = datetime.now().strftime("%Y-%m-%d")
            new_count += 1
            print(f"  [멜론티켓 신규 등록] #{m.get('melon_order')} {m['title']} (오픈: {m['event_date']})")
        combined_items.append(m)

    # 예스24 티켓 오픈 항목 처리 (신규 여부 감지 및 기존 status 보존)
    for y in yes24_items:
        if y["id"] in existing_items:
            prev = existing_items[y["id"]]
            y["status"] = prev.get("status", "unissued")
            y["created_at"] = prev.get("created_at", y["created_at"])
            y["is_new"] = prev.get("is_new", False)
        else:
            y["is_new"] = True
            y["created_at"] = datetime.now().strftime("%Y-%m-%d")
            new_count += 1
            print(f"  [예스24 신규 등록] #{y.get('yes24_order')} {y['title']} (오픈: {y['event_date']})")
        combined_items.append(y)

    # 놀 티켓 오픈예정 항목 처리 (신규 여부 감지 및 기존 status 보존)
    for n in nol_upcoming_items:
        if n["id"] in existing_items:
            prev = existing_items[n["id"]]
            n["status"] = prev.get("status", "unissued")
            n["created_at"] = prev.get("created_at", n["created_at"])
            n["is_new"] = prev.get("is_new", False)
        else:
            n["is_new"] = True
            n["created_at"] = datetime.now().strftime("%Y-%m-%d")
            new_count += 1
            print(f"  [신규 오픈예정 등록] {n['title']} (오픈: {n['event_date']})")
        combined_items.append(n)

    # 놀 티켓 둘러보기 - 콘서트 종료 임박순 항목 처리 (신규 여부 감지 및 기존 status 보존)
    for e in nol_ending_items:
        if e["id"] in existing_items:
            prev = existing_items[e["id"]]
            e["status"] = prev.get("status", "unissued")
            e["created_at"] = prev.get("created_at", e["created_at"])
            e["is_new"] = prev.get("is_new", False)
        else:
            e["is_new"] = True
            e["created_at"] = datetime.now().strftime("%Y-%m-%d")
            new_count += 1
            print(f"  [신규 콘서트 종료임박] #{e.get('closing_rank')} {e['title']} ({e['d_day_badge']})")
        combined_items.append(e)

    # 놀 티켓 둘러보기 - 전시 종료 임박순 항목 처리 (신규 여부 감지 및 기존 status 보존)
    for ex in nol_exhibition_items:
        if ex["id"] in existing_items:
            prev = existing_items[ex["id"]]
            ex["status"] = prev.get("status", "unissued")
            ex["created_at"] = prev.get("created_at", ex["created_at"])
            ex["is_new"] = prev.get("is_new", False)
        else:
            ex["is_new"] = True
            ex["created_at"] = datetime.now().strftime("%Y-%m-%d")
            new_count += 1
            print(f"  [신규 전시 종료임박] #{ex.get('closing_rank')} {ex['title']} ({ex['d_day_badge']})")
        combined_items.append(ex)

    # 8. 파일 저장
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(combined_items, f, ensure_ascii=False, indent=2)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Saved total {len(combined_items)} topics ({new_count} newly added) to {DATA_FILE}")
    return new_count

if __name__ == "__main__":
    save_topics()

