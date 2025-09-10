import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.models.user import User
from app.models.transaction import Transaction

# 測試數據庫配置
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """創建測試數據庫會話"""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def test_user(db_session):
    """創建測試用戶"""
    user = User(
        username="testuser",
        password="testpass",
        role="user"
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

@pytest.fixture(scope="function")
def test_transaction(db_session, test_user):
    """創建測試交易"""
    transaction = Transaction(
        type="income",
        amount=1000.00,
        description="測試收入",
        category="測試",
        user_id=test_user.id
    )
    db_session.add(transaction)
    db_session.commit()
    db_session.refresh(transaction)
    return transaction