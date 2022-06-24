import face_recognition
from PIL import ImageDraw, Image

location = "D:\\Pycharm_Database\\FacialRecog_Directory\\Faces\\"

# Load elon-musk-1.jpg and detect faces
image = face_recognition.load_image_file(location + "elon-musk-1.jpg")
face_locations = face_recognition.face_locations(image)

# Get the single face encoding out of elon-musk-1.jpg
face_location = face_locations[0]  # Only use the first detected face
face_encodings = face_recognition.face_encodings(image, [face_location])
elon_musk_known_face_encoding_1 = face_encodings[0]  # Pull out the one returned face encoding

# Load elon-musk-2.jpg and detect faces
image = face_recognition.load_image_file(location + "elon-musk-2.png")
face_locations = face_recognition.face_locations(image)

# Get the single face encoding out of elon-musk-2.jpg
face_location = face_locations[0]
face_encodings = face_recognition.face_encodings(image, [face_location])
elon_musk_known_face_encoding_2 = face_encodings[0]

# Load the image with unknown to compare
image = []
image.append(face_recognition.load_image_file(location + "group.png"))  # Load the image we are comparing
image.append(face_recognition.load_image_file(location + "elon-musk-in-group.jpg"))  # Load the image we are comparing


# Loop over each unknown face encoding to see if the face matches either known encodings
for img in image:
    pic = Image.fromarray(img, 'RGB')
    pic.show()
    unknown_face_encodings = face_recognition.face_encodings(img)
    face_locations = face_recognition.face_locations(img)
    print(f"{len(unknown_face_encodings)} people found")
    for unknown_face_encoding in unknown_face_encodings:
        matches = face_recognition.compare_faces(  # The known face encodings (can be only 1 - less is faster)
            [elon_musk_known_face_encoding_1, elon_musk_known_face_encoding_2],
            unknown_face_encoding  # The single unknown face encoding
        )
        if True in matches:
            face = face_locations[unknown_face_encodings.index(unknown_face_encoding)]
            imge = Image.fromarray(img, 'RGB')
            img_with_box = imge.copy()
            img_with_draw = ImageDraw.Draw(img_with_box)
            img_with_draw.rectangle(
                [
                    (face[3], face[0]),
                    (face[1], face[2])
                ],
                outline="red",
                width=5
            )
            img_with_box.show()
            print('Match found')
        else:
            print('Not match')
        print(matches)
