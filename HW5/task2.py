from decimal import Decimal


# С decimal вид какой то не очень, с float по приятнее,
# а так для денежных расчетов лучше использовать Decimal из-за точности
def premium(names: list, bids: list, percents: list) -> dict:
    percents_ = [float(i.replace('%', '')) for i in percents]
    if len(names) != len(bids) != len(percents):
        raise Exception('Invalid data')
    else:
        return dict(zip(names, map(lambda x: x[0] + (x[0] * (x[1] / 100)), zip(bids, percents_))))


print(premium(['Julia', 'Robin', 'Luffy'], [1000, 1500, 2000], ['10.50%', '15.25%', '5%']))
