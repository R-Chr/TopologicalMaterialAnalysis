import oineus
import diode
import numpy
import pandas

points = numpy.random.random((100,4))
points[:,0:3] = 10*points[0:3]
points = pandas.DataFrame(points, columns=["x","y", "z","y"])

sub = []

for i in range(100):
	z_val = points["z"].iloc[i]
	if z_val > 9 or z_val <1:
		sub.append(True)
	else:
		sub.append(False)

points["sub"]=sub
points.sort_values(by="sub", ascending=False)
simplices = diode.fill_weighted_alpha_shapes(points[["x","y","z","w"]].to_numpy())
for i in range(len(simplices)):
	simplices[i] = [sorted(simplices[i][0]), simplices[i][1]]
	
simplices = sorted(simplices, key=cmp_to_key(oineus_compare))
L = []
not_L = []
#L_to_K = []
#id_L = 0
#K_to_L = [-1 for i in range(len(simplices))]
for i,s in enumerate(simplices):
	if len(s[0])==1:
		if sub[s[0][0]]==True:
			#K_to_L[i]= id_L            
			L.append([s[0], s[1]])
			#L_to_K.append(i)
			#id_L +=1
		else:
			not_L.append([s[0],s[1]])
	else:
		sub_complex = True
		for v in s[0]:
			if sub[v] == False:
				sub_complex=False
				break
		if sub_complex == True:
			#verts = [K_to_L[v] for v in s[0]]
			L.append([s[0], s[1]])
			#L_to_K.append(i)
			#K_to_L[i] = id_L
			#id_L +=1
		else:
			not_L.append([s[0],s[1]])

K = []
for s in L:
	K.append(s)

for s in not_L:
	K.append(s)

L = [[i,s[0],s[1]] for i, s in enumerate(L)]
K = [[i,s[0],s[1]] for i, s in enumerate(K)]

params=oineus.ReductionParams()
params.n_threads=4
params.verbose=True
params.image=True
L = oineus.list_to_filtration_float(L, params)
K = oineus.list_to_filtration_float(K, params)

kicr = oineus.KerImCokReduced_float(K,L,params,False)
