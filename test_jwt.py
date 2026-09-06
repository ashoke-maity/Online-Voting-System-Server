from app.core.security import create_access_token

token = create_access_token({"sub": "ashokemaity853@gmail.com", "roles": "ADMIN"})

print(token)