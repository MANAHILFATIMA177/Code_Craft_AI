import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

project_root = Path(__file__).parent.parent
load_dotenv(project_root / '.env')


class CodeGenerator:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found")
        self.client = Groq(api_key=api_key)

    def generate_code(self, prompt, model="llama-3.3-70b-versatile"):
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system",
                     "content": "You are an expert Python developer. Write clean, production-ready code."},
                    {"role": "user", "content": f"Generate Python code for: {prompt}"}
                ],
                temperature=0.3,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"