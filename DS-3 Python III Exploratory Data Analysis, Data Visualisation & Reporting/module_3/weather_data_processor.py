"""
Weather data processing module.

This module loads IoT weather sensor data and extracts
structured measurements from weather messages.
"""

from data_ingestion import read_from_web_CSV


class WeatherDataProcessor:
    """
    Processes weather station IoT sensor data by loading raw messages
    and extracting structured measurements.

    Parameters
    ----------
    config_params : dict
        Configuration dictionary containing the weather CSV path.

    Attributes
    ----------
    df : pandas.DataFrame or None
        Processed weather dataset containing extracted measurements.
    """

    def __init__(self, config_params):
        """
        Initialize the weather data processor.

        Parameters
        ----------
        config_params : dict
            Configuration parameters required for weather processing.
        """

        self.config_params = config_params
        self.df = None


    def ingest_weather_data(self):
        """
        Load raw weather CSV data.

        Returns
        -------
        None
            Stores the raw weather DataFrame in self.df.
        """

        self.df = read_from_web_CSV(
            self.config_params["weather_csv_path"]
        )


    def process(self):
        """
        Process raw weather messages into structured measurements.
    
        Returns
        -------
        pandas.DataFrame
            Processed weather data containing
            Weather_station_ID, Message, Measurement, and Value.
        """
    
        self.ingest_weather_data()
    
        def extract_measurement(message):
            message_lower = message.lower()
    
            if (
                "temp" in message_lower
                or "temperature" in message_lower
                or "温度" in message
            ):
                return "Temperature"
    
            elif "rain" in message_lower:
                return "Rainfall"
    
            elif (
                "pollution" in message_lower
                or "air quality" in message_lower
                or "index" in message_lower
            ):
                return "Pollution_level"
    
            return None
    
    
        self.df["Measurement"] = (
            self.df["Message"]
            .apply(extract_measurement)
        )
    
    
        self.df["Value"] = (
            self.df["Message"]
            .str.extract(
                r"([-+]?\d+\.\d+)",
                expand=False
            )
            .astype(float)
        )
    
    
        return self.df[
            [
                "Weather_station_ID",
                "Message",
                "Measurement",
                "Value"
            ]
        ]