from UI import Label, RawLabel, Footer, RawRow, Link
from ENV import APP_NAME
from utils.Auth import isAuthenticated
from routes.ROUTES import LOGIN, SIGNUP

def CompFooter():
    with Footer(clas="flex flex-row justify-between items-center") as footer:
        RawLabel(APP_NAME + " &copy; 2025, All rights reserved!")
        with RawRow(clas="w-fit gap-2"):
            if not isAuthenticated():
                Link('Login', LOGIN)
                RawLabel(".")
                Link('Signup', SIGNUP)
    return footer
