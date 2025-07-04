import os
import openai
from dotenv import load_dotenv
from models import ProfileIn

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def suggest_gigs_and_tip(profile: ProfileIn):
    prompt1 = f"""
You're a freelance strategist AI. Suggest 3 tailored gig ideas for:
Name: {profile.name}
Skills: {profile.skills}
Goals: {profile.goals}
Reply as a numbered list.
"""
    prompt2 = f"Provide one freelance productivity tip for someone focused on: {profile.goals}"

    response1 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt1}]
    )
    response2 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt2}]
    )

    return {
        "gigs": response1.choices[0].message.content,
        "tip": response2.choices[0].message.content
    }