from torchvision import transforms
from nicegui import ui
from nicegui.events import MouseEventArguments

class TransformsRandomHorizontalFlip:
    def __init__(self):
        self.randomHorizontalFlipProbability = None

    def getTransform(self):
        return transforms.RandomHorizontalFlip(self.randomHorizontalFlipProbability.value)
    
    def description(self):
        return """
<div>
<strong>class torchvision.transforms.RandomHorizontalFlip(p=0.5)</strong>
<br>
Horizontally flip the given image randomly with a given probability. If the image is torch Tensor, it is expected to have […, H, W] shape, where … means an arbitrary number of leading dimensions

See <a href="https://pytorch.org/vision/stable/generated/torchvision.transforms.RandomHorizontalFlip.html#torchvision.transforms.RandomHorizontalFlip" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">PyTorch documentation for torchvision.transforms.RandomResizedCrop</a>.
</div>
"""

    def addProbabilityParameter(self, parameterChangeHorizontalFlip):
        with ui.column().classes(''):
            ui.html('''
<strong>p (float)</strong> – 
<br>
the probability of the image being flipped. Default value is 0.5.
<div style="color:#FFFFFF">
I need this hidden next, otherwise the layout breaks aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaa
</div>
''')
            with ui.row():
                self.randomHorizontalFlipProbability = ui.number(label='probability', format='%.2f', value=0.5, min=0, max=1, step=0.01,
                    on_change=lambda e: parameterChangeHorizontalFlip(),
                    validation={'Input too large': lambda value: value <= 1,
                                'Input too small': lambda value: value >= 0} ).classes('w-46')
