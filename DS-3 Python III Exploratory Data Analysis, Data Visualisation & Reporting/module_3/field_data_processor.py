import pandas as pd

from data_ingestion import create_db_engine, query_data


class FieldDataProcessor:
    """
    Processes agricultural field data by loading data from a SQL database,
    cleaning inconsistencies, and merging weather station information.

    Parameters
    ----------
    config_params : dict
        Configuration dictionary containing SQL queries, database paths,
        column correction mappings, crop value corrections, and weather
        mapping file paths.

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
        Correct incorrect crop type spelling values.

        Returns
        -------
        pandas.DataFrame
            Dataset with corrected crop types.
        """

        self.df["Crop_type"] = self.df["Crop_type"].replace(
            self.config_params["values_to_rename"]
        )

        return self.df


    def merge_weather_data(self):
        """
        Merge weather station mapping information with field data.

        Returns
        -------
        pandas.DataFrame
            Dataset containing field data linked to weather stations.
        """

        mapping_df = pd.read_csv(
            self.config_params["weather_mapping_csv"]
        )

        mapping_df = mapping_df.drop(
            columns=["Unnamed: 0"],
            errors="ignore"
        )

        self.df = self.df.merge(
            mapping_df,
            on="Field_ID",
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
        4. Merging weather station mapping.

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