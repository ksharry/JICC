import pytest
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.transaction import Transaction

def test_user_creation(db_session):
    """測試用戶創建"""
    user = User(
        username="testuser",
        password="testpass",
        role="user"
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    
    assert user.id is not None
    assert user.username == "testuser"
    assert user.role == "user"

def test_transaction_creation(db_session, test_user):
    """測試交易創建"""
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
    
    assert transaction.id is not None
    assert transaction.type == "income"
    assert transaction.amount == 1000.00
    assert transaction.user_id == test_user.id