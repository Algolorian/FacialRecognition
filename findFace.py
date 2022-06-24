import face_recognition
from PIL import Image, ImageDraw

location = "D:\\Pycharm_Database\\FacialRecog_Directory\\Faces\\"

image = face_recognition.load_image_file(location + 'single-person.jpg')

face_locations = face_recognition.face_locations(image)

amount = len(face_locations)
print(f'There are {amount} face locations')

first_face_location = face_locations[0]

print(first_face_location)

img = Image.fromarray(image, 'RGB')

img.show()

img_with_box = img.copy()
img_with_draw = ImageDraw.Draw(img_with_box)

img_with_draw.rectangle(
    [
        (first_face_location[3], first_face_location[0]),
        (first_face_location[1], first_face_location[2])
    ],
    outline="red",
    width=3
)

img_with_box.show()

img_cropped = img.crop((
    first_face_location[3],  # Left x
    first_face_location[0],  # Top y
    first_face_location[1],  # Right x
    first_face_location[2]  # Bottom y
))

img_cropped.show()
