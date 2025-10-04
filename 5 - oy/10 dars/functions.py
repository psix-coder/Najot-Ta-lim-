from database import connect
from collections import namedtuple

Models = namedtuple('Models', ['model_name', 'brand_name', 'color_name'])
Brands = namedtuple('Brands', ['brand_name', 'count'])
Brands2 = namedtuple('Brands', ['brand_name', 'count'])
Emails = namedtuple('Emails', 'email')
Country = namedtuple('Country', ['country', 'count'])
Employees = namedtuple('Employees', ['country', 'count'])
OrderDetails = namedtuple('OrderDetails', ['order_id', 'customer_first_name', 'customer_last_name','employee_first_name', 'employee_last_name','model_name', 'model_price', 'car_count', 'order_date'])
Colors = namedtuple('Colors', ['color_id', 'color_name'])
SelectBrands = namedtuple('SelectBrands', ['brand_id', 'brand_name'])

models = connect.select_models()
emails = connect.select_email()
country = connect.select_country()
employees = connect.select_employees()
brands = connect.select_brands()
brands2 = connect.select_brands_2()
show_tables = connect.show_tables()
sum_models_price = connect.sum_models_price()
brand_counts = connect.brand_counts()
color = connect.select_colors()
select_brands = connect.select_all_brands()

def showModels():
    print('-' * 60)
    print("|", "MODEL NAME".center(25, ' '), "|", "BRAND NAME".center(15, ' '), "|", "COLOR NAME".center(10, ' '), "|")
    print('-' * 60)
    for mode in models:
        model = Models(*mode)
        print("|", str(model.model_name).center(25, ' '), "|", str(model.brand_name).center(15, ' '), "|", str(model.color_name).center(10, ' '), "|")
        print('-' * 60)

def showEmails():
    print('-' * 25)
    print("|", "EMAIL".center(25, ' '), "|")
    print('-' * 25)
    for email in emails:
        em = Emails(*email)
        print("|", str(em.email).center(25, ' '), "|")
        print('-' * 25)

def showCountry():
    print('-' * 27)
    print('|', "COUNTRY".center(15, ' '), "|", "COUNT".center(5, ' '), "|")
    print('-' * 27)
    for c in country:
        count = Country(*c)
        print("|", str(count.country).center(15, ' '), "|", str(count.count).center(5, ' '), "|")
        print('-' * 27)

def showEmployees():
    print('-' * 27)
    print('|', "COUNTRY".center(15, ' '), "|", "COUNT".center(5, ' '), "|")
    print('-' * 27)
    for employe in employees:
        emp = Employees(*employe)
        print("|", str(emp.country).center(15, ' '), "|", str(emp.count).center(5, ' '), "|")
        print('-' * 27)

def showBrands():
    print('-' * 27)
    print('|', "BRAND NAME".center(15, ' '), "|", "COUNT".center(5, ' '), "|")
    print('-' * 27)
    for brand in brands:
        br = Brands(*brand)
        print("|", str(br.brand_name).center(15, ' '), "|", str(br.count).center(5, ' '), "|")
        print('-' * 27)

def showBrandsFilter():
    print('-' * 27)
    print('|', "BRAND NAME".center(15, ' '), "|", "COUNT".center(5, ' '), "|")
    print('-' * 27)
    for brand2 in brands2:
        br = Brands(*brand2)
        print("|", str(br.brand_name).center(15, ' '), "|", str(br.count).center(5, ' '), "|")
        print('-' * 27)

def showOrders():
    print('-' * 200)
    print("|", "ORDER ID".center(10, ' '), "|", "CUSTOMER FIRST NAME".center(25, ' '), "|",
          "CUSTOMER LAST NAME".center(25, ' '), "|", "EMPLOYEE FIRST NAME".center(25, ' '), "|",
          "EMPLOYEE LAST NAME".center(25, ' '), "|", "MODEL NAME".center(20, ' '), "|",
          "MODEL PRICE".center(15, ' '), "|", "CAR COUNT".center(10, ' '), "|", "ORDER DATE".center(15, ' '), "|")
    print('-' * 200)

    for order in show_tables:
        order_detail = OrderDetails(*order)
        print("|", str(order_detail.order_id).center(10, ' '), "|",
              str(order_detail.customer_first_name).center(25, ' '), "|",
              str(order_detail.customer_last_name).center(25, ' '), "|",
              str(order_detail.employee_first_name).center(25, ' '), "|",
              str(order_detail.employee_last_name).center(25, ' '), "|",
              str(order_detail.model_name).center(20, ' '), "|",
              str(order_detail.model_price).center(15, ' '), "|",
              str(order_detail.car_count).center(10, ' '), "|",
              str(order_detail.order_date).center(15, ' '), "|")
        print('-' * 200)

def sum_models():
    print('-' * 14)
    print("|", "SUM".center(10, ' '), "|")
    print('-' * 14)
    print("|", str(sum_models_price[0]).center(10, ' '), "|")
    print('-' * 14)

def brandCounts():
    print('-' * 14)
    print("|", "COUNT".center(10, ' '), "|")
    print('-' * 14)
    print("|", str(brand_counts[0]).center(10, ' '), "|")
    print('-' * 14)

def show_all_brands():
    print('-' * 27)
    print('|', "ID".center(5, ' '), "|", "BRAND NAME".center(15, ' '), "|")
    print('-' * 27)
    for brand in select_brands:
        br = SelectBrands(*brand)
        print("|", str(br.brand_id).center(5, ' '), "|", str(br.brand_name).center(15, ' '), "|")
        print('-' * 27)

def show_colors():
    print('-' * 27)
    print('|', "ID".center(5, ' '), "|", "COLOR NAME".center(15, ' '), "|")
    print('-' * 27)
    for co in color:
        br = Colors(*co)
        print("|", str(br.color_id).center(5, ' '), "|", str(br.color_name).center(15, ' '), "|")
        print('-' * 27)