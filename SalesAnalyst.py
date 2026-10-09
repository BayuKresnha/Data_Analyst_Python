sales = [
    {"product": "Laptop", "category": "Electronics", "price": 10000000, "quantity": 2},
    {"product": "Mouse", "category": "Accessories", "price": 150000, "quantity": 5},
    {"product": "Keyboard", "category": "Accessories", "price": 500000, "quantity": 3},
    {"product": "Monitor", "category": "Electronics", "price": 3000000, "quantity": 2},
    {"product": "Headset", "category": "Accessories", "price": 350000, "quantity": 4},
    {"product": "Laptop", "category": "Electronics", "price": 10000000, "quantity": 1},
    {"product": "Mouse", "category": "Accessories", "price": 150000, "quantity": 8},
    {"product": "Keyboard", "category": "Accessories", "price": 500000, "quantity": 2},
    {"product": "Monitor", "category": "Electronics", "price": 3000000, "quantity": 1},
    {"product": "Headset", "category": "Accessories", "price": 350000, "quantity": 6},
    {"product": "Laptop", "category": "Electronics", "price": 10000000, "quantity": 1},
    {"product": "Mouse", "category": "Accessories", "price": 150000, "quantity": 10},
    {"product": "Keyboard", "category": "Accessories", "price": 500000, "quantity": 4},
    {"product": "Monitor", "category": "Electronics", "price": 3000000, "quantity": 3},
    {"product": "Headset", "category": "Accessories", "price": 350000, "quantity": 5},
    {"product": "Laptop", "category": "Electronics", "price": 10000000, "quantity": 2},
    {"product": "Mouse", "category": "Accessories", "price": 150000, "quantity": 7},
    {"product": "Keyboard", "category": "Accessories", "price": 500000, "quantity": 1},
    {"product": "Monitor", "category": "Electronics", "price": 3000000, "quantity": 2},
    {"product": "Headset", "category": "Accessories", "price": 350000, "quantity": 3}
]

def error_handling(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
    return wrapper

@error_handling
def calculate_total_quantity():
    total_quantity = 0
    for sale in sales:
        total_quantity += sale["quantity"]
    return total_quantity

@error_handling
def calculate_total_revenue():
    total_revenue = 0
    for sale in sales:
        total_revenue += sale["price"] * sale["quantity"]
    return total_revenue

@error_handling
def search_best_selling_product():
    product_sales = {}
    for sale in sales:
        product = sale["product"]
        quantity = sale["quantity"]
        if product in product_sales:
            product_sales[product] += quantity
        else:
            product_sales[product] = quantity
    best_selling_product = max(product_sales, key=product_sales.get)
    return best_selling_product, product_sales[best_selling_product]

@error_handling
def biggest_revenue_product():
    product_revenue = {}
    for sale in sales:
        product = sale["product"]
        revenue = sale["price"] * sale["quantity"]
        if product in product_revenue:
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue
    biggest_revenue_product = max(product_revenue, key=product_revenue.get)
    return biggest_revenue_product, product_revenue[biggest_revenue_product]

@error_handling
def average_revenue_per_product():
    product_revenue = {}
    for sale in sales:
        product = sale["product"]
        revenue = sale["price"] * sale["quantity"]
        if product in product_revenue:
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue
    total_products = len(product_revenue)
    total_revenue = sum(product_revenue.values())
    average_revenue = total_revenue / total_products if total_products > 0 else 0
    return average_revenue

@error_handling
def search_product_by_name(product_name):
    hasil = []
    for sale in sales:
        if sale["product"].lower() == product_name.lower():
            hasil.append(sale)
    return hasil

@error_handling
def filter_sales_by_category(category_name):
    filtered_sales = [sale for sale in sales if sale["category"].lower() == category_name.lower()]
    return filtered_sales

def interactive_menu():
    while True:
        print("\nMenu:")
        print("1. Total Seluruh Jumlah Produk")
        print("2. Total Seluruh Pendapatan")
        print("3. Produk Terlaris")
        print("4. Produk dengan Pendapatan Terbesar")
        print("5. Rata-rata Pendapatan Per Produk")
        print("6. Detail Produk Berdasarkan Nama")
        print("7. Filter Produk Berdasarkan Kategori")
        print("8. Keluar")

        choice = input("Pilih menu (1-8): ")

        if choice == "1":
            print("Total Seluruh Jumlah Produk:", calculate_total_quantity())
        elif choice == "2":
            print("Total Seluruh Pendapatan:", calculate_total_revenue())
        elif choice == "3":
            best_selling_product, quantity = search_best_selling_product()
            print(f"Produk Terlaris: {best_selling_product} dengan jumlah terjual {quantity}")
        elif choice == "4":
            biggest_revenue_product_name, revenue = biggest_revenue_product()
            print(f"Produk dengan Pendapatan Terbesar: {biggest_revenue_product_name} dengan pendapatan {revenue}")
        elif choice == "5":
            average_revenue = average_revenue_per_product()
            print(f"Rata-rata Pendapatan Per Produk: {average_revenue}")
        elif choice == "6":
            product_name = input("Masukkan nama produk: ")
            product_details = search_product_by_name(product_name)
            if product_details:
                total_quantity = 0 
                total_revenue = 0
                for detail in product_details:
                    total_quantity += detail["quantity"]
                    total_revenue += detail["price"] * detail["quantity"]
                print("=== Detail Produk ===")
                print(f"Total Jumlah Terjual: {total_quantity}")
                print(f"Total Pendapatan: {total_revenue}")
            else:
                print(f"Produk '{product_name}' tidak ditemukan.")
        elif choice == "7":
            category_name = input("Masukkan nama kategori: ")
            filtered_sales = filter_sales_by_category(category_name)
            if filtered_sales:
                print(f"Produk dalam Kategori '{category_name}': {filtered_sales}")
            else:
                print(f"Tidak ada produk dalam kategori '{category_name}'.")
        elif choice == "8":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# Menggunakan fungsi interactive_menu untuk menjalankan program
interactive_menu()

# Comment yang dihasilkan dari kode di atas
# print("Total Seluruh Jumlah Produk:", calculate_total_quantity())
# print("Total Seluruh Pendapatan:", calculate_total_revenue())
# print("Produk Terlaris:", search_best_selling_product())
# print("Produk dengan Pendapatan Terbesar:", biggest_revenue_product())
# print("Rata-rata Pendapatan Per Produk:", average_revenue_per_product())
# print("Detail Produk 'Laptop':", search_product_by_name("Laptop"))
# print("Produk dalam Kategori 'Accessories':", filter_sales_by_category("Accessories"))