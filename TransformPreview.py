import io
import base64
from torchvision import transforms
from nicegui import ui
from nicegui.events import MouseEventArguments

def pilImageToBase64(img):
    with io.BytesIO() as output:
        img.save(output, format="PNG")
        return 'data:image/png;base64, '+str(base64.b64encode(output.getvalue()),encoding='utf-8')

class TransformPreview:
    def __init__(self, samples):
        self.samples = samples
        self.transform = None

    def update(self, parent, originalImage, inputImage, transform):
        parent.clear()
        with parent:
            ui.label("Original image")
            ui.interactive_image(pilImageToBase64(originalImage))
            with ui.row():
                for i in range(self.samples):
                    img = transform(inputImage)
                    ui.interactive_image(pilImageToBase64(img))

