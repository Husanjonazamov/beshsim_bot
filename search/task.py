import requests

class GetSim:
    OPERATORS = [
        'ucell', 'beeline', 'uztelecom', 'humans'
    ]

    RAQAM_TANLASH_APP_HEADER = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,uz-UZ;q=0.8,uz;q=0.7,en-GB;q=0.6,en-US;q=0.5,en;q=0.4',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'XSRF-TOKEN=eyJpdiI6IjREYld5MzdjRDdiM0tmWDBhL1JNaHc9PSIsInZhbHVlIjoiWVdDd2c5MFBVY1NuMm50WHh0aS93VWQwQjIxcXJPMURwTTVXcFo1SXpkdkZxU0hZUitOSHJNbjBwdGNMZmY0dTk0Q2N3TEFoaVk3YStoc2cxK3VPRjdFbUU2Tk5oaEFFTEdWTnVMWnkzQ2gxbUFGMWY2V0g0TzZ1R3BtQ0tKRUEiLCJtYWMiOiI1NGNmMGE3OWQwZWFlZTU3Yjg0ZTkzNmNmNzUwODI5ODk3NmVmYmYzOWNmOGQxYmI1MjlhZmQ0ZWFkZDI3OWRhIn0%3D; laravel_session=eyJpdiI6Im5neW9jMU1aamJHV0pvaWNCdEU3aUE9PSIsInZhbHVlIjoiYnFVa3c4NGpxeUFGOXZXdjdsQ3hLZnhYUHB1b3ZQNEhQYzU0S2xwVFM5YXhaaU1JM1dMQjBZbjVvaENvN1NZQmVsYmI4aTdaV01RTU8rUkNyckUwNVBpZ3VPZE9PTGxpcG1HcnBvNDNXYy9XMFdkSlVpUEdXVTh5emtlejlXN2UiLCJtYWMiOiJhYjYxNmViZDgxYjE4Y2UzOGMwY2YyNDJiYzViMDY4NDMwNDJjYTE1MjljOGVkZTdiYzA3Njc3NzRlNDJhYjY1In0%3D',
        'Origin': 'https://raqamtanlash.uz',
        'Priority': 'u=1, i',
        'Referer': 'https://raqamtanlash.uz/humans/pick-number',
        'Sec-CH-UA': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
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
            'data':[{
                'number': i['number'],
                'price': i['price'],
                'discount': 0
            } for i in response['numbers']],
            'pages':{
                'page': self.page,
                'size': response['count'],
                'total-items': None,
                'page-count': None,
                'prev': None,
                'next': None
            }
        }
    
    # ucell telefon raqamlari
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


    # beeline telefon raqamlari
    def get_beeline(self):
        price_ids = [
            {
                "price":0,
                "id":188
            },
            {
                "price":100000,
                "id":1201
            },
            {
                "price":250000,
                "id":187
            },
            {
                "price":500000,
                "id":186
            },
            {
                "price":100000000,
                "id":3008
            },
        ]
        
        url = 'https://nomer.beeline.uz/msapi/web/rms/phone-numbers/'

        contents = []

        paginations = {
            'page': self.page,
            'size': len(contents),
            'total-items':0,
            'page-count':0,
            "prev":None,
            "next":None,
        }
        
        for price in price_ids:
            params = {
                'page': self.page,
                'size': self.page_size,
                'warehouse_code': price['id'],
                'phone_number_mask': '9989****' + self.latest_numbers
            }
            
            response = requests.get(url,  params=params).json()

            paginations['total-items'] += response['totalElements']
            paginations['page-count'] += response['totalPages']
            
            for i in response['content']:
                contents.append({
                    'number': i['phoneNumber'],
                    'price': price['price'],
                    'discount': 0,
                })
        
        return {
            "data":contents,
            "pages":paginations
        }

    
    # uztelecom aloqa operatorlari
    def get_uztelecom(self):
        url = 'https://online-order.utc.uz/api/numbers'
        
        params = {
            'SortLabel': 'Price',
            'SortDirection': '2',
            'Search': '77***' + self.latest_numbers,
            'Price[0]': '0',
            'Price[1]': '30000000'
        }
        response = requests.get(url, params=params).json()
        return {
            "data": [{
                'number': i['number'],
                'price': i['price'],
                'discount': 0
            } for i in response['items']],
            'pages':{
                'page': self.page,
                'size': len(response['items']),
                'total-items': response['total_items'],
                'page-count': None,
                'prev': None,
                'next': None
            }
        }
    

    # humans aloqa operatorlari
    def get_humans(self):
        return self.get_number_with_RTX()

    
    def handler(self):
        if self.operator == 'ucell':
            return self.get_ucell()
        elif self.operator == 'beeline':
            return self.get_beeline()
        elif self.operator == 'humans':
            return self.get_humans()
        elif self.operator == 'uztelecom':
            return self.get_uztelecom()
        else:
            raise ValueError('Aloqa operator topilmadi')
    
    def __init__(self, operator:str, latest_numbers:str, page:int=0, page_size:int=10):
        
        # telefon raqamini to'g'rligini tekshirish
        if not latest_numbers.isdigit() or \
            not len(latest_numbers) == 4:
            raise ValueError("Telefon nomerning so'ngi 4ta raqamini kiriting")

        self.latest_numbers = latest_numbers
        self.operator = operator
        self.page = page
        self.page_size = page_size              
        self.latest_numbers = latest_numbers
        self.operator = operator
        self.page = page
        self.page_size = page_size


