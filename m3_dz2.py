# Рассылка писем
def send_email(messege: str, recipient: str, sender='urban.info@gmail.com'):
    if '@' not in recipient or '@' not in sender\
        or not recipient.endswith(('.com', '.ru', '.net'))\
        or sendler.endswith(('.com', '.ru', '.net')):
        print(f"Невозможно отправить сообщение с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif '.uk' in recipient:
        print(f'Недопустимый адрес: {recipient}')
    elif sender != 'urban.info@gmail.com':
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ: {sender}")
    else:
        print(f'Сообщение: {messege} отправлено с адреса: {sender} получателю: {recipient}')


messege = input('Введите текст сообщения: ')
recipient = input('Получатель: ')

send_email(messege, recipient, 'urban.info@gmail.com')
