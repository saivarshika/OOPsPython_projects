class Notifier:

    def send(self, message):
        print("Sending notification...")


class EmailNotifier(Notifier):

    def send(self, message):
        print("Email Sent:", message)


class SMSNotifier(Notifier):

    def send(self, message):
        print("SMS Sent:", message)


class PushNotifier(Notifier):

    def send(self, message):
        print("Push Notification:", message)


notifiers = [
    EmailNotifier(),
    SMSNotifier(),
    PushNotifier()
]

message = "Welcome to Python OOP!"

for notifier in notifiers:
    notifier.send(message)