import bobo

@bobo.query('/') ##bobo가 hello에 person이 필요하다는 것을 알아냄
def hello(person):
    return'Hello %s!' % person

## bobo -f ex5_12.py
## curl -i http://localhost:8080/
## curl -i http://localhost:8080/?person=Jim