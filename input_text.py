
class InputStringTF:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING",{"multiline": True, "dynamicPrompts": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Output",)

    FUNCTION = "run"

    CATEGORY = "TFCustom"

    def run(self, text):
        return (str(text), )
