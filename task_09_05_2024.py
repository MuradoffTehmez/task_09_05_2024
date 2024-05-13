import itertools

class CemHedefiTapici:
   def __init__(self):
       self.siyahi = []

   def siyahi_doldur(self, yeni_siyahi):
       """
       Verilmis yeni siyahini class'in siyahi deyerine menimsetmek ucun method.
       
       Args:
           yeni_siyahi (list): Menimsenilecek yeni siyahi.
       """
       self.siyahi = list(yeni_siyahi)

   def siyahi_goster(self):
       """
       Class'in siyahi deyerini gosterir.
       
       Returns:
           list: Class'in siyahi deyeri.
       """
       return self.siyahi

   def hedef_deyer_tap(self):
       """
       Istifadeciden hedef deyeri alir ve siyahidaki cemi bu deyere berabEr olan
       ilk cUtlUyUn indekslErini qaytarir. Eger hedef deyerine berabEr cUtlUk
       yoxdursa, -1 qaytarir.
       
       Returns:
           str veya int: CUtlUyUn indeksleri veya -1.
       """
       hedef = int(input("Hədəf dəyəri daxil edin: "))
       siyahi = self.siyahi

       for i in range(len(siyahi)):
           for j in range(i + 1, len(siyahi)):
               if siyahi[i] + siyahi[j] == hedef:
                   return f"siyahi[{i}] = {siyahi[i]} və siyahi[{j}] = {siyahi[j]}"
       return -1

#
cem_hedefi_tapici = CemHedefiTapici()
cem_hedefi_tapici.siyahi_doldur([1, 2, 3, 4, 5])
print(cem_hedefi_tapici.siyahi_goster())
print(cem_hedefi_tapici.hedef_deyer_tap())