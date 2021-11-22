# coding:utf8
import os

def check_dir():
    #手动输入文件保存地址
    #Manually enter the file save location
    dir_path = input('Please enter the save path:')
    #固定文件保存地址
    #Fixed file storage location
    if not os.path.exists(dir_path):
        dir_path = check_dir()
    return dir_path

def check_url():
    url_path = input('please enter the video url:')

    if os.system("yt-dlp -F " + url_path) != 0:
        url_path = check_url()
    return url_path

def download_vedio():
    dir_path = check_dir()
    print('文件保存路径:' + dir_path)
    os.chdir(dir_path)
    url_path = check_url()
    down_code = input('please enter code:')
    status = os.system("yt-dlp -f " + down_code + " " + url_path)
    if status == 0:
        print("Download Success!")
    else:
        print("Download Failed!")

if __name__ == '__main__':
    while True:
        download_vedio()
