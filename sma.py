from zipline.api import order_value, order_target, record, symbol, history, sid


def initialize(context):
    context.arr = [0, sid(357)];


def handle_data(context, data):
    context.arr[0] += 1
    if context.arr[0] < 200 :
        return 
    short_mavg = data.history(context.arr[1], "price", bar_count=50, frequency = "1d").mean()
    long_mavg = data.history(context.arr[1], "price", bar_count=200, frequency = "1d").mean()
    if (short_mavg < long_mavg):
        order_target(context.arr[1], context.portfolio.positions[context.arr[1]])
    else:
        order_value(context.arr[1], context.portfolio.cash)
    record(TWX=data.current(symbol('AAPL'), 'price'))
    
