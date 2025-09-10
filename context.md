# JICC 專案技術規格

## 專案概述
JICC 是一個基於 Odoo 17.0 架構設計的企業資源規劃系統，採用模組化設計，支援多種業務功能模組。

## 專案架構

### 目錄結構 (Odoo 17.0 風格)
`
JICC/
 jicc-bin              # 主啟動腳本 (類似 odoo-bin)
 jicc.bat              # Windows 批處理文件
 jicc.conf             # 配置文件 (類似 odoo.conf)
 main.py               # 主應用文件
 config_manager.py     # 配置管理模組
 .venv_py31/           # Python 3.10 虛擬環境
 core/                 # 核心框架
    config.py         # 配置管理
    database.py       # 數據庫管理
 addons/               # 業務模組目錄
    base/             # 基礎模組
       models/       # 數據模型
       views/        # 視圖模板
       controllers/  # API 控制器
       services/     # 業務邏輯服務
    user/             # 人員管理模組
    auth/             # 權限認證模組
    transaction/      # 交易管理模組
 backend/              # 舊後端 (保留)
 backup/               # 備份文件
 .vscode/              # VS Code 配置
 .git/                 # Git 版本控制
 README.md             # 項目文檔
 context.md            # 技術規格 (本文件)
 .cursorrules          # Cursor AI 規則
`

## 技術棧

### 後端技術
- **框架**: FastAPI (Python 3.10+)
- **ORM**: SQLAlchemy
- **數據庫**: SQLite (開發) / PostgreSQL (生產)
- **認證**: JWT + OAuth2
- **緩存**: Redis (計劃中)
- **任務隊列**: Celery (計劃中)
- **文檔**: Swagger/OpenAPI

### 前端技術 (計劃中)
- **框架**: React 18 + TypeScript
- **UI 庫**: Material-UI (MUI) 或 Ant Design
- **狀態管理**: Redux Toolkit + RTK Query
- **路由**: React Router v6
- **表單**: React Hook Form + Yup
- **圖表**: Chart.js 或 Recharts

### 開發工具
- **版本控制**: Git
- **IDE**: Cursor (VS Code)
- **虛擬環境**: Python venv
- **包管理**: pip
- **測試**: pytest
- **代碼檢查**: flake8

## 核心功能模組

### 1. 基礎模組 (addons/base)
- 系統配置管理
- 通用工具函數
- 基礎數據模型
- 系統設置

### 2. 人員管理模組 (addons/user)
- 用戶註冊/登入
- 用戶資料管理
- 角色權限管理
- 多因子認證

### 3. 權限認證模組 (addons/auth)
- JWT Token 管理
- 角色基礎存取控制 (RBAC)
- API 權限驗證
- 會話管理

### 4. 交易管理模組 (addons/transaction)
- 財務交易記錄
- 收入/支出管理
- 發票管理
- 付款記錄

### 5. 庫存管理模組 (計劃中)
- 產品管理
- 庫存進出
- 庫存盤點
- 供應商管理

### 6. 客戶關係管理模組 (計劃中)
- 客戶資料管理
- 聯絡人管理
- 訂單管理
- 報價單管理

## API 設計規範

### RESTful API 端點
- 使用標準 HTTP 方法 (GET, POST, PUT, DELETE)
- 統一響應格式
- 適當的 HTTP 狀態碼
- 錯誤處理和日誌記錄
- API 版本控制

### 響應格式
`json
{
  "success": true,
  "data": {},
  "message": "操作成功",
  "errors": [],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "pages": 5
  }
}
`

## 安全機制

### 認證與授權
- JWT Token 認證
- 基於角色的存取控制 (RBAC)
- API 速率限制
- CORS 配置

### 數據安全
- 輸入驗證和清理
- SQL 注入防護
- XSS 防護
- CSRF 防護
- 數據加密

## 性能要求

### 響應時間
- API 響應時間 < 200ms
- 頁面載入時間 < 3s
- 數據庫查詢優化

### 可擴展性
- 支援 1000+ 併發用戶
- 水平擴展能力
- 負載均衡支援

## 開發環境

### 本地開發
- Python 3.10+
- Node.js 18+ (前端)
- PostgreSQL 14+ (生產)
- Redis 6+ (緩存)
- Docker (可選)

### 工具鏈
- Git 版本控制
- Pre-commit hooks
- 自動化測試
- CI/CD 流程
- 代碼品質檢查

## 部署架構

### 開發環境
- 本地 Docker Compose
- 熱重載開發
- 快速測試環境

### 生產環境
- Docker 容器化
- Kubernetes 編排
- 負載均衡
- 數據庫集群
- 監控和日誌

## 開發階段

### 第一階段：基礎架構 (已完成)
-  專案重命名 (JI ERP  JICC)
-  Odoo 風格目錄結構
-  基本登入功能
-  配置管理系統
-  虛擬環境設置

### 第二階段：核心功能 (進行中)
-  用戶管理模組
-  權限認證模組
-  交易管理模組
-  API 文檔生成

### 第三階段：業務功能 (計劃中)
-  庫存管理模組
-  客戶關係管理
-  報表分析功能
-  前端界面開發

### 第四階段：優化部署 (計劃中)
-  性能優化
-  安全加固
-  測試覆蓋
-  生產部署

## 模組化設計原則

### 每個模組包含
- **models/**: 數據模型定義
- **views/**: 視圖模板和前端組件
- **controllers/**: API 端點控制器
- **services/**: 業務邏輯服務層

### 模組間依賴
- 基礎模組 (base) 為其他模組提供通用功能
- 認證模組 (auth) 為所有模組提供安全認證
- 各業務模組相對獨立，可單獨開發和測試

## 開發規範

### 代碼規範
- 遵循 PEP 8 Python 代碼規範
- 使用 TypeScript 嚴格模式
- 實現完整的錯誤處理
- 編寫單元測試和集成測試

### 文檔要求
- API 文檔 (Swagger)
- 數據庫設計文檔
- 部署文檔
- 開發指南

### 測試策略
- 單元測試覆蓋率 > 80%
- 集成測試
- 端到端測試
- 性能測試

## 學習目標

### 技術能力
- 企業級 Web 應用開發
- 微服務架構設計
- 數據庫設計和優化
- 安全機制實現

### 業務理解
- ERP 系統核心概念
- 企業流程管理
- 財務管理基礎
- 庫存管理原理

## 專案特色

### 教學導向
我們採用漸進式開發策略，從簡單的基礎功能開始：

#### 第一階段：基礎功能 (1-2週)
- 使用 SQLite + 原生 SQL
- 純 HTML/CSS/JavaScript 界面
- 基本 CRUD 操作
- 簡單的用戶認證

#### 第二階段：技術升級 (3-4週)
- 遷移到 PostgreSQL + SQLAlchemy
- React + TypeScript 前端
- JWT 認證
- 基本的權限管理

#### 第三階段：企業級 (6-8週)
- 微服務架構
- 進階的權限系統
- 完整的業務功能
- 性能優化

### 學習重點
- 理解 ERP 系統核心架構
- 掌握現代 Web 開發技術
- 學習企業級系統設計模式
- 培養全端開發能力

這個專案將幫助你從零開始，逐步建立一個完整的企業級 ERP 系統，同時學習最新的技術和最佳實踐。

## 當前狀態

### 已完成功能
-  專案架構重組 (Odoo 17.0 風格)
-  基本登入系統
-  配置管理系統
-  模組化目錄結構
-  虛擬環境設置
-  Git 版本控制

### 下一步計劃
-  實現用戶管理模組
-  完善權限認證系統
-  開發交易管理功能
-  建立 API 文檔

## 技術債務

### 需要改進的地方
- 數據庫模型需要完善
- 錯誤處理需要標準化
- 測試覆蓋率需要提升
- 文檔需要持續更新

### 優化計劃
- 引入 Redis 緩存
- 實現 Celery 異步任務
- 添加監控和日誌系統
- 建立 CI/CD 流程
