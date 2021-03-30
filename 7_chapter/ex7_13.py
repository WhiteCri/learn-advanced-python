def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1 # this code makes count variable as local, due to += operator
        total += new_value
        return total / count

    return averager

avg = make_averager()
print(avg(10))