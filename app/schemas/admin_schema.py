from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr

# registration of admin
class AdminCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# admin reponse sent to the frontend after successful registration
class AdminResponse(BaseModel):
    admin_id: int
    name: str
    email: EmailStr
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# admin login
class AdminLogin(BaseModel):
    email: EmailStr
    password: str