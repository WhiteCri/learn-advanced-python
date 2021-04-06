from collections import namedtuple
Event = namedtuple('Event', 'time proc action')

def taxi_process(ident, trips, start_time=0):
    '''각 단계 변화마다 이벤트를 생성하며 시뮬레이터에 제어권을 넘긴다.'''
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')
        yield Event(time, ident, 'going home')

print('ex16_21')
taxi = taxi_process(ident=13, trips=2, start_time=0)
t1 = next(taxi)
print(t1)
r = taxi.send(t1.time + 7)
print(r)
r = taxi.send(r.time + 23)
print(r)
r = taxi.send(r.time + 5)
print(r)
r = taxi.send(r.time + 48)
print(r)
r = taxi.send(r.time + 1)
print(r)
r = taxi.send(r.time + 10)
print(r)
r = taxi.send(r.time + 10)

import queue
class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        '''시간이 끝날 때까지 이벤트를 스케쥴링하고 출력한다'''
        # 각 택시의 첫 번째 이벤트를 스케쥴링한다.
        for _proc in sorted(self.procs.items()):
            first_event = next(_proc)
            self.events.put(first_event)

        # 시뮬레이션 핵심 루프
        sim_time = 0
        while sim_time < end_time:
            if self.events.emtpy():
                print('*** end of events')
                break

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi: ', proc_id, proc_id * '    ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of siimulation time: {} events pending ***'
            print(msg.format(self.evnets.qsize()))

num_taxis = 3
DEPARTURE_INTERVAL = 5
taxis = {i: taxi_process(i, (i +  1) * 2, i * DEPARTURE_INTERVAL)
         for i in range(num_taxis)}

sim = Simulator(taxis)
sim.run(end_time)