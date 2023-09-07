from typing import Dict

from src.repositories.images.repository import ImagesRepository


class ImageService:
    repository = ImagesRepository

    @classmethod
    async def get_images(cls, player: str) -> Dict[str, str]:
        images_and_extensions = await cls.repository.get_images()
        images = {
            image: f"images-files/{image}.{extension}"
            for image, extension in images_and_extensions.items()
        }
        return images

    @classmethod
    async def save_image(cls, image_id: str, extension: str, content: str):
        await cls.repository.save_image(image_id, extension, content)
