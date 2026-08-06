from harc_rag.uncertainty.estimator import JointEstimator


class UncertaintyService:

    def __init__(self):

        self.estimator = JointEstimator()