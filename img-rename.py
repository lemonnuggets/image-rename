import subprocess
import os

# IMG_PATH = r'sample-assets\itaots-heartbaby-profilepic.jpg'
FOLDER_PATH = './sample-assets/'
EXE_PROCESS = "hachoir-metadata"
# FILE_LIST = []
# PNG_FILE_LIST = []
image_extensions = ('.png', '.jpg', '.jpeg')
def get_metadata(img_path):
    info_dict = {}
    process = subprocess.Popen([EXE_PROCESS, img_path],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                universal_newlines=True)

    for tag in process.stdout:
        line = tag.strip().split(':')
        info_dict[line[0].strip(' -')] = line[-1].strip()

    return info_dict.items()

def handle_file(file_path):
    print(file_path)
    print(os.path.splitext(file_path))
    trash, extension = os.path.splitext(file_path)
    if extension not in image_extensions:
        return -1

    info = get_metadata(file_path)
    for k,v in info:
        print(k,':', v)
    return 0
    # use_this = file_path.replace('\\', '\\\\')
    # use_this = use_this.replace(' ', '\\ ')
    # if extension in image_extensions:
    #     FILE_LIST.append(str(file_path))
    # if extension == image_extensions[0]:
    #     PNG_FILE_LIST.append(str(file_path))

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
# handle_file(IMG_PATH)
recursive_file_search([FOLDER_PATH,])