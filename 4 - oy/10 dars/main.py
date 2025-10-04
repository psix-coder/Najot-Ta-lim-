

# img_urls = [
#    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
#    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
#    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
#    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
#    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
#    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
#    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
#    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
#    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
#    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
#    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
#    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
#    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
#    'https://images.unsplash.com/photo-1550439062-609e1531270e',
#    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
# ]
# import time
# import multiprocessing
# import requests

# def genereting_number():
#     for i in range(1,1000000):
#         print(i)
#         time.sleep(0)

#     # pr0 = multiprocessing.Process(target=genereting_number)
#     # pr1 = multiprocessing.Process(target=genereting_number)
#     # pr2 = multiprocessing.Process(target=genereting_number)

#     # pr0.start()
#     # pr1.start()
#     # pr2.start()

#     # pr0.join()
#     # pr1.join()
#     # pr2.join()

#     # end = time.time()

#     # print(f"Ketgan vaqt {round(end-start, 2)}")

 
# def download_image(image_url: str):
#     image_name = image_url.split("/")[-1] + ".jpg"
#     request = requests.get(image_url)
#     if request.status_code == 200:
#         data = request.content
#         with open(f"images/{image_name}", mode="wb") as file:
#             file.write(data)
#         print(f"{image_name} yuklandi✅")
#     else:
#         print("Qandaydir hatolik ketdi!!!")


# if __name__ == "__main__":
#     start = time.time()

#     procces = []
#     i = 0
#     for image_url in img_urls:
#         pr = multiprocessing.Process(target=download_image, args= (image_url,), name=f'Pr-{i}')
#         pr.start()
#         i += 1
#         procces.append()

#     for pr in procces:
#         pr.join()

#     end = time.time()

#     print(f"dastur ishlashi uchun {round(end - start, 2) }secund avqt ketdi")

# 1 misol

# new_dict = []
# print(new_dict)

#  2 misol

# user_imput = input("Ismingizni kiriting: ")
# print(f"Assalomu alaykum {user_imput}")

