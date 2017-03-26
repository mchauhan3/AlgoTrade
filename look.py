import pandas as pd

perf = pd.read_pickle('lol.pickle') # read in perf DataFrame
final_value =  perf.portfolio_value[-1]
init_value = perf.portfolio_value[0]
return_percentage = ((final_value - init_value)/init_value) * 100;
print return_percentage
print ("Final Value of portfolio is %f" % float(final_value))