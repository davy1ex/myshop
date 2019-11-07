import json
from django.db import models

# from product.models import Product


class ShopingCart(models.Model):
    json_product_ids = models.CharField(max_length=500, default='{"buyed_product_ids": []}') # список предполагаемых ИДшников покупок

    def get_list_product_ids(self):
        ''' извлекает жсон список ИДшников продуктов '''
        return json.loads(self.json_product_ids)['buyed_product_ids']

    def add_product_id(self, product_id):
        ''' добавляет новыйй ИДишник и упаковывает в жсон, сохраняет в БД. Всё лежит в первой записи '''
        list_product_ids = self.get_list_product_ids()
        list_product_ids.append(product_id)
        self.json_product_ids = json.dumps({"buyed_product_ids": list_product_ids})
        super().save()




