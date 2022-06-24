import face_recognition
from PIL import Image, ImageDraw

location = "D:\\Pycharm_Database\\FacialRecog_Directory\\Faces\\"
image = face_recognition.load_image_file(location + 'group.png')
face_locations = face_recognition.face_locations(image)

amount = len(face_locations)
print(f'There are {amount} face locations')

img = Image.fromarray(image, 'RGB')
img.show()

img_with_box = img.copy()
img_with_draw = ImageDraw.Draw(img_with_box)

for face in face_locations:
    img_with_draw.rectangle(
        [
            (face[3], face[0]),
            (face[1], face[2])
        ],
        outline="red",
        width=3
    )

img_with_box.show()

for face in face_locations:
    img_cropped = img.crop((
        face[3],  # Left x
        face[0],  # Top y
        face[1],  # Right x
        face[2]  # Bottom y
    ))
    img_cropped.show()
