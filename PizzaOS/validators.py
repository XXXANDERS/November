class UsersValidator:
    def __init__(self, request: dict):
        self.username = request.get('username')
        self.phone = request.get('phone')
        self.name = request.get('name')
        if self.username is None or self.phone is None or self.name is None:
            raise AttributeError('Поля не должны быть пустыми')

    def validate(self):
        return bool(
            UsersValidator.username_validate(self.username) and
            UsersValidator.phone_validate(self.phone) and
            UsersValidator.name_validate(self.name)
        )

    @staticmethod
    def username_validate(field: str) -> bool:
        for c in field:
            if c not in "abcdefjhigklmnopqrstuvwxyzABCDEFJHIGKLMNOPQRSTUVWXYZ0123456789_":
                return False
        return True

    @staticmethod
    def phone_validate(field: str):
        for c in field:
            if c not in "0123456789-":
                return False
        return True

    @staticmethod
    def name_validate(field: str):
        for c in field:
            if c not in "abcdefjhigklmnopqrstuvwxyzABCDEFJHIGKLMNOPQRSTUVWXYZ ":
                return False
        return True

    @staticmethod
    def range_id_validate(field: tuple):
        return bool(
            len(field) == 2 and
            field[0].isdigit() and
            field[1].isdigit() and
            (int(field[0]) <= int(field[1]))
        )
