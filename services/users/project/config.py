class BaseConfig:
    """Base configuration"""
    JSONIFY_PRETTYPRINT_REGULAR = False # https://stackoverflow.com/a/63974534


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass