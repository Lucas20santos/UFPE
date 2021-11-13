import smtplib
import email.message


def senha():
    arquivo = open("arquivoConfiguracao/senha.txt","r")
    return arquivo.readlines()

def emails():
    arquivo = open("arquivoConfiguracao/email.txt", "r")
    return arquivo.readlines()

def enviar_email():
    arq = senha()

    corpo_email = """
        Segundo email de teste com python smtplib
    """
    msg = email.message.Message()
    msg['Subject'] = "Elevada Temperatura"
    msg['From'] = "pythontestarcodigos@gmail.com"
    msg['To'] = arq[0].strip()
    password = arq[1].strip()
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print("Email enviado!")


while True:

    sensor = float(input("leitura: "))
    if sensor >= 40:
        enviar_email()
