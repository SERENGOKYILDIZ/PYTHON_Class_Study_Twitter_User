class USER:

    def __init__(self, name: str, pass_: str):
        self.name = name
        self.pass_ = pass_
        self.is_login = False
        print(f"\"{self.name}\" isimli yeni bir kullanici olusturuldu.")

    def Login(self, name: str, pass_: str):
        if self.name == name and self.pass_ == pass_ and self.is_login is False:
            print(f"\"{self.name}\" isimli kullaniciya Basariyla giris yaptiniz")
            self.is_login = True
        elif self.is_login is True:
            print(f"\"{self.name}\" isimli kullanici, zaten giris yaptiniz")
        else:
            print(f"\"{self.name}\" isimli kullanici icin kullanici yada sifre hatali!")

    def Get_Comment(self, text: str):
        if self.is_login is True:
            print(f"\"{self.name}\" isimli kullanicinin mesaji : {text}")
        else:
            print(f"Ilk once giris yapilmasi gerekiyor {self.name}")
