"""
Extract Module
Responsible for extracting data from various sources
"""

import pandas as pd
import requests
import logging
from typing import Dict, Any, Optional
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataExtractor:
    """
    Data Extractor class for pulling data from various sources
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the DataExtractor
        
        Args:
            config: Configuration dictionary for the extractor
        """
        self.config = config or {}
        logger.info("DataExtractor initialized")
    
    def extract_from_csv(self, file_path: str) -> pd.DataFrame:
        """
        Extract data from a CSV file
        
        Args:
            file_path: Path to the CSV file
            
        Returns:
            DataFrame containing the extracted data
        """
        try:
            logger.info(f"Extracting data from CSV: {file_path}")
            df = pd.read_csv(file_path)
            logger.info(f"Successfully extracted {len(df)} rows from CSV")
            return df
        except Exception as e:
            logger.error(f"Error extracting data from CSV: {e}")
            raise
    
    def extract_from_api(self, url: str, params: Optional[Dict] = None) -> Dict:
        """
        Extract data from an API endpoint
        
        Args:
            url: API endpoint URL
            params: Optional parameters for the request
            
        Returns:
            Dictionary containing the API response
        """
        try:
            logger.info(f"Extracting data from API: {url}")
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            logger.info("Successfully extracted data from API")
            return data
        except Exception as e:
            logger.error(f"Error extracting data from API: {e}")
            raise
    
    def extract_from_json(self, file_path: str) -> Dict:
        """
        Extract data from a JSON file
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            Dictionary containing the extracted data
        """
        try:
            logger.info(f"Extracting data from JSON: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as f:
                import json
                data = json.load(f)
            logger.info("Successfully extracted data from JSON")
            return data
        except Exception as e:
            logger.error(f"Error extracting data from JSON: {e}")
            raise
    
    def save_raw_data(self, data: pd.DataFrame, filename: str, output_dir: str = "data/raw") -> str:
        """
        Save raw extracted data to disk
        
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
            logger.info(f"Raw data saved to: {output_path}")
            return output_path
        except Exception as e:
            logger.error(f"Error saving raw data: {e}")
            raise


if __name__ == "__main__":
    # Example usage
    extractor = DataExtractor()
    logger.info("DataExtractor module ready")
