import subprocess
import crypt
salt = crypt.mksalt(crypt.METHOD_SHA512)
password="testpasswrod"
encrypted_password= crypt.crypt(password, salt)
u=input("please type type the username: ")
print(encrypted_password)
subprocess.run(["useradd","-m","-p", encrypted_password, u])