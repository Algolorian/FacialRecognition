import face_recognition
from PIL import Image, ImageDraw

location = "D:\\Pycharm_Database\\FacialRecog_Directory\\Faces\\"

# Load the image and detect face landmarks for each face within
image = face_recognition.load_image_file(location+'single-person.jpg')
face_landmarks_list = face_recognition.face_landmarks(image)

# Make a PIL image from the loaded image and then get a drawing object
img = Image.fromarray(image, 'RGB')
img_draw = ImageDraw.Draw(img)

img.show()

# Draw all the features for the first face
face_landmarks = face_landmarks_list[0]  # Get the first object corresponding to the first face
# img_draw.line(face_landmarks['chin'], fill=(r, g, b), width=5)
img_draw.line(face_landmarks['chin'])
img_draw.line(face_landmarks['left_eyebrow'])
img_draw.line(face_landmarks['right_eyebrow'])
img_draw.line(face_landmarks['nose_bridge'])
img_draw.line(face_landmarks['nose_tip'])
img_draw.line(face_landmarks['left_eye'])
img_draw.line(face_landmarks['right_eye'])
img_draw.line(face_landmarks['top_lip'])
img_draw.line(face_landmarks['bottom_lip'])

img.show()
