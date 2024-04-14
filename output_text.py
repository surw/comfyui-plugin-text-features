
class OutputStringTF:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING",{"dynamicPrompts": True}),
            },
            "optional":{
                "link": ("STRING")
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("output", "link")

    FUNCTION = "run"

    CATEGORY = "TFCustom"

    def run(self, text, link):
        return (str(text), link)
