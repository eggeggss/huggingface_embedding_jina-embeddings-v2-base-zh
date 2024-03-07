from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

def get_embedding_from_hugginface(text: str):
  
    model = SentenceTransformer(
    "jinaai/jina-embeddings-v2-base-zh", # switch to en/zh for English or Chinese
    trust_remote_code=True)

    # control your input sequence length up to 8192
    model.max_seq_length = 10240

    embeddings = model.encode(text)
    return embeddings
    
if __name__== "__main__":
    query_text = "高頻率晶體振盪器"
    query_embedding = get_embedding_from_hugginface(query_text)
    print(query_embedding)

