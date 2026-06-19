from pathlib import Path

def count_txt_files (folder_path):
    folder=Path(folder_path)

    if not folder.exists():
        print("该文件夹不存在")
        return
    if not folder.is_dir():
        print("这不是一个文件夹")
        return
    txt_count=0

    for item in folder.iterdir():
        if item.is_file() and item.suffix==".txt":
            txt_count+=1
    print(f"文件夹中.txt文件的数量：{txt_count}")

count_txt_files(Path(__file__).parent)