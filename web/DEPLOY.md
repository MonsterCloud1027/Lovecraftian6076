# Vercel 部署指南

## 前置要求

1. 一个 Vercel 账号（免费版即可）
2. GitHub/GitLab/Bitbucket 账号（用于连接代码仓库）
3. Python 后端已部署（推荐使用 Render、Railway 或 Fly.io）

## 部署步骤

### 方法一：通过 Vercel CLI（推荐）

1. **安装 Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **登录 Vercel**
   ```bash
   vercel login
   ```

3. **在 web 目录下部署**
   ```bash
   cd web
   vercel
   ```

4. **设置环境变量**
   ```bash
   vercel env add PYTHON_BACKEND_URL
   # 输入你的 Python 后端 URL，例如: https://your-backend.onrender.com
   ```

5. **生产环境部署**
   ```bash
   vercel --prod
   ```

### 方法二：通过 Vercel 网站（图形界面）

1. **访问 [vercel.com](https://vercel.com)** 并登录

2. **导入项目**
   - 点击 "Add New" → "Project"
   - 连接你的 Git 仓库（GitHub/GitLab/Bitbucket）
   - 选择包含 `web` 目录的仓库

3. **配置项目设置**
   - **Root Directory**: 设置为 `web`
   - **Framework Preset**: Next.js（自动检测）
   - **Build Command**: `npm run build`（默认）
   - **Output Directory**: `.next`（默认）
   - **Install Command**: `npm install`（默认）

4. **设置环境变量**
   在项目设置中添加：
   - `PYTHON_BACKEND_URL`: 你的 Python 后端 URL
     - 例如: `https://your-backend.onrender.com`
   - `NEXT_PUBLIC_API_BASE`: `/api`（通常不需要修改）

5. **部署**
   - 点击 "Deploy"
   - 等待构建完成

## 后端部署（Python FastAPI）

由于 Vercel 主要支持 Node.js，Python 后端需要单独部署：

### 选项 1: Render（推荐，免费）

1. 访问 [render.com](https://render.com)
2. 创建新的 Web Service
3. 连接你的 Git 仓库
4. 设置：
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn api_server:app --host 0.0.0.0 --port $PORT`
   - **Environment**: Python 3
5. 添加环境变量：
   - `ALLOWED_ORIGINS`: 你的 Vercel 前端 URL（例如: `https://your-app.vercel.app`）

### 选项 2: Railway

1. 访问 [railway.app](https://railway.app)
2. 创建新项目并连接 Git 仓库
3. 添加 `requirements.txt` 文件
4. Railway 会自动检测 Python 项目并部署

### 选项 3: Fly.io

1. 安装 Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. 登录: `fly auth login`
3. 初始化: `fly launch`
4. 部署: `fly deploy`

## 环境变量配置

### Vercel（前端）

在 Vercel 项目设置中添加：

```
PYTHON_BACKEND_URL=https://your-backend-url.com
NEXT_PUBLIC_API_BASE=/api
```

### 后端（Render/Railway/Fly.io）

```
ALLOWED_ORIGINS=https://your-frontend.vercel.app
OPENAI_API_KEY=your-api-key（如果需要）
```

## 验证部署

1. 访问你的 Vercel URL（例如: `https://your-app.vercel.app`）
2. 检查前端是否正常加载
3. 尝试创建角色并开始对话
4. 检查浏览器控制台是否有 API 连接错误

## 常见问题

### 1. CORS 错误

确保后端设置了正确的 `ALLOWED_ORIGINS`，包含你的 Vercel 前端 URL。

### 2. API 连接失败

检查 `PYTHON_BACKEND_URL` 环境变量是否正确设置，并且后端服务正在运行。

### 3. 构建失败

- 检查 Node.js 版本（Vercel 默认使用 18.x）
- 确保所有依赖都在 `package.json` 中
- 查看构建日志中的具体错误信息

### 4. 静态资源加载失败

确保 `public` 目录下的所有资源文件都已提交到 Git。

## 更新部署

每次推送到主分支，Vercel 会自动重新部署。你也可以：

1. 在 Vercel 控制台手动触发部署
2. 使用 CLI: `vercel --prod`

## 自定义域名

1. 在 Vercel 项目设置中添加自定义域名
2. 按照提示配置 DNS 记录
3. 更新后端的 `ALLOWED_ORIGINS` 包含新域名

