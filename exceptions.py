class PipelineError(Exception):
    """ Base exception for all pipeline failures. """
    pass

class ExtractionError(PipelineError):
    """ Raised when data cannot be pulled from a source. """
    pass

class TransformationError(PipelineError):
    """ Raised when data fails validation or cleaning. """
    pass

class LoadError(PipelineError):
    """ Raised when writing to a destination fails. """
    pass