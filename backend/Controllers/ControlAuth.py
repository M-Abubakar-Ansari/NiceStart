from library.dbQuery import Query
from db.db import RUN_SQL
from library.validations import IsValidEmail, IsValidName, StrengthOfPswd
from backend.Models.ModelAuth import Auth
TABLE = "users"

async def _is_unique(value: str, column: str):
    query = Query(TABLE).select("COUNT(*)").where(**{column: value}).SQL()
    result = await RUN_SQL(query, to_fetch=True)
    count = result[0] if result else 0
    return count == 0

async def _validate(values: dict) -> dict:
    name = values.get("name")
    email = values.get("email")
    pswd = values.get("password")
    conf = values.get("confirm")
    if name: name = name.strip()
    if email: email = email.strip()
    if pswd: pswd = pswd.strip()
    if conf: conf = conf.strip()
    errors = {}
    if name:
        if not IsValidName(name):
            errors['name'] = 'Name is invalid.'
        elif not await _is_unique(name, 'name'):
            errors['name'] = 'Name is already taken!'
    else:
        errors['name'] = 'Name is required!'
    if email:
        if not IsValidEmail(email):
            errors['email'] = 'Email is invalid.'
        elif not await _is_unique(email, 'email'):
            errors['email'] = 'Email is already taken!'
    else:
        errors['email'] = 'Email is required!'
    if not pswd:
        errors['password'] = 'Password is required.'
    elif StrengthOfPswd(pswd or '') < 4:
        errors['password'] = 'Password is weak!'
    elif not conf:
        errors['password'] = 'Confirm password is required.'
    elif not (pswd == conf):
        errors['password'] = 'Passwords do not match!'
    return errors

async def create(data: dict) -> dict:
    errors = await _validate(data)
    result = []
    if not errors:
        try:
            result = await Auth().create(data)
            if not isinstance(result, (list, tuple)):
                result = [result]
        except Exception as e:
            result = []
            errors['Unknown'] = "Sorry, we cannot create your account!"
    success = not bool(errors)
    return {
        "success": success,
        "errors": errors,
        "data": result
    }