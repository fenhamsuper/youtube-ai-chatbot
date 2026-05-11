from openai import NotFoundError, OpenAI
from backend.app.config import settings

client = OpenAI(
    api_key=settings.OPENROUTER_API_KEY,
    base_url=settings.OPENROUTER_BASE_URL
)

PROMPTS = {
    "horror": """
    Write a cinematic horror story for YouTube.
    Make it atmospheric, suspenseful, and engaging.
    """,

    "educational": """
    Create an educational YouTube script.

    Include:
    - Introduction
    - Main explanation
    - Key learning points
    - Conclusion
    """,

    "shorts": """
    Create a YouTube Shorts script.

    Requirements:
    - Under 60 seconds
    - Fast-paced
    - Attention grabbing
    - Viral style
    """,

    "hooks": """
    Generate:
    - 5 viral hooks
    - 5 clickable YouTube titles
    """,

    "seo": """
    Write an SEO optimized YouTube description.

    Include:
    - Keywords
    - Hashtags
    - Call to action
    """
}


def generate_content(category, topic, audience, tone):

    system_prompt = PROMPTS.get(category)

    user_prompt = f"""
    Topic: {topic}

    Audience: {audience}

    Tone: {tone}
    """

    models_to_try = [settings.MODEL_NAME, "inclusionai/ring-2.6-1t:free"]
    last_exception = None

    for model_name in dict.fromkeys(models_to_try):
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ],
                temperature=0.8,
                max_tokens=1200
            )
            return response.choices[0].message.content
        except NotFoundError as exc:
            last_exception = exc
            continue

    if last_exception:
        raise last_exception

    raise RuntimeError("Unable to generate content with configured models.")