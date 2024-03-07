from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import PointStruct
import configparser 
from hugginface_model import get_embedding_from_hugginface


config=configparser.ConfigParser()
config.read("config/config.ini")

if __name__== "__main__":
    
    client = QdrantClient(config["DEFAULT"]["qdrant_url"])
    query_text = "多層陶瓷電容"
    query_embedding = get_embedding_from_hugginface(query_text)

    search_result = client.search(
        collection_name="lyrics",
        query_vector=query_embedding,
        limit=1,
        append_payload=True,
    )

    print(search_result)
