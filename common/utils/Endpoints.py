# Define the base URL and endpoints
BASE_URL = "https://api-fantasy.llt-services.com"
LEAGUE_ID = ""
TEAM_ID = ""

endpoints = {
    # App-related endpoints
    "appConfig": "/app/config",

    # User-related endpoints
    "userInfo": "/api/v3/user/me",
    "userTime": "/api/v3/time",
    "userLeagues": "/api/v4/leagues",
    "userFormations": "/v4/teams/lineup/formations",  # ?option=free
    "userConsents": "/dsp/v1/consents",

    # Player-related endpoints
    "playerStats": lambda player_id: f"/api/v3/player/{player_id}",
    "playerMarketValue": lambda player_id: f"/api/v3/player/{player_id}/market-value",

    # Team-related endpoints
    "teamCalendar": lambda team_id=TEAM_ID: f"/api/v3/calendar/{team_id}",
    "teamPlayers": lambda team_id=TEAM_ID: f"/api/v3/player/team/{team_id}",

    # Week-related endpoints
    "weekMatches": lambda week_id: f"/stats/v1/stats/week/{week_id}",

    # Manager-Team-related endpoints
    "teamInfo": lambda team_id=TEAM_ID: f"/api/v3/teams/{team_id}",
    "teamMoney": lambda team_id=TEAM_ID: f"/api/v3/teams/{team_id}/money",
    "teamLineup": lambda team_id=TEAM_ID: f"/api/v3/teams/{team_id}/lineup",  # PUT {"defender","goalkeeper","midfield","striker","tactical_formation"}
    "teamLineupByWeek": lambda team_id=TEAM_ID, week_id=-1: f"/api/v4/teams/{team_id}/lineup/week/{week_id}",
    "teamFavouritePlayers": lambda team_id=TEAM_ID: f"/api/v4/teams/{team_id}/favourite-players",
    "teamRewards": lambda team_id: f"/api/v4/team/{team_id}/rewards",

    # League-related endpoints
    "leagueTypes": "/api/v4/leagues-types",
    "leaguePremiumConfig": "/api/v4/leagues/premium-configuration",
    "leagueInfo": lambda league_id: f"/api/v4/leagues/{league_id}",
    "leagueTeam": lambda team_id=TEAM_ID, league_id=LEAGUE_ID: f"/api/v3/leagues/{league_id}/teams/{team_id}",
    "leagueNews": lambda league_id=LEAGUE_ID: f"/api/v3/leagues/{league_id}/news",
    "leagueNewsById": lambda week_id, league_id=LEAGUE_ID: f"/api/v3/leagues/{league_id}/news/{week_id}",
    "leagueRanking": lambda league_id=LEAGUE_ID: f"/api/v5/leagues/{league_id}/ranking",
    "leagueRankingByWeek": lambda league_id=LEAGUE_ID, week_id=-1: f"/api/v5/leagues/{league_id}/ranking/{week_id}",
    "leagueMarket": lambda league_id=LEAGUE_ID: f"/api/v3/league/{league_id}/market",
    "leagueMarketHistory": lambda league_id=LEAGUE_ID: f"/api/v3/league/{league_id}/market/history",
    "leagueIncreaseBuyoutPlayer": lambda league_id=LEAGUE_ID: f"/api/v4/league/{league_id}/buyout/player",  # PUT {"playerId", "valueToIncrease"}
    "leaguePayBuyoutPlayer": lambda player_id, league_id=LEAGUE_ID: f"/api/v4/league/{league_id}/buyout/{player_id}/pay",  # PUT {"buyoutClauseToPay"}

    # Market-related actions (offerId -> marketPlayer)
    "marketOfferHistory": lambda offer_id, league_id=LEAGUE_ID: f"/api/v3/league/{league_id}/market/{offer_id}/history",
    "marketOfferSell": lambda offer_id, league_id=LEAGUE_ID: f"/api/v3/league/{league_id}/market/{offer_id}/sell",  # POST {"playerId", "salePrice"}
    "marketOfferAccept": lambda bid_id, offer_id, league_id=LEAGUE_ID: f"api/v3/league/{league_id}/market/{offer_id}/offer/{bid_id}",  # POST {"offerMoney"}
    "marketOfferDelete": lambda offer_id, league_id=LEAGUE_ID: f"api/v3/league/{league_id}/market/{offer_id}/delete",  # DELETE
    "marketOfferMakeBid": lambda offer_id, league_id=LEAGUE_ID: f"/api/v3/league/{league_id}/market/{offer_id}/bid",  # POST {"money"}
    "marketOfferEditBid": lambda bid_id, offer_id, league_id=LEAGUE_ID: f"/api/v3/league/{league_id}/market/{offer_id}/bid/{bid_id}",  # PUT {"money"}
    "marketOfferCancelBid": lambda bid_id, offer_id, league_id=LEAGUE_ID: f"/api/v3/league/{league_id}/market/{offer_id}/bid/{bid_id}/cancel",  # DELETE
    "marketImmediateSale": lambda league_id=LEAGUE_ID: f"/api/v3/league/{league_id}/market/immediate-sale",  # POST {"playerId", "salePrice"}

    # Ranking-related endpoints
    "rankingGlobal": "/api/v3/ranking/global",

    # Stats endpoints
    "statsMarketEvolutionWeek": "/stats/v1/market/evolution/week",
    "statsMarketEvolutionMonth": "/stats/v1/market/evolution/month",
    "statsMarketEvolutionSeason": "/stats/v1/market/evolution/season",
    "statsMarketEvolutionYear": "/stats/v1/market/evolution/year",
    "statsPlayerStatsBySeason": "/stats/v1/players/stats",
    "statsPlayerStatsByWeek": lambda week_id: f"/stats/v1/players/stats/week/{week_id}",

    # Store-related endpoints
    "storeProducts": "/classic/v1/store/products/user",
    "storePurchases": "/classic/v1/store/purchases/user",
    "storeConsumables": "/classic/v1/store/user-consumable",

    # Miscellaneous endpoints
    "time": "api/v3/time",
    "checkVersion": "/check-version",
    "cardCarousel": "/classic/v2/cardCarousel",
    "cardCarouselWithRegion": "/classic/v1/cardCarousel?region=18",
    "teamDefinitions": "/classic/v1/league-definitions/103/teams",
    "leaguesTypes": "/api/v4/leagues-types",

    # New endpoints
    "ideal": "/api/v4/ideal",
    "profitable": "/api/v4/profitable",
}
