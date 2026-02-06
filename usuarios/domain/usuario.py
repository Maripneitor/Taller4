from enum import Enum
from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel, Field, EmailStr


class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class Usuario(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    username: str
    email: EmailStr
    status: UserStatus = UserStatus.ACTIVE
    created_at: datetime = Field(default_factory=datetime.utcnow)

    def activate(self) -> None:
        self.status = UserStatus.ACTIVE

    def deactivate(self) -> None:
        self.status = UserStatus.INACTIVE

    def is_active(self) -> bool:
        return self.status == UserStatus.ACTIVE
