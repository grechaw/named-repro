import ray

@ray.remote
class MyClass:
    def __init__(self):
        pass

    def msg(self, msg):
        return f"hi yo {msg}"

if (__name__=="__main__"):
    ray.init(address="auto")
    x = MyClass.options(name="x", lifetime="detached").remote()




