rm -r build
mkdir build
cd build
cmake ..
make -j4
./run_app
python plot_chart_timing_live.py
