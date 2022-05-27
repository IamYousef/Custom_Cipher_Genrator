import re
import binascii
import time
from sces import SCES

t0 = time.time()
cipher = SCES()

data1 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vestibulum faucibus neque vitae sollicitudin. Vestibulum dui turpis, tempor a orci in, vulputate sollicitudin odio. Ut euismod velit a mi finibus, imperdiet varius libero pellentesque. Aenean lacus nisi, iaculis non sagittis in, suscipit et justo. Donec eu hendrerit dui. Morbi luctus eros elementum nibh hendrerit interdum. Praesent vitae massa efficitur, molestie lectus faucibus, efficitur felis. Proin semper massa vitae lectus venenatis ultrices. Proin eget laoreet est.

Donec in ornare turpis. Curabitur laoreet elit odio, sed pulvinar urna fermentum eget. Etiam ultrices, nisi eget gravida dapibus, sapien dolor pharetra lorem, vel lacinia nunc metus sed magna. Sed tempor aliquet sodales. Aenean sit amet diam viverra, condimentum dui a, interdum tellus. Nulla interdum felis ac mi ornare ultricies. Nulla tempor velit nibh, sit amet consectetur sapien volutpat finibus.

Nulla facilisi. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam pretium condimentum nisi, a fermentum metus ultrices nec. Morbi imperdiet magna in massa consectetur gravida. Nulla porttitor posuere ultrices. Sed finibus, justo nec pulvinar consequat, lorem quam tempus ex, vitae mollis urna lacus et neque. Vivamus in risus nec mauris lacinia viverra ac sed sem. Integer in vehicula erat. Suspendisse."""

data2 = "یوسف"

key = ['10', '10', '10', '10', '10', '10', '10', '10',
       '10', '10', '10', '10', '10', '10', '10', '10']
print(cipher.encrypt(data2, key))
t1 = time.time()
print(t1 - t0)

# keyr = binascii.hexlify("0123456789".encode()).decode()
keyr = binascii.hexlify("jkdhsfopidshf oidyhfoiu hsgfihsdlfhio".encode()).decode()

print(cipher.key_generator(keyr))
# ['31', '32', '33', '31', '32', '33', '31', '01', '10', '13', '33', '23', '13', '33', '23', '13']
# ['31', '32', '33', '34', '35', '31', '61', '70', '07', '16', '13', '53', '43', '33', '23', '13']