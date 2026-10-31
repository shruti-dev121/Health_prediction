
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()


def generate_remarks(glucose, haemoglobin, cholesterol):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API key not found")

    client = genai.Client(api_key=api_key)

    prompt = f"""
Analyze these patient blood test values:

Glucose: {glucose}
Haemoglobin: {haemoglobin}
Cholesterol: {cholesterol}

Provide a short report using these headings:

1. General Observations:
For each blood test (Glucose, Haemoglobin, and Cholesterol):

- Explain in simple language what the test measures.
- State whether the value appears low, within range, or high,
  only when units and suitable reference ranges are available.
- Explain what a high or low value may indicate.
- Mention whether the result needs medical attention.
- Use simple words that anyone can understand.

2. Possible Risks:
Identify potential health concerns based on abnormal values.
For example, possible diabetes risk, anemia, or cholesterol-related risk,
only when supported by the available information.

3. Recommendation:
Give a short suggestion about medical follow-up.

Rules:
- Keep the complete response under 120 words.
- Use simple, professional language.
- Do not provide a confirmed diagnosis.
- Do not assume measurement units or fasting status.
- Mention that interpretation depends on laboratory reference ranges and clinical context.
- Recommend consulting a doctor for concerning results.

Formatting:
- Use clear headings.
- Use bullet points for observations and recommendations.
- Highlight important health risks in bold.
- Keep paragraphs short.
- Return clean Markdown only.


Additional instructions:
- Explain medical terms in simple language.
- Do not just repeat the numerical values.
- Clearly distinguish between high, low, and normal results.
- Never assume units or fasting status.
- If information is missing, say that the result needs further
  evaluation rather than guessing.
"""

    response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    )

    return response.text
