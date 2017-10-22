import os
import time

DAYS = 7
FOLDERS = []

TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILES = 0
TOTAL_DELETED_DIRS = 0

now_time = time.time()
age_time = now_time - 60 * 60 * 24 * DAYS


def deleted_old_files(folder):
    global TOTAL_DELETED_SIZE
    global TOTAL_DELETED_FILES
    for path, dirs, files in os.walk(folder):
        for file in files:
            file_name = os.path.join(path, file)
            file_time = os.path.getmtime(file_name)
            if file_time < age_time:
                size_file = os.path.getsize(file_name)
                TOTAL_DELETED_SIZE += size_file
                TOTAL_DELETED_FILES += 1
                print("Deleting file: " + str(file_name))
                os.remove(file_name)


def deleted_empty_dirs(folder):
    global TOTAL_DELETED_DIRS
    empty_folders = 0
    for path, dirs, files in os.walk(folder):
        if not dirs and not files:
            TOTAL_DELETED_DIRS += 1
            print("Deleting empty dir: " + str(path))
            os.rmdir(path)
    if empty_folders > 0:
        deleted_empty_dirs(folder)


def main():
    start_time = time.asctime()
    for folder in FOLDERS:
        deleted_old_files(folder)
        deleted_empty_dirs(folder)
    finish_time = time.asctime()
    print("+++++++++++++++++++++<<START>>+++++++++++++++++++++++")
    print("Start time: " + str(start_time))
    print("Total deleted files: " + str(TOTAL_DELETED_FILES))
    print("Total deleted dirs: " + str(TOTAL_DELETED_DIRS))
    print("Total deleted size: " + str(TOTAL_DELETED_SIZE/1024/1024) + 'Mb')
    print("Finish time: " + str(finish_time))
    print("+++++++++++++++++++++<<Finish>>++++++++++++++++++++++")


if __name__ == '__main__':
    main()
