import redis
import matplotlib.pyplot as plt
import pandas as pd

# We run redis on localhost port 6379
redisconn = redis.Redis();
samples = redisconn.execute_command('ts.range sensor1 - +');

def fix(x):
    return float(x)

df = pd.DataFrame(samples, columns=['Timestamp', 'Sample']);
df['Sample'] = df['Sample'].apply(fix);
df =  df.set_index('Timestamp');
print(df);
df.plot();
plt.show();
