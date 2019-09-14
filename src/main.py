import sys, os
from core.parser import Parser
from core.output import FormatterOutput
from decoder.customer_decoder import CustomerDecoder
from service.invite_service import InviteService
from core.distance_strategy import DistanceStrategy
from constants import FILE_NAME, GLOBAL_CIRCLE_DISTANCE

def main():
    strategy = DistanceStrategy(GLOBAL_CIRCLE_DISTANCE)
    file_path = os.path.abspath(FILE_NAME)
    service = InviteService(distance_estimator=strategy)
    data = Parser.parsing(file_path=file_path, decoder=CustomerDecoder)
    result =  service.calculate(data)
    FormatterOutput.output(result)
    
if "__main__" == __name__:
    main()