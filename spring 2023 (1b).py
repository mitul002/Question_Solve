

def srt(prices):
    # Sort prices in descending order (in-place)
    prices.sort(reverse=True)
    print(prices)

lst = [181, 178, 187, 182, 192, 189, 202, 201]
srt(lst)