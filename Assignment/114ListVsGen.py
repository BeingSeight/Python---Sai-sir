# 114. List vs Generator Comprehension
large_data = range(10**6)
list_comp = [x * 2 for x in large_data]  # Consumes memory
gen_exp = (x * 2 for x in large_data)   # Memory efficient

print("List comprehension example:", list_comp[:5])
print("Generator expression example:", next(gen_exp), next(gen_exp))