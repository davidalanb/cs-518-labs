import bcrypt

def hash_password(pw):
    return bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt()) 

def verify_password(plain_password: str, hashed_password: str):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

#----------- nope ------------------

p = "password"

try:
    p = verify_password(p,p)
except ValueError as e:
    print(e)

#----------- yup ------------------

p = "password"
h = hash_password(p).decode('utf-8')

b = verify_password(p,h)
print(b)
