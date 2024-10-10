from flask.json.provider import DefaultJSONProvider
import six

from swagger_server.models.base_model_ import Model


class FlaskJSONEncoder(DefaultJSONProvider):
    """Custom JSON encoder for Flask, extending the default JSON provider."""
    pass


class JSONEncoder(FlaskJSONEncoder):
    """Custom JSON encoder that handles the serialization of Model instances."""
    
    def __init__(self, include_nulls=False):
        """Initialize the encoder with an option to include null values.
        
        Args:
            include_nulls (bool): If True, include attributes with None values.
        """
        self.include_nulls = include_nulls

    def default(self, obj):
        """Override the default method to serialize Model instances.
        
        Args:
            obj: The object to serialize.
        
        Returns:
            dict: The serialized object.
        """
        if isinstance(obj, Model):
            result = {}
            for attr, _ in six.iteritems(obj.swagger_types):
                value = getattr(obj, attr)
                if value is None and not self.include_nulls:
                    continue
                attr = obj.attribute_map[attr]
                result[attr] = value
            return result
        return super().default(obj)
