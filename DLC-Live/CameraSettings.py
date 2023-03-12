# Suport: https://github.com/DeepLabCut/DeepLabCut-live-GUI/blob/master/docs/camera_support.md
from dlclivegui import Camera

class MyNewCamera(Camera):

    def __init__(self, id="", resolution=[640, 480], exposure=0, crop=None, display_resize=1):
        super().__init__(id,
                         resolution=resolution,
                         exposure=exposure,
                         crop=crop,
                         use_tk_display=True,
                         display_resize=display_resize)
@static_method
def arg_restrictions():
    return {'use_tk_display' : [True, False],
            'resolution' : [[640, 480], [320, 240]]}