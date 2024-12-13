import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
import pdb
import cartopy.feature as cfeature

from mpl_toolkits.axes_grid1 import make_axes_locatable

def plot_data(lons, lats, data_3d, level, \
        plot_title, plot_title_str, plot_type='contourf', lat_lon_box=None):
    if level < 0 or level >= data_3d.shape[2]:
        print("Invalid level: {}. Please choose a level between 0 and {}.".format(level, data_3d.shape[2] - 1))
        return

    data = data_3d[:,:,level]

    # subset data to plot
    #data = data[1600:1750, 690:800]
    #lons = lons[1600:1750, 690:800]
    #lats = lats[1600:1750, 690:800]

    #fig = plt.figure(figsize=(10, 6))
    projection = ccrs.Mercator(central_longitude = 180.0)
    fig, ax = plt.subplots(subplot_kw={'projection': projection})

    # compute the aspect ratio
    dx = lons.max() - lons.min()
    dy = lats.max() - lats.min()
    aspect = dy / dx

    # dynamically calculate the extent from the lons and lats
    extent = [np.min(lons), np.max(lons), np.min(lats), np.max(lats)] 

    # plot data 
    mesh = ax.pcolormesh(lons, lats, data, transform=ccrs.PlateCarree(), cmap='jet')

    ax.margins(0)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.LAND, edgecolor='black')
    ax.add_feature(cfeature.LAKES, edgecolor='black')
    ax.add_feature(cfeature.RIVERS)
    states = cfeature.NaturalEarthFeature(
        category='cultural',
        scale='50m',
        facecolor='none',
        name='admin_1_states_provinces_lines')
    ax.add_feature(states, edgecolor='black')
    ax.add_feature(cfeature.BORDERS)

    # colorbar
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1, axes_class=plt.Axes)
    cbar = plt.colorbar(mesh, cax=cax)
    #cbar.set_label('Sea Surface Temperature (°C)')
    cbar.set_label(plot_title)

    ax.coastlines(resolution='110m')
    gl = ax.gridlines(draw_labels=True)

    # labels
    gl.top_labels = True
    gl.bottom_labels = True
    gl.left_labels = True   
    gl.right_labels = False  

    plt.title(plot_title_str + ' NCODA')
    plt.savefig('ncoda_' + plot_title_str + '_plot.png', dpi = 800)
