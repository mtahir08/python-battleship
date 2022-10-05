from tkinter import HORIZONTAL


request_validator = {
    "CREATE": {
        "type": "object",
        "properties": {
            "ships": {"type": "array"},
        },
        "required": ["ships"]
        }
}

VERTICAL = 'V'
HORIZONTAL = 'H'