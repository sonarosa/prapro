import numpy as np
import time


start_time = time.time()
random_array = np.random.rand(1000, 1000)
end_time = time.time()


elapsed_time = end_time - start_time
print("Time taken to create the array:", elapsed_time, "seconds")

random_bytes = random_array.tobytes()


r2 = np.frombuffer(random_bytes, dtype=random_array.dtype)
r2 = r2.reshape(random_array.shape)  

print("After loading, content of the recreated array:")
print(r2)

tolerance = 1e-6  
are_equal = np.allclose(random_array, r2, atol=tolerance)
print("Are both arrays equal?", are_equal)
