#!/bin/bash
# Harmes Agent 部署脚本
echo "🤖 Harmes Agent — 多Agent协作调度框架"
echo "======================================="
python3 -m py_compile src/agent.py && echo "✅ agent.py 语法正确"
mkdir -p output logs
echo "✅ 部署完成"
echo "使用: python src/agent.py"
