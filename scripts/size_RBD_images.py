#!/usr/bin/python
from oslo_log import log as logging
try:
    import rados
    import rbd
except ImportError:
    rados = None
    rbd = None

LOG = logging.getLogger(__name__)
cluster = rados.Rados(conffile='/etc/ceph/my_ceph.conf')
cluster.connect()
ioctx = cluster.open_ioctx('mypool')

rbd_inst = rbd.RBD()

extents = []
extents_snap = []
snapshot = 

rbd_img = rbd.Image(ioctx, name, snapshot=None, read_only=False)
def iterate_cb(offset, length, exists):
    if exists:
        extents.append(length)

rbd_img.diff_iterate(0, rbd_img.size(), None, iterate_cb, include_parent=True, whole_object=False)

def iterate_cb_snap(offset, length, exists):
    if exists:
        extents_snap.append(length)

rbd_img.diff_iterate(0, rbd_img.size(), snapshot, iterate_cb, include_parent=True, whole_object=False)

if extents:
    extents_from_0 = int(sum(extents))
    LOG.debug("RBD has %s extents", extents_from_0)
    return True

if extents_snap:
    extents_from_snap = int(sum(extents_snap))
    LOG.debug("RBD has %s extents from snapshot", extents_from_snap)
    return True

snap_size = extents_from_0 - extents_from_snap

print "Size of RBD image: %d" % extents_from_0
print "Size of snapshot: %d" % snap_size

ioctx.close()
cluster.shutdown()