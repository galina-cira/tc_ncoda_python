from read_ncoda_data import ReadNcodaData
from plot_ncoda_data import plot_data
import numpy as np
import os


def process_ncoda():
    static_path="static_data/"
    data_path = "example_data/"

    temp_file = "seatmp_pre_000000_005000_1o2161x1051_2023090700_00000000_analfld"
    saln_file = "salint_pre_000000_005000_1o2161x1051_2023090700_00000000_analfld"

    lon_file = "grdlon_sfc_000000_000000_1o2161x1051_datafld"
    lat_file = "grdlat_sfc_000000_000000_1o2161x1051_datafld"

    title_dict = {}
    title_dict['temp'] = (temp_file, "SST", "Sea Surface Temperature (°C)")
    title_dict['saln'] = (saln_file, "SSS", "Sea Surface Salinity (psu)")

    for key, (data_file, plot_title_str, plot_title) in title_dict.items():

        fndata = os.path.join(data_path, data_file)
        fnlon = os.path.join(static_path, lon_file)
        fnlat = os.path.join(static_path, lat_file)

        reader = ReadNcodaData(fndata, fnlon, fnlat)
        data_3d, data_2d_lon_deg, data_2d_lat_deg, \
            open3d_err, read3d_err, open_lon_err, read_lon_err, open_lat_err, read_lat_err = reader.read_all_data()


        if data_3d is not None and data_2d_lon_deg is not None and data_2d_lat_deg is not None:
            print("All Data Read Successfully!")

            lons = data_2d_lon_deg
            lats = data_2d_lat_deg

            # level = 0 is surface
            level = 0
            result = plot_data(lons, lats, data_3d, level, \
                    plot_title, plot_title_str, plot_type='imshow', lat_lon_box=None)
            
            

        else:
            print("Error Reading Data")


if __name__ == "__main__":

    process_ncoda()
        
