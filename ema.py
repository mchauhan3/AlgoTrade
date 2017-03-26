from zipline.api import order_value, order_target, record, symbol, history, sid


def initialize(context):
    context.arr = [0, symbol('AAPL') , 0, 0]



def handle_data(context, data):
    context.arr[0] += 1
    if context.arr[0] == 13 :
        short_mavg = data.history(context.arr[1], "price", bar_count=12, frequency = "1d").mean()
        context.arr[2] = short_mavg
        return
    elif context.arr[0] <= 26 :
        return 
    elif context.arr[0] == 27 :
        long_mavg = data.history(context.arr[1], "price", bar_count=26, frequency = "1d").mean()
        context.arr[3] = long_mavg
    mult_short = (2 / 13)
    mult_long = (2 / 27)
    current_close = data.history(context.arr[1], "price", bar_count=1, frequency = "1d")[0]
    short_ema = (current_close * mult_short) + (context.arr[2] * (1 - mult_short))
    long_ema = (current_close * mult_long) + (context.arr[3] * (1 - mult_long))
    if short_ema < long_ema :
        toSell = context.portfolio.positions[context.arr[1]].amount * -1
        order_target(context.arr[1], toSell)
    else:
        order_value(context.arr[1], context.portfolio.cash) 
    context.arr[2] = short_ema
    context.arr[3] = long_ema
    record(TWX=data.current(symbol('AAPL'), 'price'))
    