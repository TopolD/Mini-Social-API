from async_property import async_property

from app.Public.dao import PublicDao
from app.Public.schemas import OrderField, SearchS, SortField


class GetPostsByFilter:
    """
    we init param for getting columns with database by filter

    :param search:
    :param author_id:
    :param sort:
    :param order:


    """

    def __init__(self, author_id, sort: SortField, order: OrderField, search: SearchS):
        self.author_id = author_id
        self.sort = sort.value
        self.order = order.value
        self.search = search

    @async_property
    async def get_post(self):
        return await PublicDao.get_post_by_filters(
            self.author_id,
            self.sort,
            self.order,
            self.search.title,
            self.search.content,
        )
