
class InputStringTF:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING",{"multiline": True, "dynamicPrompts": True})
            },
            "optional":{
                "args": ("STRING")
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("output", "link")

    FUNCTION = "run"

    CATEGORY = "TFCustom"

    def run(self, text, args):
        return (str(text), args)
