# 智弈法衡

智弈法衡项目的独立提交版本，按前端、后端和数据三部分组织。

## 项目结构

- `frontend/`：Vue 3、TypeScript、Vite 前端
- `backend/`：FastAPI、Python 后端
- `database/law_game.db`：SQLite 数据库

## 本地运行

### 后端

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python -m uvicorn app.main:app --reload
```

启动前请根据实际环境填写 `backend/.env` 中的数据库、密钥和模型配置。

### 前端

```powershell
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```

## 数据

部署用 SQLite 数据库位于 `database/law_game.db`。如后端使用项目内相对路径，可在部署时将其复制到后端所需位置，或通过 `DATABASE_URL` 指向该文件。

真实 `.env`、依赖目录、缓存、日志及历史部署压缩包均不纳入版本控制。

## Cloud Studio

创建 `All in One` 工作空间并导入本仓库后，在终端运行：

```bash
bash scripts/cloudstudio-start.sh
```

脚本会准备 SQLite 数据库、安装前后端依赖，并启动后端 `8000` 端口和前端 `5173` 端口。运行后在 Cloud Studio 的端口面板中打开 `5173` 预览地址。

需要使用大模型或得理检索时，请在 `backend/.env` 中填写对应密钥后重新启动脚本。
