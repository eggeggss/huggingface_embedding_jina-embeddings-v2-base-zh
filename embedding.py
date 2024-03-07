from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import PointStruct
import configparser 
from hugginface_model import get_embedding_from_hugginface

config=configparser.ConfigParser()
config.read("config/config.ini")

if __name__== "__main__":

    client = QdrantClient(config["DEFAULT"]["qdrant_url"])
   
    f=open('產品型錄.txt',"r")
    data_objs=[]
    
    newid=0
    oldid=0
    line_result=""

    num_lines = sum(1 for _ in open('產品型錄.txt'))
    line_count=0

    for line in f:  
        line_count=line_count+1
        #空白行表示下一個物件 
        if len(line.strip())==0:
           newid=newid+1      
        #下一個物件則append到陣列,否則就是組字串到lyric
        if oldid!=newid:
            data_objs.append({
                "id":newid,
                "lyrics":line_result,
            })
            oldid=newid
            #print(line_result)
            line_result=""
        else:
            line_result=line_result+line      
            if (line_count==num_lines):
                data_objs.append({
                    "id":newid+1,
                    "lyrics":line_result,
                })

    client.recreate_collection(
        collection_name="lyrics",
        vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
    )

    embedding_array = [get_embedding_from_hugginface(text["lyrics"]) for text in data_objs]

    for i, vector in enumerate(embedding_array):
       
        client.upsert(
            collection_name="lyrics",
            points=[PointStruct(id=i,
                                vector=vector,
                                payload=data_objs[i])]
        )

