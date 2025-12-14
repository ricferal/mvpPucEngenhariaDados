"""
Transform Module
Responsible for transforming and cleaning data
"""

import pandas as pd
import numpy as np
import logging
import os
from typing import Dict, List, Any, Optional, Callable

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataTransformer:
    """
    Data Transformer class for cleaning and transforming data
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the DataTransformer
        
        Args:
            config: Configuration dictionary for the transformer
        """
        self.config = config or {}
        logger.info("DataTransformer initialized")
    
    def remove_duplicates(self, df: pd.DataFrame, subset: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Remove duplicate rows from DataFrame
        
        Args:
            df: Input DataFrame
            subset: Column names to consider for identifying duplicates
            
        Returns:
            DataFrame with duplicates removed
        """
        try:
            initial_count = len(df)
            df_clean = df.drop_duplicates(subset=subset)
            removed_count = initial_count - len(df_clean)
            logger.info(f"Removed {removed_count} duplicate rows")
            return df_clean
        except Exception as e:
            logger.error(f"Error removing duplicates: {e}")
            raise
    
    def handle_missing_values(self, df: pd.DataFrame, strategy: str = 'drop', 
                             fill_value: Any = None) -> pd.DataFrame:
        """
        Handle missing values in DataFrame
        
        Args:
            df: Input DataFrame
            strategy: Strategy for handling missing values ('drop', 'fill', 'ffill', 'bfill')
            fill_value: Value to use when strategy is 'fill'
            
        Returns:
            DataFrame with missing values handled
        """
        try:
            missing_count = df.isnull().sum().sum()
            logger.info(f"Found {missing_count} missing values")
            
            if strategy == 'drop':
                df_clean = df.dropna()
            elif strategy == 'fill':
                df_clean = df.fillna(fill_value)
            elif strategy == 'ffill':
                df_clean = df.ffill()
            elif strategy == 'bfill':
                df_clean = df.bfill()
            else:
                raise ValueError(f"Unknown strategy: {strategy}")
            
            logger.info(f"Missing values handled using strategy: {strategy}")
            return df_clean
        except Exception as e:
            logger.error(f"Error handling missing values: {e}")
            raise
    
    def normalize_columns(self, df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        Normalize numerical columns to 0-1 range
        
        Args:
            df: Input DataFrame
            columns: List of column names to normalize
            
        Returns:
            DataFrame with normalized columns
        """
        try:
            df_normalized = df.copy()
            for col in columns:
                if col in df.columns:
                    min_val = df[col].min()
                    max_val = df[col].max()
                    if max_val != min_val:
                        df_normalized[col] = (df[col] - min_val) / (max_val - min_val)
                    logger.info(f"Normalized column: {col}")
            return df_normalized
        except Exception as e:
            logger.error(f"Error normalizing columns: {e}")
            raise
    
    def filter_data(self, df: pd.DataFrame, condition: Callable) -> pd.DataFrame:
        """
        Filter data based on a condition
        
        Args:
            df: Input DataFrame
            condition: Callable that returns a boolean mask
            
        Returns:
            Filtered DataFrame
        """
        try:
            df_filtered = df[condition(df)]
            logger.info(f"Filtered data: {len(df_filtered)} rows remaining from {len(df)}")
            return df_filtered
        except Exception as e:
            logger.error(f"Error filtering data: {e}")
            raise
    
    def convert_types(self, df: pd.DataFrame, type_mapping: Dict[str, str]) -> pd.DataFrame:
        """
        Convert column data types
        
        Args:
            df: Input DataFrame
            type_mapping: Dictionary mapping column names to desired types
            
        Returns:
            DataFrame with converted types
        """
        try:
            df_converted = df.copy()
            for col, dtype in type_mapping.items():
                if col in df.columns:
                    df_converted[col] = df_converted[col].astype(dtype)
                    logger.info(f"Converted column {col} to {dtype}")
            return df_converted
        except Exception as e:
            logger.error(f"Error converting types: {e}")
            raise
    
    def aggregate_data(self, df: pd.DataFrame, group_by: List[str], 
                      agg_functions: Dict[str, str]) -> pd.DataFrame:
        """
        Aggregate data by grouping
        
        Args:
            df: Input DataFrame
            group_by: List of columns to group by
            agg_functions: Dictionary mapping column names to aggregation functions
            
        Returns:
            Aggregated DataFrame
        """
        try:
            df_agg = df.groupby(group_by).agg(agg_functions).reset_index()
            logger.info(f"Aggregated data: {len(df_agg)} groups created")
            return df_agg
        except Exception as e:
            logger.error(f"Error aggregating data: {e}")
            raise
    
    def save_transformed_data(self, data: pd.DataFrame, filename: str, 
                             output_dir: str = "data/processed") -> str:
        """
        Save transformed data to disk
        
        Args:
            data: DataFrame to save
            filename: Name of the output file
            output_dir: Directory to save the file
            
        Returns:
            Path to the saved file
        """
        try:
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, filename)
            data.to_csv(output_path, index=False)
            logger.info(f"Transformed data saved to: {output_path}")
            return output_path
        except Exception as e:
            logger.error(f"Error saving transformed data: {e}")
            raise


if __name__ == "__main__":
    # Example usage
    transformer = DataTransformer()
    logger.info("DataTransformer module ready")
