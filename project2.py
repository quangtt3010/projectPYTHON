#ngan hang (so du , ma otp , so tien con lai)
class ngan_hang :
    def __init__(self,name,so_du=0):
        self.name = name
        self.so_du = so_du
    def nap_tien(self,tien_nap):
        if tien_nap < 0:
            print("ecrror")
        else:
            self.so_du+=tien_nap
            print(f"so tien co trong tai khoan : {self.so_du}")
    
    def generate_otp(self,otp):
        return otp
    
    def withdraw(self, tien_rut):
        if tien_rut > self.so_du:
            print(" Số dư không đủ!")
            return
            
        
        # tạo OTP
        otp = self.generate_otp(12345)
        user_otp = int(input(" Nhập OTP để xác nhận: "))

        if user_otp == otp:
            self.so_du -= tien_rut
            print(f"Rút {tien_rut} thanh cong , so du con lai : {self.so_du}")
        else:
            print("OTP sai ,  Giao dịch bị hủy.")
        
    
    def tong_ket(self):
        print(f"ten chu tai khoan : {self.name}")
        print(f"so du hien tai {self.so_du}")
    
a = ngan_hang("quang " , 500000)
a.tong_ket()
a.nap_tien(5000)
a.withdraw(20000)
a.tong_ket()
    
