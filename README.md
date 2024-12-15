# 视频项目

基于 Vue.js 3 和 FastAPI 构建的全栈 Web 应用，具有用户认证和图书管理功能。

## 项目结构

```
video_project/
├── frontend/         # Vue.js 前端
└── backend/         # FastAPI 后端
```

## 环境要求

- Node.js (v16 或更高版本)
- Python 3.11
- PostgreSQL (v12 或更高版本)
- npm 或 yarn

## 后端设置

1. 创建并激活 Python 虚拟环境：
```bash
cd backend
python -m venv venv
# Windows系统
.\venv\Scripts\activate
# Unix或MacOS系统
source venv/bin/activate
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 数据库设置：
   - 如果未安装，请先安装 PostgreSQL
   - 创建新数据库：
   ```sql
   CREATE DATABASE fastapi_vue_admin;
   ```
   - 创建用户（如果不存在）：
   ```sql
   CREATE USER root WITH PASSWORD 'root123';
   ```
   - 授予权限：
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE fastapi_vue_admin TO root;
   ```
   - 导入初始数据：
   ```bash
   psql -U root -d fastapi_vue_admin -f demo_postgres.sql
   ```

4. 启动后端服务器：
```bash
cd backend  # 确保在backend目录下
uvicorn main:app --reload --port 5000
```
后端服务器将在 `http://localhost:5000` 运行

## 前端设置

1. 安装依赖：
```bash
cd frontend
npm install
# 或
yarn install
```

2. 启动开发服务器：
```bash
npm run dev
# 或
yarn dev
```
前端将在 `http://localhost:5173` 可访问

## 默认用户

系统预置以下用户：

管理员用户：
   - 用户名：admin
   - 密码：123456

## API 文档

后端启动后，可以通过以下地址访问 API 文档：
- Swagger UI：`http://localhost:5000/docs`
- ReDoc：`http://localhost:5000/redoc`

## 功能特性

- 用户认证（登录/注册）
- 用户资料管理
- 图书管理（增删改查）
- 响应式界面
- API 文档
- PostgreSQL 数据库

## 开发说明

- 后端使用 Tortoise ORM 进行数据库操作
- 前端基于 Vue 3 + Vite 构建
- API 认证使用 JWT 令牌
- 开发环境已启用 CORS

## 常见问题

1. 数据库连接：
   - 确保 PostgreSQL 正在运行
   - 检查 `backend/main.py` 中的连接凭据
   - 验证数据库存在且用户具有适当权限

2. 前端 API 连接：
   - 检查前端配置中的后端 URL 是否正确
   - 如遇连接问题，检查 CORS 设置
