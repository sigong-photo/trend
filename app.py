import json
import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Blog Topic Manager")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
DATA_PATH = os.path.join(BASE_DIR, "data", "topics.json")

os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

def read_topics():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def write_topics(topics):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(topics, f, ensure_ascii=False, indent=2)

class StatusUpdate(BaseModel):
    id: str
    status: str

@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request, category: str = "전체", sort: str = "register"):
    all_topics = read_topics()
    
    # 상단 요약 카운트 계산
    today_str = "2026-09-26"
    stats = {
        "new_today": len([t for t in all_topics if t.get("is_new") is True or t.get("created_at") == today_str]),
        "unissued": len([t for t in all_topics if t.get("status") == "unissued"]),
        "events": len([t for t in all_topics if "행사·뉴스" in t.get("category_badges", [])]),
        "trends": len([t for t in all_topics if "트렌드" in t.get("category_badges", [])]),
        "this_week": len([t for t in all_topics if t.get("section") == "urgent"]),
        "drafts": 0,
        "wishlist": len([t for t in all_topics if t.get("status") == "wishlist"]),
        "completed": len([t for t in all_topics if t.get("status") == "done"])
    }

    # 카테고리 필터링
    filtered = all_topics
    if category == "✨ 신규":
        filtered = [t for t in all_topics if t.get("is_new") is True or t.get("created_at") == today_str]
    elif category != "전체":
        filtered = [t for t in all_topics if category in t.get("category_badges", [])]

    # 등록순(최신 등록일순) 및 마감 임박순 정렬 처리
    if category in ["종료 임박 콘서트", "종료 임박 전시"]:
        filtered.sort(
            key=lambda x: (
                x.get("closing_rank", 999),
                x.get("end_date_sort") or "9999-12-31"
            )
        )
    elif category == "멜론 티켓 오픈소식":
        filtered.sort(
            key=lambda x: (
                x.get("melon_order", 999),
                -int(x.get("melon_csoon_id", 0))
            )
        )
    elif category == "예스24 티켓":
        filtered.sort(
            key=lambda x: (
                x.get("yes24_order", 999),
                -int(x.get("yes24_id", 0))
            )
        )
    elif sort == "register" or category in ["놀 티켓 오픈예정", "콘서트", "공연", "전시"]:
        filtered.sort(
            key=lambda x: (
                x.get("registered_at") or x.get("created_at") or "",
                x.get("id") or ""
            ),
            reverse=True
        )

    urgent_items = [t for t in filtered if t.get("section") == "urgent"]
    trend_items = [t for t in filtered if t.get("section") == "trend"]

    categories = [
        "전체", "✨ 신규", "멜론 티켓 오픈소식", "예스24 티켓", "놀 티켓 오픈예정", "종료 임박 콘서트", "종료 임박 전시",
        "콘서트", "공연", "전시", "문화", "팝업", "축제", "페스티벌", "내한공연",
        "박물관", "미술관", "도슨트", "야간관람", "팬미팅", "투어",
        "행사·뉴스", "트렌드", "단독판매",
        "여행", "먹거리", "맛집", "쇼핑", "건강", "부동산", "생활정보"
    ]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "stats": stats,
            "categories": categories,
            "current_category": category,
            "current_sort": sort,
            "urgent_items": urgent_items,
            "trend_items": trend_items
        }
    )

@app.post("/api/topic/status")
async def update_status(payload: StatusUpdate):
    topics = read_topics()
    target = next((t for t in topics if t["id"] == payload.id), None)
    if not target:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    target["status"] = payload.status
    write_topics(topics)
    return {"success": True, "id": payload.id, "status": payload.status}

@app.get("/api/topic/{topic_id}")
async def get_topic_detail(topic_id: str):
    topics = read_topics()
    target = next((t for t in topics if t["id"] == topic_id), None)
    if not target:
        raise HTTPException(status_code=404, detail="Topic not found")
    return target

@app.delete("/api/topic/{topic_id}")
async def delete_topic(topic_id: str):
    topics = read_topics()
    topics = [t for t in topics if t["id"] != topic_id]
    write_topics(topics)
    return {"success": True}

