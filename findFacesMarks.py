import face_recognition
from PIL import Image, ImageDraw

location = "D:\\Pycharm_Database\\FacialRecog_Directory\\Faces\\"

# Load the image and detect face landmarks for each face within
image = face_recognition.load_image_file(location+'group.png')
face_landmarks_list = face_recognition.face_landmarks(image)

# Make a PIL image from the loaded image and then get a drawing object
img = Image.fromarray(image, 'RGB')
img_draw = ImageDraw.Draw(img)

img.show()

for face in face_landmarks_list:
    # img_draw.line(face_landmarks['chin'], fill=(r, g, b), width=5)
    img_draw.line(face['chin'])
    img_draw.line(face['left_eyebrow'])
    img_draw.line(face['right_eyebrow'])
    img_draw.line(face['nose_bridge'])
    img_draw.line(face['nose_tip'])
    img_draw.line(face['left_eye'])
    img_draw.line(face['right_eye'])
    img_draw.line(face['top_lip'])
    img_draw.line(face['bottom_lip'])

img.show()
