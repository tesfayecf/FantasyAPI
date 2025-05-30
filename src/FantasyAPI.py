from src.services.PlayersService import PlayersService
from src.services.TeamsService import TeamsService
from src.services.MarketService import MarketService

from src.managers.RequestManager import RequestManager
from src.managers.FileManager import FileManager

class FantasyAPI:
    """
    Fantasy API
    """
    requestManager = None
    fileManager = None

    players = None
    teams = None
    market = None

    def __init__(self):
        self.requestManager = RequestManager()
        self.fileManager = FileManager(self.requestManager)

    def setRequestConfig(self, config):
        self.requestManager.setConfig(config)
    
    def setFileConfig(self, config):
        self.fileManager.setConfig(config)

    def init(self):
        self.players = PlayersService(self)
        self.teams = TeamsService(self)
        self.market = MarketService(self)
