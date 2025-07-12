

如何將Dify預設的向量資料庫 weaviate 改成 qdrant

1. 修改 vim .env =>404行 VECTOR_STORE=qdrant
2. 建立 docker-compose.override.yaml

```
version: "3.8"

services:

  # 啟用 Qdrant
  qdrant:
    image: qdrant/qdrant:latest
    restart: always
    volumes:
      - ./volumes/qdrant:/qdrant/storage
    environment:
      QDRANT_API_KEY: ${QDRANT_API_KEY:-difyai123456}
    ports:
      - "6333:6333"
```


3. 重建並遷移資料
只重建 Qdrant（及更新過的 API/Worker）容器，不影響其他服務：

```
sudo docker compose up -d --force-recreate --no-deps weaviate api worker qdrant
sudo docker compose restart nginx
# 或是依序重啟所有服務
sudo docker compose restart
```

執行 Dify 提供的 VDB 遷移指令，將現有 Weaviate 資料遷移到 Qdrant（或直接重新索引）：

```
# 在 API 容器內執行
sudo docker exec -it docker-api-1 flask vdb-migrate
```

> 這個指令會根據你的 VECTOR_STORE 設定，自動處理向量資料的搬移或重建

```
# 測試 Qdrant API
curl http://localhost:6333/collections
```

```
# 停掉 weaviate 容器
sudo docker stop docker-weaviate-1
```

## 切回 Weaviate：修改環境與 Compose 設定

1. 還原 .env 裡的 VECTOR_STORE
VECTOR_STORE=weaviate

2. 移除 docker-compose.override.yaml

3. 重建服務
```
# 停 Qdrant
sudo docker stop docker-qdrant-1

# 強制重建 Weaviate、API、Worker（不重建依賴 db、redis 等）
sudo docker compose up -d --force-recreate --no-deps weaviate api worker
```

4. 資料遷移：從 Qdrant 搬回 Weaviate

```
# 在 API 容器內執行
docker exec -it docker-api-1 flask vdb-migrate
```