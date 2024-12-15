from tortoise import Model, fields


class Books(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    author = fields.CharField(max_length=255)
    category = fields.CharField(max_length=255)
    published_date = fields.DateField(null=True)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)

    class Meta:
        table = 'books'