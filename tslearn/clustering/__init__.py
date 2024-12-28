"""
The :mod:`tslearn.clustering` module gathers time series specific clustering
algorithms.

**User guide:** See the :ref:`Clustering <clustering>` section for further 
 details.
"""
from .kshape import KShape
from .kvisibility import KVisibility
from .utils import (EmptyClusterError, silhouette_score,
                    TimeSeriesCentroidBasedClusteringMixin)
from .kmeans import (TimeSeriesKMeans, KernelKMeans)


__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'


__all__ = [
    "KShape",
    "KVisibility",
    "EmptyClusterError", "silhouette_score",
    "TimeSeriesCentroidBasedClusteringMixin",

    "TimeSeriesKMeans", "KernelKMeans"
]
