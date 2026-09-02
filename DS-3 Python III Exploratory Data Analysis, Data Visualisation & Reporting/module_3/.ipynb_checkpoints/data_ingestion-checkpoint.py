
"""
Utility functions for loading data into the analysis pipeline.

This module provides functions to create SQLAlchemy database connections,
execute SQL queries, and load CSV data from web resources into pandas
DataFrames.
"""

import logging
from sqlalchemy import create_engine, text

logger = logging.getLogger("data_ingestion")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def create_db_engine(db_path):
    """
    Create a SQLAlchemy database engine.

    Parameters
    ----------
    db_path : str
        Database connection string.

    Returns
    -------
    sqlalchemy.engine.Engine
        SQLAlchemy database engine.

    Raises
    ------
    Exception
        If the database engine cannot be created.
    """

    try:
        engine = create_engine(db_path)

        with engine.connect():
            pass

        logger.info("Database engine created successfully.")

        return engine

    except Exception as e:
        logger.error(
            f"Failed to create database engine. Error: {e}"
        )
        raise


def query_data(engine, sql_query):
    """
    Execute a SQL query and return the results as a DataFrame.

    Parameters
    ----------
    engine : sqlalchemy.engine.Engine
        SQLAlchemy database engine.

    sql_query : str
        SQL query to execute.

    Returns
    -------
    pandas.DataFrame
        Query results.

    Raises
    ------
    ValueError
        If the query returns an empty DataFrame.

    Exception
        If query execution fails.
    """

    try:

        with engine.connect() as connection:

            df = pd.read_sql_query(
                text(sql_query),
                connection
            )

        if df.empty:
            raise ValueError(
                "The query returned an empty DataFrame."
            )

        logger.info("Query executed successfully.")

        return df

    except Exception as e:

        logger.error(
            f"An error occurred while querying data: {e}"
        )

        raise


def read_from_web_CSV(URL):
    """
    Read a CSV file from a web URL.

    Parameters
    ----------
    URL : str
        URL pointing to the CSV file.

    Returns
    -------
    pandas.DataFrame
        CSV contents as a DataFrame.

    Raises
    ------
    pandas.errors.EmptyDataError
        If the CSV is empty.

    Exception
        If reading the CSV fails.
    """

    try:

        df = pd.read_csv(URL)

        logger.info(
            "CSV file read successfully."
        )

        return df

    except Exception as e:

        logger.error(
            f"Failed to read CSV: {e}"
        )

        raise
