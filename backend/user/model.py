from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(null=True, max_length=255, description="账号")
    password = fields.CharField(null=True, max_length=255, description="密码")
    nickname = fields.CharField(null=True, max_length=255, description="昵称")
    avatar = fields.CharField(null=True, max_length=255, description="头像url")

    class Meta:
        table = 'user'