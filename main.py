class Laptop:
  def spesifikasi(self):
    print('Dell, 8 GB, 256 SSd, Intel Core 7 ')

class Fungsi:
  def kegunaan(self):
    print('Help get the job done')

class My_Laptop(Laptop, Fungsi):
  pass

laptop = My_Laptop()
laptop.spesifikasi()
laptop.kegunaan()

#multiple_inheritence
