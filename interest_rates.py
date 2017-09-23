r0 = 0.03

def vasicek_int(r0):
    #define params
    T, m = 10,200
    dt = 1.0/365 # daily steps
    theta, k, beta = 0.10, 0.3, 0.03 
    dr = k*(theta-r0)*dt + beta*np.sqrt(dt)*np.random.normal(0,1,1)
    r0 = r0 + dr
    return (r0)

def ts(T,rt):
    mu, sigma, theta = 0.08, 0.05, 0.2
    rate = (mu - sigma**2/(2*theta**2)) + \
    (rt - mu + sigma**2/(2*theta**2))*(1-np.exp(-theta*T))/(theta*T) - \
    sigma**2/(2*theta**2)*(1-np.exp(-2*T))/(2*theta*T)
    return rate

