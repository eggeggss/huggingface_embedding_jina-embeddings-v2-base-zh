 
## huggingface的sentence-transformers/jina-embeddings-v2-base-zh 

https://huggingface.co/jinaai/jina-embeddings-v2-base-zh

### 換掉config/config.ini
```
[DEFAULT]
qdrant_url = 自己qdrant server的url
```

### 換成git clone後的路徑
```
docker run -v C:\Users\rogerroan-superdesk\source\jina-embeddings-v2-base-zh\:/tmp -ti python:3.11 bash
```

### 進入容器,安裝環境
```
 cd /tmp
 pip install -r requirements.txt
```

### 使用model需身分驗證
```
huggingface-cli login
貼上access token
token取得參考
https://huggingface.co/docs/hub/security-tokens
```

### 寫入vector database
```
python embedding.py
```

### 搜尋資料
```
python retreive.py
```
