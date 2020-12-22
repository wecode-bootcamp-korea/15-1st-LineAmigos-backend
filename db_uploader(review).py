import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lineamigos.settings")
django.setup()
from user.models import *
from product.models import *
from review.models import *

CSV_PATH_PRODUCTS='./review_review.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
        box = []
        data_reader = csv.reader(in_file)
        next(data_reader, None) # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
        for row in data_reader:
                if row[0]: #  product_id
                    print(row[0])
                    product_id_csv = row[0]
                if row[1]: # user_id
                    print(row[1])
                    user_id_csv = row[1]
                if row[2]: #내용
                    print(row[2])
                    contents_csv = row[2]
                if row[3]: # 평점
                    print(row[3])
                    rate_csv = row[3]
                if row[4]: # image_url
                    print(row[4])
                    image_url_csv = row[4]
                if row[5]:
                    print(row[5])
                    is_monthly_csv = row[5]
                Review.objects.create(rate=rate_csv, contents=contents_csv, is_monthly_reviewed=is_monthly_csv, product_id = product_id_csv, user_id=user_id_csv)

               # Image.objects.create(image_url=product_image_csv, product_id=category_id_csv)
                #category_pk = Category_CSV.objects.get(category_name=category_name_csv)
               # Drink_CSV.objects.create(drink_name=drink_name_csv, category=category_pk)
