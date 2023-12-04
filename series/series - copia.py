def slices(series, length):
    if length > len(series):
        raise ValueError('length bigger than series len')
    if length <= 0:
        raise ValueError('length cannot be 0 or negative')
    end = length
    start = 0
    slices = []
    while end <= len(series):
        slices.append(series[start:end])
        start += 1
        end += 1
    return slices
    

