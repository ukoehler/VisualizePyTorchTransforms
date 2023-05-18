import os
import pathlib
import base64
import io
from PIL import Image
from torchvision import transforms
from nicegui import ui
from nicegui.events import MouseEventArguments
import TransformsRandomResizedCrop
import TransformsRandomHorizontalFlip
import TransformPreview

transformsRandomResizedCrop = TransformsRandomResizedCrop.TransformsRandomResizedCrop()
transformsRandomHorizontalFlip = TransformsRandomHorizontalFlip.TransformsRandomHorizontalFlip()

def pilImageToBase64(img):
    with io.BytesIO() as output:
        img.save(output, format="PNG")
        return 'data:image/png;base64, '+str(base64.b64encode(output.getvalue()),encoding='utf-8')

def parameterChangeRandomResizedCrop():
    print("parameterChangeRandomResizedCrop")
    transform = transformsRandomResizedCrop.getTransform()
    print(transform)
    transformsRandomResizedCropPreview.update(transformsRandomResizedCropPreviewColumn,
                                              originalImage, originalImage, transform)

def parameterChangeRandomHorizontalFlip():
    print("parameterChangeRandomHorizontalFlip")
    transform = transformsRandomHorizontalFlip.getTransform()
    print(transform)
    inputImage = originalImage.resize((160, 116), Image.Resampling.BICUBIC)
    transformsRandomHorizontalFlipPreview.update(transformsRandomHorizontalFlipColumn,
                                              originalImage, inputImage, transform)
  
if __name__ in {"__main__", "__mp_main__"}:

    # default values are not documented. Print them out here
    resize = transforms.Resize(size=(128, 128))
    print("resize", resize)
    randomResizedCrop = transforms.RandomResizedCrop(size=(128, 128))
    print("randomResizedCrop", randomResizedCrop)

    mainFilePath = pathlib.Path(__file__).parent.resolve()
    print(mainFilePath)
    # originalImageBase64 = None
    # with open(os.path.join(mainFilePath, 'input.png'), 'rb') as f:
    #     originalImageBase64 = 'data:image/png;base64, '+str(base64.b64encode(f.read()),encoding='utf-8')
    originalImage = Image.open(os.path.join(mainFilePath, 'input.png'))
    print(originalImage.size)
    originalImage = originalImage.resize((250, 181), Image.Resampling.BICUBIC)
    print(originalImage.size)

    with ui.row().classes('w-full justify-center'):
        ui.label("Interactive playground for PyTorch Augmentation").classes("text-h4")
    ui.label("Geometric transformations").classes("text-h5")
    ui.label("transforms.RandomResizedCrop(imageSize)").classes("text-h6")
    with ui.column().classes('w-full'):
        ui.html(transformsRandomResizedCrop.description())#.style('background-color: #6E93D6;')
        with ui.row():
            with ui.column().classes('w-1/2'):
                transformsRandomResizedCrop.addSizeParameter(parameterChangeRandomResizedCrop)
                transformsRandomResizedCrop.addScaleParameter(parameterChangeRandomResizedCrop)
                transformsRandomResizedCrop.addRatioParameter(parameterChangeRandomResizedCrop)
                transformsRandomResizedCrop.addInterpolationParameter(parameterChangeRandomResizedCrop)
                transformsRandomResizedCrop.addAntialiasParameter(parameterChangeRandomResizedCrop)
            with ui.column().classes('max-w-lg') as transformsRandomResizedCropPreviewColumn:
                transformsRandomResizedCropPreview = TransformPreview.TransformPreview(12)
    parameterChangeRandomResizedCrop()

    ui.label("transforms.RandomHorizontalFlip()").classes("text-h6")
    with ui.column().classes('w-full'):
        ui.html(transformsRandomHorizontalFlip.description())#.style('background-color: #6E93D6;')
        with ui.row():
            with ui.column().classes('w-1/2'):
                transformsRandomHorizontalFlip.addProbabilityParameter(parameterChangeRandomHorizontalFlip)
                ui.row().classes('w-1/2')
            with ui.column().classes('max-w-lg') as transformsRandomHorizontalFlipColumn:
                transformsRandomHorizontalFlipPreview = TransformPreview.TransformPreview(6)
    parameterChangeRandomHorizontalFlip()

    with ui.row():
        ui.label("transforms.RandomRotation(90)")
    with ui.row():
        ui.label("Geometry combined")
    ui.label("Color transformations").classes("text-h5")
    with ui.row():
        ui.label("transforms.TrivialAugmentWide()")
    with ui.row():
        ui.label("transforms.ColorJitter()")
    with ui.row():
        ui.label("transforms.RandAugment()")

    ui.run()

