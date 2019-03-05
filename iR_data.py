import json

class IRData:
    """
    iRacing object for storing and manipulating iRacing data.
    """

    def __init__(self):
        self.iR_data = {}

        self.initialize_iR_data(self.iR_data)

    def fetch_iR_telemetry_data(self, iR_sdk):
        """
        Fetch the telemetry data from iRacing and build iR_data.

        Return the iR_data as a JSON representation.
        """

        air_temp = iR_sdk['AirTemp']
        fuel_level = iR_sdk['FuelLevel']
        lap = iR_sdk['Lap']
        lap_best_lap_time = iR_sdk['LapBestLapTime']
        lap_completed = iR_sdk['LapCompleted']
        oil_temp = iR_sdk['OilTemp']
        player_car_my_incident_count = iR_sdk['PlayerCarMyIncidentCount']
        race_laps = iR_sdk['RaceLaps']
        session_laps_remain = iR_sdk['SessionLapsRemainEx']
        session_time = iR_sdk['SessionTime']
        track_temp = iR_sdk['TrackTemp']
        water_temp = iR_sdk['WaterTemp']

        if air_temp:
            self.iR_data['AirTemp'] = air_temp

        if fuel_level:
            self.iR_data['FuelLevel'] = fuel_level

        if lap:
            self.iR_data['Lap'] = lap

        if lap_best_lap_time:
            self.iR_data['LapBestLapTime'] = lap_best_lap_time

        if lap_completed:
            self.iR_data['LapCompleted'] = lap_completed

        if oil_temp:
            self.iR_data['OilTemp'] = oil_temp

        if player_car_my_incident_count:
            self.iR_data['PlayerCarMyIncidentCount'] = player_car_my_incident_count

        if race_laps:
            self.iR_data['RaceLaps'] = race_laps

        if session_laps_remain:
            self.iR_data['SessionLapsRemain'] = session_laps_remain

        if session_time:
            self.iR_data['SessionTime'] = session_time

        if track_temp:
            self.iR_data['TrackTemp'] = track_temp

        if water_temp:
            self.iR_data['WaterTemp'] = water_temp

        return json.dumps(self.iR_data)

    def initialize_iR_data(self, iR_data):
        """
        Initialize all iR_data keys to None.
        """

        iR_data['AirTemp'] = None
        iR_data['FuelLevel'] = None
        iR_data['Lap'] = None
        iR_data['LapBestLapTime'] = None
        iR_data['LapCompleted'] = None
        iR_data['OilTemp'] = None
        iR_data['PlayerCarMyIncidentCount'] = None
        iR_data['RaceLaps'] = None
        iR_data['SessionLapsRemainEx'] = None
        iR_data['SessionTime'] = None
        iR_data['TrackTemp'] = None
        iR_data['WaterTemp'] = None
