"""
Load Module
Responsible for loading data into target destinations
"""

import pandas as pd
from sqlalchemy import create_engine, text
import logging
from typing import Dict, Any, Optional
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataLoader:
    """
    Data Loader class for loading data into various destinations
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the DataLoader
        
        Args:
            config: Configuration dictionary for the loader
        """
        self.config = config or {}
        self.engine = None
        logger.info("DataLoader initialized")
    
    def connect_database(self, connection_string: str) -> None:
        """
        Connect to a database
        
        Args:
            connection_string: SQLAlchemy connection string
        """
        try:
            self.engine = create_engine(connection_string)
            logger.info("Database connection established")
        except Exception as e:
            logger.error(f"Error connecting to database: {e}")
            raise
    
    def load_to_csv(self, df: pd.DataFrame, file_path: str, mode: str = 'w') -> str:
        """
        Load data to a CSV file
        
        Args:
            df: DataFrame to load
            file_path: Path to the output CSV file
            mode: Write mode ('w' for write, 'a' for append)
            
        Returns:
            Path to the saved file
        """
        try:
            logger.info(f"Loading data to CSV: {file_path}")
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            if mode == 'a' and os.path.exists(file_path):
                df.to_csv(file_path, mode='a', header=False, index=False)
            else:
                df.to_csv(file_path, mode='w', index=False)
            
            logger.info(f"Successfully loaded {len(df)} rows to CSV")
            return file_path
        except Exception as e:
            logger.error(f"Error loading data to CSV: {e}")
            raise
    
    def load_to_database(self, df: pd.DataFrame, table_name: str, 
                         if_exists: str = 'replace') -> None:
        """
        Load data to a database table
        
        Args:
            df: DataFrame to load
            table_name: Name of the target table
            if_exists: How to behave if table exists ('fail', 'replace', 'append')
        """
        try:
            if self.engine is None:
                raise ValueError("Database connection not established. Call connect_database first.")
            
            logger.info(f"Loading data to database table: {table_name}")
            df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)
            logger.info(f"Successfully loaded {len(df)} rows to {table_name}")
        except Exception as e:
            logger.error(f"Error loading data to database: {e}")
            raise
    
    def load_to_json(self, df: pd.DataFrame, file_path: str, orient: str = 'records') -> str:
        """
        Load data to a JSON file
        
        Args:
            df: DataFrame to load
            file_path: Path to the output JSON file
            orient: Format of the JSON ('records', 'index', 'columns', etc.)
            
        Returns:
            Path to the saved file
        """
        try:
            logger.info(f"Loading data to JSON: {file_path}")
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            df.to_json(file_path, orient=orient, indent=2)
            logger.info(f"Successfully loaded {len(df)} rows to JSON")
            return file_path
        except Exception as e:
            logger.error(f"Error loading data to JSON: {e}")
            raise
    
    def execute_query(self, query: str) -> pd.DataFrame:
        """
        Execute a SQL query and return results
        
        Args:
            query: SQL query to execute
            
        Returns:
            DataFrame containing query results
        """
        try:
            if self.engine is None:
                raise ValueError("Database connection not established. Call connect_database first.")
            
            logger.info("Executing SQL query")
            with self.engine.connect() as conn:
                result = pd.read_sql(text(query), conn)
            logger.info(f"Query executed successfully, returned {len(result)} rows")
            return result
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            raise
    
    def load_to_parquet(self, df: pd.DataFrame, file_path: str) -> str:
        """
        Load data to a Parquet file
        
        Args:
            df: DataFrame to load
            file_path: Path to the output Parquet file
            
        Returns:
            Path to the saved file
        """
        try:
            logger.info(f"Loading data to Parquet: {file_path}")
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            df.to_parquet(file_path, index=False)
            logger.info(f"Successfully loaded {len(df)} rows to Parquet")
            return file_path
        except Exception as e:
            logger.error(f"Error loading data to Parquet: {e}")
            raise
    
    def close_connection(self) -> None:
        """
        Close database connection
        """
        try:
            if self.engine is not None:
                self.engine.dispose()
                logger.info("Database connection closed")
        except Exception as e:
            logger.error(f"Error closing database connection: {e}")
            raise


if __name__ == "__main__":
    # Example usage
    loader = DataLoader()
    logger.info("DataLoader module ready")
