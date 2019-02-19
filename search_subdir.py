import os
def searh_file(start_path):
    for dir_path, subdir_list, file_list in os.walk(start_path):
        print(dir_path)
        print(subdir_list)
        print(file_list)
        print('-' * 100)
        #for fname in file_list:
        #    print(os.path.join(file_list, fname))

def main():
    searh_file('C:/work/My_Program/')

if __name__ == '__main__': main()
