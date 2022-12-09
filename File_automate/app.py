import os
import shutil


def Arrange_file(basepath):
    try:
        with os.scandir(basepath) as entries:
            for entry in entries:
                if (entry.is_file()):
                    file_split = entry.name.split('.')
                    file_name = entry.name
                    folder_name = file_split[-1]+"_Folder"
                    src_path = basepath+file_name
                    path = os.path.join(basepath, folder_name)
                    isFolder = os.path.isdir(path)
                    if isFolder:
                        dest_path = path
                        shutil.move(src_path, dest_path)
                    else:
                        os.mkdir(path)
                        dest_path = path
                        shutil.move(src_path, dest_path)

        return "Sucesss"
    except:
        return "failed"
