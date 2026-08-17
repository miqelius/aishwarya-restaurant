import json, os, secrets
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

app = FastAPI(title="Masala Restaurant System")
security = HTTPBasic()

ADMIN_USER = "admin"
ADMIN_PASSWORD = "masala2026"
MENU_FILE = "menu.json"

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root(): return FileResponse("static/index.html")

def verify_admin(credentials: HTTPBasicCredentials = Depends(security)):
    is_user_correct = secrets.compare_digest(credentials.username, ADMIN_USER)
    is_pass_correct = secrets.compare_digest(credentials.password, ADMIN_PASSWORD)
    if not (is_user_correct and is_pass_correct):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="არასწორი მონაცემები",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/admin")
def read_admin(username: str = Depends(verify_admin)):
    return FileResponse("static/admin.html")

@app.get("/api/menu")
def get_menu():
    if not os.path.exists(MENU_FILE): raise HTTPException(404, "Menu not found")
    with open(MENU_FILE, "r", encoding="utf-8") as f: return json.load(f)

class MenuUpdate(BaseModel):
    password: str
    data: dict

@app.post("/api/update-menu")
def update_menu(payload: MenuUpdate):
    if payload.password != ADMIN_PASSWORD: raise HTTPException(401, "არასწორი პაროლი!")
    with open(MENU_FILE, "w", encoding="utf-8") as f: json.dump(payload.data, f, ensure_ascii=False, indent=2)
    return {"success": True, "message": "მენიუ განახლდა!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
