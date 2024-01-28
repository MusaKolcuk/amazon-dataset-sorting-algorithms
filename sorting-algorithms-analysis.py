#!/usr/bin/env python
# coding: utf-8

# # SELECTİON SORT

# RANKING FOR PRODUCT ID

# In[44]:


import pandas as pd

def selection_sort(data, key):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            # Veri tipine göre kontrol yap
            if isinstance(data[j][key], str) and isinstance(data[min_index][key], str):
                # Metin değerlerini alfabetik sıraya göre sırala
                if data[j][key].lower() < data[min_index][key].lower():
                    min_index = j
            elif isinstance(data[j][key], (int, float)) and isinstance(data[min_index][key], (int, float)):
                # Sayısal değerleri nümerik sıraya göre sırala
                if data[j][key] < data[min_index][key]:
                    min_index = j
        data[i], data[min_index] = data[min_index], data[i]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Selection Sort ile sıralama yap ('product_id' özelliğine göre)
selection_sort(data_list, 'product_id')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully.")


# RANKING FOR PRODUCT NAME

# In[45]:


import pandas as pd

def selection_sort(data, key):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            # Veri tipine göre kontrol yap
            if isinstance(data[j][key], str) and isinstance(data[min_index][key], str):
                # Metin değerlerini alfabetik sıraya göre sırala
                if data[j][key].lower() < data[min_index][key].lower():
                    min_index = j
        data[i], data[min_index] = data[min_index], data[i]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Selection Sort ile sıralama yap ('product_name' özelliğine göre)
selection_sort(data_list, 'product_name')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully.")


# RANKING FOR PRICE

# In[43]:


import pandas as pd

def selection_sort(data, key):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if data[j][key] < data[min_index][key]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Selection Sort ile sıralama yap ('price' özelliğine göre)
selection_sort(data_list, 'price')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully.")


# RANKING FOR SALES QUANTİTY

# In[46]:


import pandas as pd

def selection_sort(data, key):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            # Veri tipine göre kontrol yap
            if isinstance(data[j][key], (int, float)) and isinstance(data[min_index][key], (int, float)):
                # Sayısal değerleri nümerik sıraya göre sırala
                if data[j][key] < data[min_index][key]:
                    min_index = j
        data[i], data[min_index] = data[min_index], data[i]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Selection Sort ile sıralama yap ('sales_quantity' özelliğine göre)
selection_sort(data_list, 'sales_quantity')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully.")


# RANKING FOR STOCK QUANTİTY

# In[47]:


import pandas as pd

def selection_sort(data, key):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            # Veri tipine göre kontrol yap
            if isinstance(data[j][key], (int, float)) and isinstance(data[min_index][key], (int, float)):
                # Sayısal değerleri nümerik sıraya göre sırala
                if data[j][key] < data[min_index][key]:
                    min_index = j
        data[i], data[min_index] = data[min_index], data[i]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Selection Sort ile sıralama yap ('stock_quantity' özelliğine göre)
selection_sort(data_list, 'stock_quantity')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully.")


# RANKING FOR BRAND

# In[48]:


import pandas as pd

def selection_sort(data, key):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            # Veri tipine göre kontrol yap
            if isinstance(data[j][key], str) and isinstance(data[min_index][key], str):
                # Metin değerlerini alfabetik sıraya göre sırala
                if data[j][key].lower() < data[min_index][key].lower():
                    min_index = j
        data[i], data[min_index] = data[min_index], data[i]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Selection Sort ile sıralama yap ('brand' özelliğine göre)
selection_sort(data_list, 'brand')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully.")


# RANKING FOR CATEGORY

# In[49]:


import pandas as pd

def selection_sort(data, key):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            # Veri tipine göre kontrol yap
            if isinstance(data[j][key], str) and isinstance(data[min_index][key], str):
                # Metin değerlerini alfabetik sıraya göre sırala
                if data[j][key].lower() < data[min_index][key].lower():
                    min_index = j
        data[i], data[min_index] = data[min_index], data[i]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Selection Sort ile sıralama yap ('category' özelliğine göre)
selection_sort(data_list, 'category')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully.")


# SORTING SEPARATELY BY ALL PARAMETERS IN A SINGLE CODE

# In[50]:


import pandas as pd

def selection_sort(data, key):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            # Veri tipine göre kontrol yap
            if isinstance(data[j][key], str) and isinstance(data[min_index][key], str):
                # Metin değerlerini alfabetik sıraya göre sırala
                if data[j][key].lower() < data[min_index][key].lower():
                    min_index = j
            elif isinstance(data[j][key], (int, float)) and isinstance(data[min_index][key], (int, float)):
                # Sayısal değerleri nümerik sıraya göre sırala
                if data[j][key] < data[min_index][key]:
                    min_index = j
        data[i], data[min_index] = data[min_index], data[i]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Tüm parametreler üzerinden sıralama yap
sorting_keys = ['product_id', 'product_name', 'price', 'sales_quantity', 'stock_quantity', 'brand', 'category']

for key in sorting_keys:
    print(f"\nSorting: {key}\n{'=' * 30}")
    selection_sort(data_list, key)
    for row in data_list:
        print(row)

print("\nAll rankings completed.")


# # MERGE SORT

# RANKING FOR PRODUCT ID

# In[51]:


import pandas as pd

def merge_sort(data, key):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if isinstance(left_half[i][key], str) and isinstance(right_half[j][key], str):
                if left_half[i][key].lower() < right_half[j][key].lower():
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            elif isinstance(left_half[i][key], (int, float)) and isinstance(right_half[j][key], (int, float)):
                if left_half[i][key] < right_half[j][key]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Merge Sort ile sıralama yap ('product_id' özelliğine göre)
merge_sort(data_list, 'product_id')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Merge Sort.")


# RANKING FOR PRODUCT NAME

# In[52]:


import pandas as pd

def merge_sort(data, key):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if isinstance(left_half[i][key], str) and isinstance(right_half[j][key], str):
                if left_half[i][key].lower() < right_half[j][key].lower():
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            elif isinstance(left_half[i][key], (int, float)) and isinstance(right_half[j][key], (int, float)):
                if left_half[i][key] < right_half[j][key]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Merge Sort ile sıralama yap ('product_name' özelliğine göre)
merge_sort(data_list, 'product_name')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Merge Sort.")


# In[ ]:


RANKING FOR PRİCE


# In[53]:


import pandas as pd

def merge_sort(data, key):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if isinstance(left_half[i][key], str) and isinstance(right_half[j][key], str):
                if left_half[i][key].lower() < right_half[j][key].lower():
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            elif isinstance(left_half[i][key], (int, float)) and isinstance(right_half[j][key], (int, float)):
                if left_half[i][key] < right_half[j][key]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Merge Sort ile sıralama yap ('price' özelliğine göre)
merge_sort(data_list, 'price')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Merge Sort.")


# In[ ]:


RANKING FOR SALES QUANTITY


# In[54]:


import pandas as pd

def merge_sort(data, key):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if isinstance(left_half[i][key], str) and isinstance(right_half[j][key], str):
                if left_half[i][key].lower() < right_half[j][key].lower():
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            elif isinstance(left_half[i][key], (int, float)) and isinstance(right_half[j][key], (int, float)):
                if left_half[i][key] < right_half[j][key]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Merge Sort ile sıralama yap ('sales_quantity' özelliğine göre)
merge_sort(data_list, 'sales_quantity')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Merge Sort.")


# In[ ]:


RANKING FOR STOCK  QUANTITY


# In[55]:


import pandas as pd

def merge_sort(data, key):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if isinstance(left_half[i][key], str) and isinstance(right_half[j][key], str):
                if left_half[i][key].lower() < right_half[j][key].lower():
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            elif isinstance(left_half[i][key], (int, float)) and isinstance(right_half[j][key], (int, float)):
                if left_half[i][key] < right_half[j][key]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Merge Sort ile sıralama yap ('stock_quantity' özelliğine göre)
merge_sort(data_list, 'stock_quantity')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Merge Sort.")


# In[ ]:


RANKING FOR BRAND


# In[56]:


import pandas as pd

def merge_sort(data, key):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if isinstance(left_half[i][key], str) and isinstance(right_half[j][key], str):
                if left_half[i][key].lower() < right_half[j][key].lower():
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            elif isinstance(left_half[i][key], (int, float)) and isinstance(right_half[j][key], (int, float)):
                if left_half[i][key] < right_half[j][key]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Merge Sort ile sıralama yap ('brand' özelliğine göre)
merge_sort(data_list, 'brand')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Merge Sort.")


# In[ ]:


RANKING FOR CATEGORY


# In[57]:


import pandas as pd

def merge_sort(data, key):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if isinstance(left_half[i][key], str) and isinstance(right_half[j][key], str):
                if left_half[i][key].lower() < right_half[j][key].lower():
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            elif isinstance(left_half[i][key], (int, float)) and isinstance(right_half[j][key], (int, float)):
                if left_half[i][key] < right_half[j][key]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

merge_sort(data_list, 'category')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Merge Sort.")


# # INSERTION SORT

# RANKING FOR PRODUCT ID

# In[59]:


import pandas as pd

def insertion_sort(data, key):
    n = len(data)
    for i in range(1, n):
        current = data[i]
        j = i - 1

        while j >= 0 and current[key] < data[j][key]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = current

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Insertion Sort ile sıralama yap ('product_id' özelliğine göre)
insertion_sort(data_list, 'product_id')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Insertion Sort.")


# RANKING FOR PRODUCT NAME

# In[60]:


import pandas as pd

def insertion_sort(data, key):
    n = len(data)
    for i in range(1, n):
        current = data[i]
        j = i - 1

        while j >= 0 and current[key] < data[j][key]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = current

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Insertion Sort ile sıralama yap ('product_name' özelliğine göre)
insertion_sort(data_list, 'product_name')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Insertion Sort.")


# RANKING FOR SALES QUANTITY

# In[61]:


import pandas as pd

def insertion_sort(data, key):
    n = len(data)
    for i in range(1, n):
        current = data[i]
        j = i - 1

        while j >= 0 and current[key] < data[j][key]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = current

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Insertion Sort ile sıralama yap ('sales_quantity' özelliğine göre)
insertion_sort(data_list, 'sales_quantity')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Insertion Sort.")


# RANKING FOR STOCK QUANTITY

# In[62]:


import pandas as pd

def insertion_sort(data, key):
    n = len(data)
    for i in range(1, n):
        current = data[i]
        j = i - 1

        while j >= 0 and current[key] < data[j][key]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = current

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Insertion Sort ile sıralama yap ('stock_quantity' özelliğine göre)
insertion_sort(data_list, 'stock_quantity')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Insertion Sort.")


# In[ ]:


RANKING FOR BRAND


# In[63]:


import pandas as pd

def insertion_sort(data, key):
    n = len(data)
    for i in range(1, n):
        current = data[i]
        j = i - 1

        while j >= 0 and current[key] < data[j][key]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = current

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Insertion Sort ile sıralama yap ('brand' özelliğine göre)
insertion_sort(data_list, 'brand')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Insertion Sort.")


# RANKING FOR CATEGORY

# In[58]:


import pandas as pd

def insertion_sort(data, key):
    n = len(data)
    for i in range(1, n):
        current = data[i]
        j = i - 1

        while j >= 0 and current[key] < data[j][key]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = current

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Insertion Sort ile sıralama yap ('category' özelliğine göre)
insertion_sort(data_list, 'category')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Insertion Sort.")


# SORTING SEPARATELY BY ALL PARAMETERS IN A SINGLE CODE

# In[66]:


import pandas as pd

def insertion_sort(data, key):
    n = len(data)
    for i in range(1, n):
        current = data[i]
        j = i - 1

        while j >= 0 and current[key] < data[j][key]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = current

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Parametreler listesi
parameters = ['product_id', 'product_name', 'price', 'sales_quantity', 'stock_quantity', 'brand', 'category']

# Her bir parametre için sıralama yap
for param in parameters:
    insertion_sort(data_list, param)
    
    # Sıralanmış veriyi ekrana yazdır
    print(f"\nDataset sorted by {param}:\n")
    for row in data_list:
        print(row)

print("\nDataset successfully sorted using Insertion Sort.")


# # QUICK SORT

# RANKING FOR PRODUCT ID

# In[67]:


import pandas as pd

def quick_sort(data, key):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = [item for item in data[1:] if item[key] <= pivot[key]]
        greater = [item for item in data[1:] if item[key] > pivot[key]]
        return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Quick Sort ile sıralama yap ('product_id' özelliğine göre)
sorted_data = quick_sort(data_list, 'product_id')

# Sıralanmış veriyi ekrana yazdır
for row in sorted_data:
    print(row)

print("Dataset sorted successfully using Quick Sort.")


# In[ ]:


RANKING FOR PRODUCT NAME


# In[68]:


import pandas as pd

def quick_sort(data, key):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = [item for item in data[1:] if item[key] <= pivot[key]]
        greater = [item for item in data[1:] if item[key] > pivot[key]]
        return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Quick Sort ile sıralama yap ('product_name' özelliğine göre)
sorted_data = quick_sort(data_list, 'product_name')

# Sıralanmış veriyi ekrana yazdır
for row in sorted_data:
    print(row)

print("Dataset sorted successfully using Quick Sort.")


# In[ ]:


RANKING FOR PRİCE


# In[69]:


import pandas as pd

def quick_sort(data, key):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = [item for item in data[1:] if item[key] <= pivot[key]]
        greater = [item for item in data[1:] if item[key] > pivot[key]]
        return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Quick Sort ile sıralama yap ('price' özelliğine göre)
sorted_data = quick_sort(data_list, 'price')

# Sıralanmış veriyi ekrana yazdır
for row in sorted_data:
    print(row)

print("Dataset sorted successfully using Quick Sort.")


# In[ ]:


RANKING FOR SALES QUANTITY


# In[70]:


import pandas as pd

def quick_sort(data, key):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = [item for item in data[1:] if item[key] <= pivot[key]]
        greater = [item for item in data[1:] if item[key] > pivot[key]]
        return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Quick Sort ile sıralama yap ('sales_quantity' özelliğine göre)
sorted_data = quick_sort(data_list, 'sales_quantity')

# Sıralanmış veriyi ekrana yazdır
for row in sorted_data:
    print(row)

print("Dataset sorted successfully using Quick Sort.")


# In[ ]:


RANKING FOR STOCK QUANTITY


# In[71]:


import pandas as pd

def quick_sort(data, key):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = [item for item in data[1:] if item[key] <= pivot[key]]
        greater = [item for item in data[1:] if item[key] > pivot[key]]
        return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Quick Sort ile sıralama yap ('stock_quantity' özelliğine göre)
sorted_data = quick_sort(data_list, 'stock_quantity')

# Sıralanmış veriyi ekrana yazdır
for row in sorted_data:
    print(row)

print("Dataset sorted successfully using Quick Sort.")


# In[ ]:


RANKING FOR BRAND


# In[72]:


import pandas as pd

def quick_sort(data, key):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = [item for item in data[1:] if item[key] <= pivot[key]]
        greater = [item for item in data[1:] if item[key] > pivot[key]]
        return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Quick Sort ile sıralama yap ('brand' özelliğine göre)
sorted_data = quick_sort(data_list, 'brand')

# Sıralanmış veriyi ekrana yazdır
for row in sorted_data:
    print(row)

print("Dataset sorted successfully using Quick Sort.")


# In[ ]:


RANKING FOR CATEGORY


# In[73]:


import pandas as pd

def quick_sort(data, key):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = [item for item in data[1:] if item[key] <= pivot[key]]
        greater = [item for item in data[1:] if item[key] > pivot[key]]
        return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Quick Sort ile sıralama yap ('category' özelliğine göre)
sorted_data = quick_sort(data_list, 'category')

# Sıralanmış veriyi ekrana yazdır
for row in sorted_data:
    print(row)

print("Dataset sorted successfully using Quick Sort.")


# # BUBBLE SORT

# RANKING FOR PRODUCT ID

# In[74]:


import pandas as pd

def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Bubble Sort ile sıralama yap ('product_id' özelliğine göre)
bubble_sort(data_list, 'product_id')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Bubble Sort.")


# RANKING FOR PRODUCT NAME

# In[75]:


import pandas as pd

def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Bubble Sort ile sıralama yap ('product_name' özelliğine göre)
bubble_sort(data_list, 'product_name')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Bubble Sort.")


# RANKING FOR PRİCE

# In[76]:


import pandas as pd

def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Bubble Sort ile sıralama yap ('price' özelliğine göre)
bubble_sort(data_list, 'price')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Bubble Sort.")


# RANKING FOR SALES QUANTITY

# In[ ]:


import pandas as pd

def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Bubble Sort ile sıralama yap ('sales_quantity' özelliğine göre)
bubble_sort(data_list, 'sales_quantity')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Bubble Sort.")


# In[ ]:


RANKING FOR STOCK QUANTITY


# In[77]:


import pandas as pd

def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Bubble Sort ile sıralama yap ('stock_quantity' özelliğine göre)
bubble_sort(data_list, 'stock_quantity')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Bubble Sort.")


# RANKING FOR BRAND

# In[79]:


import pandas as pd

def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Bubble Sort ile sıralama yap ('brand' özelliğine göre)
bubble_sort(data_list, 'brand')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Bubble Sort.")


# RANKING FOR CATEGORY

# In[81]:


import pandas as pd

def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Bubble Sort ile sıralama yap ('category' özelliğine göre)
bubble_sort(data_list, 'category')

# Sıralanmış veriyi ekrana yazdır
for row in data_list:
    print(row)

print("Dataset sorted successfully using Bubble Sort.")


# SORTING SEPARATELY BY ALL PARAMETERS IN A SINGLE CODE

# In[82]:


import pandas as pd

def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]

def sort_by_key(data_list, key):
    # Veriyi Python listesi formatına çevir
    data_list = df.to_dict('records')

    # Bubble Sort ile sıralama yap
    bubble_sort(data_list, key)

    # Sıralanmış veriyi ekrana yazdır
    print(f"Dataset sorted by {key}:")
    for row in data_list:
        print(row)

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Tüm parametreler üzerinden sıralama yap
sorting_keys = ['product_id', 'product_name', 'price', 'sales_quantity', 'stock_quantity', 'brand', 'category']

for key in sorting_keys:
    sort_by_key(df.to_dict('records'), key)
    print("\n" + "-"*50 + "\n")


# # RESULTS ACCORDING TO BIG O NOTATION

# INSERTION SORT BİG O NOTATİON

# In[2]:


import pandas as pd
import time

def insertion_sort(data, key):
    n = len(data)
    start_time = time.time()

    for i in range(1, n):
        current = data[i]
        j = i - 1

        while j >= 0 and current[key] < data[j][key]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = current

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Parametreler listesi
parameters = ['product_id', 'product_name', 'price', 'sales_quantity', 'stock_quantity', 'brand', 'category']

# Her bir parametre için sıralama yap ve Big O notasyonu hesapla
for param in parameters:
    data_copy = data_list.copy()  # Veriyi kopyala, orijinal veriyi değiştirmemek için
    execution_time = insertion_sort(data_copy, param)
    print(f"Insertion Sort için Big O Notasyonu ({param}): O({len(data_copy)}^2), Çalışma Süresi: {execution_time} saniye")


# In[ ]:


SELECTION SORT BİG O NOTATİON


# In[3]:


import pandas as pd
import time

def selection_sort(data, key):
    n = len(data)
    start_time = time.time()

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            # Veri tipine göre kontrol yap
            if isinstance(data[j][key], str) and isinstance(data[min_index][key], str):
                # Metin değerlerini alfabetik sıraya göre sırala
                if data[j][key].lower() < data[min_index][key].lower():
                    min_index = j
            elif isinstance(data[j][key], (int, float)) and isinstance(data[min_index][key], (int, float)):
                # Sayısal değerleri nümerik sıraya göre sırala
                if data[j][key] < data[min_index][key]:
                    min_index = j

        data[i], data[min_index] = data[min_index], data[i]

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Parametreler listesi
parameters = ['product_id', 'product_name', 'price', 'sales_quantity', 'stock_quantity', 'brand', 'category']

# Her bir parametre için sıralama yap ve Big O notasyonu hesapla
for param in parameters:
    data_copy = data_list.copy()  # Veriyi kopyala, orijinal veriyi değiştirmemek için
    execution_time = selection_sort(data_copy, param)
    print(f"Selection Sort için Big O Notasyonu ({param}): O({len(data_copy)}^2), Çalışma Süresi: {execution_time} saniye")


# In[ ]:


QUICK SORT BİG O NOTATİON


# In[4]:


import pandas as pd
import time

def quick_sort(data, key):
    start_time = time.time()

    def _quick_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [item for item in arr[1:] if item[key] <= pivot[key]]
            greater = [item for item in arr[1:] if item[key] > pivot[key]]
            return _quick_sort(less) + [pivot] + _quick_sort(greater)

    data_sorted = _quick_sort(data)

    end_time = time.time()
    execution_time = end_time - start_time

    return data_sorted, execution_time

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Parametreler listesi
parameters = ['product_id', 'product_name', 'price', 'sales_quantity', 'stock_quantity', 'brand', 'category']

# Her bir parametre için sıralama yap ve Big O notasyonu hesapla
for param in parameters:
    data_copy = data_list.copy()  # Veriyi kopyala, orijinal veriyi değiştirmemek için
    sorted_data, execution_time = quick_sort(data_copy, param)
    print(f"Quick Sort için Big O Notasyonu ({param}): O(n log n), Çalışma Süresi: {execution_time} saniye")


# In[ ]:


MERGE SORT BİG O NOTATİON


# In[5]:


import pandas as pd
import time

def merge_sort(data, key):
    start_time = time.time()

    def _merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            _merge_sort(left_half)
            _merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i][key] < right_half[j][key]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    data_copy = data.copy()  # Veriyi kopyala, orijinal veriyi değiştirmemek için
    _merge_sort(data_copy)

    end_time = time.time()
    execution_time = end_time - start_time

    return data_copy, execution_time

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Parametreler listesi
parameters = ['product_id', 'product_name', 'price', 'sales_quantity', 'stock_quantity', 'brand', 'category']

# Her bir parametre için sıralama yap ve Big O notasyonu hesapla
for param in parameters:
    data_copy = data_list.copy()  # Veriyi kopyala, orijinal veriyi değiştirmemek için
    sorted_data, execution_time = merge_sort(data_copy, param)
    print(f"Merge Sort için Big O Notasyonu ({param}): O(n log n), Çalışma Süresi: {execution_time} saniye")


# In[ ]:


BUBBLE SORT BİG O NOTATİON


# In[9]:


import pandas as pd
import time

def bubble_sort(data, key):
    start_time = time.time()

    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]

    end_time = time.time()
    execution_time = end_time - start_time

    return data, execution_time

file_path = r'C:\Users\musa_\Downloads\amazon\amazon-sales-datasets.csv'

# CSV dosyasını oku
df = pd.read_csv(file_path)

# Veriyi Python listesi formatına çevir
data_list = df.to_dict('records')

# Parametreler listesi
parameters = ['product_id', 'product_name', 'price', 'sales_quantity', 'stock_quantity', 'brand', 'category']

# Her bir parametre için sıralama yap ve Big O notasyonu hesapla
for param in parameters:
    data_copy = data_list.copy()  # Veriyi kopyala, orijinal veriyi değiştirmemek için
    sorted_data, execution_time = bubble_sort(data_copy, param)
    print(f"Bubble Sort için Big O Notasyonu ({param}): O(n^2), Çalışma Süresi: {execution_time} saniye")
    # İsterseniz sorted_data'ya erişerek sıralanmış veriyi kontrol edebilirsiniz


# In[ ]:




