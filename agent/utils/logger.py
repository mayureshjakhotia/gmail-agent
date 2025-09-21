import logging

def setup_logger(log_level='INFO'):
    """
    Set up logger with specified log level
    
    :param log_level: Logging level
    :return: Configured logger instance
    """
    # Convert log level string to logging constant
    level = getattr(logging, log_level.upper(), logging.INFO)
    
    # Configure logger
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    return logging.getLogger('event_agent')

logger = setup_logger()
