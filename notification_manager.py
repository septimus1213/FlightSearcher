import smtplib

class NotificationManager:
    """It sends an email to the provided address for each deal found."""
    
    def __init__(self,my_email,my_pass,message) -> None:
        
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_pass)
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=message)