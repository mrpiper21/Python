class phone:
    classCount = 0
    def __init__(self, apps, notifications, Ram, storage):
        self.apps = apps
        self.notifications = notifications
        self.Ram = Ram
        self.storage = storage
        phone.classCount += 1

    def __del__(self):
        phone.classCount -= 1

    def __str__(self):
        return('apps: (), notifs: (), ram: (), storage: ()'.format(self.apps, self.notifications, self.Ram, self.storage))


Phone1 = phone(31, 12234, 4, 16)
Phone2 = phone(24, 342, 8, 64)
print(Phone2.apps, Phone2.notifications, Phone2.Ram, Phone2.storage)
print(Phone2)

