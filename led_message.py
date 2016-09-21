#!/usr/bin/python3
class LedStateMessage:

    def __init__(self, sense_hat, rotation=0):
        self.sense = sense_hat
        self.rotation = rotation
        pass

    def _show_pixel_message(self, pixels):
        self.sense.set_pixels(pixels)
        self.sense.set_rotation(self.rotation)
        pass

    def _get_blank_pixels(self):
        O = (0, 0, 0)

        blank_pixles = [
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
        ]

        return blank_pixles;

    def _get_ok_pixels(self):
        X = (0, 80, 0)
        O = (0, 0, 0)

        ok_pixles = [
            X, X, X, X, X, X, X, X,
            X, O, O, O, O, O, O, X,
            X, O, O, O, O, O, X, X,
            X, O, O, O, O, X, O, X,
            X, O, O, O, X, O, O, X,
            X, X, O, X, O, O, O, X,
            X, O, X, O, O, O, O, X,
            X, X, X, X, X, X, X, X
        ]

        return ok_pixles;

    def _get_warning_pixels(self):
        X = (100, 50, 0)
        O = (0, 0, 0)

        warning_pixles = [
            X, X, X, X, X, X, X, X,
            X, O, O, X, X, O, O, X,
            X, O, O, X, X, O, O, X,
            X, O, O, X, X, O, O, X,
            X, O, O, O, O, O, O, X,
            X, O, O, X, X, O, O, X,
            X, O, O, O, O, O, O, X,
            X, X, X, X, X, X, X, X
        ]

        return warning_pixles;

    def _get_error_pixels(self):
        X = (80, 0, 0)
        O = (0, 0, 0)

        error_pixles = [
            X, X, X, X, X, X, X, X,
            X, X, O, O, O, O, X, X,
            X, O, X, O, O, X, O, X,
            X, O, O, X, X, O, O, X,
            X, O, O, X, X, O, O, X,
            X, O, X, O, O, X, O, X,
            X, X, O, O, O, O, X, X,
            X, X, X, X, X, X, X, X
        ]

        return error_pixles;
    
    def clear(self):
        self._show_pixel_message(self._get_blank_pixels())
        pass

    def show_ok_message(self):
        self._show_pixel_message(self._get_ok_pixels())
        pass

    def show_warning_message(self):
        self._show_pixel_message(self._get_warning_pixels())
        pass

    def show_error_message(self):
        self._show_pixel_message(self._get_error_pixels())
        pass
