#!/usr/bin/env python3
"""
Harmes Agent - 后端主入口
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="Harmes Agent",
    description="Hermes Agent医疗AI代理框架",
    version="1.0.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "欢迎使用Harmes Agent", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Harmes Agent"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
