from .demo import ImageSizerTF
from .log_anything import LogAnythingTF
from .input_text import InputStringTF
from .output_text import OutputStringTF
NODE_CLASS_MAPPINGS = {
    "ImageSizerTF": ImageSizerTF,
    "LogAnythingTF":LogAnythingTF,
    "InputStringTF": InputStringTF,
    "OutputStringTF": OutputStringTF
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageSizerTF": "Image Sizer TF",
    "LogAnythingTF": "Log anything",
    "InputStringTF": "Input String TF",
    "OutputStringTF": "Output String TF"
}