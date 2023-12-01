import matplotlib.pyplot as plt
import pandas as pd
import sys

print(sys.argv)
#f="data.csv"
#x="x"
#y="a"

csv_file=sys.argv[1];
#y(x)
_sep=sys.argv[2];
x=sys.argv[3];
y=sys.argv[4];
func=y+"("+x+")"
out_file=csv_file+"_"+func+".png";

dataframe = pd.read_csv(csv_file,sep=_sep)

xs = dataframe[x]
ys = dataframe[y]

plt.plot(xs, ys, label=func)
plt.title(csv_file)
plt.xlabel(x)
plt.ylabel(y)
plt.legend()
plt.xticks(rotation=45)
plt.savefig(out_file)
plt.show()
