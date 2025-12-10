#quản lý giá bán sản phẩm và chiết khấu của sản phẩm 
class Product:
    def __init__(self, name, price, discount):
        self.__name = name
        # Khởi tạo giá trị mặc định để tránh lỗi trước khi set
        self.__price = 0
        self.__discount = 0
        
        # Gọi hàm set thủ công để kiểm tra dữ liệu đầu vào ngay khi khởi tạo
        self.set_price(price)
        self.set_discount(discount)

    # --- 1. Thủ công cho Price ---
    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value > 0:
            self.__price = value
        else:
            print(f"❌ Lỗi: Giá bán ({value}) phải lớn hơn 0!")

    # --- 2. Thủ công cho Discount ---
    def get_discount(self):
        return self.__discount

    def set_discount(self, value):
        if 0 <= value <= 100:
            self.__discount = value
        else:
            print(f"❌ Lỗi: Giảm giá ({value}%) phải từ 0 đến 100!")

    # --- 3. Tính giá bán (Chỉ có hàm get, không có hàm set) ---
    def get_selling_price(self):
        return self.__price * (1 - self.__discount / 100)

    def show_info(self):
        # Lưu ý: Phải gọi hàm get_...() thay vì truy cập biến
        return f"SP: {self.__name} | Gốc: {self.get_price()} | Bán: {self.get_selling_price()}"

# --- CHẠY THỬ (SO SÁNH KHÁC BIỆT) ---

laptop = Product("Laptop Gaming", 20000000, 10)

# KHÁC BIỆT 1: Khi lấy dữ liệu
# Dùng property: print(laptop.price)
# Cách này:
print(f"Giá gốc hiện tại: {laptop.get_price()}")

print(f"gia ban thuc te : {laptop.get_selling_price()}")