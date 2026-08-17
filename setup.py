import os, json

os.makedirs("static", exist_ok=True)

with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write("fastapi==0.110.0\nuvicorn==0.28.0\npydantic==2.6.4\n")

menu_data = {
  "categories": {
    "ka": {
      "Starter": "წასახემსებლები", "Eggs": "კვერცხის კერძები", "Salad": "სალათები", "Hot Soup": "ცხელი წვნილები",
      "Tandoor": "თონე (Tandoor)", "Mutton": "ცხვრის ხორცი", "Chicken": "ქათმის კერძები", "Fish & Seafood": "თევზეული და ზღვის პროდუქტები",
      "Vegetables": "ბოსტნეული", "Paneer": "პანირი (ყველი)", "Rice": "ბრინჯი"
    },
    "en": {
      "Starter": "Starters", "Eggs": "Eggs", "Salad": "Salads", "Hot Soup": "Hot Soups",
      "Tandoor": "Tandoor", "Mutton": "Mutton", "Chicken": "Chicken", "Fish & Seafood": "Fish & Seafood",
      "Vegetables": "Vegetables", "Paneer": "Paneer", "Rice": "Rice"
    },
    "hi": {
      "Starter": "स्टार्टर्स (Starters)", "Eggs": "अंडे (Eggs)", "Salad": "सलाद (Salad)", "Hot Soup": "गरम सूप (Hot Soup)",
      "Tandoor": "तंदूर (Tandoor)", "Mutton": "मटन (Mutton)", "Chicken": "चिकन (Chicken)", "Fish & Seafood": "मछली और सीफूड (Fish & Seafood)",
      "Vegetables": "सब्जियां (Vegetables)", "Paneer": "पनीर (Paneer)", "Rice": "चावल (Rice)"
    }
  },
  "sections": {
    "Starter": [["Chicken Pakora","25 ₾","12 pcs"],["Chilli Chicken","25 ₾",""],["Chicken Manchurian","25 ₾",""],["Garlic Chicken","30 ₾",""],["Chicken Nuggets","25 ₾","8 pcs"],["Veg Chilli Paneer","30 ₾","8 pcs"],["Chilli Potatoes","20 ₾","10–12 pcs"],["Paneer Tikka","35 ₾","5–6 pcs"],["Paneer Pakora","25 ₾","8 pcs"],["Gobi 65","25 ₾","10 pcs"],["Paneer 65","35 ₾","8 pcs"],["Masala Boondi","10 ₾",""],["Fish Amritsari Fry","35 ₾","8 pcs"],["Fish Nuggets","45 ₾","8 pcs"],["Shrimp Chilli","45 ₾",""],["Shrimp Pakora","45 ₾","8 pcs"]],
    "Eggs": [["Egg Curry","25 ₾","Boiled egg in smooth onion-tomato gravy with North Indian spices."],["Omelette","22 ₾",""],["Egg Bhurji","14 ₾",""]],
    "Salad": [["Green Salad","12 ₾","Cucumber, tomato, onion, carrot, green chili and lemon."],["Kachumber Salad","10 ₾","Cabbage, capsicum, onion, tomato, green chili, cucumber, lemon and Indian spices."],["Onion Salad","5 ₾",""]],
    "Hot Soup": [["Tomato Soup","10 ₾","Cream of tomato infused with herbs and spices."],["Chicken Soup","12 ₾","Chicken stock, fresh herbs, shredded chicken and coriander."],["Vegetable Soup","10 ₾","Vegetable stock, herbs, vegetables and coriander."],["Mushroom Soup","10 ₾","Mushroom stock with milk cream."],["Lentil Soup","10 ₾","Yellow lentils, garlic, onion, turmeric and lemon."],["Hot & Sour Soup Chicken","12 ₾",""],["Hot & Sour Soup Veg","12 ₾",""],["Veg Noodles","20 ₾",""],["Chicken Noodles","25 ₾",""]],
    "Tandoor": [["Chicken Tikka","30 ₾",""],["Chicken Tandoori","32 ₾",""],["Chicken Afghani","37 ₾",""],["Tandoori Fish","47 ₾",""],["Tandoori Shrimp","57 ₾",""],["Tandoori Mixed Grill","67 ₾",""],["Tandoori Vegetables","42 ₾",""]],
    "Mutton": [["Kashmiri Roghan Josh","37 ₾","Tender lamb cubes in yogurt-based sauce with herbs and light spices."],["Mutton Curry","37 ₾","Tender lamb slow cooked in light gravy with fresh ground spices and chili paste."],["Mutton Masala","34 ₾","Tender lamb with fresh tomatoes, oriental spices and a touch of cream."],["Lamb Karahi","37 ₾","6 pcs"],["Mutton Korma","37 ₾","6 pcs"],["Mutton Palak","37 ₾",""]],
    "Chicken": [["Karahi Chicken","32 ₾","Boneless chicken with capsicum, onions, garlic, ginger, tomatoes and Indian seasoning."],["Chicken Tikka Masala","32 ₾","Tandoor-roasted boneless chicken with peppers and special sauce."],["Chicken Curry","28 ₾","Chicken with bone in light gravy and fresh ground spices."],["Butter Chicken","32 ₾","Tandoor-roasted boneless chicken in creamy tomato sauce."],["Chicken Lababdar","32 ₾","Boneless chicken with onion, capsicum and ginger in a flavorful sauce."],["Chicken Korma","32 ₾",""],["Achari Chicken","30 ₾","6 pcs"],["Chicken Keema","32 ₾",""],["Schezwan Chicken","32 ₾",""],["Chicken Masala","32 ₾","6 pcs"],["Methi Chicken","32 ₾","6 pcs"],["Hariyali Chicken","32 ₾","6 pcs"],["Pepper Chicken","32 ₾","6 pcs"],["Lemon Chicken","32 ₾","6 pcs"],["Chicken Jalfrezi","37 ₾","8 pcs"]],
    "Fish & Seafood": [["Fish Curry","30 ₾","Fish in light onion, garlic and ginger gravy with fresh ground spices."],["Fish Masala","32 ₾","Fish with onion, garlic, ginger and Indian spices."],["Salmon Curry","37 ₾","Salmon fillet with tomato, coconut milk and aromatic Indian spices."],["Shrimp Masala","44 ₾","Shrimp with coconut oil, curry leaves, fennel, black pepper, cumin and spices."],["Shrimp Curry","42 ₾","Prawn with onion, garlic, ginger, tomatoes, coriander and chili."]],
    "Vegetables": [["Dal Makhani","25 ₾","Black dal, chana dal and kidney beans slow simmered with onion, garlic, ginger and cream."],["Chana Masala","25 ₾","Chickpeas cooked in an exotic blend of North Indian spices."],["Tadka Dal","25 ₾","Yellow lentils tempered with onion, garlic, ginger and tomatoes."],["Dal Palak","25 ₾",""],["Palak Corn","22 ₾",""],["Mix Vegetable","22 ₾","Seasonal vegetables cooked in curry sauce."],["Methi Aloo","20 ₾",""],["Aloo Matar","20 ₾",""],["Aloo Gobi","20 ₾","Cauliflower and potatoes with ginger, cumin, tomato and coriander."],["Palak Chana","28 ₾",""],["Rajma Masala","22 ₾",""],["Aloo Jeera","20 ₾","Potatoes cooked with cumin seeds and aromatic spices."]],
    "Paneer": [["Paneer Tikka Masala","32 ₾","Homemade Indian soft cheese, tomato, onion and capsicum, roasted and finished in creamy sauce."],["Paneer Butter Masala","32 ₾","Paneer with cashew, coconut and creamy tomato sauce."],["Malai Kofta","28 ₾","Soft cheese and potato balls with dry nuts."],["Palak Paneer","28 ₾","Spinach with paneer, herbs and spices."],["Mutter Paneer","28 ₾",""],["Karahi Paneer","32 ₾","Paneer with onions, capsicum, herbs and spices."],["Paneer Labaddar","32 ₾",""],["Paneer Korma","34 ₾",""],["Mushroom Masala","28 ₾",""]],
    "Rice": [["Steamed Rice","10 ₾","Fluffy long-grain Indian basmati rice."],["Jeera Rice","14 ₾",""],["Vegetable Biryani","25 ₾","Aromatic basmati rice with seasonal vegetables, herbs, spices and nuts."],["Vegetable Fried Rice","22 ₾",""],["Biryani Rice","22 ₾",""],["Garlic Rice","14 ₾",""],["Egg Biryani","24 ₾","Aromatic basmati rice and eggs with Indian herbs and spices."],["Egg Fried Rice","22 ₾",""],["Chicken Biryani","30 ₾",""],["Chicken Fried Rice","27 ₾",""],["Mutton Biryani","34 ₾",""],["Vegetable Pulao","24 ₾",""],["Shrimp Biryani","47 ₾",""]]
  }
}

with open("menu.json", "w", encoding="utf-8") as f:
    json.dump(menu_data, f, ensure_ascii=False, indent=2)

with open("main.py", "w", encoding="utf-8") as f:
    f.write('''import json, os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="Masala Restaurant System")
ADMIN_PASSWORD = "masala2026"
MENU_FILE = "menu.json"

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root(): return FileResponse("static/index.html")

@app.get("/admin")
def read_admin(): return FileResponse("static/admin.html")

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
''')

with open("static/index.html", "w", encoding="utf-8") as f:
    f.write('''<!doctype html>
<html lang="ka">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <title>MASALA — Indian Kitchen • Tbilisi</title>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root{--ink:#17130f;--cream:#f7f0e4;--gold:#c99a3b;--red:#8e241b;--muted:#756b60}
    *{box-sizing:border-box}body{margin:0;background:var(--cream);color:var(--ink);font-family:Inter,sans-serif}
    .container{width:min(1160px,92%);margin:auto}
    header{position:fixed;z-index:20;top:0;left:0;right:0;padding:18px 0;background:rgba(23,19,15,.94);backdrop-filter:blur(12px)}
    .nav{display:flex;align-items:center;justify-content:space-between}
    .logo{font-family:"Cormorant Garamond";font-size:32px;color:#fff;text-decoration:none;font-weight:700}
    nav a{color:#fff;text-decoration:none;margin-left:20px;font-size:14px;font-weight:600}
    .hero{min-height:700px;display:grid;place-items:center;text-align:center;color:#fff;background:linear-gradient(rgba(17,10,5,.7),rgba(17,10,5,.7)),url("https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=1800&q=85") center/cover;padding-top:100px}
    h1{font-family:"Cormorant Garamond";font-size:clamp(50px,8vw,100px);margin:20px 0}
    .btn{display:inline-block;padding:12px 24px;background:var(--gold);color:#fff;text-decoration:none;font-weight:700;border-radius:4px;margin:5px}
    section{padding:80px 0}.menu-wrap{background:#fffaf2}
    .accordion-item{border:1px solid #d9cbb8;border-radius:6px;background:#fff;margin-bottom:12px;overflow:hidden}
    .accordion-header{width:100%;padding:18px 25px;background:none;border:none;display:flex;justify-content:space-between;align-items:center;font-family:"Cormorant Garamond";font-size:26px;font-weight:600;cursor:pointer}
    .accordion-content{max-height:0;overflow:hidden;transition:max-height .3s ease-out;padding:0 25px}
    .accordion-item.active .accordion-content{max-height:1500px;padding:0 25px 20px}
    .item{padding:14px 0;border-bottom:1px dashed #ddd0bf;display:flex;justify-content:space-between;gap:20px}
    .item h4{margin:0 0 4px;font-family:"Cormorant Garamond";font-size:20px}
    .item p{margin:0;font-size:12px;color:var(--muted)}
    .price{color:var(--red);font-weight:700;white-space:nowrap}
  </style>
</head>
<body>
<header><div class="container nav"><a class="logo" href="#">MASALA</a><nav><a href="#menu">Menu</a><a href="/admin" target="_blank">Admin</a></nav></div></header>
<section class="hero"><div class="container"><h1>Flavour of India</h1><p>Authentic Indian dishes in Tbilisi</p><a class="btn" href="#menu">Explore Menu</a></div></section>
<section class="menu-wrap" id="menu">
  <div class="container">
    <h2 style="font-family:'Cormorant Garamond';font-size:48px;text-align:center;margin-bottom:40px">Menu</h2>
    <div id="menuAccordion"></div>
  </div>
</section>
<script>
async function loadMenu() {
  const res = await fetch('/api/menu');
  const data = await res.json();
  const container = document.getElementById('menuAccordion');
  const cats = data.categories['en'];
  const secs = data.sections;
  
  Object.entries(secs).forEach(([key, items], idx) => {
    const title = cats[key] || key;
    const div = document.createElement('div');
    div.className = 'accordion-item' + (idx === 0 ? ' active' : '');
    div.innerHTML = `
      <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
        <span>${title}</span><span>+</span>
      </button>
      <div class="accordion-content">
        ${items.map(i => `<div class="item"><div><h4>${i[0]}</h4><p>${i[2]||''}</p></div><div class="price">${i[1]}</div></div>`).join('')}
      </div>`;
    container.appendChild(div);
  });
}
loadMenu();
</script>
</body>
</html>
''')

with open("static/admin.html", "w", encoding="utf-8") as f:
    f.write('''<!doctype html>
<html lang="ka">
<head><meta charset="utf-8"><title>Admin</title><style>body{font-family:sans-serif;background:#f4f0ea;padding:30px}.box{max-width:700px;margin:auto;background:#fff;padding:20px;border-radius:6px}textarea{width:100%;height:400px;font-family:monospace}</style></head>
<body><div class="box"><h2>Admin Panel</h2>
<input type="password" id="pwd" placeholder="Password (masala2026)"><button onclick="login()">Load</button>
<br><br><textarea id="json"></textarea><br><button onclick="save()">Save</button></div>
<script>
async function login(){
  const res = await fetch('/api/menu');
  document.getElementById('json').value = JSON.stringify(await res.json(), null, 2);
}
async function save(){
  await fetch('/api/update-menu', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({password:document.getElementById('pwd').value, data:JSON.parse(document.getElementById('json').value)})});
  alert('Saved!');
}
</script></body></html>
''')

print("All files created successfully!")
