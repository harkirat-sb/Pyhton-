# # # # ITERABLE -  WHICH GIVES I
# # # for i in range(100):
# # #     print(i)
# #
# #
# #
# # def gen(n):
# #     for i in range(n):
# #         yield i
# #
# # # print(gen(100000)) ise ram save hoti ahi
# #
# # # print(i)
# # a = gen(10)
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # # print(next(a))
# # # print(next(a))
# # # print(next(a))
# # # print(next(a))
# #
# #
# #
# # # after some attempts it would stop working for exmple required number se ek phele if 10 then after 9 wont work
# #
# # num = [1,2,3]
# # a = num.__iter__()
# # print(dir(num))
# # # if durection mein __iter__ it means it can be iterated hence
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # while True:
# #     try:
# #         item = next(a)
# # #         print(a)
# # #     except StopIteration:
# # #         break
# # # print(dir(a))
# #
# # class Myrange:
# #     def __init__(self,start,end):
# #         self.value = start
# #         self.end = end
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         if self.value >= self.end:
# #             raise StopIteration
# #         current = self.value
# #         self.value += 1
# #         return current
# #
# # Nums = Myrange(1,10)
# # for num in Nums:
# #     print(next(Nums))
#
# #Generator
# def square_numbers(nums):
#     result = []
#     for i in nums:
#         yield (i ** 2)
# my_numbers = square_numbers([1,2,4,5,6])
# print(my_numbers)
# # converting to generator use yeild
# print(next(my_numbers))
# print(next(my_numbers))
#
# print(next(my_numbers))
# print(next(my_numbers))
# print(next(my_numbers))
# # to make it for loop
# for num in my_numbers:
#     print(num)
#
#
#
#

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()
    def __iter__(self):
        return self
    def __next__(self):
        if self .index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]

s1 = Sentence("This is a test")
for word in s1:
    print(word)
