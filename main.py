from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Profile, ProfileIn
from match_ai import suggest_gigs_and_tip
from db import init_db, profile_collection
import uvicorn

app = FastAPI()
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "FlexMatch API (Python-FastAPI) is live"}

@app.post("/api/profile/upload")
async def upload_profile(profile: ProfileIn):
   
    try:
        print("📩 Received profile:", profile)
        result = await suggest_gigs_and_tip(profile)
        print("✅ GPT response:", result)
        await profile_collection.insert_one(profile.model_dump())
        return {
            "profile": profile,
            "gigs": result["gigs"],
            "coachingTip": result["tip"]
        }
    except Exception as e:
        print("🔥 BACKEND ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)