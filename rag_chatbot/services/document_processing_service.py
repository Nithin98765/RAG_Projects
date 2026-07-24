from ..models import Document
from .embedding_service import EmbeddingService

class DocumentProcessingSerice:

    @staticmethod
    def process_document(document_id):
        #orm query to get document details 
        documemt = Document.objects.get(id=document_id)
        #generate the embeddings
        embedding = EmbeddingService.generate_embedding(documemt.content)
        documemt.embedding = embedding
        documemt.save() # save the embeddings in the database

        return documemt