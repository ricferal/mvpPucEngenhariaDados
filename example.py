#!/usr/bin/env python
"""
Example script demonstrating the ETL pipeline usage
"""

import os
import sys

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.extract.extractor import DataExtractor
from src.transform.transformer import DataTransformer
from src.load.loader import DataLoader
from src.pipeline import ETLPipeline
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def example_individual_modules():
    """
    Example using individual modules
    """
    logger.info("=" * 60)
    logger.info("Example 1: Using Individual Modules")
    logger.info("=" * 60)
    
    # Check if sample data exists
    source_file = "data/raw/sample_data.csv"
    if not os.path.exists(source_file):
        logger.error(f"Sample data not found. Please run: python src/generate_sample_data.py")
        return
    
    # Extract
    extractor = DataExtractor()
    df = extractor.extract_from_csv(source_file)
    logger.info(f"Extracted: {len(df)} rows, {len(df.columns)} columns")
    
    # Transform
    transformer = DataTransformer()
    
    # Remove duplicates
    df = transformer.remove_duplicates(df)
    
    # Handle missing values
    df = transformer.handle_missing_values(df, strategy='drop')
    
    logger.info(f"After transformation: {len(df)} rows")
    
    # Load
    loader = DataLoader()
    output_file = "data/processed/example_output.csv"
    loader.load_to_csv(df, output_file)
    
    # Also save as JSON
    json_file = "data/processed/example_output.json"
    loader.load_to_json(df, json_file)
    
    logger.info("Individual modules example completed successfully!")


def example_pipeline():
    """
    Example using the complete pipeline
    """
    logger.info("=" * 60)
    logger.info("Example 2: Using Complete Pipeline")
    logger.info("=" * 60)
    
    # Check if sample data exists
    source_file = "data/raw/sample_data.csv"
    if not os.path.exists(source_file):
        logger.error(f"Sample data not found. Please run: python src/generate_sample_data.py")
        return
    
    # Initialize pipeline
    pipeline = ETLPipeline()
    
    # Define transformation configuration
    transform_config = {
        'missing_values': {
            'strategy': 'drop'
        }
    }
    
    # Run pipeline
    output_file = "data/processed/pipeline_output.csv"
    pipeline.run_pipeline(source_file, output_file, transform_config)
    
    logger.info("Pipeline example completed successfully!")


def example_with_config():
    """
    Example using configuration file
    """
    logger.info("=" * 60)
    logger.info("Example 3: Using Pipeline with Configuration")
    logger.info("=" * 60)
    
    # Check if sample data exists
    source_file = "data/raw/sample_data.csv"
    if not os.path.exists(source_file):
        logger.error(f"Sample data not found. Please run: python src/generate_sample_data.py")
        return
    
    config_file = "config/pipeline_config.yaml"
    
    # Initialize pipeline with config
    pipeline = ETLPipeline(config_path=config_file)
    
    # Get pipeline stats
    stats = pipeline.get_pipeline_stats()
    logger.info(f"Pipeline configuration loaded: {stats}")
    
    # Run pipeline
    output_file = "data/processed/config_output.csv"
    pipeline.run_pipeline(source_file, output_file)
    
    logger.info("Configuration example completed successfully!")


def main():
    """
    Main function to run all examples
    """
    logger.info("=" * 60)
    logger.info("ETL Pipeline Examples")
    logger.info("=" * 60)
    
    # Check if sample data exists, if not generate it
    if not os.path.exists("data/raw/sample_data.csv"):
        logger.info("Sample data not found. Generating...")
        from src.generate_sample_data import save_sample_data
        save_sample_data()
    
    # Run examples
    try:
        example_individual_modules()
        print("\n")
        example_pipeline()
        print("\n")
        example_with_config()
        
        logger.info("=" * 60)
        logger.info("All examples completed successfully!")
        logger.info("Check the 'data/processed/' directory for output files")
        logger.info("=" * 60)
        
    except Exception as e:
        logger.error(f"Error running examples: {e}")
        raise


if __name__ == "__main__":
    main()
