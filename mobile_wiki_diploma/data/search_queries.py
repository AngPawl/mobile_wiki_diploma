import dataclasses


@dataclasses.dataclass
class SearchQuery:
    query: str


appium_search_query = SearchQuery(query='Appium')
selene_search_query = SearchQuery(query='Selene')
invalid_search_query = SearchQuery(query='fgfgfgfgfgfgfg')
