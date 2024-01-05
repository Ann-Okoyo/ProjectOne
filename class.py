
name = input("What is your name")
age = input("What is your age ")
nationality = input("What is your nationality")

print("My name is " + name + ". I am " + str(age) + " years old. I am a " + nationality + ".")



price_product_1 = input ("THe price of product one is :")
quantity_product_1 = input ("The quantity of product one is :")
price_product_2 = input ("THe price of product two is :")
quantity_product_2 = input ("The quantity of product two is :")
price_product_3 = input ("THe price of product three is :")
quantity_product_3 = input ("The quantity of product three is :")

result = float(price_product_1)* float(quantity_product_1)
final_results= float(price_product_1)*float(quantity_product_1)+ float(quantity_product_2)*float(price_product_2)+ float(quantity_product_3)*float(price_product_3)
print(final_results)

print(result)

