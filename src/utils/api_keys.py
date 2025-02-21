import os
from typing import Dict
from dotenv import load_dotenv
from src.config.logging_config import logger

load_dotenv()

class APIKeyManager:
    """Manage API keys and credentials for various services."""
    
    @staticmethod
    def get_api_keys() -> Dict[str, str]:
        """
        Retrieve all API keys from environment variables.
        
        Returns:
            Dict[str, str]: Dictionary containing all API keys
        """
        required_keys = [
            "TAVILY_API_KEY",
            "OPENAI_API_KEY",
            "ANTHROPIC_API_KEY",
            "AIRTABLE_API_KEY"
        ]
        
        api_keys = {}
        missing_keys = []
        
        for key in required_keys:
            value = os.getenv(key)
            if value:
                api_keys[key] = value
            else:
                missing_keys.append(key)
        
        if missing_keys:
            error_msg = f"Missing required API keys: {', '.join(missing_keys)}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        logger.info("Successfully loaded all API keys")
        return api_keys
    
    @staticmethod
    def get_airtable_config() -> Dict[str, str]:
        """
        Retrieve Airtable configuration from environment variables.
        
        Returns:
            Dict[str, str]: Dictionary containing Airtable configuration
        """
        required_config = [
            "AIRTABLE_BASE_ID",
            "AIRTABLE_TABLE_NAME"
        ]
        
        config = {}
        missing_config = []
        
        for key in required_config:
            value = os.getenv(key)
            if value:
                config[key] = value
            else:
                missing_config.append(key)
        
        if missing_config:
            error_msg = f"Missing required Airtable configuration: {', '.join(missing_config)}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        logger.info("Successfully loaded Airtable configuration")
        return config 