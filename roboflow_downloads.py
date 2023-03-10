# Для загрузки размеченых данных с робофлов
from roboflow import Roboflow

def download(version):
    rf = Roboflow(api_key="OwBeTBZjZOylGw1HUTGP")
    project = rf.workspace("project-934k6").project("s-uacg7")
    dataset = project.version(version).download("yolov8")

if __name__ ==  "__main__":
    download(version=1)