from sqlalchemy.orm import Session
from .models.user import User

class UserService:
    def __init__(self, db: Session):
        self.db = db
    
    def authenticate_user(self, username: str, password: str) -> User:
        user = self.db.query(User).filter(
            User.username == username, 
            User.password == password
        ).first()
        return user
    
    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()
    
    def create_user(self, username: str, password: str, role: str = "user") -> User:
        user = User(username=username, password=password, role=role)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
