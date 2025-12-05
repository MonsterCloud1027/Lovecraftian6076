# 后端部署指南

本指南将帮助你部署 FastAPI 后端到不同的云平台。

## 📋 前置要求

1. 一个 GitHub/GitLab/Bitbucket 账号
2. 代码已推送到 Git 仓库
3. OpenAI API Key（如果需要）

## 🚀 部署选项

### 选项 1: Render（推荐，免费版可用）

**优点：** 免费版可用，配置简单，自动部署  
**缺点：** 免费版会在 15 分钟无活动后休眠

#### 步骤：

1. **访问 [render.com](https://render.com)** 并注册/登录

2. **创建新的 Web Service**
   - 点击 "New +" → "Web Service"
   - 连接你的 Git 仓库

3. **配置服务**
   - **Name**: `coc-solo-api`（或你喜欢的名字）
   - **Region**: 选择离你最近的区域
   - **Branch**: `main` 或 `master`
   - **Root Directory**: 留空（使用仓库根目录）
   - **Runtime**: `Python 3`
   - **Build Command**: 
     ```bash
     pip install -r requirements-production.txt
     ```
   - **Start Command**: 
     ```bash
     uvicorn api_server:app --host 0.0.0.0 --port $PORT
     ```

4. **设置环境变量**
   在 "Environment" 标签页添加：
   - `ALLOWED_ORIGINS`: 你的前端 URL（例如：`https://your-app.vercel.app`）
     - 多个 URL 用逗号分隔：`https://app1.vercel.app,https://app2.vercel.app`
   - `OPENAI_API_KEY`: （可选）如果你想在后端存储 API Key

5. **选择计划**
   - 免费版：适合测试和小型项目
   - 付费版：无休眠限制，性能更好

6. **部署**
   - 点击 "Create Web Service"
   - 等待构建完成（通常 5-10 分钟）

7. **获取 URL**
   - 部署完成后，Render 会提供一个 URL
   - 例如：`https://coc-solo-api.onrender.com`
   - 将这个 URL 添加到 Vercel 的 `PYTHON_BACKEND_URL` 环境变量

#### 使用 render.yaml（可选）

如果你有 `render.yaml` 文件，可以：
1. 在 Render 中选择 "New +" → "Blueprint"
2. 连接仓库，Render 会自动读取配置

---

### 选项 2: Railway

**优点：** 免费额度充足，配置灵活，支持 Docker  
**缺点：** 免费版有使用限制

#### 步骤：

1. **访问 [railway.app](https://railway.app)** 并登录（支持 GitHub 登录）

2. **创建新项目**
   - 点击 "New Project"
   - 选择 "Deploy from GitHub repo"
   - 选择你的仓库

3. **配置服务**
   - Railway 会自动检测 Python 项目
   - 如果没有自动检测，在 "Settings" → "Build" 中设置：
     - **Build Command**: `pip install -r requirements-production.txt`
     - **Start Command**: `uvicorn api_server:app --host 0.0.0.0 --port $PORT`

4. **设置环境变量**
   - 在 "Variables" 标签页添加：
     - `ALLOWED_ORIGINS`: 你的前端 URL
     - `OPENAI_API_KEY`: （可选）

5. **部署**
   - Railway 会自动开始部署
   - 等待构建完成

6. **获取 URL**
   - 在 "Settings" → "Networking" 中生成公共域名
   - 或使用 Railway 提供的默认域名

---

### 选项 3: Fly.io

**优点：** 全球边缘部署，性能好，免费额度  
**缺点：** 需要 CLI，配置稍复杂

#### 步骤：

1. **安装 Fly CLI**
   ```bash
   # Windows (PowerShell)
   iwr https://fly.io/install.ps1 -useb | iex
   
   # macOS/Linux
   curl -L https://fly.io/install.sh | sh
   ```

2. **登录 Fly.io**
   ```bash
   fly auth login
   ```

3. **初始化项目**
   ```bash
   fly launch
   ```
   - 选择应用名称
   - 选择区域
   - 选择 Python 配置

4. **创建 fly.toml 配置文件**
   ```toml
   app = "your-app-name"
   primary_region = "iad"
   
   [build]
     builder = "paketobuildpacks/builder:base"
   
   [http_service]
     internal_port = 8000
     force_https = true
     auto_stop_machines = true
     auto_start_machines = true
     min_machines_running = 0
     processes = ["app"]
   
   [[services]]
     http_checks = []
     internal_port = 8000
     processes = ["app"]
     protocol = "tcp"
     script_checks = []
   
     [services.concurrency]
       hard_limit = 25
       soft_limit = 20
       type = "connections"
   
     [[services.ports]]
       force_https = true
       handlers = ["http"]
       port = 80
   
     [[services.ports]]
       handlers = ["tls", "http"]
       port = 443
   
     [[services.tcp_checks]]
       grace_period = "1s"
       interval = "15s"
       restart_limit = 0
       timeout = "2s"
   ```

5. **设置环境变量**
   ```bash
   fly secrets set ALLOWED_ORIGINS=https://your-app.vercel.app
   fly secrets set OPENAI_API_KEY=your-key-here
   ```

6. **部署**
   ```bash
   fly deploy
   ```

---

### 选项 4: Docker + 任意平台

如果你熟悉 Docker，可以使用提供的 `Dockerfile`：

```bash
# 构建镜像
docker build -t coc-solo-api .

# 运行容器
docker run -p 8000:8000 \
  -e ALLOWED_ORIGINS=https://your-app.vercel.app \
  -e OPENAI_API_KEY=your-key \
  coc-solo-api
```

然后可以部署到：
- AWS ECS/Fargate
- Google Cloud Run
- Azure Container Instances
- DigitalOcean App Platform
- 等等

---

## 🔧 环境变量说明

| 变量名 | 必需 | 说明 | 示例 |
|--------|------|------|------|
| `ALLOWED_ORIGINS` | ✅ | 允许的前端域名（CORS） | `https://app.vercel.app` |
| `OPENAI_API_KEY` | ❌ | OpenAI API Key（可选，如果前端不传） | `sk-...` |

**注意：** 多个域名用逗号分隔：
```
ALLOWED_ORIGINS=https://app1.vercel.app,https://app2.vercel.app
```

---

## ✅ 验证部署

部署完成后，验证服务是否正常运行：

```bash
# 健康检查
curl https://your-backend-url.com/api/health

# 应该返回: {"status":"ok"}
```

---

## 🔍 常见问题

### 1. CORS 错误

**问题：** 前端无法连接到后端，浏览器控制台显示 CORS 错误

**解决：**
- 确保 `ALLOWED_ORIGINS` 环境变量包含你的前端 URL
- 检查 URL 格式（必须包含 `https://`）
- 重启后端服务

### 2. 服务休眠（Render 免费版）

**问题：** 首次请求很慢（>30秒）

**解决：**
- 这是 Render 免费版的正常行为
- 15 分钟无活动后服务会休眠
- 首次请求会唤醒服务（需要等待）
- 升级到付费版可避免休眠

### 3. 构建失败

**问题：** 部署时构建失败

**解决：**
- 检查 `requirements-production.txt` 是否存在
- 确认所有依赖都列在文件中
- 查看构建日志中的具体错误信息
- 确保 Python 版本兼容（推荐 3.11+）

### 4. 端口错误

**问题：** 服务无法启动

**解决：**
- 确保使用 `$PORT` 环境变量（Render/Railway 自动提供）
- 不要硬编码端口号
- 检查启动命令是否正确

### 5. 日志文件无法下载

**问题：** 下载日志功能不工作

**解决：**
- Render 免费版休眠时无法读取文件系统
- 唤醒服务后重试
- 考虑使用外部存储（S3、云存储等）存储日志

---

## 📊 平台对比

| 平台 | 免费额度 | 休眠 | 部署难度 | 推荐度 |
|------|---------|------|---------|--------|
| Render | ✅ 可用 | ⚠️ 15分钟 | ⭐ 简单 | ⭐⭐⭐⭐⭐ |
| Railway | ✅ $5/月 | ❌ 无 | ⭐⭐ 中等 | ⭐⭐⭐⭐ |
| Fly.io | ✅ 可用 | ❌ 无 | ⭐⭐⭐ 较难 | ⭐⭐⭐ |
| Docker | - | - | ⭐⭐⭐⭐ 困难 | ⭐⭐ |

---

## 🔄 更新部署

大多数平台支持自动部署：

1. **推送到 Git 仓库**
   ```bash
   git add .
   git commit -m "Update backend"
   git push origin main
   ```

2. **平台自动检测并重新部署**
   - Render: 自动触发
   - Railway: 自动触发
   - Fly.io: 需要手动 `fly deploy`

---

## 📝 下一步

部署完成后：

1. ✅ 测试健康检查端点
2. ✅ 在 Vercel 中设置 `PYTHON_BACKEND_URL` 环境变量
3. ✅ 测试前端与后端的连接
4. ✅ 验证完整功能（创建角色、聊天等）

---

## 🆘 需要帮助？

如果遇到问题：

1. 查看平台的构建/运行日志
2. 检查环境变量是否正确设置
3. 验证代码是否已正确推送到 Git
4. 确认所有依赖都在 `requirements-production.txt` 中

