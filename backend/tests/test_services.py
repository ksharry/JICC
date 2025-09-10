import pytest
from app.services.user_service import UserService
from app.services.transaction_service import TransactionService
from app.schemas.user import UserCreate
from app.schemas.transaction import TransactionCreate

def test_user_service_authenticate(db_session, test_user):
    """測試用戶服務認證"""
    user_service = UserService(db_session)
    
    # 測試正確的用戶名和密碼
    user = user_service.authenticate_user("testuser", "testpass")
    assert user is not None
    assert user.username == "testuser"
    
    # 測試錯誤的密碼
    user = user_service.authenticate_user("testuser", "wrongpass")
    assert user is None

def test_transaction_service_get_transactions(db_session, test_user, test_transaction):
    """測試交易服務獲取交易"""
    transaction_service = TransactionService(db_session)
    
    transactions = transaction_service.get_transactions()
    assert len(transactions) == 1
    assert transactions[0].type == "income"
    assert transactions[0].amount == 1000.00

def test_transaction_service_create_transaction(db_session, test_user):
    """測試交易服務創建交易"""
    transaction_service = TransactionService(db_session)
    
    transaction_data = TransactionCreate(
        type="expense",
        amount=500.00,
        description="測試支出",
        category="測試"
    )
    
    transaction = transaction_service.create_transaction(transaction_data, test_user.id)
    assert transaction.id is not None
    assert transaction.type == "expense"
    assert transaction.amount == 500.00