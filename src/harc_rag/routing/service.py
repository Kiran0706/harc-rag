from harc_rag.routing.router import AdaptiveRouter


class RoutingService:

    def __init__(self):

        self.router = AdaptiveRouter()

    def decide(
        self,
        confidence: float,
    ):

        return self.router.route(confidence)