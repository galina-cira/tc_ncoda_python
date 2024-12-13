from read_ncoda_3d import ReadNcoda3D
from read_ncoda_lon_lat import ReadNcodaLonLat

class ReadNcodaData:
    def __init__(self, fndata, fnlon, fnlat):
        self.fndata = fndata
        self.fnlon = fnlon
        self.fnlat = fnlat

    def read_all_data(self):
        reader_3d = ReadNcoda3D()
        reader_lon_lat = ReadNcodaLonLat()

        data_3d, open3d_err, read3d_err = reader_3d.read_ncoda_3d(self.fndata)
        data_2d_lon_deg, open_lon_err, read_lon_err = reader_lon_lat.read_ncoda_lon(self.fnlon)
        data_2d_lat_deg, open_lat_err, read_lat_err = reader_lon_lat.read_ncoda_lat(self.fnlat)

        return data_3d, data_2d_lon_deg, data_2d_lat_deg, \
               open3d_err, read3d_err, open_lon_err, read_lon_err, open_lat_err, read_lat_err

