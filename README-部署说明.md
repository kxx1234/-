# 腾讯云部署目录

本目录为独立部署拷贝，不影响原项目。

## 结构
- `frontend/`：前端项目（来自 `law/law/law-game-platform`）
- `backend/`：后端项目（来自 `law/law/law-game-backend`）
- `database/law_game.db`：部署用 SQLite 数据库

## 说明
- 已尽量排除 `node_modules`、`dist`、`__pycache__` 等非必要文件
- 原项目未做任何修改
- 当前有效数据库来源：`backend/law_game.db` 的副本

## 建议部署方式
- 前端：在腾讯云服务器内进入 `frontend/` 后安装依赖并构建
- 后端：在腾讯云服务器内进入 `backend/` 后安装 Python 依赖并启动服务
- 数据库：默认使用 `database/law_game.db`，如后端配置写死为项目内相对路径，可将该文件再复制到后端运行所需位置
