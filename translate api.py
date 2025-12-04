

from google import genai
from google.genai import types
Api_key = 'AIzaSyCGssK_PY3vcf3h890fpD2naaI7Cw6nzr8'
client = genai.Client(api_key=Api_key)
response = client.models.generate_content(
   model='gemini-2.5-flash',
   contents='translate the following English text to French: text = "Hello, how are you?"',
   config=types.GenerateContentConfig(
       max_output_tokens=100,
       temperature=0.7
   )
)
print(response.text)
