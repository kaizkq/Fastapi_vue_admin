from typing import List, Optional

import book.model as model
import book.schema as schema


async def create(obj_in: schema.Books) -> model.Books:
    obj = model.Books(**obj_in.model_dump(exclude_unset=True))
    await obj.save()
    return obj


async def query_by_id(id: int) -> Optional[model.Books]:
    return await model.Books.get_or_none(id=id)


async def update(id: int, obj_in: schema.Books) -> Optional[model.Books]:
    obj = await query_by_id(id)
    if obj:
        for field, value in obj_in.model_dump(exclude_unset=True).items():
            setattr(obj, field, value)
        await obj.save()
    return obj


async def delete_by_id(id: int) -> Optional[model.Books]:
    obj = await query_by_id(id)
    if obj:
        await obj.delete()
    return obj


async def count(**kwargs) -> int:
    return await model.Books.filter(**kwargs).count()


async def query_all_by_limit(page_number: int, page_size: int,
                             **kwargs) -> List[model.Books]:
    offset = (page_number - 1) * page_size
    limit = page_size
    return await model.Books.filter(**kwargs).offset(offset).limit(limit).all()