# # 1
# class MyNumbers:
#     def __iter__(self):
#         self.current = 2  # Boshlanish nuqtasini belgilaymiz
#         return self  # O'zini qaytaradi, bu - qutini ochib qo'yish
       
#     def __next__(self):
#         if self.current <= 5:  # Agar hali 5 ga yetmagan bo'lsa
#             number = self.current  # Hozirgi raqamni saqlab olamiz
#             self.current += 1  # Keyingi safar uchun raqamni oshiramiz
#             return number  # Raqamni qaytaradi
#         else:
#             raise StopIteration  # Agar qutidagi barcha shirinliklar tamom bo'lsa, to'xtatadi

# # Obyektni yaratamiz
# numbers = MyNumbers()

# # Qutini ochib, ichidan bittadan shirinlik olamiz
# for num in numbers:
#     print(num)


# # 2
# class Oyinchilar:
#     def __init__(self, royxat):
#         self.royxat = royxat

#     def __iter__(self):
#         self.index = 0  # Boshlanish nuqtasi
#         return self

#     def __next__(self):
#         if self.index < len(self.royxat):
#             element = self.royxat[self.index]
#             self.index += 1
#             return element
#         else:
#             raise StopIteration  # Oyinchilar tugaganda xatolik chiqaradi

# # Oyinchilarni royxatini yaratamiz
# oyinchilar = Oyinchilar(["Mario", "Luigi", "Peach", "Toad"])

# # Endi ularni bitta-bitta oqiymiz
# for oyinchi in oyinchilar:
#     print(oyinchi)



# # 3
# class MyBag:
#     def __init__(self, items):
#         self.items = items

#     def __iter__(self):
#         self.index = 0  # boshlanish nuqtasi
#         return self

#     def __next__(self):
#         if self.index < len(self.items):
#             result = self.items[self.index]  # navbatdagi shirinlik
#             self.index += 1  # keyingi indeksga o‘tish
#             return result
#         else:
#             raise StopIteration  # oxiriga yetganimizni bildiradi

# my_bag = MyBag(['olma', 'banan', 'gilos'])

# for item in my_bag:
#     print(item)



# # 4
# class MyIterator:
#     def __init__(self, max_value):
#         self.max_value = max_value
#         self.current = 0

#     def __iter__(self):
#         self.current = 0  # Boshlanish nuqtasini o'rnatamiz
#         return self

#     def __next__(self):
#         if self.current < self.max_value:
#             result = self.current
#             self.current += 1
#             return result
#         else:
#             raise StopIteration  # Elementlar tugaganda xatolik chiqaradi

# # MyIterator obyekti
# my_iter = MyIterator(5)

# # Bu obyekt endi iterable bo‘lgani uchun `for` tsiklida foydalanish mumkin
# for num in my_iter:
#     print(num)



# # 5
# class MyIterator:
#     def __iter__(self):
#         self.current = 1  # Boshlanish nuqtasini o‘rnatamiz
#         return self

#     def __next__(self):
#         if self.current <= 3:
#             result = self.current
#             self.current += 1
#             return result
#         else:
#             raise StopIteration  # Elementlar tugaganda to‘xtatish uchun xato chiqaradi

# # MyIterator obyekti
# my_iter = MyIterator()

# # `for` tsiklida foydalanamiz
# for num in my_iter:
#     print(num)



# # 6
# class Counter:
#     def __init__(self):
#         self.current = 1  # Boshlanish nuqtasini o'rnatamiz

#     def __next__(self):
#         if self.current <= 3:
#             result = self.current
#             self.current += 1
#             return result
#         else:
#             print("raise StopIteration  # To'xtatish uchun xato chiqaradi")

# # Counter obyekti
# counter = Counter()

# # `next()` yordamida qiymatlarni chiqaramiz
# print(next(counter))  # 1
# print(next(counter))  # 2
# print(next(counter))  # 3
# # print(next(counter))  # StopIteration chiqariladi


# # 7
# class MyNext:
#     def __init__(self):
#         self.current = 1
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current <= 4:
#             result = self.current
#             self.current += 1
#             return result
        
# my_next = MyNext()

# for i in my_next:
#     print(i)

# print(next(my_next))
# print(next(my_next))
# print(next(my_next))
# print(next(my_next))



# 8
class Teacher:
    def __init__(self, name: str):
        self.name = name
    
    def voice(self):
        print('Maladest\nbali')

class Student(Teacher):
    def voice(self):
        print('Ustoooz\nKechiring')

teacher1 = Teacher('Ustoz1')
teacher2 = Teacher('Ustoz2')
student1 = Student('Talaba1')
student2 = Student('Talaba2')
student3 = Student('Talaba3')

list_of_human = [teacher1, teacher2, student1, student2, student3]

for h in list_of_human:
    h.voice()
