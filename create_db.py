
from app import db, create_app

from webapp import db
from webapp import create_app


app = create_app()
with app.app_context(): #контекст нам нужен если мы обращаемся к приложению или к каким-то его компонентам если мы находимя вне модуля приложения например create_db и wrbapp у тебя на одном уровне, поэтому нужен контекст, если мы из модуля приложения будем, вызывать, то контекст скорее всего не понадобится
    db.create_all()

