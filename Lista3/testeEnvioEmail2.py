import smtplib
import email.message

def enviar_email():
    corpo_email = """
        Segundo email de teste com python smtplib
    """
    msg = email.message.Message()
    msg['Subject'] = "Email Automatico"
    msg['From'] = "pythontestarcodigos@gmail.com"
    msg['To'] = "lucas210souza@gmail.com"
    password = "Qwertyuiop201302"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print("Email enviado!")


enviar_email()

