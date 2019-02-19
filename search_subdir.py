import os

# 디렉토리로 부터 모든 하위 디렉토리까지 확장자별로 파일 찾기 (값이 없으면 전체)
def searh_subdirs_files(start_path, filter_ext):
    for full_path, subdir_list, file_list in os.walk(start_path):
        for file_name in file_list:
            file_ext = os.path.splitext(file_name)[-1]
            if (not filter_ext or file_ext in filter_ext):
                print(full_path.replace('/', '\\'), '\\', file_name, sep='')

def main():
    searh_subdirs_files('C:/work/hospital/보건소/', ('.exe'))

if __name__ == '__main__': main()
