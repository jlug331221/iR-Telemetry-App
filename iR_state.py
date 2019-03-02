class iR_state:
    """
    iRacing state data
    """

    def __init__(self):
        self.iR_connected = False
        self.last_car_setup_tick = -1

    def set_iR_connected(self, iR_connected_val):
        self.iR_connected = iR_connected_val

    def set_last_car_setup_tick(self, last_car_setup_tick_val):
        self.last_car_setup_tick = last_car_setup_tick_val
        