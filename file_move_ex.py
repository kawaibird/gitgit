import json
import os
import shutil
import glob

done = 'done'
Etc = 'Etc'
trash = 'trash'
phrase = '_color_type_manufacturer_model'
top_dir_name = '20211108000000_0001_CH17_015'


os.makedirs(f'check/{top_dir_name}/', exist_ok=True)
check_dir = f'check/{top_dir_name}/'

for middle_path_name in [done, Etc]:
    json_list = glob.glob(f'{top_dir_name}/{middle_path_name}/*.json')
    move_list = []
    for path in json_list:
        with open(path, "r") as file:
            file = json.load(file)
        if file['color'] == "Magenta" or file['color'] == 'Brown' or file['color'] == 'Beige':
            move_list.append(path)

    for path in move_list:
        jpg_path = (os.path.splitext(path))[0] + '.jpg'
        shutil.move(jpg_path, check_dir + os.path.basename(jpg_path))
        shutil.move(path, check_dir + os.path.basename(path))

    for last in [done, Etc]:
        if os.path.exists(f'{top_dir_name}/{middle_path_name}/{last}{phrase}'):
            json_list = glob.glob(f'{top_dir_name}/{middle_path_name}/{last}{phrase}/*.json')
            move_list = []
            for path in json_list:
                with open(path, "r") as file:
                    file = json.load(file)
                if file['color'] == "Magenta" or file['color'] == 'Brown' or file['color'] == 'Beige':
                    move_list.append(path)
            for path in move_list:
                jpg_path = (os.path.splitext(path))[0] + '.jpg'
                shutil.move(jpg_path, check_dir + os.path.basename(jpg_path))
                shutil.move(path, check_dir + os.path.basename(path))
