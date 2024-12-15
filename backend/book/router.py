from tortoise import Tortoise

import book.dao as dao
import book.schema as schema
from fastapi import APIRouter, Depends

books = APIRouter(prefix="/Books", tags=["Books"])


@books.get("/{id}", summary="通过ID查询详情")
async def query_books_by_id(id: int) -> schema.Result[schema.Books]:
    return schema.Result.ok(await dao.query_by_id(id))


@books.get("", summary="分页条件查询")
async def query_books_all_by_limit(query: schema.Books = Depends(),
                                   page: schema.PageParam = Depends()
                                   ) -> schema.PageResult[schema.Books]:
    total = await dao.count(**query.model_dump(exclude_none=True))
    data = await dao.query_all_by_limit(**query.model_dump(exclude_none=True),
                                        page_number=page.page_number,
                                        page_size=page.page_size)
    return schema.PageResult.ok(data=data, total=total)


@books.post("", summary="新增数据")
async def create_books(instance: schema.Books) -> schema.Result[schema.Books]:
    return schema.Result.ok(await dao.create(instance))


@books.patch("/{id}", summary="更新数据")
async def update_books_by_id(
        id: int, instance: schema.Books) -> schema.Result[schema.Books]:
    return schema.Result.ok(await dao.update(id, instance))


@books.delete("/{id}", summary="删除数据")
async def delete_books_by_id(id: int) -> schema.Result[schema.Books]:
    return schema.Result.ok(await dao.delete_by_id(id))


@books.get("/chart/bar", summary="书籍作者统计")
async def get_bar_chart_data():
    con = Tortoise.get_connection("default")
    result = await con.execute_query_dict(
        """
        SELECT author, COUNT(*) AS book_count
        FROM books
        GROUP BY author;
        """
    )

    # 提取作者列表和对应的书籍数量
    authors = [item['author'] for item in result]
    book_counts = [item['book_count'] for item in result]

    # 构建ECharts的options，使用真实的书籍数量
    options = {
        "title": {
            "text": "书籍作者统计"
        },
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {
                "type": "shadow"
            }
        },
        "grid": {
            "left": "3%",
            "right": "4%",
            "bottom": "3%",
            "containLabel": True
        },
        "xAxis": {
            "type": "value",
            "boundaryGap": [0, 0.01]
        },
        "yAxis": {
            "type": "category",
            "data": authors
        },
        "series": [
            {
                "name": "书籍数量",
                "type": "bar",
                "data": book_counts
            }
        ]
    }

    return schema.Result.ok({"options": options})

@books.get("/chart/pie", summary="书籍分类占比")
async def get_pie_chart_data():
    con = Tortoise.get_connection("default")
    result = await con.execute_query_dict(
        """
        SELECT category, COUNT(*) AS book_count
        FROM books
        GROUP BY category;
        """
    )
    # 转成饼图能用的数据
    result = [{"value": item['book_count'], "name": item['category']} for item in result]
    options = {
        "title": {
            "text": "书籍分类占比"
        },
        "tooltip": {
            "trigger": "item"
        },
        "series": [
            {
                "name": "书籍分类占比",
                "type": "pie",
                "radius": "50%",
                "data": result,
                "label": {
                    "formatter": "{b}: {d}%"
                },

            }
        ]
    }
    return schema.Result.ok({"options": options})

