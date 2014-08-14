import numpy as np

try:
    from mayavi import mlab
except ImportError as e:
    print "You don't seem to have Mayavi installed on your system, so you won't be able to"\
          " view this demonstratio, I'm afraid. You can download it from their website as"\
          " per http://mayavi.sourceforge.net/install.html, though."

def plot_spheres(azimuths, altitudes, even_azimuths, even_altitudes):
    # Cool visualisation of point picking on a sphere

    # Create a sphere
    r = 0.3
    pi = np.pi
    cos = np.cos
    sin = np.sin
    theta, phi = np.mgrid[0:pi:200j, 0:2*pi:200j]

    print "Converting phi and theta into x,y and z"
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    print "...done\n"

    print "Converting data points from spherical to Cartesian coords..."
    x_points = r * sin(azimuths) * cos(altitudes)
    y_points = r * sin(azimuths) * sin(altitudes)
    z_points = r * cos(azimuths)

    x_points_even = r * sin(even_azimuths) * cos(even_altitudes)
    y_points_even = r * sin(even_azimuths) * sin(even_altitudes)
    z_points_even = r * cos(even_azimuths)
    print "...done"

    mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(400, 300))
    mlab.clf()

    print "Making spherical surface plot..."
    mlab.mesh(x, y, z, color=(1,0,0))
    mlab.points3d(x_points_even, y_points_even, z_points_even, mode="point")
    mlab.text3d(0, 0, 0.5, "Incorrect", scale=0.1)

    mlab.mesh(x+0.5, y+0.5, z+0.5, color=(0,0,1))
    mlab.points3d(x_points+0.5, y_points+0.5, z_points+0.5, mode="point")
    mlab.text3d(0.5, 0.5, 1.0, "Correct", scale=0.1)

    mlab.title("Point Picking on a Sphere")
    print "...done\n"

    print "Showing result..."
    mlab.show()
    print "...done"

    return True
