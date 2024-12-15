# 版本要求
Python 3.11

# 修改数据库账号密码
1. 打开`mian.py`文件
```python
register_tortoise(
    app,
    # 修改为你自己的账号 密码；这里的root 是账号 123456是密码 demo是数据库
    db_url="mysql://root:123456@127.0.0.1:3306/demo",
    modules={"models": ["user.model", "book.model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
```

# 安装依赖
```python
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

# 启动后端
```shell
python main.py
```
