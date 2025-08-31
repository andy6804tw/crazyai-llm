%%writefile app.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


# === FastAPI 應用 ===
app = FastAPI(
    title="Store Inventory API",
    version="1.0.0",
    description="提供商品類別、商品清單與庫存查詢的 API，便於 Agent 工具呼叫。",
    servers=[{"url": "/", "description": "API網址"}],
)

# --- CORS 設定 ---
origins = ["*"]            
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允許的網域
    allow_credentials=True,
    allow_methods=["*"],    # 允許所有 HTTP 方法
    allow_headers=["*"],    # 允許所有自訂 Header
)


# ---- 假資料（實務可換成 DB or ERP） ----
INVENTORY = {
    "iPhone 15": {"category": "手機", "stock": 12, "unit": "台"},
    "Pixel 8": {"category": "手機", "stock": 5, "unit": "台"},
    "AirPods Pro": {"category": "配件", "stock": 30, "unit": "副"},
    "MagSafe 充電器": {"category": "配件", "stock": 18, "unit": "個"},
    "MacBook Air 13": {"category": "筆電", "stock": 7, "unit": "台"},
    "ThinkPad X1": {"category": "筆電", "stock": 3, "unit": "台"},
}
CATEGORIES = sorted({v["category"] for v in INVENTORY.values()})

# ---- Schema ----
class CategoryList(BaseModel):
    categories: List[str] = Field(..., description="目前商店可供查詢的商品類別列表")

class ProductList(BaseModel):
    category: str = Field(..., description="查詢目標類別")
    products: List[str] = Field(..., description="屬於該類別的所有商品名稱")

class InventoryItem(BaseModel):
    product_name: str = Field(..., description="商品名稱（精確匹配）")
    stock: int = Field(..., description="現有庫存數量")
    unit: str = Field(..., description="庫存單位（台、個、件…）")
    last_updated: datetime = Field(..., description="最後更新時間")

class ErrorMsg(BaseModel):
    detail: str = Field(..., description="錯誤說明")

# ---- 1) 提供可用商品類別（讓 Agent 引導使用者先選類別） ----
@app.get(
    "/categories",
    response_model=CategoryList,
    tags=["catalog"],
    summary="取得可用商品類別",
    description="回傳目前商店的販售類別清單。建議 Agent 先用這個路由引導使用者選擇要查詢的商品種類。",
)
def get_categories():
    return {"categories": CATEGORIES}

# ---- 2) 依類別列出商品名稱（讓 Agent 知道商店有哪些商品） ----
@app.get(
    "/products",
    response_model=ProductList,
    responses={404: {"model": ErrorMsg}},
    tags=["catalog"],
    summary="列出指定類別的所有商品名稱",
    description="輸入商品類別，回傳該類別底下的所有商品名稱列表，用於引導或後續庫存查詢。",
)
def list_products_by_category(
    category: str = Query(..., description="商品類別（例如：手機、配件、筆電）")
):
    if category not in CATEGORIES:
        return {"detail": f"找不到類別：{category}"}, 404
    products = [name for name, v in INVENTORY.items() if v["category"] == category]
    return {"category": category, "products": products}

# ---- 3) 直接查商品庫存（使用者可直接講商品名稱） ----
@app.get(
    "/inventory",
    response_model=InventoryItem,
    responses={404: {"model": ErrorMsg}},
    tags=["inventory"],
    summary="查詢單一商品的庫存數量",
    description="輸入商品名稱（精確匹配），回傳庫存數量、單位與最後更新時間。適合讓使用者直接詢問：「AirPods Pro 庫存多少？」",
)
def get_inventory(
    product_name: str = Query(..., description="商品名稱（需精確匹配）")
):
    item = INVENTORY.get(product_name)
    if not item:
        return {"detail": f"找不到商品：{product_name}"}, 404
    return {
        "product_name": product_name,
        "stock": item["stock"],
        "unit": item["unit"],
        "last_updated": datetime.utcnow(),
    }
