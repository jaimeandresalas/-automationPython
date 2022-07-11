import os
from email.message import EmailMessage
import ssl
from smtplib import SMTP_SSL
import imghdr
email_emisor = 'jsalasmoreira@gmail.com'
email_contrasena = os.environ.get('PythonGmail')
print(email_contrasena)
email_receptor = 'jaimes12.17@hotmail.com'

# Prueba de envio de Email para correo
asunto = 'Envio de Foto'
cuerpo = """
  He publicado un nuevo video y me gustaria que lo revises, pureba de envio de correo
"""
em = EmailMessage()

em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)
context = ssl.create_default_context()
# Adjuntar Archivo en un correo electronico
with open('./assets/pug.png', 'rb') as file:
    file_data = file.read()
    file_type = imghdr.what(file.name)
    file_name = file.name
em.add_attachment(file_data, filename=file_name,
                  subtype=file_type, maintype='image')
# Enviar Email
with SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())
