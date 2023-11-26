import streamlit as st
import requests
import pymongo

# התחבר ל-MongoDB
client = pymongo.MongoClient("mongodb+srv://eli:yc36DGPyZDhgamk0@atlascluster.m6tavxq.mongodb.net/?retryWrites=true&w=majority")
db = client["my_db"]
collection = db["images"]


# פונקציה לקבלת תמונה מהמשתמש
def get_image():
    # קבל את התמונה מהמשתמש
    image = st.file_uploader("העלה תמונה")
    # אם התמונה לא ריקה
    if image is not None:
        image_name = "eli.jpeg"
        # שמור את התמונה ב-MongoDB
        collection.insert_one({"name": image_name, "image": image.read() })
        return image_name
    return None


# פונקציה להצגת התמונה מה-DB
def show_image(image_name):
    # קבל את התמונה מה-DB
    image = collection.find_one({"name": image_name})["image"]
    # הצג את התמונה
    st.image(image)


# כותרת הראשית
st.title("אפליקציית העלאת תמונות")

# קבל את התמונה מהמשתמש
image_name = get_image()


# אם קיבלנו תמונה
# if image_name is not None:
#     # הצג את התמונה
#     show_image(image_name)


def show_all_images():
    # קבל את כל התמונות מה-DB
    images = collection.find()
    # עבור על כל התמונות
    for image in images:
        # הצג את התמונה
        st.image(image["image"])


show_all_images()
