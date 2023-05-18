from torchvision import transforms
from nicegui import ui
from nicegui.events import MouseEventArguments

class TransformsRandomResizedCrop:
    def __init__(self):
        self.randomResizeScaleWidth = None
        self.randomResizeScaleHeight = None
        self.randomResizeScaleLower = None
        self.randomResizeScaleUpper = None
        self.randomResizeRatioLower = None
        self.randomResizeRatioUpper = None

    def getTransform(self):
        return transforms.RandomResizedCrop(
            (self.randomResizeScaleHeight.value, self.randomResizeScaleWidth.value), 
            scale=(self.randomResizeScaleLower.value, 
                self.randomResizeScaleUpper.value),
            ratio=(self.randomResizeRatioLower.value, 
                self.randomResizeRatioUpper.value) )
    
    def description(self):
        return """
<div>
<strong>class torchvision.transforms.RandomResizedCrop(size, scale, ratio, interpolation, antialias: Optional)</strong>
<br>
Crop a random portion of image and resize it to a given size.
<br>
If the image is torch Tensor, it is expected to have […, H, W] shape, where … means an arbitrary number of leading dimensions
<br>
A crop of the original image is made: the crop has a random area (H * W) and a random aspect ratio. This crop is finally resized to the given size. This is popularly used to train the Inception networks.

See <a href="https://pytorch.org/vision/stable/generated/torchvision.transforms.RandomResizedCrop.html#torchvision.transforms.RandomResizedCrop" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">PyTorch documentation for torchvision.transforms.RandomResizedCrop</a>.
</div>
"""

    def addSizeParameter(self, parameterChangeRandomResizedCrop):
        with ui.column().classes(''):
            ui.html('''
<strong>size (int or sequence)</strong> –
<br>
expected output size of the crop, for each edge. If size is an int instead of 
sequence like (h, w), a square output size (size, size) is made. If provided a 
sequence of length 1, it will be interpreted as (size[0], size[0]).
<br>
<strong>Fixed. This parameter is determined by the model input.</strong>
''')
            with ui.row():
                self.randomResizeScaleWidth = ui.number(label='Width', format='%i', value=160, min=160, max=160, step=1,
                    on_change=lambda e: parameterChangeRandomResizedCrop(),
                    validation={'Input too large': lambda value: value <= 160,
                                'Input too small': lambda value: value >= 160}).classes('w-46')
                self.randomResizeScaleHeight = ui.number(label='height', format='%i', value=116, min=116, max=116, step=1,
                    on_change=lambda e: parameterChangeRandomResizedCrop(),
                    validation={'Input too large': lambda value: value <= 116,
                                'Input too small': lambda value: value >= 116}).classes('w-46')
            self.randomResizeScaleWidth.disable()
            self.randomResizeScaleHeight.disable()

    def addScaleParameter(self, parameterChangeRandomResizedCrop):
        with ui.column().classes(''):
            ui.html('''
<strong>scale (tuple of python:float)</strong> – 
<br>
Specifies the lower and upper bounds for the random area of the crop, before 
resizing. The scale is defined with respect to the area of the original image.
''')
            with ui.row():
                self.randomResizeScaleLower = ui.number(label='scale lower', format='%.2f', value=0.08, min=0, max=1, step=0.01,
                    on_change=lambda e: parameterChangeRandomResizedCrop(),
                    validation={'Input too large': lambda value: value <= 1,
                                'Input too small': lambda value: value >= 0} ).classes('w-46')
                self.randomResizeScaleUpper = ui.number(label='scale upper', format='%.2f', value=1.0, min=0, max=1, step=0.01,
                    on_change=lambda e: parameterChangeRandomResizedCrop(),
                    validation={'Input too large': lambda value: value <= 1,
                                'Input too small': lambda value: value >= 0} ).classes('w-46')

    def addRatioParameter(self, parameterChangeRandomResizedCrop):
        with ui.column().classes(''):
            ui.html('''
<strong>ratio (tuple of python:float)</strong> – 
<br>
Specifies the lower and upper bounds for the random aspect ratio of the crop, before resizing.
''')
            with ui.row():
                self.randomResizeRatioLower = ui.number(label='ratio lower', format='%.2f', value=0.75, min=0.5, max=1.5, step=0.01,
                    on_change=lambda e: parameterChangeRandomResizedCrop(),
                    validation={'Input too large': lambda value: value <= 1.5,
                                'Input too small': lambda value: value >= 0.5} ).classes('w-46')
                self.randomResizeRatioUpper = ui.number(label='ratio upper', format='%.2f', value=1.3333, min=0.5, max=1.5, step=0.01,
                    on_change=lambda e: parameterChangeRandomResizedCrop(),
                    validation={'Input too large': lambda value: value <= 1.5,
                                'Input too small': lambda value: value >= 0.5} ).classes('w-46')

    def addInterpolationParameter(self, parameterChangeRandomResizedCrop):
        with ui.column().classes(''):
            ui.html('''
<strong>interpolation (InterpolationMode)</strong> – 
<br>
Desired interpolation enum defined by torchvision.transforms.InterpolationMode. Default is 
InterpolationMode.BILINEAR. If input is Tensor, only InterpolationMode.NEAREST, 
InterpolationMode.NEAREST_EXACT, InterpolationMode.BILINEAR and 
InterpolationMode.BICUBIC are supported. The corresponding Pillow integer 
constants, e.g. PIL.Image.BILINEAR are accepted as well.
<br>
<strong>Fixed to sensible default InterpolationMode.BILINEAR</strong>
''')
            ui.number(label='Parameter 1', format='%i', value=50, min=0, max=100, step=1,
                on_change=lambda e: parameterChangeRandomResizedCrop(),
                validation={'Input too large': lambda value: value <= 100,
                            'Input too small': lambda value: value >= 0}).classes('w-46').set_visibility(False)

    def addAntialiasParameter(self, parameterChangeRandomResizedCrop):
        with ui.column().classes('w-94'):
            ui.html('''
<strong>antialias (bool, optional)</strong> – 
<br>
Whether to apply antialiasing. It only affects tensors with bilinear or bicubic modes and it is ignored otherwise: on PIL 
images, antialiasing is always applied on bilinear or bicubic modes; on other modes 
(for PIL images and tensors), antialiasing makes no sense and this parameter is 
ignored
<br>
<strong>Fixed to default warn</strong>
''')
            ui.number(label='Parameter 1', format='%i', value=50, min=0, max=100, step=1,
                on_change=lambda e: parameterChangeRandomResizedCrop(),
                validation={'Input too large': lambda value: value <= 100,
                            'Input too small': lambda value: value >= 0}).classes('w-46').set_visibility(False)




