from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


class Email:
    def __init__(self, destinatario: str) -> None:
        # Rementente
        self.fromaddr = 'robovagas@gmail.com'
        # Destinatários
        self.toaddr = destinatario

    def enviar_email(self):
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr

        # Assunto do email
        msg['Subject'] = "E-mail de test"
        # Corpo do emial
        body = "Email enviado do nosso robô"

        msg.attach(MIMEText(body, 'plain'))

        # Arquivo a ser anexado
        filename = "vagas.xlsx"
        anexo = open("vagas.xlsx", "rb")

        p = MIMEBase('aplication', 'octet-stream')
        p.set_payload((anexo).read())
        encoders.encode_base64(p)
        p.add_header("Content-Disposition",
                     "attachment; filename= %s" % filename)
        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)

        # Segurança
        s.starttls()

        s.login(self.fromaddr, '123Batatinha')

        # Converte para String
        text = msg.as_string()

        s.sendmail(self.fromaddr, self.toaddr, text)

        s.quit()
