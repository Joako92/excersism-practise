def slices(series, length):
    if length <= len(series) and length > 0:
        series_list = []
        s = 0
        for i in series:
            sliced = series[slice(s,length)]
            series_list.append(sliced)
            s += 1
            if len(series) - length > 0:
                length += 1
            else:
                break
                    
        return series_list

    else:
        raise ValueError("length out of range")
    

