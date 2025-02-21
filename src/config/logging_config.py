import os
import logging
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger
from dotenv import load_dotenv

load_dotenv()

def setup_logging():
    """Configure logging for the application."""
    log_level = os.getenv("LOG_LEVEL", "INFO")
    log_file = os.getenv("LOG_FILE", "logs/app.log")
    
    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Create logger
    logger = logging.getLogger("content_creation")
    logger.setLevel(getattr(logging, log_level))
    
    # Create JSON formatter
    formatter = jsonlogger.JsonFormatter(
        '%(asctime)s %(name)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Create and export logger instance
logger = setup_logging() 