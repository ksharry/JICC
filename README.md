# JICC 企業資源規劃系統

一個基於 FastAPI + React 的現代化 ERP 系統，專為中小企業設計，提供完整的業務管理解決方案。

## 功能特色

### 核心模塊
- **用戶管理** - 完整的用戶認證與權限控制系統
- **財務管理** - 收入/支出記錄、發票管理、財務報表
- **庫存管理** - 產品管理、庫存進出、供應商管理
- **客戶關係管理** - 客戶資料、訂單追蹤、服務記錄
- **報表分析** - 多維度數據分析、圖表展示、導出功能

### 技術特色
- **現代化架構** - 基於 FastAPI + React 的前後端分離架構
- **微服務設計** - 模組化設計，易於擴展和維護
- **RESTful API** - 標準化的 API 接口設計
- **實時更新** - WebSocket 支持實時數據更新
- **響應式設計** - 支持多設備訪問

## 快速開始

### 環境要求
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Redis 6+

### 安裝步驟

1. **克隆項目**
`ash
git clone https://github.com/ksharry/JICC.git
cd JICC
`

2. **後端設置**
`ash
# 創建虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt

# 配置數據庫
cp jicc.conf.example jicc.conf
# 編輯 jicc.conf 文件，設置數據庫連接信息

# 運行數據庫遷移
python -m alembic upgrade head

# 啟動後端服務
python jicc-bin
`

3. **前端設置**
`ash
cd frontend
npm install
npm run dev
`

4. **訪問系統**
- 前端界面: http://localhost:3000
- 後端 API: http://localhost:8000
- API 文檔: http://localhost:8000/docs

## 項目結構

`
JICC/
 jicc-bin                 # 主入口文件
 jicc.conf               # 配置文件
 core/                   # 核心模組
    config/            # 配置管理
    database/          # 數據庫連接
    auth/              # 認證授權
    utils/             # 工具函數
 modules/               # 業務模組
    users/             # 用戶管理
    finance/           # 財務管理
    inventory/         # 庫存管理
    crm/               # 客戶關係管理
 frontend/              # 前端應用
    src/
       components/    # React 組件
       pages/         # 頁面組件
       hooks/         # 自定義 Hooks
       services/      # API 服務
    public/            # 靜態資源
 tests/                 # 測試文件
 docs/                  # 項目文檔
 .github/workflows/     # CI/CD 配置
`

## 開發指南

### 代碼規範
- 後端使用 Python 3.11+ 和 FastAPI
- 前端使用 React 18+ 和 TypeScript
- 數據庫使用 PostgreSQL 和 SQLAlchemy ORM
- 代碼風格遵循 PEP 8 和 ESLint 規範

### 提交規範
- feat: 新功能
- fix: 修復問題
- docs: 文檔更新
- style: 代碼格式調整
- refactor: 代碼重構
- test: 測試相關
- chore: 構建過程或輔助工具的變動

### 分支管理
- master - 主分支，用於生產環境
- develop - 開發分支，用於集成測試
- eature/* - 功能分支，用於新功能開發
- hotfix/* - 熱修復分支，用於緊急修復

## 部署指南

### Docker 部署
`ash
# 構建鏡像
docker-compose build

# 啟動服務
docker-compose up -d

# 查看日誌
docker-compose logs -f
`

### 生產環境部署
1. 配置環境變量
2. 設置數據庫連接
3. 配置反向代理 (Nginx)
4. 設置 SSL 證書
5. 配置監控和日誌

## 貢獻指南

1. Fork 本項目
2. 創建功能分支 (git checkout -b feature/AmazingFeature)
3. 提交更改 (git commit -m 'Add some AmazingFeature')
4. 推送到分支 (git push origin feature/AmazingFeature)
5. 開啟 Pull Request

## 授權

本項目採用 MIT 授權協議 - 查看 [LICENSE](LICENSE) 文件了解詳情。

## 聯繫方式

- 項目維護者: ksharry
- 郵箱: your-email@example.com
- 項目地址: https://github.com/ksharry/JICC

## 更新日誌

### v1.0.0 (2024-01-01)
- 初始版本發布
- 基礎用戶管理功能
- 財務管理模組
- 庫存管理模組
- 客戶關係管理模組
- 基礎報表功能

---

**JICC** - 讓企業管理更簡單、更高效！
