class Individual:
    def __init__(self, id, is_robot=False):
        self._is_robot = is_robot
        self._id = id
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

    def interact(self):
        assert False, 'You need to implement this function in a subclass'

    def move(self):
        assert False, 'You need to implement this function in a subclass'
