from UI import Button
from utils.Storage import clearUserStorage
from utils import navigate

async def create():
    Button("LogOut", on_click=lambda: [clearUserStorage(), navigate('/')])
