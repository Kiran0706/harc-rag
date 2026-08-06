from abc import ABC, abstractmethod

from harc_rag.uncertainty.models import JointUncertainty


class UncertaintyEstimator(ABC):

    @abstractmethod
    def estimate(self, *args, **kwargs) -> JointUncertainty:
        pass