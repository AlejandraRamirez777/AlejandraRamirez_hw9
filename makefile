cpp_vs_python.png : times_cpp.csv times_python.csv
	python AlejandraRamirez_Graficas.py
times_cpp.csv : gen_times.x
	./gen_times.x > times_cpp.csv
times_python.csv : 
	python AlejandraRamirez_GenerarTiempos.py > times_python.csv
gen_times.x : 
	c++ AlejandraRamirez_GenerarTiempos.cpp -o gen_times.x

clean: 
	rm times_cpp.csv times_python.csv cpp_vs_python.png gen_times.x
