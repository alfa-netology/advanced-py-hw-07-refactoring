from decouple import config

options = {
    'mail_ru': {
        'smtp_server': 'smtp.mail.ru',
        'login': config('mail_ru_login', default=''),
        'password': config('mail_ru_password', default='')
    },
    'gmail': {
        'smtp_server': 'smtp.gmail.com',
        'login': config('gmail_login', default=''),
        'password': config('gmail_password', default='')
    }
}