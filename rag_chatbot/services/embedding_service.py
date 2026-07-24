from google import genai
from django.conf import settings



client = genai.Client(api_key=settings.GEMINI_API_KEY)

class EmbeddingService:

    @staticmethod
    def generate_embedding(text:str):
        response = client.models.embed_content(model = "gemini-embedding-001",contents=text)

        return response.embeddings[0].values
    
