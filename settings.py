import pickle


class Setter:
    def update(self):
        pickle_out = open("saved_settings.settings", "wb")
        pickle.dump(self, pickle_out)
        pickle_out.close()

    def __init__(self, wake_word="alexa", min_volume=10, width_res=300, height_res=200, max_pause=2):
        self._wake_word = wake_word
        self._min_volume = min_volume
        self._width_res = width_res
        self._height_res = height_res
        self._max_pause = max_pause
        self.update()

    def set_wake_word(self, wake_word):
        self._wake_word = wake_word
        self.update()

    def get_wake_word(self):
        return self._wake_word

    def set_min_volume(self, min_volume):
        self._min_volume = min_volume
        self.update()

    def get_min_volume(self):
        return self._min_volume

    def set_width_res(self, width_res):
        self._width_res = width_res
        self.update()

    def get_width_res(self):
        return self._width_res

    def set_height_res(self, height_res):
        self._height_res = height_res
        self.update()

    def get_height_res(self):
        return self._height_res

    def set_max_pause(self, max_pause):
        self._max_pause = max_pause
        self.update()

    def get_max_pause(self):
        return self._max_pause


if __name__ == "__main__":
    from settings import Setter
    s = Setter("ala", 10)
    print(s.get_min_volume())
    print(s.get_max_pause())
