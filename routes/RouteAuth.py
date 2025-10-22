from .ROUTES import LOGIN, SIGNUP
from nicegui.ui import page
from pages.Auth.PageSignUp import create as create_signup

@page(LOGIN)
def render_login():
    pass 

@page(SIGNUP)
async def render_signup():
    await create_signup()
