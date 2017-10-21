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


def main():
    pass


if __name__ == '__main__':
    main()
