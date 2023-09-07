import os
from typing import Dict


class ImagesRepository:
    images_folder_path = os.path.join("src", "static", "images")

    @classmethod
    async def get_images(cls) -> Dict[str, str]:
        images = {
            "".join(image.split(".")[:-1]): "".join(image.split(".")[-1])
            for image in os.listdir(cls.images_folder_path)
        }
        return images

    @classmethod
    async def save_image(cls, image_id: str, content: str, extension: str):
        path = os.path.join(cls.images_folder_path, image_id, extension)
        with open(path, "w") as file:
            file.write(content)
