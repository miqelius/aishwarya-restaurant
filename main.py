import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dotenv import load_dotenv

# ვტვირთავთ .env ფაილის ცვლადებს
load_dotenv()

app = FastAPI()
security = HTTPBasic()

# ვიღებთ ადმინის მონაცემებს უსაფრთხო გარემოდან (.env-დან)
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "secret123")

def verify_admin(credentials: HTTPBasicCredentials = Depends(security)):
    """ავტორიზაციის შემოწმება HTTP Basic Auth-ით"""
    if credentials.username != ADMIN_USER or credentials.password != ADMIN_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="არასწორი მომხმარებელი ან პაროლი",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.post("/api/update-menu")
async def update_menu(menu_data: dict, admin: str = Depends(verify_admin)):
    """
    მენიუს განახლების ენდფოინთი. 
    მოითხოვს ავტორიზაციას (admin:password ჰედერიდან).
    პაროლი აღარ იგზავნება body-ში!
    """
    # შენი ძველი მენიუს განახლების ლოგიკა აქ იქნება...
    
    return {
        "status": "success", 
        "message": "მენიუ წარმატებით განახლდა",
        "updated_by": admin
    }
