import face_recognition
from PIL import Image, ImageDraw

location = "D:\\Pycharm_Database\\FacialRecog_Directory\\Faces\\"
image = face_recognition.load_image_file(location + 'group.png')
face_locations = face_recognition.face_locations(image)
face_landmarks_list = face_recognition.face_landmarks(image)

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

for face in face_landmarks_list:
    # img_draw.line(face_landmarks['chin'], fill=(r, g, b), width=5)
    img_with_draw.line(face['chin'])
    img_with_draw.line(face['left_eyebrow'])
    img_with_draw.line(face['right_eyebrow'])
    img_with_draw.line(face['nose_bridge'])
    img_with_draw.line(face['nose_tip'])
    img_with_draw.line(face['left_eye'])
    img_with_draw.line(face['right_eye'])
    img_with_draw.line(face['top_lip'])
    img_with_draw.line(face['bottom_lip'])

img_with_box.show()

for face in face_locations:
    # crop original faces
    img_cropped = img.crop((
        face[3],  # Left x
        face[0],  # Top y
        face[1],  # Right x
        face[2]  # Bottom y
    ))
    img_cropped.show()

    # crop marked faces
    img_cropped = img_with_box.crop((
        face[3],  # Left x
        face[0],  # Top y
        face[1],  # Right x
        face[2]  # Bottom y
    ))
    img_cropped.show()
