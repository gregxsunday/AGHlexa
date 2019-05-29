import pickle


class Setter:
    def update(self):
        pickle_out = open("saved_settings.settings", "wb")
        pickle.dump(self, pickle_out)
        pickle_out.close()

    def __init__(self, wake_word="alexa", min_volume=10, width_res=300, height_res=200):
        self._wake_word = wake_word
        self._min_volume = min_volume
        self._width_res = width_res
        self._height_res = height_res
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


if __name__ == "__main__":
    s = Setter("ala", 29)
    print(s.get_min_volume())
