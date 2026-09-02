import pandas as pd

from data_ingestion import create_db_engine, query_data


class FieldDataProcessor:
    """
    Processes agricultural field data by loading data from a SQL database,
    cleaning inconsistencies, and merging weather station information.

    Parameters
    ----------
    config_params : dict
        Configuration dictionary containing:
        
        - sql_query : str
            SQL query used to extract field data.
        - db_path : str
            Database connection path.
        - columns_to_rename : dict
            Dictionary used to correct swapped column names.
        - values_to_rename : dict
            Dictionary used to correct incorrect crop type values.
        - weather_csv_path : str
            Path to weather station data CSV file.
        - weather_mapping_csv : str
            Path to field-weather station mapping CSV file.

    Attributes
    ----------
    df : pandas.DataFrame
        Processed agricultural dataset after all cleaning and merging steps.
    """

    def __init__(self, config_params):
        """
        Initialize the FieldDataProcessor.

        Parameters
        ----------
        config_params : dict
            Configuration parameters required for processing.
        """

        self.config_params = config_params
        self.df = None


    def ingest_sql_data(self):
        """
        Load agricultural field data from the SQL database.

        Returns
        -------
        pandas.DataFrame
            Raw field data loaded from the database.
        """

        engine = create_db_engine(
            self.config_params["db_path"]
        )

        self.df = query_data(
            engine,
            self.config_params["sql_query"]
        )

        return self.df


    def rename_columns(self):
        """
        Correct swapped column names in the dataset.

        Returns
        -------
        pandas.DataFrame
            Dataset with corrected column names.
        """

        self.df.rename(
            columns={
                "Annual_yield": "Crop_type_Temp",
                "Crop_type": "Annual_yield",
            },
            inplace=True
        )

        self.df.rename(
            columns={
                "Crop_type_Temp": "Crop_type",
            },
            inplace=True
        )

        return self.df


    def apply_corrections(self):
        """
        Correct crop type spelling errors.

        Returns
        -------
        pandas.DataFrame
            Dataset with corrected crop types.
        """

        print("Columns before correction:")
        print(self.df.columns.tolist())

        self.df["Crop_type"] = self.df["Crop_type"].replace(
            self.config_params["values_to_rename"]
        )

        return self.df


    def merge_weather_data(self):
        """
        Merge weather station measurements with field data.

        Returns
        -------
        pandas.DataFrame
            Dataset containing field and weather information.
        """

        weather_df = pd.read_csv(
            self.config_params["weather_csv_path"]
        )

        mapping_df = pd.read_csv(
            self.config_params["weather_mapping_csv"]
        )

        self.df = self.df.merge(
            mapping_df,
            on="Field_ID",
            how="left"
        )

        self.df = self.df.merge(
            weather_df,
            on="Station",
            how="left"
        )

        return self.df


    def process(self):
        """
        Run the complete field data processing pipeline.

        The pipeline performs:

        1. Loading data from SQL.
        2. Correcting swapped column names.
        3. Fixing crop type spelling errors.
        4. Merging weather station information.

        Returns
        -------
        pandas.DataFrame
            Fully processed field dataset.
        """

        self.ingest_sql_data()
        self.rename_columns()
        self.apply_corrections()
        self.merge_weather_data()

        return self.df