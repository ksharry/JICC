# JICC 企業資源規劃系統
python -m pytest tests/ -v


一個基於 FastAPI + React 的現代化 ERP 系統，專為中小企業設計，提供完整的業務管理解決方案。

##  功能特色

### 核心模塊
- **用戶管理** - 完整的用戶認證與權限控制系統
- **財務管理** - 收入/支出記錄、發票管理、財務報表
- **庫存管理** - 產品管理、庫存進出、供應商管理
- **銷售管理** - 客戶管理、訂單管理、報價單系統
- **採購管理** - 供應商管理、採購流程、付款管理
- **報表分析** - 多維度數據分析與可視化報表

### 技術特色
- **現代化架構** - FastAPI + React + TypeScript
- **響應式設計** - 支持多設備訪問
- **實時數據** - WebSocket 支持實時更新
- **安全可靠** - JWT 認證、數據加密、權限控制
- **易於擴展** - 模塊化設計、微服務架構準備

##  系統要求

### 開發環境
- Python 3.9+
- Node.js 18+
- PostgreSQL 14+ (生產環境)
- Redis 6+ (緩存)
- Git

### 生產環境
- Docker & Docker Compose
- Kubernetes (可選)
- Nginx (反向代理)

##  快速開始

### 1. 克隆項目
```bash
git clone <repository-url>
cd ji_erp
```

### 2. 後端設置
```bash
# 創建虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt

# 初始化數據庫
python init_db.py

# 啟動後端服務
python main.py
```

### 3. 前端設置
```bash
cd frontend
npm install
npm start
```

### 4. 訪問系統
- 後端 API: http://localhost:8000
- 前端應用: http://localhost:3000
- API 文檔: http://localhost:8000/docs

##  測試帳號

| 角色 | 用戶名 | 密碼 | 權限 |
|------|--------|------|------|
| 管理員 | admin | admin123 | 全部權限 |
| 財務 | finance | finance123 | 財務模塊 |
| 庫存 | inventory | inv123 | 庫存模塊 |
| 銷售 | sales | sales123 | 銷售模塊 |

##  項目結構

```
ji_erp/
 backend/                 # 後端代碼
    app/
       api/            # API 路由
       core/           # 核心配置
       models/         # 數據模型
       schemas/        # Pydantic 模式
       services/       # 業務邏輯
       utils/          # 工具函數
    tests/              # 測試文件
    requirements.txt    # Python 依賴
 frontend/               # 前端代碼
    src/
       components/     # React 組件
       pages/          # 頁面組件
       hooks/          # 自定義 Hooks
       services/       # API 服務
       store/          # 狀態管理
       utils/          # 工具函數
    package.json
 docs/                   # 項目文檔
 docker/                 # Docker 配置
 .cursorrules           # Cursor AI 規則
 context.md             # 項目上下文
 README.md              # 項目說明
```

##  開發指南

### 代碼規範
- **Python**: 遵循 PEP 8 規範
- **TypeScript**: 使用嚴格模式
- **Git**: 使用 Conventional Commits
- **測試**: 保持 80%+ 測試覆蓋率

### 開發流程
1. 創建功能分支
2. 實現功能並編寫測試
3. 提交代碼並創建 PR
4. 代碼審查
5. 合併到主分支

### 環境變量
```bash
# 後端環境變量
DATABASE_URL=postgresql://user:password@localhost/ji_erp
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30

# 前端環境變量
REACT_APP_API_URL=http://localhost:8000
REACT_APP_WS_URL=ws://localhost:8000/ws
```

##  API 文檔

### 認證端點
- `POST /api/auth/login` - 用戶登入
- `POST /api/auth/logout` - 用戶登出
- `POST /api/auth/refresh` - 刷新 Token

### 用戶管理
- `GET /api/users` - 獲取用戶列表
- `POST /api/users` - 創建用戶
- `PUT /api/users/{id}` - 更新用戶
- `DELETE /api/users/{id}` - 刪除用戶

### 財務管理
- `GET /api/transactions` - 獲取交易記錄
- `POST /api/transactions` - 創建交易
- `GET /api/reports/financial` - 財務報表

詳細 API 文檔請訪問: http://localhost:8000/docs

##  部署

### Docker 部署
```bash
# 構建並啟動所有服務
docker-compose up -d

# 查看服務狀態
docker-compose ps

# 查看日誌
docker-compose logs -f
```

### 生產環境部署
```bash
# 使用 Kubernetes
kubectl apply -f k8s/

# 或使用 Docker Swarm
docker stack deploy -c docker-compose.prod.yml ji-erp
```

##  測試

### 運行測試
```bash
# 後端測試
cd backend
pytest

# 前端測試
cd frontend
npm test

# 端到端測試
npm run test:e2e
```

### 測試覆蓋率
```bash
# 後端覆蓋率
pytest --cov=app tests/

# 前端覆蓋率
npm run test:coverage
```

##  性能監控

### 監控指標
- API 響應時間
- 數據庫查詢性能
- 內存使用情況
- 錯誤率統計

### 日誌管理
- 應用日誌
- 錯誤日誌
- 訪問日誌
- 審計日誌

##  貢獻指南

1. Fork 項目
2. 創建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 創建 Pull Request

##  更新日誌

### v1.0.0 (2024-01-01)
- 初始版本發布
- 基礎用戶管理功能
- 簡單的財務記錄功能

### v1.1.0 (計劃中)
- 庫存管理模塊
- 客戶關係管理
- 基礎報表功能

##  許可證

本項目採用 MIT 許可證 - 查看 [LICENSE](LICENSE) 文件了解詳情

##  支持

- 文檔: [項目文檔](docs/)
- 問題反饋: [GitHub Issues](https://github.com/your-repo/ji-erp/issues)
- 討論: [GitHub Discussions](https://github.com/your-repo/ji-erp/discussions)

##  致謝

感謝所有為這個項目做出貢獻的開發者！

---

**注意**: 這是一個學習和開發中的項目，請勿在生產環境中使用未經充分測試的功能。
