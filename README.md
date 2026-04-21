# Harmes Agent

Hermes Agent医疗AI代理框架

## 项目简介

医疗AI代理框架，支持多模态交互和工具调用

## 功能特性

- 🏥 医疗AI核心功能
- 🔬 智能诊断与分析
- 📊 数据可视化
- 🤖 多模态交互
- 🔒 数据安全与隐私保护

## 技术栈

- **后端**: Python, FastAPI
- **前端**: React, TypeScript, Tailwind CSS
- **AI框架**: LangChain, CrewAI
- **数据库**: PostgreSQL, Redis
- **部署**: Docker, Kubernetes

## 快速开始

### 环境要求

- Python 3.10+
- Node.js 18+
- Docker & Docker Compose

### 安装步骤

1. 克隆仓库
```bash
git clone https://github.com/MoKangMedical/Harmes-Agent.git
cd Harmes-Agent
```

2. 安装依赖
```bash
# 后端依赖
cd backend
pip install -r requirements.txt

# 前端依赖
cd ../frontend
npm install
```

3. 配置环境变量
```bash
cp .env.example .env
# 编辑.env文件，配置必要的API密钥和数据库连接
```

4. 启动服务
```bash
docker-compose up -d
```

## 项目结构

```
Harmes-Agent/
├── backend/           # 后端API服务
├── frontend/          # 前端Web界面
├── ai-engine/         # AI模型与算法
├── data/              # 数据存储
├── docs/              # 项目文档
├── tests/             # 测试用例
├── docker-compose.yml # Docker编排文件
└── README.md          # 项目说明
```

## API文档

启动服务后，访问以下地址查看API文档：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 贡献指南

我们欢迎任何形式的贡献！请遵循以下步骤：

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

## 许可证

本项目采用 [MIT License](LICENSE) 许可证。

## 联系方式

- 项目维护者: MoKangMedical
- 邮箱: contact@mokangmedical.com
- 项目主页: https://github.com/MoKangMedical/Harmes-Agent

## 致谢

感谢所有为这个项目做出贡献的开发者和医疗领域专家！
