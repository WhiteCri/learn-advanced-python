class A:
    def ping(self):
        print('A ping:', self)

class B(A):
    def pong(self):
        print('B pong:', self)

class C(A):
    def pong(self):
        print('C PONG: ', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping: ', self)

    # def ping(self):
    #     A.ping(self) # since A.ping is not binded to D, we need to specify 'self'
    #     print('post-ping', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

#d = D()
#d.ping()

d = D()
d.pingpong()