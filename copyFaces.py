import face_recognition
from PIL import Image, ImageDraw
import os

location = "D:\\Pycharm_Database\\FacialRecog_Directory\\Unknown_Photos\\"
faces_dir = "D:\\Pycharm_Database\\FacialRecog_Directory\\Faces\\"
for filename in os.listdir(location):
    print(filename)
    image = face_recognition.load_image_file(location + filename)
    face_locations = face_recognition.face_locations(image)

    amount = len(face_locations)
    print(f'There are {amount} face locations')

    if len(face_locations) == 0:
        continue
    os.system(f"copy {location}{filename} {faces_dir}")
    img = Image.fromarray(image, 'RGB')
    img_with_box = img.copy()
    img_with_draw = ImageDraw.Draw(img_with_box)

    for i in range(len(face_locations)):
        img_with_draw.rectangle(
            [
                (face_locations[i][3], face_locations[i][0]),
                (face_locations[i][1], face_locations[i][2])
            ],
            outline="red",
            width=8
        )

    img_with_box.show()
