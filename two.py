import ray
from ray import serve

ray.init(address="auto")
serve.start(detached=True)
x = ray.get_actor("x")

answer = x.msg.remote("message")

print(ray.get(answer))




