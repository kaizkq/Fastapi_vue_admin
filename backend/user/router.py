import security
import user.dao as dao
import user.schema as schema
from fastapi import APIRouter, Depends

user = APIRouter(prefix="/User", tags=["User"])


@user.post("/login", summary="登录")
async def login(instance: schema.User) -> schema.Result[schema.Login]:
    obj = await dao.model.User.get_or_none(username=instance.username)
    if obj and security.verify_password(instance.password, obj.password):
        token = security.create_access_token(data={"sub": obj.username})
        return schema.Result.ok(dict(token=token, user=obj))
    return schema.Result.error("账号或密码错误")


@user.post("/register", summary="注册")
async def register(instance: schema.User) -> schema.Result:
    obj = await dao.model.User.get_or_none(username=instance.username)
    if obj:
        return schema.Result.error("用户已存在")
    instance.password = security.get_password_hash(instance.password)
    await dao.create(instance)
    return schema.Result.ok(None)


@user.get("/{id}", summary="通过ID查询详情")
async def query_user_by_id(id: int) -> schema.Result[schema.User]:
    return schema.Result.ok(await dao.query_by_id(id))


@user.get("", summary="分页条件查询")
async def query_user_all_by_limit(query: schema.User = Depends(),
                                  page: schema.PageParam = Depends()
                                  ) -> schema.PageResult[schema.User]:
    total = await dao.count(**query.model_dump(exclude_none=True))
    data = await dao.query_all_by_limit(**query.model_dump(exclude_none=True),
                                        page_number=page.page_number,
                                        page_size=page.page_size)
    return schema.PageResult.ok(data=data, total=total)


@user.post("", summary="新增数据")
async def create_user(instance: schema.User) -> schema.Result[schema.User]:
    return schema.Result.ok(await dao.create(instance))


@user.patch("/{id}", summary="更新数据")
async def update_user_by_id(
        id: int, instance: schema.User) -> schema.Result[schema.User]:
    if instance.password:
        instance.password = security.get_password_hash(instance.password)

    return schema.Result.ok(await dao.update(id, instance))


@user.delete("/{id}", summary="删除数据")
async def delete_user_by_id(id: int) -> schema.Result[schema.User]:
    return schema.Result.ok(await dao.delete_by_id(id))
