import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

project_root = Path(__file__).parent.parent
load_dotenv(project_root / '.env')


class DocGenerator:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found")
        self.client = Groq(api_key=api_key)

    def generate_docs(self, code, doc_type="google", model="llama-3.3-70b-versatile"):
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Generate professional documentation."},
                    {"role": "user", "content": f"Generate {doc_type} style documentation for:\n\n{code}"}
                ],
                temperature=0.3,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"