from application import connection
from application.classes import Postman

recipients = ['prime-alfa@mail.ru']
subject = 'PY-37-advanced-hw-07-task-with-star'
message_content = 'Task solved'

gmail_options = connection.options.get('gmail')
gmail_postman = Postman(**gmail_options)
gmail_sender = gmail_options.get('login')

mail_ru_options = connection.options.get('mail_ru')
mail_ru_postman = Postman(**mail_ru_options)
mail_ru_sender = mail_ru_options.get('login')

message = gmail_postman.prepare_message_to_send(gmail_sender, recipients, subject, message_content)
gmail_postman.send_message(message)

message = mail_ru_postman.prepare_message_to_send(mail_ru_sender, recipients, subject, message_content)
mail_ru_postman.send_message(message)
