from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "JI ERP"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # 數據庫配置
    database_url: str = "sqlite:///./ji_erp.db"
    
    # 安全配置
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # API 配置
    api_v1_str: str = "/api/v1"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# 創建全局設置實例
settings = Settings()