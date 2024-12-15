from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field
from pydantic.alias_generators import to_camel

T = TypeVar('T')


class Result(BaseModel, Generic[T]):
    success: bool = Field(..., description="是否成功")
    message: str = Field(..., description="额外消息")
    data: Optional[T] = Field(None, description="响应数据")

    @classmethod
    def ok(cls, data: T, message: str = "成功"):
        return cls(data=data, message=message, success=True)

    @classmethod
    def error(cls, message: str = "失败"):
        return cls(data=None, message=message, success=False)


class PageResult(Result[T]):
    total: int = Field(0, description="数据总数")
    data: List[T] = Field(default_factory=list, description="响应数据")

    @classmethod
    def ok(cls, data: List[T], message: str = "成功", total: int = 0):
        return cls(data=data, total=total, message=message, success=True)


class PageParam(BaseModel):
    page_number: int = Field(1, description="页码")
    page_size: int = Field(10, description="每页数量")

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class User(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = Field(None, description='账号')
    password: Optional[str] = Field(None, description='密码')
    nickname: Optional[str] = Field(None, description='昵称')
    avatar: Optional[str] = Field(None, description='头像url')
    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class Login(BaseModel):
    user: Optional[User] = None
    token: Optional[str] = None
