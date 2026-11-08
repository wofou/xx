# 导入框架
from fastapi import FastAPI
# 解决跨域问题（前端页面和后端域名/端口不同，必须加）
from fastapi.middleware.cors import CORSMiddleware

# 实例化应用
app = FastAPI()

# 配置跨域，允许前端页面访问接口
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源，本地测试用
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. GET 接口：后端主动返回数据（前端获取信息）
@app.get("/api/get_msg")
def get_message():
    # 以 JSON 格式返回给前端
    return {
        "code": 200,
        "data": "Hello 前后端互通123！",
        "author": "Python后端"
    }

# 2. POST 接口：接收前端传过来的数据，处理后再返回
@app.post("/api/post_data")
def post_data(name: str, content: str):
    """接收前端的姓名和内容，拼接后返回"""
    res = f"收到 {name} 的消息：{content}"
    return {
        "code": 200,
        "result": res
    }

# 启动服务
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)