import os
from email.message import EmailMessage
import ssl
from smtplib import SMTP_SSL
email_emisor = 'jsalasmoreira@gmail.com'
email_contrasena = os.environ.get('PythonGmail')
print(email_contrasena)
email_receptor = 'jaimes12.17@hotmail.com'

# Prueba de envio de Email para correo
asunto = 'Revisa mi video'
cuerpo = """
  He publicado un nuevo video y me gustaria que lo revises
"""
em = EmailMessage()

em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)
context = ssl.create_default_context()
with SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())
