from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

activity_logs = [
    {"timestamp": str(datetime.now()), "action": "Agent 3 analyzed 23 listings in Florida."},
    {"timestamp": str(datetime.now()), "action": "Analyst 7 flagged undervalued property in Dallas."},
    {"timestamp": str(datetime.now()), "action": "County analyst for Arizona updated cap rate forecasts."}
]

chat_log = [
    {"sender": "Head Analyst CA", "message": "Weekly valuation model deployed."},
    {"sender": "CEO", "message": "Make sure to rerun the multi-market comparison."}
]

class ChatMessage(BaseModel):
    sender: str
    message: str

@router.get("/api/admin/logs")
def get_logs():
    return activity_logs

@router.get("/api/admin/chat")
def get_chat():
    return chat_log

@router.post("/api/admin/chat")
def post_chat(message: ChatMessage):
    chat_log.append({"sender": message.sender, "message": message.message})
    return {"status": "Message received"}

@router.get("/api/admin/weekly-summary")
def get_weekly_summary():
    return {
        "summary": (
            "📈 Weekly Market Summary\n\n"
            "- Top State: Texas (Score: 91/100)\n"
            "- Best Cap Rate: Columbus, OH (12.3%)\n"
            "- Fastest Market Shift: Phoenix, AZ (+7% YoY)\n\n"
            "🧠 AI Engine Notes:\n"
            "- 532 new leads processed\n"
            "- 41 high-priority investment targets\n"
            "- 17 cold outreach calls scheduled via agents\n"
        )
    }
