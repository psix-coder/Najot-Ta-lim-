# # import time 
# # import threading


# # def generete_number():
# #     for i in range(1,11):
# #         print(i)
# #         time.sleep(1)

# # start = time.time()

# # th1 = threading.Thread(target=generete_number)
# # th2 = threading.Thread(target=generete_number)
# # th3 = threading.Thread(target=generete_number)

# # th1.start()
# # th2.start()
# # th3.start()

# # th1.join()
# # th2.join()
# # th3.join()


# # end = time.time()

# # print(f"Dastur ishlashi uchun {round(end - start)} sonya ketdi!")
# import time
# import threading


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



# def download_image(image_url: str):
#     image_url = image_url.split("/")[-1] + "jpg"
#     request = request.get(image_url)
#     if request.status_code == 200:
#         data = request.content
#         with open(f"images/{image_url}", mode="wb") as file:
#             file.write(data)
#         print(f"{image_url} yakunlandi")
#     else:
#         print("Qandaydir xatolik yuz berdi!")

# start = time.time()

# ths = []
# for i in img_urls:
#     th = threading.Thread(target=)





def kattalikka_tekshir(sonlar):
    kattalikka_sonlar = [son for son in sonlar if son > 75]
    return kattalikka_sonlar

user_input = input("Sonlarni kiriting (Vergul bilan ajratilgan holda: ) ")

sonlar = [int(son.strip()) for son in user_input.split(",")]

result = kattalikka_tekshir(sonlar)
print(result)

