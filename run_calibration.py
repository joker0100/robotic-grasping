#!/usr/bin/env python
import numpy as np

from hardware.calibrate_camera import Calibration

if __name__ == '__main__':
    calibration = Calibration(
        cam_id=912112074213,
        calib_grid_step=0.05,
        # checkerboard_offset_from_tool=[0.0, 0.0215, 0.0115],
        checkerboard_offset_from_tool=[0.0, 0.0, 0.0],
        # workspace_limits=np.asarray([[0.3, 0.45], [-0.05, 0.05], [0.1, 0.2]])
        workspace_limits=np.asarray([[0.3, 0.4], [-0.15, -0.05], [0.1, 0.2]])
    )
     
    calibration.run()
