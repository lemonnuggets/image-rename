import subprocess
import os
import maya
from PIL import Image
from PIL.ExifTags import TAGS

FOLDER_PATH = '.\\sample-assets\\'
image_extensions = ('.png', '.jpg', '.jpeg')
# def get_metadata(img_path):
#     info_dict = {}
#     image = Image.open(img_path)
#     exif_data = image.getexif()
#     # iterating over all EXIF data fields
#     for tag_id in exif_data:
#         # get the tag name, instead of human unreadable tag id
#         tag = TAGS.get(tag_id, tag_id)
#         data = exif_data.get(tag_id)
#         # decode bytes 
#         if isinstance(data, bytes):
#             data = data.decode('iso-8859-1', 'replace')
#         # print(f"{tag:25}: {data}")
#         info_dict[tag] = data
#     return info_dict

def get_datetime(img_path, extension):
    required_exif_tags = ('DateTimeOriginal','DateTimeDigitized','DateTime')
    required_info_tags = ('data:create', 'date:modify')
    info_dict = {}
    image = Image.open(img_path)
    if extension == '.png':
        image.load()
        # print(image.info)
        datetime = None
        for tag in required_info_tags:
            if tag in image.info:
                datetime = image.info[tag]
        if datetime != None:
            # print(maya.parse(datetime).datetime())
            datetime = maya.parse(datetime).datetime()
            date = datetime.date()
            time = datetime.time()
            return f'{date} {time}'
    exif_data = image.getexif()
    # print(exif_data)
    # iterating over all EXIF data fields
    for tag_id in exif_data:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        if tag not in required_exif_tags:
            continue
        data = exif_data.get(tag_id)
        # decode bytes 
        if isinstance(data, bytes):
            data = data.decode('iso-8859-1', 'replace')
        info_dict[tag] = data

    # returns value of highest priority tag from required_exif_tags
    # that exists within the image metadata
    for tag in required_exif_tags:
        if tag in info_dict.keys():
            return info_dict[tag]

def handle_file(file_path):
    print(file_path)
    trash, extension = os.path.splitext(file_path)
    head, file_name = os.path.split(file_path)
    print(head, file_name, extension)
    if extension not in image_extensions:
        return -1

    datetime = get_datetime(file_path, extension)
    if datetime != None:
        datetime = datetime.replace(':', '-')
        print(f'{head}\\{datetime}{extension}')
        # os.rename(file_path, f'{head}\\{datetime}{extension}')
    return 0

def recursive_file_search(paths):
    paths.sort()
    for path in paths:
        if os.path.isdir(path):
            for file_ in os.listdir(path):
                if os.path.isdir(os.path.join(path, file_)):
                    recursive_file_search([os.path.join(path, file_)])
                elif os.path.isfile(os.path.join(path, file_)):
                    handle_file(os.path.join(path, file_))
        elif os.path.isfile(path):
            handle_file(path)
        elif os.path.exists(path):
            print("{} Path isn't an image file or directory".format(path))

recursive_file_search([FOLDER_PATH,])
