
FITTING_OPTIONS = ["cover", "contain", "inside", "outside"]
IMAGE_FORMAT_OPTIONS = ["auto", "jpg", "png", "webp", "tiff"]


class ImageFileTransform:

    def __init__(
        self, 
        fit: str | None = None, 
        width: int | None = None, height: int | None = None, 
        quality: int | None = None, 
        withoutEnlargement: bool | None = None, 
        img_format: str | None = None, 
        **kwargs
    ):
        parameters = {
            "fit": fit if fit in FITTING_OPTIONS else None,
            "width": width,
            "height": height,
            "quality": quality,
            "withoutEnlargement": withoutEnlargement,
            "format": img_format if img_format in IMAGE_FORMAT_OPTIONS else None
        }

        self.parameters = {k:v for k,v in parameters.items() if v is not None}

        if kwargs:
            transforms = []

            for k, v in kwargs.items():
                parameter_list = [k, *(v if isinstance(v, list) else [v])]
                transforms.append(parameter_list)

            self.parameters["transforms"] = transforms