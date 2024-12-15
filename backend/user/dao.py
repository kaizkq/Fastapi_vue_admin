from typing import List, Optional

import user.model as model
import user.schema as schema


async def create(obj_in: schema.User) -> model.User:
    obj = model.User(**obj_in.model_dump(exclude_unset=True))
    await obj.save()
    return obj


async def query_by_id(id: int) -> Optional[model.User]:
    return await model.User.get_or_none(id=id)


async def update(id: int, obj_in: schema.User) -> Optional[model.User]:
    obj = await query_by_id(id)
    if obj:
        for field, value in obj_in.model_dump(exclude_unset=True, exclude_none=True).items():
            setattr(obj, field, value)
        await obj.save()
    return obj


async def delete_by_id(id: int) -> Optional[model.User]:
    obj = await query_by_id(id)
    if obj:
        await obj.delete()
    return obj


async def count(**kwargs) -> int:
    return await model.User.filter(**kwargs).count()


async def query_all_by_limit(page_number: int, page_size: int,
                             **kwargs) -> List[model.User]:
    offset = (page_number - 1) * page_size
    limit = page_size
    return await model.User.filter(**kwargs).offset(offset).limit(limit).all()