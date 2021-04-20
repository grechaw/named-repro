import ray

@ray.remote
class MyClass:
    def __init__(self):
        pass

    def msg(self, msg):
        return f"hi yo {msg}"

ray.init(address="auto")
x = MyClass.options(name="x", lifetime="detached").remote()




