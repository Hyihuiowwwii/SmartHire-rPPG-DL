import numpy as np


class BPMEstimator:
    def __init__(self, fps=30):
        self.fps = fps

    def estimate_bpm(self, signal):
        if signal is None or len(signal) < 60:
            return 0

        signal = np.array(signal)
        signal = signal - np.mean(signal)

        fft_values = np.fft.rfft(signal)
        fft_freqs = np.fft.rfftfreq(len(signal), d=1.0 / self.fps)

        valid_idx = np.where((fft_freqs >= 0.75) & (fft_freqs <= 3.0))[0]

        if len(valid_idx) == 0:
            return 0

        fft_values = np.abs(fft_values[valid_idx])
        fft_freqs = fft_freqs[valid_idx]

        peak_freq = fft_freqs[np.argmax(fft_values)]
        bpm = peak_freq * 60.0

        return round(bpm, 1)
