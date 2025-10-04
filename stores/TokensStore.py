import time
from datetime import datetime, timedelta

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

    # def isValid(self, token: str) -> bool:
    #     result = self.con.query("SELECT * FROM tokens WHERE id = %s", (token,))
    #
    #     if len(result) == 0:
    #         return False
    #
    #     expiresAt: datetime = result[0][2]
    #
    #     if self.con.dbTimeNow() < expiresAt:
    #         # Renew token TTL
    #         expiresAt = self._nowPlusTTL()
    #         self.con.executeCount("UPDATE tokens SET expires_at = %s WHERE id = %s", (expiresAt, token))
    #         return True
    #
    #     # This token exists, but is expired - let's delete it
    #     self.con.executeCount("DELETE FROM tokens WHERE id = %s", (token,))
    #
    #     return False
    #
    # def isValidUser(self, token: str, userId: str) -> bool:
    #     result = self.con.query("SELECT * FROM tokens WHERE id = %s AND user = %s", (token, userId))
    #
    #     if len(result) == 0:
    #         return False
    #
    #     expiresAt: datetime = result[0][2]
    #
    #     if self.con.dbTimeNow() < expiresAt:
    #         # Renew token TTL
    #         expiresAt = self._nowPlusTTL()
    #         self.con.executeCount("UPDATE SET expires_at = %s WHERE id = %s", (expiresAt, token))
    #         return True
    #
    #     return False
    #
    # def getUserId(self, token: str) -> Optional[str]:
    #     result = self.con.query("SELECT user FROM tokens WHERE id = %s", (token,))
    #
    #     if len(result) == 0:
    #         return None
    #
    #     userId = result[0][0]
    #     return userId
    #
    # def deleteToken(self, token: str) -> bool:
    #     result = self.con.executeCount("DELETE FROM tokens WHERE id = %s", (token,))
    #     return result > 0

    def _now(self) -> datetime:
        nowTimestamp = datetime.now()
        return nowTimestamp

    def _nowPlusTTL(self) -> datetime:
        nowPlusTTL = self._now() + timedelta(seconds=TokensStore.TTL)
        return nowPlusTTL
