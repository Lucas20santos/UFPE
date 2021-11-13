import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("pythontestarcodigos@gmail.com", "Qwertyuiop201302")
server.sendmail(
    "pythontestarcodigos@gmail.com",
    "pythontestarcodigos@gmail.com",
    "testando o smtplit com python"
)
server.quit()