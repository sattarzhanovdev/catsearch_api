from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ccxt import NetworkError, ExchangeError
import ccxt

@api_view(['GET'])
def get_binance_prices(request):
    # Список бирж для подключения
    exchanges = [
        {'name': 'Binance', 'api_key': 'AuZSjtXy2Ij7QiBEGZojT6kFu8qLQSQrroiYHUKgOUR96EfuBsxNY3ssJFxLJr14', 'secret': 'q197N89pRmuZVsUzJOlCDTYolP9p6OMpcOpLI0MizdPzKhJfsBpsYSqmy8wwyELg'},
        {'name': 'Bybit', 'api_key': 'fDUu6KSrgeP3ARMbL9', 'secret': 'I3fL8LJBgn0eo2xdEoQXwQEAygUAcW7QJ85E'},
        {'name': 'OKX', 'api_key': '807b990b-152a-483a-a0a4-0fd534404517', 'secret': '3F86EABDD2D920F231B923CEAA89A80C'},
    ]

    data_by_exchange = {}

    for exchange_info in exchanges:
        if exchange_info['name'] == 'Binance':
            exchange = ccxt.binance({
                'apiKey': exchange_info['api_key'],
                'secret': exchange_info['secret'],
            })
        else:
            continue  # Пропустить биржу, если ее нет в списке

        try:
            # Получите данные о ценах для пар криптовалют
            markets = exchange.load_markets()
            
            # Фильтрация символов: оставляем только те, которые связаны с USDT
            usdt_symbols = [symbol for symbol, info in markets.items() if 'USDT' in info['quote']]
            symbols = usdt_symbols[:200]  # Выберите первые 200 символов для примера
            
            ticker_data = exchange.fetch_tickers(symbols)

            prices = {symbol: {'price': ticker['last'],
                               'askPrice': ticker['ask'],
                               'bidPrice': ticker['bid'],
                               'percentage': ticker['percentage']} for symbol, ticker in ticker_data.items()}

            # Проверка наличия данных перед добавлением
            if prices:
                data_by_exchange[exchange_info['name']] = prices

        except ccxt.NetworkError as e:
            data_by_exchange[exchange_info['name']] = {'error': str(e)}

        except ccxt.ExchangeError as e:
            data_by_exchange[exchange_info['name']] = {'error': str(e)}

    return JsonResponse(data_by_exchange)

@api_view(['GET'])
def get_bybit_prices(request):
    # Список бирж для подключения
    exchanges = [
        {'name': 'Binance', 'api_key': 'AuZSjtXy2Ij7QiBEGZojT6kFu8qLQSQrroiYHUKgOUR96EfuBsxNY3ssJFxLJr14', 'secret': 'q197N89pRmuZVsUzJOlCDTYolP9p6OMpcOpLI0MizdPzKhJfsBpsYSqmy8wwyELg'},
        {'name': 'Bybit', 'api_key': 'fDUu6KSrgeP3ARMbL9', 'secret': 'I3fL8LJBgn0eo2xdEoQXwQEAygUAcW7QJ85E'},
        {'name': 'OKX', 'api_key': '807b990b-152a-483a-a0a4-0fd534404517', 'secret': '3F86EABDD2D920F231B923CEAA89A80C'},
    ]

    data_by_exchange = {}

    for exchange_info in exchanges:
        if exchange_info['name'] == 'Bybit':
            exchange = ccxt.bybit({
                'apiKey': exchange_info['api_key'],
                'secret': exchange_info['secret'],
            })
        else:
            continue  # Пропустить биржу, если ее нет в списке

        try:
            # Получите данные о ценах для пар криптовалют
            markets = exchange.load_markets()
            
            # Фильтрация символов: оставляем только те, которые связаны с USDT
            usdt_symbols = [symbol for symbol, info in markets.items() if 'USDT' in info['quote']]
            symbols = usdt_symbols[::100]  # Выберите первые 200 символов для примера
            
            ticker_data = exchange.fetch_tickers(symbols)

            prices = {symbol: {'price': ticker['last'],
                               'askPrice': ticker['ask'],
                               'bidPrice': ticker['bid'],
                               'percentage': ticker['percentage']} for symbol, ticker in ticker_data.items()}

            # Проверка наличия данных перед добавлением
            if prices:
                data_by_exchange[exchange_info['name']] = prices

        except ccxt.NetworkError as e:
            data_by_exchange[exchange_info['name']] = {'error': str(e)}

        except ccxt.ExchangeError as e:
            data_by_exchange[exchange_info['name']] = {'error': str(e)}

    return JsonResponse(data_by_exchange)

@api_view(['GET'])
def get_okx_prices(request):
    # Список бирж для подключения
    exchanges = [
        {'name': 'Binance', 'api_key': 'AuZSjtXy2Ij7QiBEGZojT6kFu8qLQSQrroiYHUKgOUR96EfuBsxNY3ssJFxLJr14', 'secret': 'q197N89pRmuZVsUzJOlCDTYolP9p6OMpcOpLI0MizdPzKhJfsBpsYSqmy8wwyELg'},
        {'name': 'Bybit', 'api_key': 'fDUu6KSrgeP3ARMbL9', 'secret': 'I3fL8LJBgn0eo2xdEoQXwQEAygUAcW7QJ85E'},
        {'name': 'OKX', 'api_key': '807b990b-152a-483a-a0a4-0fd534404517', 'secret': '3F86EABDD2D920F231B923CEAA89A80C'},
    ]

    data_by_exchange = {}

    for exchange_info in exchanges:
        if exchange_info['name'] == 'OKX':
            exchange = ccxt.okx({
                'apiKey': exchange_info['api_key'],
                'secret': exchange_info['secret'],
            })
        else:
            continue  # Пропустить биржу, если ее нет в списке

        try:
            # Получите данные о ценах для пар криптовалют
            markets = exchange.load_markets()
            
            # Фильтрация символов: оставляем только те, которые связаны с USDT
            usdt_symbols = [symbol for symbol, info in markets.items() if 'USDT' in info['quote']]
            symbols = usdt_symbols[:200]  # Выберите первые 200 символов для примера
            
            ticker_data = exchange.fetch_tickers(symbols)

            prices = {symbol: {'price': ticker['last'],
                               'askPrice': ticker['ask'],
                               'bidPrice': ticker['bid'],
                               'percentage': ticker['percentage']} for symbol, ticker in ticker_data.items()}

            # Проверка наличия данных перед добавлением
            if prices:
                data_by_exchange[exchange_info['name']] = prices

        except ccxt.NetworkError as e:
            data_by_exchange[exchange_info['name']] = {'error': str(e)}

        except ccxt.ExchangeError as e:
            data_by_exchange[exchange_info['name']] = {'error': str(e)}

    return JsonResponse(data_by_exchange)

@api_view(['GET'])
def get_all_prices(request):
    # Список бирж для подключения
    exchanges = [
        {'name': 'Binance', 'api_key': 'AuZSjtXy2Ij7QiBEGZojT6kFu8qLQSQrroiYHUKgOUR96EfuBsxNY3ssJFxLJr14', 'secret': 'q197N89pRmuZVsUzJOlCDTYolP9p6OMpcOpLI0MizdPzKhJfsBpsYSqmy8wwyELg'},
        {'name': 'Bybit', 'api_key': 'fDUu6KSrgeP3ARMbL9', 'secret': 'I3fL8LJBgn0eo2xdEoQXwQEAygUAcW7QJ85E'},
        {'name': 'OKX', 'api_key': '807b990b-152a-483a-a0a4-0fd534404517', 'secret': '3F86EABDD2D920F231B923CEAA89A80C'},
    ]

    data_by_exchange = {}

    for exchange_info in exchanges:
        if exchange_info['name'] == 'Binance':
            exchange = ccxt.okx({
                'apiKey': exchange_info['api_key'],
                'secret': exchange_info['secret'],
            })
        elif exchange_info['name'] == 'Bybit':
            exchange = ccxt.okx({
                'apiKey': exchange_info['api_key'],
                'secret': exchange_info['secret'],
            })
        elif exchange_info['name'] == 'OKX':
            exchange = ccxt.okx({
                'apiKey': exchange_info['api_key'],
                'secret': exchange_info['secret'],
            })
        else:
            continue  # Пропустить биржу, если ее нет в списке

        try:
            # Получите данные о ценах для пар криптовалют
            markets = exchange.load_markets()
            
            # Фильтрация символов: оставляем только те, которые связаны с USDT
            usdt_symbols = [symbol for symbol, info in markets.items() if 'USDT' in info['quote']]
            symbols = usdt_symbols  # Выберите первые 400 символов для примера
            
            ticker_data = exchange.fetch_tickers(symbols)

            prices = {symbol: {'price': ticker['last'], 'askPrice': ticker['ask'], 'bidPrice': ticker['bid'], 'percentage': ticker['percentage'], 'volume': ticker['quoteVolume']} for symbol, ticker in ticker_data.items()}

            # Проверка наличия данных перед добавлением
            if prices:
                data_by_exchange[exchange_info['name']] = prices

        except ccxt.NetworkError as e:
            data_by_exchange[exchange_info['name']] = {'error': str(e)}

        except ccxt.ExchangeError as e:
            data_by_exchange[exchange_info['name']] = {'error': str(e)}

    return JsonResponse(data_by_exchange)


@api_view(['GET'])
def get_crypto_prices(request):
    # Получаем имена бирж из параметров запроса
    exchange_names = request.GET.getlist('exchanges', [])

    # Список бирж для подключения
    exchanges = [
        {'name': 'Binance', 'api_key': 'AuZSjtXy2Ij7QiBEGZojT6kFu8qLQSQrroiYHUKgOUR96EfuBsxNY3ssJFxLJr14', 'secret': 'q197N89pRmuZVsUzJOlCDTYolP9p6OMpcOpLI0MizdPzKhJfsBpsYSqmy8wwyELg'},
        {'name': 'Bybit', 'api_key': 'fDUu6KSrgeP3ARMbL9', 'secret': 'I3fL8LJBgn0eo2xdEoQXwQEAygUAcW7QJ85E'},
        {'name': 'OKX', 'api_key': '807b990b-152a-483a-a0a4-0fd534404517', 'secret': '3F86EABDD2D920F231B923CEAA89A80C'},
    ]

    # Ваш остальной код
    prices_by_exchange = {}

    for exchange_info in exchanges:
        if exchange_info['name'] in exchange_names:
            try:
                exchange = getattr(ccxt, exchange_info['name'].lower())({
                    'apiKey': exchange_info['api_key'],
                    'secret': exchange_info['secret'],
                })

                # Получите данные о ценах для всех монет, связанных с USDT
                markets = exchange.load_markets()
                usdt_symbols = [symbol for symbol, info in markets.items() if 'USDT' in info['quote']]

                print(f"Symbols on {exchange_info['name']}: {usdt_symbols}")

                ticker_data = exchange.fetch_tickers(usdt_symbols)

                prices_by_exchange[exchange_info['name']] = ticker_data

            except NetworkError as e:
                prices_by_exchange[exchange_info['name']] = {'error': str(e)}

            except ExchangeError as e:
                prices_by_exchange[exchange_info['name']] = {'error': str(e)}

    # Если есть хотя бы одна биржа с данными, продолжим
    if prices_by_exchange:
        # Находим максимальную и минимальную цены для каждой биржи
        result = {}
        for exchange_name, ticker_data in prices_by_exchange.items():
            max_price_info = max(ticker_data.values(), key=lambda x: x['last'])
            min_price_info = min(ticker_data.values(), key=lambda x: x['last'])

            result[exchange_name] = {
                'max_price_coin': max_price_info['symbol'],
                'max_price': max_price_info['last'],
                'min_price_coin': min_price_info['symbol'],
                'min_price': min_price_info['last'],
                'difference': max_price_info['last'] - min_price_info['last'],
            }

        # Возвращаем результат в заданном формате
        formatted_result = format_output(result)
        return Response(formatted_result, status=200)

    return Response({'error': 'No data available for the specified exchanges.'}, status=404)

def format_output(data):
    # Форматирование данных в заданный формат
    formatted_output = []
    for exchange, info in data.items():
        formatted_exchange_info = {
            'exchange': exchange,
            'max_price_coin': info['max_price_coin'],
            'max_price': info['max_price'],
            'min_price_coin': info['min_price_coin'],
            'min_price': info['min_price'],
            'difference': info['difference'],
        }
        formatted_output.append(formatted_exchange_info)

    return formatted_output


@api_view(['GET'])
def get_binance_price(request, symbol='BTC/USDT'):
    try:
        exchange = ccxt.binance()

        # Получение цены для указанного символа
        ticker_data = exchange.fetch_ticker(symbol)

        # Формирование ответа
        response_data = {
            'symbol': symbol,
            'price': ticker_data['last'],
        }

        return Response(response_data, status=200)

    except NetworkError as e:
        return Response({'error': str(e)}, status=500)

    except ExchangeError as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def get_binance_price_dynamic(request, symbol):
    try:
        exchange = ccxt.binance()
        coin = exchange.fetch_ticker(symbol),

        # Получение стакана (order book) для указанного символа
        order_book_data = exchange.fetch_order_book(symbol)

        # Получение последних 4 bid и ask цен
        bids = order_book_data['bids'][:4]
        asks = order_book_data['asks'][:4]

        # Формирование ответа
        response_data = {
            'symbol': symbol,
            'price': coin[0]['last'],
            'stock': 'Binance',
            'bids': [
                {
                    'price': bids[0][0],
                    'volume': bids[0][0] * bids[0][1],
                },
                {
                    'price': bids[1][0],
                    'volume': bids[1][0] * bids[1][1],
                },
                {
                    'price': bids[2][0],
                    'volume': bids[2][0] * bids[2][1],
                },
                {
                    'price': bids[3][0],
                    'volume': bids[3][0] * bids[3][1],
                }
            ],
            'asks': [
                {
                    'price': asks[0][0],
                    'volume': asks[0][0] * asks[0][1],
                },
                {
                    'price': asks[1][0],
                    'volume': asks[1][0] * asks[1][1],
                },
                {
                    'price': asks[2][0],
                    'volume': asks[2][0] * asks[2][1],
                },
                {
                    'price': asks[3][0],
                    'volume': asks[3][0] * asks[3][1],
                }
            ],
        }

        return Response(response_data, status=200)

    except NetworkError as e:
        return Response({'error': str(e)}, status=500)

    except ExchangeError as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def get_bybit_price_dynamic(request, symbol):
    try:
        exchange = ccxt.bybit()
        coin = exchange.fetch_ticker(symbol),

        # Получение стакана (order book) для указанного символа
        order_book_data = exchange.fetch_order_book(symbol)

        # Получение последних 4 bid и ask цен
        bids = order_book_data['bids'][:4]
        asks = order_book_data['asks'][:4]

        # Формирование ответа
        response_data = {
            'symbol': symbol,
            'price': coin[0]['last'],
            'stock': 'Bybit',
            'bids': [
                {
                    'price': bids[0][0],
                    'volume': bids[0][0] * bids[0][1],
                },
                {
                    'price': bids[1][0],
                    'volume': bids[1][0] * bids[1][1],
                },
                {
                    'price': bids[2][0],
                    'volume': bids[2][0] * bids[2][1],
                },
                {
                    'price': bids[3][0],
                    'volume': bids[3][0] * bids[3][1],
                }
            ],
            'asks': [
                {
                    'price': asks[0][0],
                    'volume': asks[0][0] * asks[0][1],
                },
                {
                    'price': asks[1][0],
                    'volume': asks[1][0] * asks[1][1],
                },
                {
                    'price': asks[2][0],
                    'volume': asks[2][0] * asks[2][1],
                },
                {
                    'price': asks[3][0],
                    'volume': asks[3][0] * asks[3][1],
                }
            ],
        }

        return Response(response_data, status=200)

    except NetworkError as e:
        return Response({'error': str(e)}, status=500)

    except ExchangeError as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def get_okx_price_dynamic(request, symbol):
    try:
        exchange = ccxt.okx()
        coin = exchange.fetch_ticker(symbol)

        # Получение стакана (order book) для указанного символа
        order_book_data = exchange.fetch_order_book(symbol)

        # Получение последних 4 bid и ask цен
        bids = order_book_data['bids'][:4]
        asks = order_book_data['asks'][:4]

        # Формирование ответа
        response_data = {
            'symbol': symbol,
            'price': coin['last'],
            'stock': 'OKX',
            'bids': [
                {
                    'price': bids[0][0],
                    'volume': bids[0][0] * bids[0][1],
                },
                {
                    'price': bids[1][0],
                    'volume': bids[1][0] * bids[1][1],
                },
                {
                    'price': bids[2][0],
                    'volume': bids[2][0] * bids[2][1],
                },
                {
                    'price': bids[3][0],
                    'volume': bids[3][0] * bids[3][1],
                }
            ],
            'asks': [
                {
                    'price': asks[0][0],
                    'volume': asks[0][0] * asks[0][1],
                },
                {
                    'price': asks[1][0],
                    'volume': asks[1][0] * asks[1][1],
                },
                {
                    'price': asks[2][0],
                    'volume': asks[2][0] * asks[2][1],
                },
                {
                    'price': asks[3][0],
                    'volume': asks[3][0] * asks[3][1],
                }
            ],
        }

        return Response(response_data, status=200)

    except NetworkError as e:
        return Response({'error': str(e)}, status=500)

    except ExchangeError as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def getUSDTsFirst(request, coin_symbol='USDT'):
    exchanges = [ccxt.okx(), ccxt.binance(), ccxt.bybit()]  # Add more exchanges as needed
    fromCount = 0  # Adjust the number of top pairs as needed
    toCount = 100  # Adjust the number of top pairs as needed
    base_currency = 'USDT'

    result_data = []

    # Получение списка всех доступных торговых пар на бирже
    all_symbols = set()
    for exchange in exchanges:
        try:
            symbols = exchange.load_markets().keys()
            all_symbols.update(symbols)
        except ccxt.NetworkError as e:
            return Response({'error': str(e)}, status=500)
        except ccxt.ExchangeError as e:
            return Response({'error': str(e)}, status=500)

    # Ограничение списка торговых пар до первых top_pairs_count пар с базовой валютой USDT
    usdt_pairs = [symbol for symbol in all_symbols if base_currency in symbol and symbol.endswith(f'/{base_currency}')]
    usdt_pairs = usdt_pairs[fromCount:toCount]

    for symbol in usdt_pairs:
        symbol_result_data = []

        for exchange in exchanges:
            try:
                # Проверка, поддерживает ли биржа указанную торговую пару
                if symbol in exchange.symbols:
                    # Получение цены для указанной торговой пары
                    ticker_data = exchange.fetch_ticker(symbol)

                    # Получение стакана (order book) для указанной торговой пары
                    order_book = exchange.fetch_order_book(symbol)
                    bids = order_book['bids'][:4]
                    asks = order_book['asks'][:4]
                    # Проверка, что 'last' цена существует и не является None
                    if 'last' in ticker_data and ticker_data['last'] is not None:
                        # Формирование записи о цене, bid, ask и order book
                        price_data = {
                            'exchange': exchange.id,
                            'pair': symbol,
                            'last_price': ticker_data['last'],
                            'percentage': ticker_data['percentage'],
                            'bid_price': ticker_data['bid'],
                            'ask_price': ticker_data['ask'],
                            'volume': ticker_data['quoteVolume'],
                            'order_book': {
                                'bids': bids,
                                'asks': asks,
                            }
                        }

                        symbol_result_data.append(price_data)

            except ccxt.NetworkError as e:
                return Response({'error': str(e)}, status=500)

            except ccxt.ExchangeError as e:
                return Response({'error': str(e)}, status=500)

        # Фильтрация записей, где 'last' цена отсутствует, равна None или есть одинаковые цены
        symbol_result_data = [entry for entry in symbol_result_data if 'last_price' in entry and entry['last_price'] is not None]
        if len(set(entry['last_price'] for entry in symbol_result_data)) > 1:
            # Сортировка по цене (от дешевого к дорогому)
            symbol_result_data.sort(key=lambda x: x['last_price'])

            # Выбор самой дешевой и самой дорогой биржи для текущей торговой пары
            cheap_exchange = symbol_result_data[0]
            expensive_exchange = symbol_result_data[-1]

            result_data.append({
                'pair': symbol,
                'expensiveExchange': expensive_exchange['exchange'],
                'expensivePrice': expensive_exchange['last_price'],
                'expensiveBid': expensive_exchange['bid_price'],
                'expensiveAsk': expensive_exchange['ask_price'],
                'expensivePercentage': expensive_exchange['percentage'],
                'expensiveVolume': expensive_exchange['volume'],
                'expensiveOrderBook': expensive_exchange['order_book'],
                'cheapExchange': cheap_exchange['exchange'],
                'cheapPrice': cheap_exchange['last_price'],
                'cheapBid': cheap_exchange['bid_price'],
                'cheapAsk': cheap_exchange['ask_price'],
                'cheapPercentage': expensive_exchange['percentage'],
                'cheapVolume': expensive_exchange['volume'],
                'cheapOrderBook': cheap_exchange['order_book'],
                'obat': (cheap_exchange['order_book']['asks'][0][0]+cheap_exchange['order_book']['asks'][1][0]+cheap_exchange['order_book']['asks'][2][0]+cheap_exchange['order_book']['asks'][3][0])/4,
                'obbt': (expensive_exchange['order_book']['bids'][0][0]+expensive_exchange['order_book']['bids'][1][0]+expensive_exchange['order_book']['bids'][2][0]+expensive_exchange['order_book']['bids'][3][0])/4,
            })

    return Response(result_data, status=200)

@api_view(['GET'])
def getUSDTsSecond(request, coin_symbol='USDT'):
    exchanges = [ccxt.okx(), ccxt.binance(), ccxt.bybit()]  # Add more exchanges as needed
    fromCount = 100  # Adjust the number of top pairs as needed
    toCount = 200  # Adjust the number of top pairs as needed
    base_currency = 'USDT'

    result_data = []

    # Получение списка всех доступных торговых пар на бирже
    all_symbols = set()
    for exchange in exchanges:
        try:
            symbols = exchange.load_markets().keys()
            all_symbols.update(symbols)
        except ccxt.NetworkError as e:
            return Response({'error': str(e)}, status=500)
        except ccxt.ExchangeError as e:
            return Response({'error': str(e)}, status=500)

    # Ограничение списка торговых пар до первых top_pairs_count пар с базовой валютой USDT
    usdt_pairs = [symbol for symbol in all_symbols if base_currency in symbol and symbol.endswith(f'/{base_currency}')]
    usdt_pairs = usdt_pairs[fromCount:toCount]

    for symbol in usdt_pairs:
        symbol_result_data = []

        for exchange in exchanges:
            try:
                # Проверка, поддерживает ли биржа указанную торговую пару
                if symbol in exchange.symbols:
                    # Получение цены для указанной торговой пары
                    ticker_data = exchange.fetch_ticker(symbol)

                    # Получение стакана (order book) для указанной торговой пары
                    order_book = exchange.fetch_order_book(symbol)
                    bids = order_book['bids'][:4]
                    asks = order_book['asks'][:4]
                    # Проверка, что 'last' цена существует и не является None
                    if 'last' in ticker_data and ticker_data['last'] is not None:
                        # Формирование записи о цене, bid, ask и order book
                        price_data = {
                            'exchange': exchange.id,
                            'pair': symbol,
                            'last_price': ticker_data['last'],
                            'percentage': ticker_data['percentage'],
                            'bid_price': ticker_data['bid'],
                            'ask_price': ticker_data['ask'],
                            'volume': ticker_data['quoteVolume'],
                            'order_book': {
                                'bids': bids,
                                'asks': asks,
                            }
                        }

                        symbol_result_data.append(price_data)

            except ccxt.NetworkError as e:
                return Response({'error': str(e)}, status=500)

            except ccxt.ExchangeError as e:
                return Response({'error': str(e)}, status=500)

        # Фильтрация записей, где 'last' цена отсутствует, равна None или есть одинаковые цены
        symbol_result_data = [entry for entry in symbol_result_data if 'last_price' in entry and entry['last_price'] is not None]
        if len(set(entry['last_price'] for entry in symbol_result_data)) > 1:
            # Сортировка по цене (от дешевого к дорогому)
            symbol_result_data.sort(key=lambda x: x['last_price'])

            # Выбор самой дешевой и самой дорогой биржи для текущей торговой пары
            cheap_exchange = symbol_result_data[0]
            expensive_exchange = symbol_result_data[-1]

            result_data.append({
                'pair': symbol,
                'expensiveExchange': expensive_exchange['exchange'],
                'expensivePrice': expensive_exchange['last_price'],
                'expensiveBid': expensive_exchange['bid_price'],
                'expensiveAsk': expensive_exchange['ask_price'],
                'expensivePercentage': expensive_exchange['percentage'],
                'expensiveVolume': expensive_exchange['volume'],
                'expensiveOrderBook': expensive_exchange['order_book'],
                'cheapExchange': cheap_exchange['exchange'],
                'cheapPrice': cheap_exchange['last_price'],
                'cheapBid': cheap_exchange['bid_price'],
                'cheapAsk': cheap_exchange['ask_price'],
                'cheapPercentage': cheap_exchange['percentage'],
                'cheapVolume': expensive_exchange['volume'],
                'cheapOrderBook': cheap_exchange['order_book'],
                'obat': cheap_exchange['order_book']['asks'][0][0]+cheap_exchange['order_book']['asks'][1][0]+cheap_exchange['order_book']['asks'][2][0]+cheap_exchange['order_book']['asks'][3][0],
                'obbt': expensive_exchange['order_book']['bids'][0][0]+expensive_exchange['order_book']['bids'][1][0]+expensive_exchange['order_book']['bids'][2][0]+expensive_exchange['order_book']['bids'][3][0],
            })

    return Response(result_data, status=200)


@api_view(['GET'])
def getUSDTsThird(request, coin_symbol='USDT'):
    exchanges = [ccxt.okx(), ccxt.binance(), ccxt.bybit()]  # Add more exchanges as needed
    fromCount = 0  # Adjust the number of top pairs as needed
    toCount = 5  # Adjust the number of top pairs as needed
    base_currency = 'USDT'

    result_data = []

    # Получение списка всех доступных торговых пар на бирже
    all_symbols = set()
    for exchange in exchanges:
        try:
            symbols = exchange.load_markets().keys()
            all_symbols.update(symbols)
        except ccxt.NetworkError as e:
            return Response({'error': str(e)}, status=500)
        except ccxt.ExchangeError as e:
            return Response({'error': str(e)}, status=500)

    # Ограничение списка торговых пар до первых top_pairs_count пар с базовой валютой USDT
    usdt_pairs = [symbol for symbol in all_symbols if base_currency in symbol and symbol.endswith(f'/{base_currency}')]
    usdt_pairs = usdt_pairs[fromCount:toCount]

    for symbol in usdt_pairs:
        symbol_result_data = []

        for exchange in exchanges:
            try:
                # Проверка, поддерживает ли биржа указанную торговую пару
                if symbol in exchange.symbols:
                    # Получение цены для указанной торговой пары
                    ticker_data = exchange.fetch_ticker(symbol)

                    # Получение стакана (order book) для указанной торговой пары
                    order_book = exchange.fetch_order_book(symbol)
                    bids = order_book['bids'][:4]
                    asks = order_book['asks'][:4]
                    # Проверка, что 'last' цена существует и не является None
                    if 'last' in ticker_data and ticker_data['last'] is not None:
                        # Формирование записи о цене, bid, ask и order book
                        price_data = {
                            'exchange': exchange.id,
                            'pair': symbol,
                            'last_price': ticker_data['last'],
                            'percentage': ticker_data['percentage'],
                            'bid_price': ticker_data['bid'],
                            'ask_price': ticker_data['ask'],
                            'volume': ticker_data['quoteVolume'],
                            'order_book': {
                                'bids': bids,
                                'asks': asks,
                            }
                        }

                        symbol_result_data.append(price_data)

            except ccxt.NetworkError as e:
                return Response({'error': str(e)}, status=500)

            except ccxt.ExchangeError as e:
                return Response({'error': str(e)}, status=500)

        # Фильтрация записей, где 'last' цена отсутствует, равна None или есть одинаковые цены
        symbol_result_data = [entry for entry in symbol_result_data if 'last_price' in entry and entry['last_price'] is not None]
        if len(set(entry['last_price'] for entry in symbol_result_data)) > 1:
            # Сортировка по цене (от дешевого к дорогому)
            symbol_result_data.sort(key=lambda x: x['last_price'])

            # Выбор самой дешевой и самой дорогой биржи для текущей торговой пары
            cheap_exchange = symbol_result_data[0]
            expensive_exchange = symbol_result_data[-1]

            result_data.append({
                'pair': symbol,
                'expensiveExchange': expensive_exchange['exchange'],
                'expensivePrice': expensive_exchange['last_price'],
                'expensiveBid': expensive_exchange['bid_price'],
                'expensiveAsk': expensive_exchange['ask_price'],
                'expensivePercentage': expensive_exchange['percentage'],
                'expensiveVolume': expensive_exchange['volume'],
                'expensiveOrderBook': expensive_exchange['order_book'],
                'cheapExchange': cheap_exchange['exchange'],
                'cheapPrice': cheap_exchange['last_price'],
                'cheapBid': cheap_exchange['bid_price'],
                'cheapAsk': cheap_exchange['ask_price'],
                'cheapPercentage': expensive_exchange['percentage'],
                'cheapVolume': expensive_exchange['volume'],
                'cheapOrderBook': cheap_exchange['order_book'],
                'obat': (cheap_exchange['order_book']['asks'][0][0]+cheap_exchange['order_book']['asks'][1][0]+cheap_exchange['order_book']['asks'][2][0]+cheap_exchange['order_book']['asks'][3][0])/4,
                'obbt': (expensive_exchange['order_book']['bids'][0][0]+expensive_exchange['order_book']['bids'][1][0]+expensive_exchange['order_book']['bids'][2][0]+expensive_exchange['order_book']['bids'][3][0])/4,
            })

    return Response(result_data, status=200)



@api_view(['GET'])
def getUSDTsFourth(request, coin_symbol='USDT'):
    exchanges = [ccxt.okx(), ccxt.binance(), ccxt.bybit()]  # Add more exchanges as needed
    fromCount = 300  # Adjust the number of top pairs as needed
    toCount = 400  # Adjust the number of top pairs as needed
    base_currency = 'USDT'

    result_data = []

    # Получение списка всех доступных торговых пар на бирже
    all_symbols = set()
    for exchange in exchanges:
        try:
            symbols = exchange.load_markets().keys()
            all_symbols.update(symbols)
        except ccxt.NetworkError as e:
            return Response({'error': str(e)}, status=500)
        except ccxt.ExchangeError as e:
            return Response({'error': str(e)}, status=500)

    # Ограничение списка торговых пар до первых top_pairs_count пар с базовой валютой USDT
    usdt_pairs = [symbol for symbol in all_symbols if base_currency in symbol and symbol.endswith(f'/{base_currency}')]
    usdt_pairs = usdt_pairs[fromCount:toCount]

    for symbol in usdt_pairs:
        symbol_result_data = []

        for exchange in exchanges:
            try:
                # Проверка, поддерживает ли биржа указанную торговую пару
                if symbol in exchange.symbols:
                    # Получение цены для указанной торговой пары
                    ticker_data = exchange.fetch_ticker(symbol)

                    # Получение стакана (order book) для указанной торговой пары
                    order_book = exchange.fetch_order_book(symbol)
                    bids = order_book['bids'][:4]
                    asks = order_book['asks'][:4]
                    # Проверка, что 'last' цена существует и не является None
                    if 'last' in ticker_data and ticker_data['last'] is not None:
                        # Формирование записи о цене, bid, ask и order book
                        price_data = {
                            'exchange': exchange.id,
                            'pair': symbol,
                            'last_price': ticker_data['last'],
                            'percentage': ticker_data['percentage'],
                            'bid_price': ticker_data['bid'],
                            'ask_price': ticker_data['ask'],
                            'volume': ticker_data['quoteVolume'],
                            'order_book': {
                                'bids': bids,
                                'asks': asks,
                            },
                        }

                        symbol_result_data.append(price_data)

            except ccxt.NetworkError as e:
                return Response({'error': str(e)}, status=500)

            except ccxt.ExchangeError as e:
                return Response({'error': str(e)}, status=500)

        # Фильтрация записей, где 'last' цена отсутствует, равна None или есть одинаковые цены
        symbol_result_data = [entry for entry in symbol_result_data if 'last_price' in entry and entry['last_price'] is not None]
        if len(set(entry['last_price'] for entry in symbol_result_data)) > 1:
            # Сортировка по цене (от дешевого к дорогому)
            symbol_result_data.sort(key=lambda x: x['last_price'])

            # Выбор самой дешевой и самой дорогой биржи для текущей торговой пары
            cheap_exchange = symbol_result_data[0]
            expensive_exchange = symbol_result_data[-1]

            result_data.append({
                'pair': symbol,
                'expensiveExchange': expensive_exchange['exchange'],
                'expensivePrice': expensive_exchange['last_price'],
                'expensiveBid': expensive_exchange['bid_price'],
                'expensiveAsk': expensive_exchange['ask_price'],
                'expensivePercentage': expensive_exchange['percentage'],
                'expensiveVolume': expensive_exchange['volume'],
                'expensiveOrderBook': expensive_exchange['order_book'],
                'cheapExchange': cheap_exchange['exchange'],
                'cheapPrice': cheap_exchange['last_price'],
                'cheapBid': cheap_exchange['bid_price'],
                'cheapAsk': cheap_exchange['ask_price'],
                'cheapPercentage': expensive_exchange['percentage'],
                'cheapVolume': expensive_exchange['volume'],
                'cheapOrderBook': cheap_exchange['order_book'],
                'obat': (cheap_exchange['order_book']['asks'][0][0]+cheap_exchange['order_book']['asks'][1][0]+cheap_exchange['order_book']['asks'][2][0]+cheap_exchange['order_book']['asks'][3][0])/4,
                'obbt': (expensive_exchange['order_book']['bids'][0][0]+expensive_exchange['order_book']['bids'][1][0]+expensive_exchange['order_book']['bids'][2][0]+expensive_exchange['order_book']['bids'][3][0])/4,
            })

    return Response(result_data, status=200)