"""
ETL Pipeline Orchestrator
Main pipeline that orchestrates the Extract, Transform, Load process
"""

import logging
from typing import Dict, Any, Optional
import yaml
import os
import sys
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.extract.extractor import DataExtractor
from src.transform.transformer import DataTransformer
from src.load.loader import DataLoader

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ETLPipeline:
    """
    ETL Pipeline orchestrator that manages the entire data pipeline
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the ETL Pipeline
        
        Args:
            config_path: Path to the configuration file
        """
        self.config = self._load_config(config_path) if config_path else {}
        self.extractor = DataExtractor(self.config.get('extract', {}))
        self.transformer = DataTransformer(self.config.get('transform', {}))
        self.loader = DataLoader(self.config.get('load', {}))
        logger.info("ETL Pipeline initialized")
    
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """
        Load configuration from YAML file
        
        Args:
            config_path: Path to the configuration file
            
        Returns:
            Configuration dictionary
        """
        try:
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            logger.info(f"Configuration loaded from {config_path}")
            return config
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            raise
    
    def run_pipeline(self, source_path: str, output_path: str, 
                     transform_config: Optional[Dict] = None) -> None:
        """
        Run the complete ETL pipeline
        
        Args:
            source_path: Path to the source data
            output_path: Path to save the output
            transform_config: Optional transformation configuration
        """
        try:
            start_time = datetime.now()
            logger.info("=" * 50)
            logger.info("Starting ETL Pipeline")
            logger.info("=" * 50)
            
            # Extract
            logger.info("Step 1: Extracting data")
            df = self.extractor.extract_from_csv(source_path)
            logger.info(f"Extracted {len(df)} rows, {len(df.columns)} columns")
            
            # Transform
            logger.info("Step 2: Transforming data")
            df = self.transformer.remove_duplicates(df)
            
            if transform_config:
                if 'missing_values' in transform_config:
                    df = self.transformer.handle_missing_values(
                        df, 
                        strategy=transform_config['missing_values'].get('strategy', 'drop'),
                        fill_value=transform_config['missing_values'].get('fill_value')
                    )
            
            logger.info(f"Transformation complete: {len(df)} rows remaining")
            
            # Load
            logger.info("Step 3: Loading data")
            self.loader.load_to_csv(df, output_path)
            
            # Pipeline complete
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            logger.info("=" * 50)
            logger.info(f"ETL Pipeline completed successfully in {duration:.2f} seconds")
            logger.info(f"Output saved to: {output_path}")
            logger.info("=" * 50)
            
        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            raise
    
    def get_pipeline_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the pipeline
        
        Returns:
            Dictionary containing pipeline statistics
        """
        stats = {
            'extractor': 'DataExtractor',
            'transformer': 'DataTransformer',
            'loader': 'DataLoader',
            'config': self.config
        }
        return stats


def main():
    """
    Main function to run the ETL pipeline
    """
    # Example pipeline execution
    pipeline = ETLPipeline()
    
    # Example: Process a sample dataset
    source_file = "data/raw/sample_data.csv"
    output_file = "data/processed/processed_data.csv"
    
    if os.path.exists(source_file):
        transform_config = {
            'missing_values': {
                'strategy': 'drop'
            }
        }
        
        pipeline.run_pipeline(source_file, output_file, transform_config)
    else:
        logger.warning(f"Source file not found: {source_file}")
        logger.info("Pipeline is ready to process data when source file is available")


if __name__ == "__main__":
    main()
