import numpy as np
import time


start_time = time.time()
random_array = np.random.rand(1000, 1000)
end_time = time.time()


elapsed_time = end_time - start_time
print("Time taken to create the array:", elapsed_time, "seconds")

random_dtype = random_array.dtype
random_shape = random_array.shape
random_bytes = random_array.tobytes()

r2 = np.frombuffer(random_bytes, dtype=random_dtype)
r2 = r2.reshape(random_shape)  

print("After loading, content of the recreated array:")
print(r2)

np.testing.assert_array_equal(random_array, r2)
print("Arrays are equal.")

