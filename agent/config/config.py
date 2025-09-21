import os
import configparser


def get_config():
    env = os.getenv("ENV", "dev")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_common_path = os.path.join(base_dir, 'config_common.ini')
    env_config_path = os.path.join(base_dir, f'config_{env}.ini')

    # Create config parser
    config = configparser.ConfigParser()

    # reading multiple files, later files can override values from earlier files
    config.read([config_common_path, env_config_path])

    # Prepare final configuration
    final_config = {}

    # First, add common config values
    if 'DEFAULT' in config:
        for key, value in config['DEFAULT'].items():
            final_config[key.upper()] = value

    # Then, add values from other sections (e.g. SECRETS)
    for section in config.sections():
        for key, value in config[section].items():
            final_config[key.upper()] = value

    # Return the final merged config as a dictionary
    return {
        "DB_FILE": final_config.get("DB_FILE", "events_dev.db"),
        "OLLAMA_MODEL": final_config.get("OLLAMA_MODEL", "ollama"),
        "GMAIL_SCOPES": final_config.get("GMAIL_SCOPES", "https://www.googleapis.com/auth/gmail.readonly").split(","),
        "LOG_LEVEL": final_config.get("LOG_LEVEL", "INFO")
    }


conf = get_config()
