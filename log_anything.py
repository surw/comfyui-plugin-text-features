
from .models import WILDCARD
class LogAnythingTF:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input": (WILDCARD)
            }
        }
    RETURN_TYPES = ["STRING"]
    RETURN_NAMES = ["output"]
    OUTPUT_NODE = True
    FUNCTION = "run"

    CATEGORY = "debugging"

    def run(self, input):
        print(input)
        # Return the width and height as a tuple of integers
        return ()
