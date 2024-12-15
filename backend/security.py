from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from jose import jwt, JWTError

from user.model import User

KEY = "XXXXokoafowpefpwkefpwfe"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证明文密码 vs hash密码
    :param plain_password: 明文密码
    :param hashed_password: hash密码
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    加密明文
    :param password: 明文密码
    :return:
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    生成token
    :param data: 字典
    :param expires_delta: 有效时间
    :return:
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, KEY, algorithm="HS256")
    return encoded_jwt


async def check_token(security: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    """检查用户token"""
    token = security.credentials
    try:
        payload = jwt.decode(token, KEY, algorithms=["HS256"])
        username: str = payload.get("sub")
        return await User.get(username=username)
    except JWTError:
        raise HTTPException(detail="token认证失败")
