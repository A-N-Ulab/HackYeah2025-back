from datetime import datetime, timedelta
from typing import Optional

import ulid

from db_models.Token import Token
from lib import db


class TokensStore:
    TTL = 24 * 60 * 60 * 30  # 30 days in seconds

    def createToken(self, userId: int) -> str:
        token = "TOKN" + str(ulid.new())

        createdAt = self._now()
        expiresAt = self._nowPlusTTL()

        newToken = Token(id=token, user_id=userId, created_at=createdAt, expires_at=expiresAt)
        db.session.add(newToken)
        db.session.commit()

        return token

    def isValid(self, token: str) -> bool:
        result = Token.query.filter_by(id=token).first()

        if result is None:
            return False

        expiresAt: datetime = result.expires_at

        if self._now() < expiresAt:
            # Renew token TTL
            expiresAt = self._nowPlusTTL()
            Token.query.filter_by(id=token).first().expires_at = expiresAt
            return True

        db.session.delete(result)
        db.session.commit()
        return False

    def isValidUser(self, token: str, userId: str) -> bool:
        result = Token.query.filter_by(id=token, user_id=userId).first()
        return result is not None

    def getUserId(self, token: str) -> Optional[str]:
        result = Token.query.filter_by(id=token).first()

        if result is None:
            return None

        userId = result.user_id
        return userId

    def getUserToken(self, userId: int) -> Optional[str]:
        result = Token.query.filter_by(user_id=userId).first()

        if result is None:
            return None

        token = result.id
        return token

    def deleteToken(self, token: str) -> bool:
        deletedCount = Token.query.filter_by(id=token).delete()
        db.session.commit()
        deletedAnything = deletedCount > 0
        return deletedAnything

    def _now(self) -> datetime:
        nowTimestamp = datetime.now()
        return nowTimestamp

    def _nowPlusTTL(self) -> datetime:
        nowPlusTTL = self._now() + timedelta(seconds=TokensStore.TTL)
        return nowPlusTTL
