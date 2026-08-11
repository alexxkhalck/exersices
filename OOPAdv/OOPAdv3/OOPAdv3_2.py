#Створіть XML-файл із вкладеними елементами та скористайтеся мовою пошуку XPATH. Спробуйте здійснити пошук вмісту за
# створеним документом XML, ускладнюючи свої запити та додаючи нові елементи, якщо буде потрібно.
from pathlib import Path
from lxml import etree

file_path = Path(__file__).parent / "shop.xml"

tree = etree.parse(file_path)
root = tree.getroot()

# 1. Знайти назви всіх товарів
products = root.xpath("//product/name/text()")

print("Усі товари:")
for name in products:
    print(name)

# 2. Знайти лише доступні товари
available_products = root.xpath("//product[@available='true']/name/text()")

print("\nДоступні товари:")
for name in available_products:
    print(name)

# 3. Знайти товари дорожчі за 25 000
expensive_products = root.xpath("//product[price > 25000]/name/text()")

print("\nТовари дорожчі за 25 000:")
for name in expensive_products:
    print(name)

# 4. Отримати ціну iPhone
iphone_price = root.xpath("//product[name='iPhone']/price/text()")

print("\nЦіна iPhone:")
print(iphone_price[0])

# 5. Знайти всі товари бренду Apple
apple_products = root.xpath("//product[brand='Apple']/name/text()")

print("\nТовари Apple:")
for name in apple_products:
    print(name)

# 6. Знайти категорію кожного товару
categories = root.xpath("//category")

print("\nКатегорії та їх товари:")
for category in categories:
    category_name = category.get("name")
    product_names = category.xpath("./products/product/name/text()")

    print(f"{category_name}: {', '.join(product_names)}")