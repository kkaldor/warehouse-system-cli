from core.base_repository import BaseRepository
from models.user import User

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__("data/users.json", User)