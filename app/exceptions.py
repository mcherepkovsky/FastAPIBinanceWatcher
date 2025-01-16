from fastapi import HTTPException, status


class WatcherException(HTTPException):  # <-- наследуемся от HTTPException, который наследован от Exception
    status_code = 500  # <-- задаем значения по умолчанию
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class PairDoesntExists(WatcherException):
    status_code = status.HTTP_409_CONFLICT
    detail = "This pair doesn\'t exists"


class UserIsNotPresentException(WatcherException):
    status_code = status.HTTP_401_UNAUTHORIZED


class NotificationCannotBeAddedException(WatcherException):
    status_code = status.HTTP_409_CONFLICT
    detail = "The notice has not been added"


class TokenAbsentException(WatcherException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token is missing"


class IncorrectTokenFormatException(WatcherException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"


class SubscriptionNotFound(WatcherException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Subscription not found"
