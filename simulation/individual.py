class Individual:
    _ind_id = 0

    def __init__(self, is_robot=False):
        self._is_robot = is_robot
        self._id = Individual._ind_id
        Individual._ind_id += 1
        self._position = None
        self._velocity = None

    def get_id(self):
        return self._id

    def get_position(self):
        return self._position

    def get_velocity(self):
        return self._velocity

    def is_robot(self):
        return self._is_robot

    def run(self, simu):
        self.interact(simu)
        self.move(simu)

    def interact(self, simu):
        assert False, 'You need to implement this function in a subclass'

    def move(self, simu):
        assert False, 'You need to implement this function in a subclass'
