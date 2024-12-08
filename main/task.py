import requests

class GetSim:
    def __init__(self, operator: str, latest_numbers: str, page: int = 0, page_size: int = 10):
        # Telefon raqamini to'g'rligini tekshirish
        if not latest_numbers.isdigit() or not len(latest_numbers) == 4:
            raise ValueError("Telefon nomerning so'ngi 4ta raqamini kiriting")
        
        self.latest_numbers = latest_numbers
        self.operator = operator
        self.page = page
        self.page_size = page_size
        
    def get_ucell(self):
        data = {
            "pager": {"pageNum": self.page, "pageSize": self.page_size},
            "filter": {
                "region_id": 2,
                "locality_id": 29,
                "msisdn_type": 0,
                "search_type": 2,
                "query": self.latest_numbers,
                "price_min": 0,
                "price_max": 0,
                "discounted": 0
            }
        }

        response = requests.post('https://ucell.uz/numberreserve/mrsrchwds', json=data).json()

        return {
            'data': [{
                'number': i['msisdn'],
                'price': i['price'],
                'discount': i['discount']
            } for i in response['SearchRes']['data']],
            'pages': {
                'current': self.page,
                'total-items': response['SearchRes']['paging']['TotalItems'],
                'page-count': response['SearchRes']['paging']['PagesCount'],
                'prev': None if self.page == 0 else self.page - 1,
                'next': None if self.page == response['SearchRes']['paging']['PagesCount'] else self.page + 1
            }
        }

    def get_number_with_RTX(self):
        url = 'https://raqamtanlash.uz/api/' + self.operator

        data = {
            'number_3': '',
            'number_4': '',
            'number_5': '',
            'number_6': self.latest_numbers[0],
            'number_7': self.latest_numbers[1],
            'number_8': self.latest_numbers[2],
            'number_9': self.latest_numbers[3]
        }

        response = requests.post(url, headers=self.RAQAM_TANLASH_APP_HEADER, data=data).json()
        
        return {
            'data': [{
                'number': i['number'],
                'price': i['price'],
                'discount': 0
            } for i in response['numbers']],
            'pages': {
                'page': self.page,
                'size': response['count'],
                'total-items': None,
                'page-count': None,
                'prev': None,
                'next': None
            }
        }

    def get_mobiuz(self):
        return self.get_number_with_RTX()

    def handler(self):
        if self.operator == 'ucell':
            return self.get_ucell()
        elif self.operator == 'mobiuz':
            return self.get_mobiuz()
        else:
            raise ValueError('Aloqa operator topilmadi')
