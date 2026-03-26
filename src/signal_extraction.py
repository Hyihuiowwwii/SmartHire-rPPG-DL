import numpy as np


class SignalExtractor:
    def __init__(self):
        self.green_signal = []

    def extract_mean_rgb(self, roi):
        if roi is None or roi.size == 0:
            return None

        mean_b = np.mean(roi[:, :, 0])
        mean_g = np.mean(roi[:, :, 1])
        mean_r = np.mean(roi[:, :, 2])

        return mean_r, mean_g, mean_b

    def update_green_signal(self, roi):
        rgb_values = self.extract_mean_rgb(roi)

        if rgb_values is None:
            return None

        _, mean_g, _ = rgb_values
        self.green_signal.append(mean_g)

        if len(self.green_signal) > 300:
            self.green_signal.pop(0)

        return mean_g

    def get_signal(self):
        return self.green_signal
