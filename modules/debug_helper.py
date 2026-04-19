import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

project_root = Path(__file__).parent.parent
load_dotenv(project_root / '.env')


class DebugHelper:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found")
        self.client = Groq(api_key=api_key)

    def debug_code(self, code, error_message="", model="llama-3.3-70b-versatile"):
        try:
            prompt = f"Debug this code:\n\nCode:\n{code}"
            if error_message:
                prompt += f"\n\nError:\n{error_message}"

            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are an expert debugger. Find and fix errors."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"